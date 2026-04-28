import streamlit as st
import sys, os
from config import *
from core.logger import ThreatLogger
from core.detector import ThreatDetector
from core.guardian import AutonomousGuardian
from core.simulator import AttackSimulator

def init_kavach():
    """Initializes and returns shared Kavach AI components."""
    logger = ThreatLogger(DB_PATH)
    try:
        from core.sniffer import NetworkSniffer
        detector = ThreatDetector(MODEL_PATH)
        guardian = AutonomousGuardian(demo_mode=DEMO_MODE)
        simulator = AttackSimulator(detector, guardian, logger)
        sniffer = NetworkSniffer(detector, guardian, logger)
        return logger, detector, guardian, simulator, sniffer
    except Exception:
        return logger, None, None, None, None
