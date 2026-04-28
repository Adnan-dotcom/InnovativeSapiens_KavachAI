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
    border-radius: var(--radius) !important;
    padding: 24px 20px !important;
    box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5) !important;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
    animation: fadeInUp 0.7s cubic-bezier(0.16, 1, 0.3, 1) both;
}
div[data-testid="stMetric"]:hover {
    background: rgba(255,255,255,0.04) !important;
    border-color: var(--border-hover) !important;
    transform: translateY(-5px) !important;
    box-shadow: 0 20px 40px -15px rgba(0,242,255,0.15) !important;
}
div[data-testid="stMetric"] label {
    color: var(--text-dim) !important;
    font-size: 0.7rem !important;
    text-transform: uppercase !important;
    letter-spacing: 1.5px !important;
    font-weight: 700 !important;
    margin-bottom: 4px !important;
}
div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
    color: #fff !important;
    font-weight: 900 !important;
    font-size: 2.2rem !important;
    letter-spacing: -1px !important;
    margin-top: 4px !important;
}
div[data-testid="stMetric"] div[data-testid="stMetricDelta"] { font-size: 0.75rem !important; }
div[data-testid="stMetric"] div[data-testid="stMetricDelta"] svg { display: none !important; }

/* ── Headings ── */
h1 {
    background: linear-gradient(135deg, #fff 0%, var(--text-dim) 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    font-weight: 900 !important;
    font-size: 3.5rem !important;
    letter-spacing: -2px !important;
    margin-bottom: 0.5rem !important;
    animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) both !important;
}
h2, h3 {
    color: #fff !important;
    font-weight: 800 !important;
    letter-spacing: -0.8px !important;
}
h4, h5 {
    color: var(--text-dim) !important;
    font-weight: 500 !important;
    letter-spacing: 0.3px !important;
}

/* ── Sidebar ── */
div[data-testid="stSidebar"] {
    background: rgba(4,4,12,0.95) !important;
    backdrop-filter: blur(32px) !important;
    border-right: 1px solid var(--glass-border) !important;
}
div[data-testid="stSidebar"] > div:first-child {
    animation: slideInLeft 0.4s ease-out both;
}
section[data-testid="stSidebar"] .stButton button {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid var(--glass-border) !important;
    color: var(--text) !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    padding: 12px !important;
    transition: all 0.3s ease !important;
}
section[data-testid="stSidebar"] .stButton button:hover {
    background: var(--cyan-dim) !important;
    border-color: var(--cyan-glow) !important;
    color: var(--cyan) !important;
    transform: translateX(4px) !important;
}

/* ── Buttons (main area) ── */
div.stButton button {
    border-radius: var(--radius-sm) !important;
    font-weight: 600 !important;
    transition: all 0.25s ease !important;
}

/* ── Selectbox / Inputs ── */
div[data-testid="stSelectbox"] > div > div {
    background: var(--glass-bg) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: var(--radius-sm) !important;
}

/* ── Dataframes ── */
div[data-testid="stDataFrame"] {
    border-radius: var(--radius) !important;
    overflow: hidden !important;
    border: 1px solid var(--glass-border) !important;
    animation: fadeInUp 0.5s ease-out both;
}

/* ── Divider ── */
hr {
    border-color: var(--border) !important;
    opacity: 0.5 !important;
}

/* ── Expander ── */
details {
    background: var(--glass-bg) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: var(--radius-sm) !important;
}

/* ── Plotly chart containers ── */
div[data-testid="stPlotlyChart"] {
    animation: fadeInUp 0.5s ease-out both;
}

/* ═══════════════ Custom Component Classes ═══════════════ */

/* Glass card wrapper */
.glass-card {
    background: var(--glass-bg);
    backdrop-filter: blur(24px);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius);
    padding: 28px;
    margin-bottom: 24px;
    box-shadow: 0 10px 40px -10px rgba(0,0,0,0.5);
    animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
}
.glass-card:hover {
    border-color: var(--border-hover);
    box-shadow: 0 15px 50px -15px rgba(0,242,255,0.1);
}

/* Section title */
.section-title {
    font-size: 0.85rem;
    font-weight: 800;
    color: var(--text-dim);
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 12px;
}
.section-title::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--border), transparent);
}

/* Threat event cards */
.threat-card, .normal-card {
    padding: 16px 20px;
    border-radius: 12px;
    margin: 8px 0;
    font-size: 0.9rem;
    background: rgba(255,255,255,0.02);
    border: 1px solid var(--glass-border);
    transition: all 0.3s ease;
    animation: fadeInUp 0.5s ease-out both;
}
.threat-card { border-left: 4px solid var(--coral); }
.normal-card { border-left: 4px solid var(--emerald); }

