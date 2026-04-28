"""Kavach AI — ShadowGuard: AI Decoy & Deception Engine"""
import random, hashlib, time
from datetime import datetime, timedelta

class ShadowGuard:
    """Generates honeyfiles, tracks intruder behavior, and fingerprints attackers."""

    HONEYFILE_TEMPLATES = [
        {'name': 'passwords_2026.xlsx', 'type': 'Credentials', 'icon': '🔑', 'risk': 'critical'},
        {'name': 'private_keys.json', 'type': 'Crypto Keys', 'icon': '🔐', 'risk': 'critical'},
        {'name': 'employee_salaries.csv', 'type': 'Financial', 'icon': '💰', 'risk': 'high'},
        {'name': 'board_meeting_notes.docx', 'type': 'Confidential', 'icon': '📝', 'risk': 'high'},
        {'name': 'aws_credentials.env', 'type': 'Cloud Access', 'icon': '☁️', 'risk': 'critical'},
        {'name': 'database_backup.sql', 'type': 'Database', 'icon': '🗃️', 'risk': 'critical'},
        {'name': 'vpn_config.ovpn', 'type': 'Network', 'icon': '🌐', 'risk': 'high'},
        {'name': 'customer_data_export.csv', 'type': 'PII Data', 'icon': '👥', 'risk': 'critical'},
        {'name': 'api_tokens.yaml', 'type': 'API Access', 'icon': '🎫', 'risk': 'high'},
        {'name': 'ssh_id_rsa', 'type': 'SSH Keys', 'icon': '🔒', 'risk': 'critical'},
        {'name': 'bitcoin_wallet.dat', 'type': 'Crypto Wallet', 'icon': '₿', 'risk': 'critical'},
        {'name': 'admin_panel_creds.txt', 'type': 'Admin Access', 'icon': '⚙️', 'risk': 'critical'},
    ]

    DECOY_PATHS = [
        '/home/admin/.ssh/', '/var/backups/confidential/', '/opt/secrets/',
        '/srv/finance/reports/', '/home/ceo/documents/', '/etc/vault/',
        'C:\\Users\\Admin\\Desktop\\', 'C:\\Backup\\Sensitive\\',
        '/root/.config/keys/', '/mnt/shared/executive/',
    ]

    ATTACKER_IPS = [
        ('185.220.101.42', 'Moscow, Russia', '🇷🇺'), ('45.155.205.89', 'Beijing, China', '🇨🇳'),
        ('194.26.135.17', 'Pyongyang, DPRK', '🇰🇵'), ('103.75.201.55', 'Tehran, Iran', '🇮🇷'),
        ('91.240.118.33', 'São Paulo, Brazil', '🇧🇷'), ('162.247.74.201', 'Tor Exit Node', '🌐'),
        ('23.129.64.15', 'VPN - Unknown', '🕵️'), ('5.188.62.98', 'Bucharest, Romania', '🇷🇴'),
        ('77.247.181.42', 'Amsterdam, NL', '🇳🇱'), ('198.98.51.189', 'Dark Web Proxy', '🕸️'),
    ]

    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64)', 'python-requests/2.31.0',
        'curl/8.4.0', 'Wget/1.21.3', 'Go-http-client/2.0',
        'Nmap Scripting Engine', 'Metasploit/6.3', 'Cobalt Strike/4.9',
    ]

    def generate_deployed_honeyfiles(self, count=8):
        """Generate a set of deployed decoy files."""
        selected = random.sample(self.HONEYFILE_TEMPLATES, min(count, len(self.HONEYFILE_TEMPLATES)))
        files = []
        for i, tmpl in enumerate(selected):
            path = random.choice(self.DECOY_PATHS)
            deployed = datetime.now() - timedelta(hours=random.randint(1, 720))
            trips = random.randint(0, 12)
            files.append({
                'id': i + 1,
                'name': tmpl['name'],
                'type': tmpl['type'],
                'icon': tmpl['icon'],
                'risk': tmpl['risk'],
                'path': path + tmpl['name'],
                'deployed': deployed.strftime('%Y-%m-%d %H:%M'),
                'trips': trips,
                'status': 'TRIGGERED' if trips > 0 else 'DEPLOYED',
                'hash': hashlib.md5(tmpl['name'].encode()).hexdigest()[:12],
            })
        return files

    def generate_trip_events(self, count=10):
        """Generate honeyfile access events (trips)."""
        events = []
        now = datetime.now()
        for i in range(count):
            ip, loc, flag = random.choice(self.ATTACKER_IPS)
            file = random.choice(self.HONEYFILE_TEMPLATES)
            ts = now - timedelta(minutes=random.randint(1, 1440))
            ua = random.choice(self.USER_AGENTS)
            is_bot = 'bot' if ua in self.USER_AGENTS[4:] else 'human'
            events.append({
                'timestamp': ts.strftime('%Y-%m-%dT%H:%M:%S'),
                'ip': ip,
                'location': loc,
                'flag': flag,
                'file': file['name'],
                'file_type': file['type'],
                'user_agent': ua,
                'classification': is_bot,
                'dwell_time': round(random.uniform(0.5, 45.0), 1),
                'actions': random.randint(1, 25),
                'confidence': round(random.uniform(0.75, 0.99), 2),
            })
        events.sort(key=lambda x: x['timestamp'], reverse=True)
        return events

    def generate_behavioral_profile(self):
        """Generate behavioral fingerprint analysis."""
        profiles = []
        for ip, loc, flag in random.sample(self.ATTACKER_IPS, 5):
            is_bot = random.choice([True, False])
            profiles.append({
                'ip': ip,
                'location': f"{flag} {loc}",
                'classification': 'Automated Bot' if is_bot else 'Human Operator',
                'mouse_entropy': round(random.uniform(0.1, 0.4) if is_bot else random.uniform(0.6, 0.95), 2),
                'typing_rhythm': round(random.uniform(0.95, 0.99) if is_bot else random.uniform(0.4, 0.8), 2),
                'navigation_pattern': 'Linear Scan' if is_bot else 'Exploratory',
                'session_duration': f"{random.randint(1, 120)}m" if not is_bot else f"{random.randint(1, 30)}s",
                'risk_score': round(random.uniform(0.7, 0.99), 2),
                'files_accessed': random.randint(1, 30) if is_bot else random.randint(1, 8),
            })
        return profiles
