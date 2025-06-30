import asyncio
import subprocess
import os
import sys
import psutil

REPO_DIR = os.path.abspath(os.path.dirname(__file__))
TARGET_SCRIPT = "KAC_Chan.py"
CHECK_INTERVAL = 30  # seconds

current_commit = None
process = None


async def get_current_commit():
    proc = await asyncio.create_subprocess_exec(
        "git", "rev-parse", "HEAD",
        cwd=REPO_DIR,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, _ = await proc.communicate()
    return stdout.decode().strip()


async def pull_latest():
    proc = await asyncio.create_subprocess_exec(
        "git", "pull",
        cwd=REPO_DIR
    )
    await proc.wait()


def stop_process_tree(proc):
    if proc is None:
        return
    try:
        parent = psutil.Process(proc.pid)
        children = parent.children(recursive=True)
        for child in children:
            child.kill()
        parent.kill()
    except psutil.NoSuchProcess:
        pass


def start_script():
    return subprocess.Popen([sys.executable, TARGET_SCRIPT], cwd=REPO_DIR)


async def watch_for_updates():
    global current_commit, process

    current_commit = await get_current_commit()
    print(f"[INIT] Starting {TARGET_SCRIPT} at commit {current_commit}")
    process = start_script()

    while True:
        await asyncio.sleep(CHECK_INTERVAL)
        new_commit = await get_current_commit()

        if new_commit != current_commit:
            print(f"[UPDATE] Change detected: {current_commit} → {new_commit}")
            print("[INFO] Stopping running script...")
            stop_process_tree(process)

            print("[INFO] Pulling latest changes...")
            await pull_latest()

            current_commit = new_commit
            print(f"[INFO] Restarting {TARGET_SCRIPT} at commit {current_commit}")
            process = start_script()


async def main():
    try:
        await watch_for_updates()
    except KeyboardInterrupt:
        print("[EXIT] Caught KeyboardInterrupt. Shutting down...")
        stop_process_tree(process)


if __name__ == "__main__":
    try:
        import psutil
    except ImportError:
        print("[ERROR] 'psutil' not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
        import psutil

    asyncio.run(main())

