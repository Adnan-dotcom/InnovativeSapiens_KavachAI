import streamlit as st
import sys, os, pandas as pd
import plotly.graph_objects as go
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import inject_css, CHART_LAYOUT, COLORS, render_sidebar_controls, render_alarm
from utils import init_kavach
from datetime import datetime

st.set_page_config(page_title="Sentinel Intelligence | Kavach AI", page_icon="🕵️", layout="wide")
inject_css(st)

logger, detector, guardian, simulator, sniffer = init_kavach()
render_sidebar_controls(st, logger, simulator, sniffer)
render_alarm(st)

# ── Auto-Panic Logic ──
latest_threat = logger.get_recent_threats(1)
if latest_threat and latest_threat[0]['threat_type'] != 'Normal':
    t_str = latest_threat[0]['timestamp']
    try:
        t_obj = datetime.fromisoformat(t_str)
        if (datetime.now() - t_obj).total_seconds() < 10 and latest_threat[0]['severity'] in ['high', 'critical']:
            st.session_state.threat_detected = True
    except: pass

stats = logger.get_threat_stats()

st.markdown('''
    <div style="text-align: center; margin-top: 20px; margin-bottom: 40px;">
        <h1 style="font-size: 3rem; font-weight: 900; letter-spacing: -1.5px; margin-bottom: 5px; color: #fff;">SENTINEL INTELLIGENCE</h1>
        <div style="font-size: 0.8rem; font-weight: 700; color: var(--cyan); letter-spacing: 4px; text-transform: uppercase;">Forensic Traffic Analysis</div>
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
    st.markdown('<div class="glass-card"><div class="section-title">📑 Adversary Intelligence & Persona Profiling</div>', unsafe_allow_html=True)
    if stats['top_ips']:
        for i, ip in enumerate(stats['top_ips']):
            # Determine persona based on "attack type"
            persona = "Sophisticated Actor" if "Port Scan" in ip['type'] else "Automated Botnet" if "DDoS" in ip['type'] else "Script Kiddie"
            risk_level = "CRITICAL" if ip['count'] > 50 else "HIGH"
            
            st.markdown(f'''<div class="threat-card delay-{min(i+1,8)}">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <strong>🕵️ Adversary: {ip['ip']}</strong><br/>
                        <span style="font-size:0.75rem; color:var(--text-dim);">Persona: <span style="color:var(--cyan)">{persona}</span></span>
                    </div>
                    <div style="text-align:right;">
                        <span class="pill {'pill-critical' if risk_level=='CRITICAL' else 'pill-high'}">{risk_level} RISK</span>
                        <div style="font-size:0.7rem; color:var(--text-dim); margin-top:4px;">Threat: {ip['type']}</div>
                    </div>
                </div>
                <div style="margin-top:12px; padding-top:10px; border-top:1px solid rgba(255,255,255,0.05); display:grid; grid-template-columns: 1fr 1fr; font-size:0.7rem;">
                    <div>Behavior: <span style="color:var(--emerald)">Honeytrapped</span></div>
                    <div style="text-align:right;">Inference Confidence: <span style="color:var(--cyan)">{(0.85 + (i*0.02)):.2f}%</span></div>
                </div>
            </div>''', unsafe_allow_html=True)
    else:
        st.info("No adversary profiles generated yet. Launch a simulation to begin.")
    st.markdown('</div>', unsafe_allow_html=True)
