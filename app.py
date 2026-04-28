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
    <div style="text-align: center; margin-top: 20px; margin-bottom: 40px;">
        <h1 style="font-size: 3.5rem; font-weight: 900; letter-spacing: -2px; margin-bottom: 5px; color: #fff;">KAVACH AI</h1>
        <div style="font-size: 0.85rem; font-weight: 700; color: var(--cyan); letter-spacing: 5px; text-transform: uppercase;">Autonomous Defense Protocol</div>
    </div>
''', unsafe_allow_html=True)

stats = logger.get_threat_stats()
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

# ── Hero Section ──
score_color = COLORS['emerald'] if score > 80 else COLORS['amber'] if score > 50 else COLORS['coral']
st.markdown(f'''
    <div class="glass-card" style="text-align: center; padding: 100px 20px; background: radial-gradient(circle at center, {score_color}10, transparent);">
        <div style="font-size: 0.85rem; font-weight: 800; color: var(--text-dim); text-transform: uppercase; letter-spacing: 5px; margin-bottom: 25px;">Security Pulse Index</div>
        <div style="font-size: 11rem; font-weight: 950; color: #fff; line-height: 0.8; letter-spacing: -8px; margin-bottom: 30px;">{score:.0f}<span style="font-size: 3rem; color: {score_color}; vertical-align: top; margin-left: 10px;">%</span></div>
        <div style="font-size: 1.5rem; font-weight: 700; color: {score_color}; letter-spacing: 3px; text-transform: uppercase;">System { 'Optimal' if score > 80 else 'Degraded' if score > 50 else 'Critical' }</div>
    </div>
''', unsafe_allow_html=True)

# ── Triple Pillar Row ──
p1, p2, p3 = st.columns(3, gap="large")

with p1:
    st.markdown(f'''<div class="glass-card" style="text-align:center; padding: 40px 20px;">
        <div style="font-size:3rem; margin-bottom:20px;">📡</div>
        <div class="section-title">Telemetry</div>
        <div style="font-size:2rem; font-weight:900; color:#fff;">{stats['total_events']:,}</div>
        <div style="font-size:0.75rem; color:var(--text-dim);">Live Packets Analyzed</div>
    </div>''', unsafe_allow_html=True)

with p2:
    st.markdown(f'''<div class="glass-card" style="text-align:center; padding: 40px 20px;">
        <div style="font-size:3rem; margin-bottom:20px;">🪤</div>
        <div class="section-title">Deception</div>
        <div style="font-size:2rem; font-weight:900; color:#fff;">ACTIVE</div>
        <div style="font-size:0.75rem; color:var(--text-dim);">ShadowGuard Traps Ready</div>
    </div>''', unsafe_allow_html=True)

with p3:
    st.markdown(f'''<div class="glass-card" style="text-align:center; padding: 40px 20px;">
        <div style="font-size:3rem; margin-bottom:20px;">🛡️</div>
        <div class="section-title">Defense</div>
        <div style="font-size:2rem; font-weight:900; color:{COLORS['emerald']}">{stats['ips_blocked']}</div>
        <div style="font-size:0.75rem; color:var(--text-dim);">Threats Contained</div>
    </div>''', unsafe_allow_html=True)

# ── Response Row ──
st.markdown('<div class="glass-card"><div class="section-title">📡 Autonomous Response Log</div>', unsafe_allow_html=True)
recent = logger.get_recent_threats(5)
if recent:
    for t in recent:
        is_threat = t['threat_type'] != 'Normal'
        color = COLORS['coral'] if is_threat else COLORS['emerald']
        st.markdown(f'''
            <div style="display:flex; justify-content:space-between; align-items:center; padding: 18px 0; border-bottom: 1px solid rgba(255,255,255,0.03);">
                <div style="display:flex; align-items:center; gap:25px;">
                    <div style="width:12px; height:12px; border-radius:50%; background:{color}; box-shadow: 0 0 15px {color};"></div>
                    <div>
                        <div style="font-weight:700; font-size:1.1rem; color:#fff;">{t['threat_type']}</div>
                        <div style="font-size:0.8rem; color:var(--text-dim);">{t['src_ip']}</div>
                    </div>
                </div>
                <div style="text-align:right;">
                    <div style="font-weight:900; font-size:0.9rem; color:#fff;">{t['action_taken']}</div>
                    <div style="font-size:0.75rem; color:var(--text-dim);">Confidence: {t['confidence']*100:.0f}%</div>
                </div>
            </div>
        ''', unsafe_allow_html=True)
else:
    st.info("System initializing. No threats detected.")
st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ──
st.markdown('<div style="text-align:center; margin-top:80px; padding-top:40px; border-top:1px solid rgba(255,255,255,0.05); color:var(--text-dim); font-size:0.8rem; letter-spacing:4px; font-weight:700; text-transform:uppercase;">AUTONOMOUS AI DEFENSE · KAVACH AI</div>', unsafe_allow_html=True)


