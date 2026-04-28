import streamlit as st
import sys, os, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import inject_css, COLORS, render_sidebar_controls
from utils import init_kavach
from core.guardian_iot import GuardianIoT
from core.cleancode import CleanCodeAI

st.set_page_config(page_title="Infrastructure Security | Kavach AI", page_icon="📡", layout="wide")
inject_css(st)

logger, detector, guardian, simulator, sniffer = init_kavach()
render_sidebar_controls(st, logger, simulator, sniffer)

iot = GuardianIoT()
cc = CleanCodeAI()

st.markdown('''
    <div style="display: flex; align-items: center; gap: 24px; margin-top: 10px; margin-bottom: 20px;">
        <div class="kavach-symbol" style="width: 55px; height: 55px; margin: 0;"></div>
        <div>
            <h1 style="margin: 0; line-height: 1.1;">Infrastructure Security</h1>
            <p class="page-subtitle">IoT Protection & Supply Chain Integrity Audit</p>
        </div>
    </div>
''', unsafe_allow_html=True)

if 'iot_devices' not in st.session_state or 'cc_scan' not in st.session_state:
    st.session_state.iot_devices = iot.generate_device_inventory()
    st.session_state.cc_scan = cc.scan_repository()

tab_iot, tab_audit = st.tabs(["🖥️ IoT Ecosystem", "🔬 Supply Chain Audit"])

with tab_iot:
    st.markdown('<div class="glass-card"><div class="section-title">🖥️ Smart Infrastructure Inventory</div>', unsafe_allow_html=True)
    cols = st.columns(4)
    for i, dev in enumerate(st.session_state.iot_devices[:8]):
        col = cols[i % 4]
        is_bad = dev['status'] == 'COMPROMISED'
        border = COLORS['coral'] if is_bad else COLORS['emerald']
        col.markdown(f'''<div style="background:rgba(255,255,255,0.02);border:1px solid {border}33;border-radius:12px;padding:15px;text-align:center;">
            <div style="font-size:1.8rem">{dev['icon']}</div>
            <div style="font-weight:700;font-size:0.85rem;margin:5px 0">{dev['name']}</div>
            <span class="pill {'pill-critical' if is_bad else 'pill-info'}">{dev['status']}</span>
        </div>''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab_audit:
    st.markdown('<div class="glass-card"><div class="section-title">💣 Logic Bomb Detection</div>', unsafe_allow_html=True)
    for i, bomb in enumerate(st.session_state.cc_scan['logic_bombs']):
        st.markdown(f'''<div class="threat-card">
            🔴 <strong>{bomb['file']}:{bomb['line']}</strong> &nbsp;·&nbsp; 
            Intent: <span style="color:{COLORS['amber']}">{bomb['intent']}</span>
            <br/><code style="font-size:0.75rem">{bomb['code'][:80]}...</code>
        </div>''', unsafe_allow_html=True)
    
    st.markdown('<div class="section-title" style="margin-top:20px">📦 Dependency Risks</div>', unsafe_allow_html=True)
    for pkg in st.session_state.cc_scan['vulnerable_packages'][:4]:
        st.markdown(f'''<div class="normal-card">
            <strong>{pkg['name']}</strong> &nbsp;·&nbsp; Risk: <span class="pill pill-high">{pkg['risk']}</span>
            <br/><span style="color:var(--text-dim);font-size:0.8rem">Issue: {pkg['issue']} · ✅ Fix: Update to latest</span>
        </div>''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
