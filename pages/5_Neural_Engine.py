import streamlit as st
import sys, os, json, numpy as np, pandas as pd
import plotly.graph_objects as go
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import METRICS_PATH
from styles import inject_css, CHART_LAYOUT, COLORS, render_sidebar_controls
from utils import init_kavach

st.set_page_config(page_title="Neural Engine | Kavach AI", page_icon="🧠", layout="wide")
inject_css(st)

logger, detector, guardian, simulator, sniffer = init_kavach()
render_sidebar_controls(st, logger, simulator, sniffer)

if not os.path.exists(METRICS_PATH):
    st.error("Model metrics not found. Run train_model.py first!")
    st.stop()

with open(METRICS_PATH) as f:
    metrics = json.load(f)

st.markdown('''
    <div style="text-align: center; margin-top: 20px; margin-bottom: 40px;">
        <h1 style="font-size: 3rem; font-weight: 900; letter-spacing: -1.5px; margin-bottom: 5px; color: #fff;">NEURAL ENGINE</h1>
        <div style="font-size: 0.8rem; font-weight: 700; color: var(--cyan); letter-spacing: 4px; text-transform: uppercase;">XAI & Deep Learning Metrics</div>
    </div>
''', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown('<div class="glass-card"><div class="section-title">🔬 Feature Sensitivity (XAI)</div>', unsafe_allow_html=True)
    imp = metrics['feature_importance']
    sorted_feats = sorted(imp.items(), key=lambda x: x[1], reverse=True)
    names = [f[0].replace('_', ' ').title() for f in sorted_feats]
    values = [f[1] for f in sorted_feats]
    fig = go.Figure(data=[go.Bar(x=values, y=names, orientation='h', marker=dict(color=COLORS['cyan']))])
    fig.update_layout({**CHART_LAYOUT, 'height': 300, 'margin': dict(t=10, b=10, l=120, r=10)})
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass-card"><div class="section-title">🎯 Confusion Matrix</div>', unsafe_allow_html=True)
    cm = np.array(metrics['confusion_matrix'])
    fig = go.Figure(data=go.Heatmap(z=cm, x=metrics['class_names'], y=metrics['class_names'], colorscale=[[0, '#020205'], [1, COLORS['cyan']]], text=cm, texttemplate="%{text}", showscale=False))
    fig.update_layout({**CHART_LAYOUT, 'height': 300})
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="glass-card"><div class="section-title">🏗️ Architecture Blueprint</div>', unsafe_allow_html=True)
st.markdown(f'''
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;">
    <div class="normal-card"><strong>Core:</strong> Random Forest Ensemble</div>
    <div class="normal-card"><strong>Trees:</strong> 200 Stimulated Decisors</div>
    <div class="normal-card"><strong>Inference:</strong> < 0.5ms/packet</div>
    <div class="normal-card"><strong>Precision:</strong> {metrics['accuracy']:.1%}</div>
    <div class="normal-card"><strong>Samples:</strong> {metrics['train_size']:,}</div>
    <div class="normal-card"><strong>Classes:</strong> {len(metrics['class_names'])}</div>
</div>
''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
