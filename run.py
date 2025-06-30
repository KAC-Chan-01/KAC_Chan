import subprocess
import time
import os
import psutil
import sys

CHECK_INTERVAL = 30  # seconds
REPO_DIR = os.path.abspath(os.path.dirname(__file__))
TARGET_SCRIPT = "KAC_Chan.py"

current_commit = None
process = None

def get_current_commit():
    result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO_DIR, capture_output=True, text=True)
    return result.stdout.strip()

def pull_latest():
    subprocess.run(["git", "pull"], cwd=REPO_DIR)

def stop_process_tree(proc):
    if proc is None:
        return
    parent = psutil.Process(proc.pid)
    children = parent.children(recursive=True)
    for child in children:
        child.kill()
    parent.kill()

def start_script():
    return subprocess.Popen([sys.executable, TARGET_SCRIPT], cwd=REPO_DIR)

def main():
    global current_commit, process

    current_commit = get_current_commit()
    print(f"[INIT] Starting {TARGET_SCRIPT} at commit {current_commit}")
    process = start_script()

    while True:
        time.sleep(CHECK_INTERVAL)
        new_commit = get_current_commit()
        if new_commit != current_commit:
            print(f"[UPDATE] Change detected: {current_commit} → {new_commit}")
            print("[INFO] Stopping running script...")
            stop_process_tree(process)
            print("[INFO] Pulling latest changes...")
            pull_latest()
            current_commit = new_commit
            print(f"[INFO] Restarting {TARGET_SCRIPT} at commit {current_commit}")
            process = start_script()

if __name__ == "__main__":
    try:
        import psutil
    except ImportError:
        print("[ERROR] 'psutil' is required. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
        import psutil

    main()




