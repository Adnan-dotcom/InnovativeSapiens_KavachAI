import joblib, numpy as np, os
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

class ThreatDetector:
    ATTACK_TYPES = {0: 'Normal', 1: 'DDoS Attack', 2: 'Port Scan', 3: 'Brute Force', 4: 'DNS Amplification'}
    SEVERITY = {'Normal': 'info', 'DDoS Attack': 'critical', 'Port Scan': 'high', 'Brute Force': 'high', 'DNS Amplification': 'critical'}

    def __init__(self, model_path):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model not found at {model_path}. Run train_model.py first!")
        self.model = joblib.load(model_path)

    def predict(self, features):
        """Classify packet features [packet_length, protocol, src_port, dst_port]"""
        X = np.array(features).reshape(1, -1)
        pred = self.model.predict(X)[0]
        proba = self.model.predict_proba(X)[0]
        threat_type = self.ATTACK_TYPES.get(pred, 'Unknown')
        return {
            'is_threat': pred != 0,
            'threat_type': threat_type,
            'confidence': float(max(proba)),
            'severity': self.SEVERITY.get(threat_type, 'info'),
            'prediction_id': int(pred),
            'probabilities': {self.ATTACK_TYPES[i]: float(p) for i, p in enumerate(proba)}
        }
