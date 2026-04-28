import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import inject_css, COLORS, render_sidebar_controls, render_alarm
from utils import init_kavach
from core.ransomware import RansomwareShield
from core.phishing import PhishGuard

st.set_page_config(page_title="Behavioral Defense | Kavach AI", page_icon="🚨", layout="wide")
inject_css(st)

logger, detector, guardian, simulator, sniffer = init_kavach()
render_sidebar_controls(st, logger, simulator, sniffer)
render_alarm(st)

rs = RansomwareShield()
pg = PhishGuard()

st.markdown('''
    <div style="text-align: center; margin-top: 20px; margin-bottom: 40px;">
        <h1 style="font-size: 3rem; font-weight: 900; letter-spacing: -1.5px; margin-bottom: 5px; color: #fff;">BEHAVIORAL DEFENSE</h1>
        <div style="font-size: 0.8rem; font-weight: 700; color: var(--cyan); letter-spacing: 4px; text-transform: uppercase;">Ransomware & Phishing Guard</div>
    </div>
''', unsafe_allow_html=True)

if 'rs_detections' not in st.session_state or 'phish_logs' not in st.session_state:
    st.session_state.rs_detections = rs.generate_detections(10)
    st.session_state.phish_logs = pg.scan_messages(8)

tab_malware, tab_phish = st.tabs(["🛡️ Malware Neutralization", "🎣 Phishing Defense"])

with tab_malware:
    st.markdown('<div class="glass-card"><div class="section-title">🚨 Active Ransomware Threats</div>', unsafe_allow_html=True)
    if st.button("🚨 Simulate Malware Attack", use_container_width=True, type="primary"):
        st.session_state.is_under_attack = True
        st.session_state.threat_detected = True
        st.rerun()

    for i, d in enumerate(st.session_state.rs_detections[:6]):
        st.markdown(f'''<div class="threat-card">
            🔴 <strong style="color:{COLORS['coral']}">{d['family']}</strong> &nbsp;·&nbsp; 
            Type: {d['type']} &nbsp;·&nbsp; Action: <strong>{d['action']}</strong>
            <br/><span style="color:var(--text-dim);font-size:0.75rem">Target: {d['target_dir']} · Files Protected: {d['files_affected']}</span>
        </div>''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab_phish:
    st.markdown('<div class="glass-card"><div class="section-title">🎣 Social Engineering Monitor</div>', unsafe_allow_html=True)
    for log in st.session_state.phish_logs:
        is_high = log['is_phishing']
        st.markdown(f'''<div class="{'threat-card' if is_high else 'normal-card'}">
            <strong>📧 {log['platform']}: {log['sender']}</strong> &nbsp;·&nbsp; 
            Risk: <span class="pill {'pill-critical' if is_high else 'pill-info'}">{log['nlp_score']:.0%}</span>
            <br/><span style="color:var(--text-dim);font-size:0.8rem">Content: {log['content']}</span>
            <br/><span style="color:{COLORS['amber']};font-size:0.75rem">Verdict: {log['verdict']} · Action: {log['action']}</span>
        </div>''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.get('is_under_attack'):
    if not st.session_state.get('threat_detected'): # If alarm was cleared but attack state remains
        if st.button("🛑 STOP ATTACK", use_container_width=True, type="primary"):
            st.session_state.is_under_attack = False
            st.rerun()
