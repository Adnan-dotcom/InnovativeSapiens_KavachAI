"""Generate progress.md with all source code for the GitHub repo."""
import os

PROJECT = r"c:\Users\Adnan\Desktop\Sentil1_AI"
OUTPUT = os.path.join(PROJECT, "InnovativeSapiens_KavachAI", "progress.md")

FILES = [
    (".streamlit/config.toml", "toml"),
    ("requirements.txt", "text"),
    ("config.py", "python"),
    ("app.py", "python"),
    ("styles.py", "python"),
    ("train_model.py", "python"),
    ("core/__init__.py", "python"),
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
    ("core/phishing.py", "python"),
    ("pages/1_Live_Monitor.py", "python"),
    ("pages/2_Analytics.py", "python"),
    ("pages/3_AI_Model.py", "python"),
    ("pages/4_ShadowGuard.py", "python"),
    ("pages/5_DeepTrust.py", "python"),
    ("pages/6_Guardian_IoT.py", "python"),
    ("pages/7_CleanCode_AI.py", "python"),
    ("pages/8_Ransomware_Shield.py", "python"),
    ("pages/9_Phishing_Defense.py", "python"),
    ("pages/10_Forensics_Report.py", "python"),
]

with open(OUTPUT, "w", encoding="utf-8") as out:
    out.write("# 🛡️ Kavach AI — Full Source Code\n\n")
    out.write("> Autonomous Cyber Defense System — *Detect. Decide. Defend.*\n\n")
    out.write("---\n\n")
    
    for rel_path, lang in FILES:
        full = os.path.join(PROJECT, rel_path)
        if not os.path.exists(full):
            continue
        with open(full, "r", encoding="utf-8") as f:
            code = f.read()
        out.write(f"## `{rel_path}`\n\n")
        out.write(f"```{lang}\n{code}```\n\n---\n\n")
    
    # Also include README
    readme = os.path.join(PROJECT, "README.md")
    if os.path.exists(readme):
        with open(readme, "r", encoding="utf-8") as f:
            out.write("## `README.md`\n\n")
            out.write(f"```markdown\n{f.read()}```\n\n")

print(f"DONE - progress.md generated at: {OUTPUT}")
print(f"   Size: {os.path.getsize(OUTPUT):,} bytes")
