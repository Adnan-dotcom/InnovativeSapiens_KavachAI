"""Kavach AI — Shared Premium CSS Design System"""

GLOBAL_CSS = """<style>
/* ═══════════════════════════════════════════════════════
   KAVACH AI  ·  Premium Design System v2.0
   ═══════════════════════════════════════════════════════ */

/* ── Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --cyan: #00f2ff;
    --emerald: #10ff99;
    --coral: #ff3366;
    --amber: #ffaa33;
    --violet: #8b5cf6;
    --text: #f0f0ff;
    --text-dim: #94a3b8;
    --bg-deep: #030712;
    --glass-bg: rgba(17, 25, 40, 0.65);
    --glass-border: rgba(255, 255, 255, 0.08);
}

* { font-family: 'Inter', -apple-system, sans-serif !important; }

/* ── App Background ── */
.stApp {
    background: var(--bg-deep) !important;
}

@keyframes pulseGlow {
    0% { transform: scale(1); box-shadow: 0 0 20px rgba(255, 51, 102, 0.4); }
    50% { transform: scale(1.05); box-shadow: 0 0 50px rgba(255, 51, 102, 0.8); }
    100% { transform: scale(1); box-shadow: 0 0 20px rgba(255, 51, 102, 0.4); }
}
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* ── Glassmorphism Cards (Metric) ── */
div[data-testid="stMetric"] {
    background: var(--glass-bg) !important;
    backdrop-filter: blur(24px) !important;
    -webkit-backdrop-filter: blur(24px) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: 12px !important;
    padding: 24px 20px !important;
    box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5) !important;
    animation: fadeInUp 0.7s cubic-bezier(0.16, 1, 0.3, 1) both;
}
div[data-testid="stMetric"]:hover {
    background: rgba(255,255,255,0.04) !important;
    transform: translateY(-5px) !important;
}

/* ── Sidebar ── */
div[data-testid="stSidebar"] {
    background: rgba(4,4,12,0.95) !important;
    backdrop-filter: blur(32px) !important;
    border-right: 1px solid var(--glass-border) !important;
}
button[data-testid="stSidebarCollapse"], 
[data-testid="collapsedControl"], 
[data-testid="stHeader"] {
    display: none !important;
}
footer { display: none !important; }

/* ── Glass card wrapper ── */
.glass-card {
    background: var(--glass-bg);
    backdrop-filter: blur(24px);
    border: 1px solid var(--glass-border);
    border-radius: 24px;
    padding: 28px;
    margin-bottom: 24px;
    box-shadow: 0 10px 40px -10px rgba(0,0,0,0.5);
    animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
}

.section-title {
    font-size: 0.85rem;
    font-weight: 800;
    color: var(--text-dim);
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 20px;
}

.threat-card {
    padding: 16px 20px;
    border-radius: 12px;
    margin: 8px 0;
    font-size: 0.9rem;
    background: rgba(255,255,255,0.02);
    border: 1px solid var(--glass-border);
    border-left: 4px solid var(--coral);
}

.status-dot {
    display: inline-block;
    width: 9px; height: 9px;
    border-radius: 50%;
    background: var(--emerald);
    animation: pulseGlow 2s infinite;
    margin-right: 6px;
}

.pill {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 0.72rem;
    font-weight: 600;
    text-transform: uppercase;
}
.pill-critical { background: rgba(255,77,106,0.1); color: var(--coral); border: 1px solid rgba(255,77,106,0.2); }

.block-container { padding-top: 2rem !important; }
</style>"""

CHART_LAYOUT = dict(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#c0c0e0', family='Inter', size=12),
    margin=dict(t=10, b=30, l=40, r=10),
    xaxis=dict(gridcolor='rgba(255,255,255,0.04)', zeroline=False),
    yaxis=dict(gridcolor='rgba(255,255,255,0.04)', zeroline=False),
)

COLORS = {
    'cyan': '#00d4ff',
    'emerald': '#00ff88',
    'coral': '#ff4d6a',
    'amber': '#ffb347',
}
PIE_COLORS = ['#ff4d6a', '#ffb347', '#a78bfa', '#f472b6', '#00d4ff']

def inject_css(st):
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

