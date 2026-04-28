"""Kavach AI — Ransomware Shield: Detection & Protection Engine"""
import random, hashlib
from datetime import datetime, timedelta

class RansomwareShield:
    RANSOMWARE_FAMILIES = [
        {'name': 'LockBit 4.0', 'type': 'Encryption', 'icon': '🔴', 'ext': '.lockbit4', 'severity': 'critical'},
        {'name': 'BlackCat/ALPHV', 'type': 'Double Extortion', 'icon': '🐱', 'ext': '.alphv', 'severity': 'critical'},
        {'name': 'Cl0p', 'type': 'Data Theft', 'icon': '💀', 'ext': '.cl0p', 'severity': 'critical'},
        {'name': 'Royal', 'type': 'Encryption', 'icon': '👑', 'ext': '.royal', 'severity': 'critical'},
        {'name': 'Play', 'type': 'Double Extortion', 'icon': '🎭', 'ext': '.play', 'severity': 'critical'},
        {'name': 'Akira', 'type': 'Hybrid', 'icon': '⚡', 'ext': '.akira', 'severity': 'critical'},
        {'name': 'Medusa', 'type': 'Triple Extortion', 'icon': '🐍', 'ext': '.medusa', 'severity': 'critical'},
        {'name': 'Rhysida', 'type': 'Encryption', 'icon': '🦂', 'ext': '.rhysida', 'severity': 'high'},
    ]
    INDICATORS = [
        'Mass file rename operations', 'Entropy spike in file contents',
        'Shadow copy deletion attempt', 'Registry persistence modification',
        'Suspicious PowerShell execution', 'Abnormal API call sequence',
        'Network beacon to C2 server', 'Rapid file extension changes',
        'Volume shadow service terminated', 'Anomalous encryption API usage',
    ]
    TARGET_DIRS = [
        'C:\\Users\\Documents', 'C:\\Users\\Desktop', 'C:\\Projects',
        'D:\\Backups', 'C:\\Database', '\\\\FileServer\\Shared',
        'C:\\Users\\Pictures', 'C:\\Financial', 'C:\\HR_Records',
    ]

    def get_protection_status(self):
        return {
            'real_time': True, 'behavior_monitor': True, 'signature_db': True,
            'honeypot_traps': True, 'backup_integrity': random.choice([True, True, True, False]),
            'last_signature_update': (datetime.now() - timedelta(hours=random.randint(1, 12))).strftime('%Y-%m-%d %H:%M'),
            'signatures_loaded': random.randint(12000, 18000),
            'files_protected': random.randint(45000, 120000),
            'canary_files': random.randint(50, 200),
            'rollback_points': random.randint(3, 8),
        }

    def generate_detections(self, count=8):
        events = []
        now = datetime.now()
        for _ in range(count):
            family = random.choice(self.RANSOMWARE_FAMILIES)
            ts = now - timedelta(minutes=random.randint(1, 2880))
            target = random.choice(self.TARGET_DIRS)
            indicators = random.sample(self.INDICATORS, random.randint(2, 5))
            files_affected = random.randint(0, 45)
            action = random.choice(['BLOCKED', 'BLOCKED', 'BLOCKED', 'QUARANTINED', 'ROLLED BACK'])
            events.append({
                'timestamp': ts.strftime('%Y-%m-%dT%H:%M:%S'),
                'family': family['name'], 'type': family['type'],
                'icon': family['icon'], 'severity': family['severity'],
                'target_dir': target, 'files_affected': files_affected,
                'files_recovered': files_affected if action == 'ROLLED BACK' else 0,
                'indicators': indicators, 'action': action,
                'hash': hashlib.sha256(f"{family['name']}{ts}".encode()).hexdigest()[:16],
                'confidence': round(random.uniform(0.88, 0.99), 2),
            })
        events.sort(key=lambda x: x['timestamp'], reverse=True)
        return events

    def generate_signature_db(self):
        sigs = []
        for fam in self.RANSOMWARE_FAMILIES:
            variants = random.randint(5, 30)
            sigs.append({
                'family': fam['name'], 'icon': fam['icon'], 'type': fam['type'],
                'variants': variants, 'severity': fam['severity'],
                'detection_rate': round(random.uniform(0.95, 0.999), 3),
                'last_seen': (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d'),
                'hashes': [hashlib.md5(f"{fam['name']}_v{i}".encode()).hexdigest()[:12] for i in range(min(3, variants))],
            })
        return sigs

    def generate_file_monitor(self):
        now = datetime.now()
        entries = []
        for _ in range(12):
            is_suspicious = random.random() < 0.2
            d = random.choice(self.TARGET_DIRS)
            ext = random.choice(['.docx','.xlsx','.pdf','.jpg','.py','.sql','.bak'])
            fname = f"file_{random.randint(100,999)}{ext}"
            entries.append({
                'time': (now - timedelta(seconds=random.randint(1, 300))).strftime('%H:%M:%S'),
                'file': f"{d}\\{fname}", 'operation': random.choice(['MODIFIED','CREATED','RENAMED','DELETED']),
                'entropy': round(random.uniform(7.2, 7.99) if is_suspicious else random.uniform(3.0, 6.5), 2),
                'suspicious': is_suspicious,
                'process': 'unknown.exe' if is_suspicious else random.choice(['explorer.exe','word.exe','python.exe']),
            })
        entries.sort(key=lambda x: x['time'], reverse=True)
        return entries
