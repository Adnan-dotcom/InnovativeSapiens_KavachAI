import os
import shutil

targets = [
    'test_sniffer.py',
    'InnovativeSapiens_KavachAI'
]

for target in targets:
    path = os.path.join(os.getcwd(), target)
    if os.path.exists(path):
        try:
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
            print(f"Removed: {target}")
        except Exception as e:
            print(f"Error removing {target}: {e}")
    else:
        print(f"Not found: {target}")
