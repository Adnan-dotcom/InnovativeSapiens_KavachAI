import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import inject_css, COLORS, render_sidebar_controls
from utils import init_kavach
from core.shadowguard import ShadowGuard
from core.deeptrust import DeepTrust

st.set_page_config(page_title="Deception & Identity | Kavach AI", page_icon="🪤", layout="wide")
inject_css(st)

logger, detector, guardian, simulator, sniffer, honeyport = init_kavach()
render_sidebar_controls(st, logger, simulator, sniffer)

sg = ShadowGuard()
dt = DeepTrust()

st.markdown('''
    <div style="text-align: center; margin-top: 20px; margin-bottom: 40px;">
        <h1 style="font-size: 3rem; font-weight: 900; letter-spacing: -1.5px; margin-bottom: 5px; color: #fff;">DECEPTION & IDENTITY</h1>
        <div style="font-size: 0.8rem; font-weight: 700; color: var(--cyan); letter-spacing: 4px; text-transform: uppercase;">ShadowGuard & DeepTrust Protocol</div>
    </div>
''', unsafe_allow_html=True)

if 'sg_files' not in st.session_state or 'dt_risks' not in st.session_state:
    st.session_state.sg_files = sg.generate_deployed_honeyfiles()
    st.session_state.sg_trips = sg.generate_trip_events(12)
    st.session_state.dt_scans = dt.scan_video_calls(10)
    st.session_state.dt_risks = dt.assess_communication_risk(10)

tab_decoys, tab_behavior, tab_identity = st.tabs(["🍯 Generative Decoys", "🧬 Behavioral Fingerprints", "🛡️ Identity Assurance"])

with tab_decoys:
    st.markdown(f'''
        <div class="glass-card" style="background: linear-gradient(135deg, rgba(0, 242, 255, 0.05) 0%, rgba(139, 92, 246, 0.05) 100%);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div class="section-title">🛰️ Active Honeyport (Live Trap)</div>
                <div class="pill pill-online">ONLINE: PORT 9999</div>
            </div>
            <div style="font-size: 0.85rem; color: var(--text-dim); margin-top: -15px; margin-bottom: 20px;">
                Direct your friend's laptop to <code>http://{st.session_state.get('local_ip', 'YOUR_IP')}:9999</code> to trigger a deceptive alert.
            </div>
        </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card"><div class="section-title">🍯 Active Honeyfiles</div>', unsafe_allow_html=True)
    for i, f in enumerate(st.session_state.sg_files[:8]):
        color = COLORS['coral'] if f['status'] == 'TRIGGERED' else COLORS['emerald']
        st.markdown(f'''<div class="{'threat-card' if f['status']=='TRIGGERED' else 'normal-card'}">
            <strong>{f['icon']} {f['name']}</strong> &nbsp;·&nbsp; <code>{f['path']}</code> &nbsp;·&nbsp; 
            Status: <strong style="color:{color}">{f['status']}</strong>
        </div>''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab_behavior:
    st.markdown('<div class="glass-card"><div class="section-title">🧬 Intruder Fingerprinting</div>', unsafe_allow_html=True)
    for i, t in enumerate(st.session_state.sg_trips[:6]):
        st.markdown(f'''<div class="threat-card delay-{min(i+1,8)}">
            👤 <strong>Attacker: {t['ip']}</strong> ({t['location']}) &nbsp;·&nbsp; 
            Classification: <span class="pill pill-critical">{t['classification'].upper()}</span>
            <br/><span style="color:var(--text-dim);font-size:0.8rem">Dwell Time: {t['dwell_time']}s · Mouse Entropy: High · Behavior: Malicious Probe</span>
        </div>''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab_identity:
    st.markdown('<div class="glass-card"><div class="section-title">🛡️ Neural Identity Protection</div>', unsafe_allow_html=True)
    for log in st.session_state.dt_risks[:6]:
        is_threat = log['risk_score'] > 0.6
        color = COLORS['coral'] if is_threat else COLORS['emerald']
        st.markdown(f'''<div class="{'threat-card' if is_threat else 'normal-card'}">
            <div style="display:flex; justify-content:space-between;">
                <strong>👤 {log['person']}</strong>
                <span class="pill {'pill-critical' if is_threat else 'pill-info'}">Risk: {log['risk_score']:.0%}</span>
            </div>
            <span style="color:var(--text-dim);font-size:0.75rem">Method: {log['platform']} · Intent: {log['intent']} · Status: <strong style="color:{color}">{log['action']}</strong></span>
        </div>''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
