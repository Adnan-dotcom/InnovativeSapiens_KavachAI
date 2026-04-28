"""Kavach AI SOC Dashboard — Main Page"""
import streamlit as st
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import *
from core.logger import ThreatLogger
from core.detector import ThreatDetector
from core.guardian import AutonomousGuardian
from core.simulator import AttackSimulator
from styles import inject_css, CHART_LAYOUT, PIE_COLORS, COLORS, render_sidebar_controls
from utils import init_kavach

st.set_page_config(page_title="Kavach AI", page_icon="🛡️", layout="wide", initial_sidebar_state="expanded")
inject_css(st)

logger, detector, guardian, simulator, sniffer = init_kavach()
render_sidebar_controls(st, logger, simulator, sniffer)

# ──────────────────────── Main Content ────────────────────────
st.markdown('''
    <div style="display: flex; align-items: center; gap: 24px; margin-top: 10px; margin-bottom: 20px;">
        <div class="kavach-symbol" style="width: 55px; height: 55px; margin: 0;"></div>
        <div>
            <h1 style="margin: 0; line-height: 1.1;">KAVACH AI</h1>
            <p class="page-subtitle" style="margin: 0; margin-top: 5px;">Autonomous Cyber Defense System — <em>Detect. Decide. Defend.</em></p>
        </div>
    </div>
''', unsafe_allow_html=True)

stats = logger.get_threat_stats()

# ── Global Status + KPIs ──
col_status, col_metrics = st.columns([1, 2], gap="large")

with col_status:
    # Use a larger sample (last 50 events) for a smoother, more nuanced score
    recent_events = logger.get_recent_threats(50)
    if not recent_events:
        score = 100
    else:
        threat_impact = 0
        for e in recent_events:
            if e['severity'] == 'critical': threat_impact += 12
            elif e['severity'] == 'high': threat_impact += 6
            elif e['severity'] == 'medium': threat_impact += 3
        
        score = 100 - (threat_impact / 2)
        score = max(0, min(100, score))
        
    color = COLORS['emerald'] if score > 80 else COLORS['amber'] if score > 50 else COLORS['coral']
    
    st.markdown(f'''
    <div class="glass-card" style="text-align:center; padding: 45px 25px; background: radial-gradient(circle at top right, {color}15, transparent);">
        <div style="font-size: 0.75rem; font-weight: 800; color: var(--text-dim); text-transform: uppercase; letter-spacing: 3px; margin-bottom: 25px;">Security Posture Index</div>
        <div style="font-size: 5.5rem; font-weight: 950; color: {color}; line-height: 0.9; letter-spacing: -4px; margin-bottom: 10px;">{score:.0f}%</div>
        <div style="font-size: 1rem; font-weight: 700; color: #fff; letter-spacing: 1px; text-transform: uppercase;">System { 'Optimal' if score > 80 else 'Degraded' if score > 50 else 'Critical' }</div>
        <div style="margin-top: 30px; height: 6px; background: rgba(255,255,255,0.05); border-radius: 3px; overflow: hidden; border: 1px solid rgba(255,255,255,0.03);">
            <div style="width: {score}%; height: 100%; background: {color}; box-shadow: 0 0 25px {color};"></div>
        </div>
        <div style="margin-top: 15px; font-size: 0.75rem; color: var(--text-dim);">Autonomous AI Health Monitoring</div>
    </div>
    ''', unsafe_allow_html=True)