.threat-card:hover, .normal-card:hover {
    background: rgba(255,255,255,0.05);
    transform: scale(1.01) translateX(4px);
}

/* Status indicator */
.status-dot {
    display: inline-block;
    width: 9px; height: 9px;
    border-radius: 50%;
    background: var(--emerald);
    animation: pulseGlow 2s infinite;
    margin-right: 6px;
    vertical-align: middle;
}

/* Pill badge */
.pill {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}
.pill-critical { background: var(--coral-dim); color: var(--coral); border: 1px solid rgba(255,77,106,0.25); }
.pill-high { background: var(--amber-dim); color: var(--amber); border: 1px solid rgba(255,179,71,0.25); }
.pill-info { background: var(--emerald-dim); color: var(--emerald); border: 1px solid rgba(0,255,136,0.25); }
.pill-online { background: var(--cyan-dim); color: var(--cyan); border: 1px solid rgba(0,212,255,0.25); }

/* Logo section */
.logo-container {
    text-align: center;
    padding: 20px 0 8px 0;
    animation: fadeInUp 0.3s ease-out both;
}
.logo-icon {
    font-size: 2.8rem;
    display: block;
    margin-bottom: 6px;
    filter: drop-shadow(0 0 12px rgba(0,212,255,0.3));
}
.logo-text {
    font-size: 0.9rem;
    font-weight: 800;
    letter-spacing: 3px;
    background: linear-gradient(135deg, var(--cyan), var(--emerald));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
.page-subtitle {
    color: var(--text-dim);
    font-size: 0.88rem;
    font-weight: 400;
    margin-top: -10px;
    margin-bottom: 20px;
    animation: fadeInUp 0.5s ease-out 0.1s both;
}

/* Logo Symbol (The Sentinel Hexagon)
   Meaning: The Hexagon represents structural integrity and cellular defense. 
   The central pulsing core represents the Agentic AI "Self" that never sleeps. */
.kavach-symbol {
    width: 50px;
    height: 50px;
    background: linear-gradient(135deg, var(--cyan), var(--violet));
    clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
    display: flex;
    align-items: center;
    justify-content: center;
    filter: drop-shadow(0 0 10px var(--cyan-glow));
    animation: float 4s infinite ease-in-out;
    margin: 10px auto; /* Added margin to prevent cropping */
    flex-shrink: 0;
}
.kavach-symbol::after {
    content: '';
    width: 10px;
    height: 10px;
    background: #fff;
    border-radius: 50%;
    box-shadow: 0 0 15px #fff, 0 0 30px var(--cyan);
    animation: pulseGlow 2s infinite;
}

/* Version badge */
.version-badge {
    text-align: center;
    padding: 6px 0;
    font-size: 0.7rem;
    color: var(--text-dim);
    letter-spacing: 0.5px;
}

/* Info card for model architecture etc */
.info-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    font-size: 0.85rem;
}
.info-table tr {
    transition: background 0.2s ease;
}
.info-table tr:hover {
    background: var(--surface-hover);
}
.info-table td {
    padding: 10px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
}
.info-table td:first-child {
    color: var(--text-dim);
    font-weight: 600;
    width: 35%;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}

/* Filter bar */
.filter-bar {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius);
    padding: 14px 18px;
    margin-bottom: 16px;
    animation: fadeInUp 0.4s ease-out both;
}

/* Staggered animation delays for cards */
.delay-1 { animation-delay: 0.05s !important; }
.delay-2 { animation-delay: 0.10s !important; }
.delay-3 { animation-delay: 0.15s !important; }
.delay-4 { animation-delay: 0.20s !important; }
.delay-5 { animation-delay: 0.25s !important; }
.delay-6 { animation-delay: 0.30s !important; }
.delay-7 { animation-delay: 0.35s !important; }
.delay-8 { animation-delay: 0.40s !important; }

/* ── Minimalist Glass Cards ── */
.glass-card {
    background: var(--glass-bg) !important;
    backdrop-filter: blur(20px) saturate(180%) !important;
    -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: 24px !important;
    padding: 30px !important;
    margin-bottom: 20px !important;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
}
.glass-card:hover {
    border-color: rgba(0, 242, 255, 0.3) !important;
    transform: translateY(-5px) !important;
}

