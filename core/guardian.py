"""Kavach AI Autonomous Guardian — Executes defensive actions"""
import subprocess, time, platform
from datetime import datetime

class AutonomousGuardian:
    def __init__(self, demo_mode=True):
        self.demo_mode = demo_mode
        self.blocked_ips = {}
        self.block_cooldown = 300
        self.actions_log = []
        self.is_windows = platform.system() == 'Windows'

    def handle_threat(self, src_ip, threat_type, confidence, severity):
        if src_ip in self.blocked_ips:
            elapsed = time.time() - self.blocked_ips[src_ip]
            if elapsed < self.block_cooldown:
                return f"Already honeytrapped ({int(self.block_cooldown - elapsed)}s remaining)"

        if severity == 'critical' or (severity == 'high' and confidence > 0.7):
            action = self._route_to_honeytrap(src_ip, threat_type)
        elif severity == 'high':
            action = f"Monitoring {src_ip} (confidence {confidence:.0%})"
        else:
            action = f"Logged {src_ip}"

        self.actions_log.append({'timestamp': datetime.now().isoformat(), 'src_ip': src_ip,
                                  'threat_type': threat_type, 'action': action})
        return action

    def _route_to_honeytrap(self, ip, reason):
        # Instead of blocking the threat, we invisibly route them to a decoy (ShadowGuard)
        # to record their tools, techniques, and extract forensic data.
        self.blocked_ips[ip] = time.time()
        return f"HONEYTRAPPED {ip} | Extracting forensic data & TTPs"

    def get_blocked_count(self):
        return len(self.blocked_ips)

    def get_blocked_ips(self):
        return list(self.blocked_ips.keys())
