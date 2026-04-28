"""Kavach AI — Guardian-IoT: Edge-AI for Smart Infrastructure"""
import random
from datetime import datetime, timedelta

class GuardianIoT:
    DEVICE_CATALOG = [
        {'name': 'Smart Thermostat', 'brand': 'Nest', 'type': 'Climate', 'icon': '🌡️', 'ports': [443, 8883]},
        {'name': 'IP Camera - Front', 'brand': 'Ring', 'type': 'Security', 'icon': '📷', 'ports': [554, 80]},
        {'name': 'IP Camera - Back', 'brand': 'Hikvision', 'type': 'Security', 'icon': '📹', 'ports': [554, 8080]},
        {'name': 'Smart Lock', 'brand': 'August', 'type': 'Access', 'icon': '🔒', 'ports': [443]},
        {'name': 'Smart Fridge', 'brand': 'Samsung', 'type': 'Appliance', 'icon': '🧊', 'ports': [443, 8080]},
        {'name': 'Smart TV', 'brand': 'LG WebOS', 'type': 'Entertainment', 'icon': '📺', 'ports': [443, 3000]},
        {'name': 'Voice Assistant', 'brand': 'Alexa', 'type': 'Hub', 'icon': '🔊', 'ports': [443, 8443]},
        {'name': 'Robot Vacuum', 'brand': 'Roborock', 'type': 'Appliance', 'icon': '🤖', 'ports': [443]},
        {'name': 'Smart Plug', 'brand': 'TP-Link', 'type': 'Power', 'icon': '🔌', 'ports': [9999]},
        {'name': 'Smart Doorbell', 'brand': 'Ring', 'type': 'Security', 'icon': '🚪', 'ports': [443, 8555]},
        {'name': 'Mesh Router', 'brand': 'Eero', 'type': 'Network', 'icon': '📡', 'ports': [443, 80]},
        {'name': 'Smart Bulb', 'brand': 'Philips Hue', 'type': 'Lighting', 'icon': '💡', 'ports': [443, 80]},
    ]
    ANOMALY_TYPES = [
        ('Lateral Movement', 'critical', 'Device accessing unauthorized segment'),
        ('Cryptojacking', 'critical', 'Unusual CPU/power — possible mining'),
        ('Data Exfiltration', 'high', 'Abnormal outbound data volume'),
        ('Firmware Tampering', 'critical', 'Firmware hash mismatch'),
        ('Port Scanning', 'high', 'Scanning ports outside normal behavior'),
        ('DNS Tunneling', 'high', 'Suspicious DNS query patterns'),
    ]
    CVE_DB = [
        {'id': 'CVE-2026-1847', 'brand': 'Ring', 'sev': 'Critical', 'desc': 'RCE via RTSP overflow'},
        {'id': 'CVE-2026-2103', 'brand': 'Hikvision', 'sev': 'Critical', 'desc': 'Auth bypass in web UI'},
        {'id': 'CVE-2026-0891', 'brand': 'TP-Link', 'sev': 'High', 'desc': 'Hardcoded credentials'},
        {'id': 'CVE-2026-3344', 'brand': 'Samsung', 'sev': 'High', 'desc': 'MQTT injection'},
        {'id': 'CVE-2026-4201', 'brand': 'LG WebOS', 'sev': 'Critical', 'desc': 'Unauth root shell'},
    ]

    def generate_device_inventory(self):
        devices = []
        for i, dev in enumerate(self.DEVICE_CATALOG):
            comp = random.random() < 0.12
            off = random.random() < 0.08
            mac = ':'.join([f'{random.randint(0,255):02x}' for _ in range(6)])
            cpu = round(random.uniform(60, 98) if comp else random.uniform(2, 35), 1)
            pwr = round(random.uniform(8, 25) if comp else random.uniform(0.5, 6), 1)
            devices.append({
                'id': i+1, 'name': dev['name'], 'brand': dev['brand'], 'type': dev['type'], 'icon': dev['icon'],
                'ip': f"192.168.1.{100+i}", 'mac': mac.upper(),
                'status': 'COMPROMISED' if comp else 'OFFLINE' if off else 'HEALTHY',
                'cpu': cpu, 'power': pwr, 'ports': dev['ports'],
                'firmware': f"v{random.randint(2,5)}.{random.randint(0,9)}.{random.randint(0,99)}",
                'risk': round(random.uniform(0.7, 0.99) if comp else random.uniform(0.01, 0.25), 2),
            })
        return devices

    def generate_anomalies(self, count=8):
        events = []
        now = datetime.now()
        for _ in range(count):
            at, sev, desc = random.choice(self.ANOMALY_TYPES)
            dev = random.choice(self.DEVICE_CATALOG)
            ts = now - timedelta(minutes=random.randint(1, 720))
            action = random.choice(['Connection severed', 'Port blocked', 'Device quarantined', 'Alert escalated'])
            events.append({'timestamp': ts.strftime('%Y-%m-%dT%H:%M:%S'),
                'device': f"{dev['icon']} {dev['name']}", 'brand': dev['brand'],
                'anomaly': at, 'severity': sev, 'description': desc,
                'action': action, 'resolved': random.choice([True, False])})
        events.sort(key=lambda x: x['timestamp'], reverse=True)
        return events

    def generate_firewall_rules(self):
        rules = []
        for i, cve in enumerate(self.CVE_DB):
            for dev in [d for d in self.DEVICE_CATALOG if d['brand'] == cve['brand']]:
                rules.append({'id': f"FW-{2000+len(rules)}", 'cve': cve['id'],
                    'device': f"{dev['icon']} {dev['name']}",
                    'rule': f"DENY {dev['name']} → ANY:{dev['ports'][0]}",
                    'severity': cve['sev'], 'desc': cve['desc'], 'status': 'ACTIVE'})
        return rules

    def generate_energy_data(self):
        hours = list(range(24))
        baseline = [round(random.uniform(1.5, 4.0), 1) for _ in hours]
        actual = list(baseline)
        spike = random.randint(1, 18)
        for h in range(spike, min(spike+4, 24)):
            actual[h] = round(actual[h] + random.uniform(6, 15), 1)
        return {'hours': [f"{h:02d}:00" for h in hours], 'baseline': baseline, 'actual': actual}