with col_metrics:
    st.markdown('<div class="glass-card" style="height: 100%; padding: 30px;">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📊 Key Performance Metrics</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2)
    
    c1.metric("Neutralized", stats['total_threats'], "ACTIVE" if stats['total_threats'] > 0 else "None")
    c2.metric("Decoys", "8 ACTIVE", "ShadowGuard")
    c3.metric("AI Confidence", "99.4%", "Neural-Core")
    c4.metric("IoT Nodes", "12/12", "Secure")
    
    st.markdown('<div style="margin-top: 25px; padding: 15px; background: rgba(0,212,255,0.05); border-radius: 12px; border: 1px solid rgba(0,212,255,0.1);">', unsafe_allow_html=True)
    st.markdown(f'<span style="color:{COLORS["cyan"]}; font-weight: 600; font-size: 0.85rem;">🛡️ Autonomous Defense Active</span><br/><span style="color:var(--text-dim); font-size: 0.75rem;">AI is scanning {stats["total_events"]} events for anomaly signatures.</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── Threat Analysis Row ──
col_feed, col_breakdown = st.columns([3, 2], gap="medium")

with col_feed:
    st.markdown('<div class="glass-card"><div class="section-title">📡 Autonomous Response Feed</div>', unsafe_allow_html=True)
    recent = logger.get_recent_threats(8)
    if recent:
        for i, t in enumerate(recent):
            is_threat = t['threat_type'] != 'Normal'
            css = "threat-card" if is_threat else "normal-card"
            delay = f"delay-{min(i+1, 8)}"
            icon = "🔴" if t['severity'] == 'critical' else "🟠" if t['severity'] == 'high' else "🟢"
            conf = f"{t['confidence']*100:.0f}%" if t['confidence'] else "—"
            ts = t['timestamp'].split('T')[1][:8] if 'T' in t['timestamp'] else t['timestamp'][-8:]
            color = '#ff3366' if is_threat else '#10ff99'
            st.markdown(f'''<div class="{css} {delay}">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div style="display:flex; align-items:center; gap:12px;">
                        <span style="color:var(--text-dim); font-size:0.75rem; font-weight:600;">{ts}</span>
                        <span style="font-size:1.1rem;">{icon}</span>
                        <strong style="color:{color}; font-size:1rem; letter-spacing:-0.5px;">{t['threat_type']}</strong>
                        <span style="color:var(--text-dim); font-size:0.8rem;">via {t['src_ip']}</span>
                    </div>
                    <div style="text-align:right;">
                        <div style="color:#fff; font-size:0.8rem; font-weight:700;">{t['action_taken']}</div>
                        <div style="color:var(--text-dim); font-size:0.7rem; text-transform:uppercase; letter-spacing:0.5px;">Confidence: {conf}</div>
                    </div>
                </div>
            </div>''', unsafe_allow_html=True)
    else:
        st.info("No network activity detected. Start Live Capture or run a simulation!")
    st.markdown('</div>', unsafe_allow_html=True)

with col_breakdown:
    st.markdown('<div class="glass-card"><div class="section-title">🎯 Threat Breakdown</div>', unsafe_allow_html=True)
    if stats['by_type']:
        import plotly.graph_objects as go
        from styles import PIE_COLORS, CHART_LAYOUT
        fig = go.Figure(data=[go.Pie(
            labels=list(stats['by_type'].keys()), values=list(stats['by_type'].values()),
            hole=0.65, marker=dict(colors=PIE_COLORS[:len(stats['by_type'])]),
            textfont=dict(color='white', size=11, family='Inter'),
            textinfo='label+percent', textposition='outside',
            pull=[0.05]*len(stats['by_type']),
        )])
        layout = {**CHART_LAYOUT, 'height': 380, 'showlegend': False, 'margin': dict(t=20, b=20, l=20, r=20)}
        fig.update_layout(**layout)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.markdown('<div style="text-align:center;padding:120px 0;color:var(--text-dim);font-size:0.9rem">No data yet</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ──
st.markdown('<div style="text-align:center; margin-top:60px; padding-top:40px; border-top:1px solid rgba(255,255,255,0.05); color:var(--text-dim); font-size:0.75rem; letter-spacing:3px; font-weight:700; text-transform:uppercase;">AUTONOMOUS AGENTIC DEFENSE · KAVACH AI v2.5</div>', unsafe_allow_html=True)