def render_alarm(st, latest_threat=None):
    """
    Triggers a professional full-screen red glow overlay for the 'Money Shot' demo.
    """
    if not st.session_state.get('demo_armed', False):
        st.session_state.threat_detected = False
        return

    if st.session_state.get('threat_detected'):
        threat_info = latest_threat[0] if latest_threat else {}
        attacker_ip = threat_info.get('src_ip', 'UNKNOWN')
        threat_type = threat_info.get('threat_type', 'BREACH')
        
        st.markdown(f"""
            <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; 
                        background: rgba(180, 0, 0, 0.4); z-index: 999999; pointer-events: none;
                        box-shadow: inset 0 0 150px #f00; display: flex; 
                        align-items: center; justify-content: center; flex-direction: column;
                        backdrop-filter: blur(2px);">
                <div style="font-size: 8rem; font-weight: 900; color: #fff; text-shadow: 0 0 30px #f00;
                            letter-spacing: -5px;">{threat_type.split()[0].upper()}</div>
                <div style="font-size: 1.5rem; font-weight: 700; color: #fff; letter-spacing: 10px; margin-top: 20px;">SOURCE IP: {attacker_ip}</div>
                <div style="font-size: 0.8rem; font-weight: 500; color: rgba(255,255,255,0.7); letter-spacing: 5px; margin-top: 10px;">AUTONOMOUS RESPONSE ACTIVE</div>
            </div>
            <style>
            .stApp {{ filter: grayscale(0.3) contrast(1.1) !important; }}
            .glass-card {{ border: 2px solid #ff4d6a !important; box-shadow: 0 0 30px rgba(255,77,106,0.3) !important; }}
            </style>
        """, unsafe_allow_html=True)
        
        st.error(f"🚨 KAVACH AI: {threat_type} DETECTED FROM {attacker_ip} - NEUTRALIZING...")
        if st.button("🛑 SILENCE ALARM & CLEAR BREACH", type="primary", use_container_width=True):
            st.session_state.threat_detected = False
            st.rerun()

def render_sidebar_controls(st, logger=None, simulator=None, sniffer=None):
    with st.sidebar:
        st.markdown(f'''
            <div style="text-align: center; padding: 20px 0;">
                <div style="font-size: 1.8rem; font-weight: 900; letter-spacing: -1px; color: #fff;">🛡️ KAVACH</div>
                <div style="font-size: 0.65rem; font-weight: 700; color: var(--cyan); letter-spacing: 3px; margin-top: 5px;">AGENTIC CORE v2.5</div>
            </div>
        ''', unsafe_allow_html=True)
        
        st.divider()
        
        st.markdown('<p style="color:var(--text-dim); font-size:0.7rem; font-weight:800; letter-spacing:2px; text-transform:uppercase; margin-bottom:12px;">⚡ Attack Simulation</p>', unsafe_allow_html=True)
        scenario = st.selectbox("Scenario", ["mixed", "ddos", "port_scan", "brute_force", "dns_amp", "normal"], label_visibility="collapsed")
        if st.button("🚀 Launch Simulation", use_container_width=True):
            if simulator:
                simulator.run_scenario(scenario)
                st.rerun()

        st.divider()

        st.markdown('<p style="color:var(--text-dim); font-size:0.7rem; font-weight:800; letter-spacing:2px; text-transform:uppercase; margin-bottom:12px;">📡 Live Network Capture</p>', unsafe_allow_html=True)
        if sniffer and sniffer.running:
            st.success("🛰️ Sniffer Active")
            if st.button("🛑 Stop Live Capture", use_container_width=True, type="primary"):
                sniffer.stop()
                st.rerun()
        else:
            if st.button("🛰️ Start Live Sniffer", use_container_width=True):
                if sniffer: sniffer.start(); st.rerun()

        st.divider()

        st.markdown('<p style="color:var(--text-dim); font-size:0.7rem; font-weight:800; letter-spacing:2px; text-transform:uppercase; margin-bottom:12px;">🎭 Demo Controls</p>', unsafe_allow_html=True)
        st.session_state.demo_armed = st.toggle("🚨 ARM RED ALERT", value=st.session_state.get('demo_armed', False))
        st.session_state.target_ip = st.text_input("🎯 Target Attacker IP", value=st.session_state.get('target_ip', ''), placeholder="e.g. 192.168.1.50")

        if st.button("🚨 TRIGGER EMERGENCY BREACH", use_container_width=True):
            st.session_state.threat_detected = True
            st.rerun()

        st.divider()

        if st.button("🧹 Clear Logs", use_container_width=True):
            if logger: logger.clear_all(); st.session_state.clear(); st.rerun()

        st.markdown(f'''
            <div style="margin-top: 20px; padding: 12px; background: rgba(16,255,153,0.05); border: 1px solid rgba(16,255,153,0.1); border-radius: 12px; text-align: center;">
                <span class="status-dot"></span>
                <span style="color:var(--emerald); font-size: 0.72rem; font-weight: 700;">AI SENTINEL ACTIVE</span>
            </div>
        ''', unsafe_allow_html=True)
