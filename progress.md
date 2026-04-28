# Sentinel AI — Push to GitHub Guide

## Prerequisites
- Git installed on your system
- A GitHub account with access to the repository
- GitHub CLI or personal access token for authentication

## Repository Details
- **Repo:** [InnovativeSapiens_KavachAI](https://github.com/Adnan-dotcom/InnovativeSapiens_KavachAI)
- **Branch:** `main`

---

## Steps to Push the Entire Code to GitHub

### 1. Open Terminal in the Project Directory
```bash
cd C:\Users\Adnan\Desktop\Sentil1_AI
```

### 2. Initialize Git (if not already done)
```bash
git init
```

### 3. Set the Remote Origin
```bash
git remote add origin https://github.com/Adnan-dotcom/InnovativeSapiens_KavachAI.git
```
> If the remote already exists, update it:
```bash
git remote set-url origin https://github.com/Adnan-dotcom/InnovativeSapiens_KavachAI.git
```

### 4. Ensure `.gitignore` is in Place
Make sure a `.gitignore` file exists in the root to exclude unnecessary files:
```
__pycache__/
*.py[cod]
*.db
*.pkl
venv/
.env
.vscode/
.idea/
```

### 5. Reset Staged Files (to apply .gitignore properly)
```bash
git rm -r --cached .
```

### 6. Stage All Files
```bash
git add .
```

### 7. Commit the Code
```bash
git commit -m "Initial commit: Sentinel AI / Kavach AI cybersecurity platform"
```

### 8. Set Branch to `main`
```bash
git branch -M main
```

### 9. Push to GitHub
```bash
git push -u origin main
```

> **Note:** If prompted for authentication, use a **Personal Access Token (PAT)** as your password.  
> Generate one at: [GitHub → Settings → Developer Settings → Personal Access Tokens](https://github.com/settings/tokens)

---

## If the Remote Repo Already Has Files (e.g., README)
If GitHub shows a conflict because the remote already has commits, use:
```bash
git pull origin main --rebase
git push -u origin main
```
Or to force push (⚠️ overwrites remote):
```bash
git push -u origin main --force
```

---

## Project Structure Being Pushed
```
Sentil1_AI/
├── .gitignore
├── .streamlit/config.toml
├── README.md
├── app.py                  # Main Streamlit dashboard
├── config.py               # Configuration settings
├── styles.py               # UI styling (glassmorphic theme)
├── train_model.py           # ML model training script
├── requirements.txt         # Python dependencies
├── progress.md              # This file
├── core/
│   ├── __init__.py
│   ├── detector.py          # Threat detection engine
│   ├── simulator.py         # Attack simulation
│   ├── sniffer.py           # Network packet sniffer
│   ├── logger.py            # Logging utility
│   ├── shadowguard.py       # Deception/decoy module
│   ├── deeptrust.py         # Identity verification
│   ├── guardian_iot.py       # IoT security module
│   ├── cleancode.py         # Supply chain auditing
│   └── ransomware.py        # Ransomware protection engine
├── pages/
│   ├── 1_Live_Monitor.py
│   ├── 2_Analytics.py
│   ├── 3_AI_Model.py
│   ├── 4_ShadowGuard.py
│   ├── 5_DeepTrust.py
│   ├── 6_Guardian_IoT.py
│   ├── 7_CleanCode_AI.py
│   └── 8_Ransomware_Shield.py
└── models/
    └── model_metrics.json
```

---

## Quick One-Liner (after initial setup)
For future pushes:
```bash
git add . && git commit -m "your message here" && git push
```
