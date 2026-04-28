"""Kavach AI — DeepTrust: Multi-Modal Identity Verification Engine"""
import random
from datetime import datetime, timedelta

class DeepTrust:
    """Simulates deepfake detection, voiceprint analysis, and contextual risk scoring."""

    NAMES = ['Rahul Sharma', 'Priya Patel', 'Arjun Singh', 'Sneha Gupta', 'Vikram Reddy',
             'Anjali Nair', 'Karan Mehta', 'Divya Iyer', 'Rohan Joshi', 'Neha Kapoor']
    PLATFORMS = ['Zoom', 'Google Meet', 'Microsoft Teams', 'Slack Huddle', 'WhatsApp Video',
                 'LinkedIn Message', 'Email', 'Telegram', 'Discord', 'Phone Call']
    INTENTS = ['Wire Transfer Request', 'Password Reset', 'Access Grant', 'Document Signing',
               'Vendor Payment', 'Code Deploy Approval', 'NDA Review', 'Salary Discussion',
               'Client Data Access', 'Infrastructure Change']

    DEEPFAKE_ARTIFACTS = [
        'Inconsistent eye blinking pattern', 'Lighting direction mismatch',
        'Facial boundary artifacts', 'Temporal flickering detected',
        'Lip-sync desynchronization', 'Unnatural head movement', 
        'Skin texture anomaly', 'Pupil reflection inconsistency',
        'Ear geometry distortion', 'Hair rendering artifacts',
    ]

    VOICE_ARTIFACTS = [
        'Spectral flatness anomaly', 'Missing micro-tremors',
        'Unnatural pitch transitions', 'Breathing pattern absent',
        'Formant frequency deviation', 'Background noise consistency',
        'Vocal fry missing', 'Phoneme transition smoothing',
    ]

    def scan_video_calls(self, count=8):
        """Generate video call authenticity scans."""
        scans = []
        now = datetime.now()
        for i in range(count):
            is_deepfake = random.random() < 0.3
            person = random.choice(self.NAMES)
            platform = random.choice(self.PLATFORMS[:5])
            ts = now - timedelta(minutes=random.randint(5, 2880))

            if is_deepfake:
                auth_score = round(random.uniform(0.08, 0.35), 2)
                artifacts = random.sample(self.DEEPFAKE_ARTIFACTS, random.randint(2, 5))
                verdict = 'DEEPFAKE DETECTED'
            else:
                auth_score = round(random.uniform(0.82, 0.99), 2)
                artifacts = []
                verdict = 'VERIFIED AUTHENTIC'

            scans.append({
                'timestamp': ts.strftime('%Y-%m-%dT%H:%M:%S'),
                'person': person,
                'platform': platform,
                'authenticity_score': auth_score,
                'verdict': verdict,
                'is_fake': is_deepfake,
                'artifacts': artifacts,
                'frame_analysis': random.randint(120, 1800),
                'blink_rate': round(random.uniform(2, 8) if is_deepfake else random.uniform(12, 22), 1),
                'micro_expression_score': round(random.uniform(0.1, 0.4) if is_deepfake else random.uniform(0.7, 0.95), 2),
            })
        scans.sort(key=lambda x: x['timestamp'], reverse=True)
        return scans

    def analyze_voiceprints(self, count=6):
        """Generate voice authenticity analysis."""
        results = []
        for i in range(count):
            is_cloned = random.random() < 0.25
            person = random.choice(self.NAMES)
            results.append({
                'person': person,
                'is_cloned': is_cloned,
                'match_score': round(random.uniform(0.15, 0.45) if is_cloned else random.uniform(0.88, 0.99), 2),
                'verdict': 'AI-GENERATED VOICE' if is_cloned else 'AUTHENTIC VOICE',
                'artifacts': random.sample(self.VOICE_ARTIFACTS, random.randint(2, 4)) if is_cloned else [],
                'frequency_bands_analyzed': random.randint(64, 256),
                'duration_analyzed': f"{random.randint(5, 120)}s",
                'neural_confidence': round(random.uniform(0.80, 0.98), 2),
            })
        return results

    def assess_communication_risk(self, count=8):
        """Generate contextual risk assessments for communications."""
        assessments = []
        now = datetime.now()
        for i in range(count):
            person = random.choice(self.NAMES)
            platform = random.choice(self.PLATFORMS)
            intent = random.choice(self.INTENTS)
            is_suspicious = random.random() < 0.35
            ts = now - timedelta(minutes=random.randint(5, 4320))

            risk_factors = []
            if is_suspicious:
                risk_factors = random.sample([
                    'Unusual time of request', 'First contact via this platform',
                    'High-value financial request', 'Urgency language detected',
                    'Sender identity unverified', 'Request bypasses normal workflow',
                    'New device/location detected', 'Impersonation indicators',
                ], random.randint(2, 4))

            risk_score = round(random.uniform(0.65, 0.95) if is_suspicious else random.uniform(0.05, 0.35), 2)
            assessments.append({
                'timestamp': ts.strftime('%Y-%m-%dT%H:%M:%S'),
                'person': person,
                'platform': platform,
                'intent': intent,
                'risk_score': risk_score,
                'risk_level': 'CRITICAL' if risk_score > 0.8 else 'HIGH' if risk_score > 0.6 else 'MEDIUM' if risk_score > 0.3 else 'LOW',
                'risk_factors': risk_factors,
                'action': 'BLOCKED & FLAGGED' if risk_score > 0.8 else 'FLAGGED FOR REVIEW' if risk_score > 0.6 else 'MONITORED' if risk_score > 0.3 else 'ALLOWED',
            })
        assessments.sort(key=lambda x: x['risk_score'], reverse=True)
        return assessments
