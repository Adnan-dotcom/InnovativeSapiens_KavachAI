import streamlit as st
import sys, os
from config import *
from core.logger import ThreatLogger
from core.detector import ThreatDetector
from core.guardian import AutonomousGuardian
from core.simulator import AttackSimulator
from core.honeypot import HoneyportServer

@st.cache_resource
def init_kavach():
    """Initializes and returns shared Kavach AI components."""
    logger = ThreatLogger(DB_PATH)
    # Initialize Honeyport separately for reliability
    honeyport = None
    try:
        honeyport = HoneyportServer(port=9999)
        honeyport.start()
    except Exception as e:
        print(f"Honeyport failed to start: {e}")

    try:
        from core.sniffer import NetworkSniffer
        detector = ThreatDetector(MODEL_PATH)
        guardian = AutonomousGuardian(demo_mode=DEMO_MODE)
        simulator = AttackSimulator(detector, guardian, logger)
        sniffer = NetworkSniffer(detector, guardian, logger)
        return logger, detector, guardian, simulator, sniffer, honeyport
    except Exception as e:
        return logger, None, None, None, None, honeyport