.section-title {
    font-size: 0.85rem !important;
    font-weight: 800 !important;
    color: var(--text-dim) !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
    margin-bottom: 25px !important;
}

/* Hide default streamlit padding bloat */
.block-container { padding-top: 2rem !important; padding-bottom: 1rem !important; }
div[data-testid="stSidebarContent"] { padding-top: 0 !important; }

</style>"""


# ── Chart theme helper ──
CHART_LAYOUT = dict(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#c0c0e0', family='Inter', size=12),
    margin=dict(t=10, b=30, l=40, r=10),
    xaxis=dict(gridcolor='rgba(255,255,255,0.04)', zeroline=False),
    yaxis=dict(gridcolor='rgba(255,255,255,0.04)', zeroline=False),
    legend=dict(font=dict(color='#c0c0e0', size=11), bgcolor='rgba(0,0,0,0)'),
    hoverlabel=dict(bgcolor='#111127', font_color='#e0e0ff', bordercolor='rgba(0,212,255,0.3)'),
)

COLORS = {
    'cyan':    '#00d4ff',
    'emerald': '#00ff88',
    'coral':   '#ff4d6a',
    'amber':   '#ffb347',
    'violet':  '#a78bfa',
    'rose':    '#f472b6',
}

PIE_COLORS = ['#ff4d6a', '#ffb347', '#a78bfa', '#f472b6', '#00d4ff']
BAR_COLORS = ['#ff4d6a', '#ffb347', '#a78bfa', '#f472b6', '#00d4ff']
PROTO_COLORS = {'TCP': '#00d4ff', 'UDP': '#ffb347', 'ICMP': '#ff4d6a'}


def inject_css(st):
    """Call at top of every page to inject the shared design system."""
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

def render_sidebar_controls(st, logger=None, simulator=None, sniffer=None):
    """Shared sidebar controls for consistent global navigation and simulation."""
    with st.sidebar:
        st.markdown(f'''
            <div style="text-align: center; padding: 20px 0;">
                <div style="font-size: 1.8rem; font-weight: 900; letter-spacing: -1px; color: #fff;">🛡️ KAVACH</div>
                <div style="font-size: 0.65rem; font-weight: 700; color: var(--cyan); letter-spacing: 3px; margin-top: 5px;">AGENTIC CORE v2.5</div>
            </div>
        ''', unsafe_allow_html=True)
        
        st.divider()
        
        # ── Attack Simulation ──
        st.markdown('<p style="color:var(--text-dim); font-size:0.7rem; font-weight:800; letter-spacing:2px; text-transform:uppercase; margin-bottom:12px;">⚡ Attack Simulation</p>', unsafe_allow_html=True)
        scenario = st.selectbox("Scenario", ["mixed", "ddos", "port_scan", "brute_force", "dns_amp", "normal"], label_visibility="collapsed")
        
        if st.button("🚀 Launch Simulation", use_container_width=True):
            if simulator:
                with st.spinner("Injecting scenarios..."):
                    results = simulator.run_scenario(scenario)
                    st.toast(f"Detected {len([r for r in results if r['is_threat']])} threats!", icon="🛡️")
                    st.rerun()
            else:
                st.error("Simulator Unavailable")

        st.divider()

        # ── Live Capture ──
        st.markdown('<p style="color:var(--text-dim); font-size:0.7rem; font-weight:800; letter-spacing:2px; text-transform:uppercase; margin-bottom:12px;">📡 Live Network Capture</p>', unsafe_allow_html=True)
        
        if sniffer and sniffer.running:
            if st.button("🛑 Stop Live Capture", use_container_width=True, type="primary"):
                sniffer.stop()
                st.rerun()
        else:
            if st.button("🛰️ Start Live Sniffer", use_container_width=True):
                if sniffer:
                    sniffer.start()
                    st.toast("Neural Sniffer Active", icon="📡")
                    st.rerun()
                else:
                    st.error("Sniffer Unavailable")

        st.divider()
        
        if st.button("🧹 Clear Logs", use_container_width=True):
            if logger:
                logger.clear_all()
                st.session_state.clear()
                st.rerun()

        st.markdown(f'''
            <div style="margin-top: 20px; padding: 12px; background: rgba(16,255,153,0.05); border: 1px solid rgba(16,255,153,0.1); border-radius: 12px; text-align: center;">
                <span class="status-dot"></span>
                <span style="color:var(--emerald); font-size: 0.72rem; font-weight: 700;">AI SENTINEL ACTIVE</span>
            </div>
        ''', unsafe_allow_html=True)
