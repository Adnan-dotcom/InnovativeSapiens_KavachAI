import streamlit as st
import sys, os, pandas as pd
import plotly.graph_objects as go
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import inject_css, CHART_LAYOUT, COLORS, render_sidebar_controls
from utils import init_kavach

st.set_page_config(page_title="Sentinel Intelligence | Kavach AI", page_icon="🕵️", layout="wide")
inject_css(st)

logger, detector, guardian, simulator, sniffer = init_kavach()
render_sidebar_controls(st, logger, simulator, sniffer)
stats = logger.get_threat_stats()

st.markdown('''
    <div style="display: flex; align-items: center; gap: 24px; margin-top: 10px; margin-bottom: 20px;">
        <div class="kavach-symbol" style="width: 55px; height: 55px; margin: 0;"></div>
        <div>
            <h1 style="margin: 0; line-height: 1.1;">Sentinel Intelligence</h1>
            <p class="page-subtitle" style="margin: 0; margin-top: 5px;">Unified Visibility, Pattern Recognition & Forensic Attribution</p>
        </div>
    </div>
''', unsafe_allow_html=True)

tab_live, tab_analytics, tab_forensics = st.tabs(["📡 Live Feed", "📊 Visual Analytics", "📑 Forensic Briefing"])

with tab_live:
    st.markdown('<div class="glass-card"><div class="section-title">📡 Real-Time Traffic Stream</div>', unsafe_allow_html=True)
    recent = logger.get_recent_threats(30)
    if recent:
        df = pd.DataFrame(recent)
        df = df[['timestamp', 'src_ip', 'protocol', 'threat_type', 'confidence', 'severity', 'action_taken']]
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("No traffic detected.")
    st.markdown('</div>', unsafe_allow_html=True)

with tab_analytics:
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.markdown('<div class="glass-card"><div class="section-title">🔴 Threat Distribution</div>', unsafe_allow_html=True)
        if stats['by_type']:
            fig = go.Figure(data=[go.Pie(labels=list(stats['by_type'].keys()), values=list(stats['by_type'].values()), hole=0.6)])
            fig.update_layout({**CHART_LAYOUT, 'height': 300, 'showlegend': True})
            st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="glass-card"><div class="section-title">📈 Temporal Patterns</div>', unsafe_allow_html=True)
        if stats['time_series']:
            df_ts = pd.DataFrame(stats['time_series'])
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df_ts['time'], y=df_ts['total'], name='Total Traffic', line=dict(color=COLORS['cyan'])))
            fig.add_trace(go.Scatter(x=df_ts['time'], y=df_ts['threats'], name='Threats', fill='tozeroy', line=dict(color=COLORS['coral'])))
            fig.update_layout({**CHART_LAYOUT, 'height': 300})
            st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

with tab_forensics:
    st.markdown('<div class="glass-card"><div class="section-title">📑 Adversary Intelligence Report</div>', unsafe_allow_html=True)
    if stats['top_ips']:
        for i, ip in enumerate(stats['top_ips']):
            st.markdown(f'''<div class="threat-card delay-{min(i+1,8)}">
                <div style="display:flex; justify-content:space-between;">
                    <strong>🕵️ Adversary: {ip['ip']}</strong>
                    <span class="pill pill-critical">MITRE ATT&CK: Reconnaissance</span>
                </div>
                <div style="color:var(--text-dim); font-size:0.8rem; margin-top:8px;">
                    Primary Attack: <strong>{ip['type']}</strong> · Total Interactions: {ip['count']} · 
                    Status: <span style="color:{COLORS['emerald']}">HONEYTRAPPED</span>
                </div>
            </div>''', unsafe_allow_html=True)
    else:
        st.info("No adversary profiles generated yet.")
    st.markdown('</div>', unsafe_allow_html=True)
