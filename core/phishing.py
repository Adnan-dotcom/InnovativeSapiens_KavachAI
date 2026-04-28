"""Kavach AI — PhishGuard: NLP-based Phishing & Social Engineering Defense"""
import random
from datetime import datetime, timedelta

class PhishGuard:
    SENDERS = ['support@paypal-security.com', 'admin@hr-portal.internal', 'ceo.urgent@company.com', 'alert@aws-billing.net', 'IT-Desk@slack-msg.com']
    PLATFORMS = ['Email', 'Slack', 'Teams', 'Discord', 'SMS']
    
    PHISHING_PATTERNS = [
        "Urgent: Your account will be suspended in 24 hours. Click here to verify.",
        "Kindly review the attached invoice for your recent purchase of $1,299.",
        "Hi, I'm stuck in a meeting. Can you quickly buy some gift cards for a client?",
        "Security Alert: Unauthorized login attempt from Russia. Reset your password immediately.",
        "You have a new encrypted voice message from HR. Listen here."
    ]
    
    NORMAL_PATTERNS = [
        "Hey team, here are the meeting notes from yesterday's sync.",
        "Can we reschedule our 1 PM to 2 PM? Thanks.",
        "The new deployment is live. Please test your endpoints.",
        "Lunch in 10 mins? Meet at the usual spot.",
        "Attached is the Q3 financial report for your review."
    ]

    def scan_messages(self, count=8):
        results = []
        now = datetime.now()
        for i in range(count):
            is_phishing = random.random() < 0.4
            platform = random.choice(self.PLATFORMS)
            ts = now - timedelta(minutes=random.randint(1, 1440))
            
            if is_phishing:
                sender = random.choice(self.SENDERS)
                content = random.choice(self.PHISHING_PATTERNS)
                score = round(random.uniform(0.75, 0.99), 2)
                verdict = 'PHISHING DETECTED'
                action = 'QUARANTINED & BLOCKED'
                indicators = random.sample(['Urgency Keywords', 'Spoofed Domain', 'Suspicious Link', 'Unusual Request'], random.randint(2, 3))
            else:
                sender = f"user{random.randint(10,99)}@internal.com"
                content = random.choice(self.NORMAL_PATTERNS)
                score = round(random.uniform(0.01, 0.15), 2)
                verdict = 'CLEAN'
                action = 'DELIVERED'
                indicators = []

            results.append({
                'timestamp': ts.strftime('%Y-%m-%dT%H:%M:%S'),
                'platform': platform,
                'sender': sender,
                'content': content,
                'nlp_score': score,
                'verdict': verdict,
                'action': action,
                'indicators': indicators,
                'is_phishing': is_phishing
            })
            
        results.sort(key=lambda x: x['timestamp'], reverse=True)
        return results
