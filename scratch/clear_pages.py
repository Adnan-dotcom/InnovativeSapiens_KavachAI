import os, shutil
pages_dir = 'pages'
if os.path.exists(pages_dir):
    for f in os.listdir(pages_dir):
        path = os.path.join(pages_dir, f)
        try:
            if os.path.isfile(path): os.remove(path)
            elif os.path.isdir(path): shutil.rmtree(path)
        except: pass
print("Pages directory cleared.")
