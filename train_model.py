"""Kavach AI Model Training — Generates synthetic data & trains the AI Brain"""
import numpy as np, pandas as pd, joblib, json, os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

np.random.seed(42)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, 'models'); os.makedirs(MODEL_DIR, exist_ok=True)
MODEL_PATH = os.path.join(MODEL_DIR, 'sentinel_brain.pkl')
METRICS_PATH = os.path.join(MODEL_DIR, 'model_metrics.json')
FEATURES = ['packet_length', 'protocol', 'src_port', 'dst_port']
LABELS = {0:'Normal', 1:'DDoS Attack', 2:'Port Scan', 3:'Brute Force', 4:'DNS Amplification'}

def gen_normal(n=200):
    d = []
    for _ in range(n):
        t = np.random.choice(['http','https','dns','email','ssh','other'])
        if t=='http': d.append([np.random.randint(200,1500),6,np.random.randint(1024,65535),80])
        elif t=='https': d.append([np.random.randint(200,1500),6,np.random.randint(1024,65535),443])
        elif t=='dns': d.append([np.random.randint(50,200),17,np.random.randint(1024,65535),53])
        elif t=='email': d.append([np.random.randint(100,2000),6,np.random.randint(1024,65535),np.random.choice([25,587,993])])
        elif t=='ssh': d.append([np.random.randint(100,500),6,np.random.randint(1024,65535),22])
        else: d.append([np.random.randint(64,1500),6,np.random.randint(1024,65535),np.random.randint(1024,65535)])
    return d

def gen_ddos(n=100):
    d = []
    for _ in range(n):
        v = np.random.choice(['icmp','syn','udp'])
        if v=='icmp': d.append([np.random.randint(6000,10000),1,0,0])
        elif v=='syn': d.append([np.random.randint(5000,9000),6,np.random.randint(1,1024),np.random.choice([80,443])])
        else: d.append([np.random.randint(5000,8000),17,np.random.randint(1,65535),np.random.randint(1,65535)])
    return d

def gen_portscan(n=100):
    return [[np.random.randint(40,64),6,np.random.randint(1024,65535),np.random.randint(1,1024)] for _ in range(n)]

def gen_bruteforce(n=100):
    return [[np.random.randint(100,300),6,np.random.randint(1024,65535),np.random.choice([22,3389,21,23,3306])] for _ in range(n)]

def gen_dnsamp(n=100):
    return [[np.random.randint(2000,6000),17,53,np.random.randint(1024,65535)] for _ in range(n)]

def main():
    print("="*60)
    print("  KAVACH AI | Model Training Pipeline")
    print("="*60)

    X = gen_normal(200) + gen_ddos(100) + gen_portscan(100) + gen_bruteforce(100) + gen_dnsamp(100)
    y = [0]*200 + [1]*100 + [2]*100 + [3]*100 + [4]*100
    df = pd.DataFrame(X, columns=FEATURES); df['label'] = y

    print(f"\n  Total samples: {len(df)}")
    for lid, name in LABELS.items():
        print(f"  - {name}: {len(df[df['label']==lid])}")

    X_train, X_test, y_train, y_test = train_test_split(df[FEATURES], df['label'], test_size=0.2, random_state=42, stratify=df['label'])
    print(f"\n  Train: {len(X_train)} | Test: {len(X_test)}")

    print("\n  Training Random Forest (200 trees)...")
    model = RandomForestClassifier(n_estimators=200, max_depth=15, min_samples_split=5, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=list(LABELS.values()), output_dict=True)
    cm = confusion_matrix(y_test, y_pred).tolist()
    importance = dict(zip(FEATURES, model.feature_importances_.tolist()))

    print(f"\n  Accuracy: {acc:.2%}")
    print(f"\n{classification_report(y_test, y_pred, target_names=list(LABELS.values()))}")
    print("  Feature Importance:")
    for f, imp in sorted(importance.items(), key=lambda x: x[1], reverse=True):
        print(f"    {f:20s} {imp:.4f} {'#'*int(imp*40)}")

    joblib.dump(model, MODEL_PATH)
    with open(METRICS_PATH, 'w') as fp:
        json.dump({'accuracy': acc, 'report': report, 'confusion_matrix': cm, 'feature_importance': importance,
                   'feature_names': FEATURES, 'class_names': list(LABELS.values()),
                   'train_size': len(X_train), 'test_size': len(X_test)}, fp, indent=2)

    print(f"\n  Model saved: {MODEL_PATH}")
    print(f"  Metrics saved: {METRICS_PATH}")
    print("="*60)
    print("  Kavach AI Brain is READY!")
    print("="*60)

if __name__ == '__main__':
    main()
