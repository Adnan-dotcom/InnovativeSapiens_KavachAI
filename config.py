"""Kavach AI Central Configuration"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, 'models')
MODEL_PATH = os.path.join(MODEL_DIR, 'sentinel_brain.pkl')
METRICS_PATH = os.path.join(MODEL_DIR, 'model_metrics.json')
DB_PATH = os.path.join(BASE_DIR, 'sentinel.db')

FEATURE_NAMES = ['packet_length', 'protocol', 'src_port', 'dst_port']

ATTACK_TYPES = {0: 'Normal', 1: 'DDoS Attack', 2: 'Port Scan', 3: 'Brute Force', 4: 'DNS Amplification'}
ATTACK_SEVERITY = {'Normal': 'info', 'DDoS Attack': 'critical', 'Port Scan': 'high', 'Brute Force': 'high', 'DNS Amplification': 'critical'}
ATTACK_COLORS = {'Normal': '#00ff88', 'DDoS Attack': '#ff4444', 'Port Scan': '#ff8800', 'Brute Force': '#ff6600', 'DNS Amplification': '#ff2222'}

DEMO_MODE = True
BLOCK_COOLDOWN = 300
