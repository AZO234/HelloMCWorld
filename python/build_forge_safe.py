import os
import subprocess
import platform
import shutil
import sys
import time

FORGE_PROJECT = ":forge"
GRADLEW = "gradlew.bat" if platform.system() == "Windows" else "./gradlew"
GRADLE_CACHE_DIR = os.path.expanduser("~/.gradle/caches/forge_gradle")

def run_gradle_task(tasks, extra_args=None):
    cmd = [GRADLEW] + tasks
    if extra_args:
        cmd += extra_args
    print(f"▶️ Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    return result.returncode == 0

def clean_and_build_forge():
    print("🔄 Cleaning :forge project...")
    if not run_gradle_task([f"{FORGE_PROJECT}:clean"]):
        print("⚠️ Failed to clean :forge project")
        return False

    print("🏗️ Building :forge project with --refresh-dependencies...")
    return run_gradle_task([f"{FORGE_PROJECT}:build"], ["--refresh-dependencies"])

def delete_forge_cache():
    print(f"🧹 Deleting Forge Gradle cache: {GRADLE_CACHE_DIR}")
    shutil.rmtree(GRADLE_CACHE_DIR, ignore_errors=True)
    time.sleep(1)

def main():
    success = clean_and_build_forge()
    if success:
        print("✅ Forge build completed successfully.")
        return

    print("❌ Initial build failed. Trying after deleting Forge Gradle cache...")
    delete_forge_cache()

    if clean_and_build_forge():
        print("✅ Forge build succeeded after cache reset.")
    else:
        print("🛑 Forge build failed even after cache reset.")
        sys.exit(1)

if __name__ == "__main__":
    main()