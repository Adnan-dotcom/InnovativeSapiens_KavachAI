import os

PROJECT = r"c:\Users\Adnan\Desktop\Sentil1_AI"
OUTPUT = os.path.join(PROJECT, "progress.md")

# 1. READ EXISTING ROADMAP
with open(OUTPUT, "r", encoding="utf-8") as f:
    roadmap = f.read().split("## 📂 Final Repository Architecture")[0]

FILES = [
    (".streamlit/config.toml", "toml"),
    ("requirements.txt", "text"),
    ("config.py", "python"),
    ("app.py", "python"),
    ("utils.py", "python"),
    ("styles.py", "python"),
    ("train_model.py", "python"),
    ("core/detector.py", "python"),
    ("core/logger.py", "python"),
    ("core/guardian.py", "python"),
    ("core/simulator.py", "python"),
    ("core/sniffer.py", "python"),
    ("core/shadowguard.py", "python"),
    ("core/deeptrust.py", "python"),
    ("core/guardian_iot.py", "python"),
    ("core/cleancode.py", "python"),
    ("core/ransomware.py", "python"),
    ("pages/1_Sentinel_Intelligence.py", "python"),
    ("pages/2_Deception_Identity.py", "python"),
    ("pages/3_Infrastructure_Security.py", "python"),
    ("pages/4_Behavioral_Defense.py", "python"),
    ("pages/5_Neural_Engine.py", "python"),
]

# 2. GENERATE COMPREHENSIVE DOCUMENT
with open(OUTPUT, "w", encoding="utf-8") as out:
    out.write(roadmap)
    out.write("## 📂 Final Repository Architecture (6-Module System)\n")
    out.write("1. **Command Center:** Global Security Pulse & Autonomous Log.\n")
    out.write("2. **Sentinel Intelligence:** Forensic traffic analysis & Adversary Profiling.\n")
    out.write("3. **Deception & Identity:** ShadowGuard Decoys & DeepTrust Verification.\n")
    out.write("4. **Infrastructure Security:** IoT Protection & Supply Chain Integrity.\n")
    out.write("5. **Behavioral Defense:** Ransomware Shield & Phishing Guard.\n")
    out.write("6. **Neural Engine:** XAI Metrics & Model Transparency.\n\n")
    out.write("---\n\n")
    out.write("# 📄 Full Project Source Code (Manifest)\n\n")
    
    for rel_path, lang in FILES:
        full = os.path.join(PROJECT, rel_path)
        if not os.path.exists(full):
            continue
        with open(full, "r", encoding="utf-8") as f:
            code = f.read()
        out.write(f"### `{rel_path}`\n\n")
        out.write(f"```{lang}\n{code}```\n\n---\n\n")
    
    # Include Documentation Files
    for doc in ["README.md", "KAVACH_AI_USER_GUIDE.md"]:
        full = os.path.join(PROJECT, doc)
        if os.path.exists(full):
            with open(full, "r", encoding="utf-8") as f:
                out.write(f"### `{doc}`\n\n")
                out.write(f"```markdown\n{f.read()}```\n\n---\n\n")

print(f"DONE - Full Progress Report & Manifest generated at: {OUTPUT}")
