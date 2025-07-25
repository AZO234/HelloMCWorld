import os
import platform
import subprocess
import sys
import json
import argparse

parser = argparse.ArgumentParser(description="Build Minecraft mod with optional targets")
parser.add_argument('--target', nargs='+', choices=['fabric', 'forge', 'neoforge', 'all'], default=['all'], help='Build target(s)')
args = parser.parse_args()

with open("python/current_mc_version.json") as f:
    mcv = json.load(f)
MC_VER = os.environ.get("MC_VER", mcv["current_mc_version"])
os.environ["MC_VER"] = MC_VER

PYTHON_SCRIPTS_COMMON = [
    "python/generate_properties.py",
    "python/preprocess_resources.py",
    "python/preprocess_api.py"
]
PYTHON_SCRIPTS_BY_TARGET = {
    "fabric": ["python/preprocess_fabric.py"],
    "forge": ["python/preprocess_forge.py"],
    "neoforge": ["python/preprocess_neoforge.py"]
}

if os.name == "nt" or platform.system() == "Windows":
    GRADLE_CMD_BASE = ["gradlew.bat"]
else:
    GRADLE_CMD_BASE = ["./gradlew"]

def run_script(script):
    print(f"▶️ Running {script}...")
    result = subprocess.run(["python", script], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Failed: {script}")
        print(result.stderr)
        sys.exit(result.returncode)
    else:
        print(result.stdout)

def run_gradle(target):
    print(f"🏗️ Running Gradle build for :{target}...")
    result = subprocess.run(GRADLE_CMD_BASE + [f":{target}:build"])
    if result.returncode != 0:
        print(f"❌ Gradle build failed for :{target}")
        sys.exit(result.returncode)
    print(f"✅ Gradle build for :{target} completed")

if __name__ == "__main__":
    targets = ['fabric', 'forge', 'neoforge'] if 'all' in args.target else args.target

    for script in PYTHON_SCRIPTS_COMMON:
        run_script(script)

    for target in targets:
        for script in PYTHON_SCRIPTS_BY_TARGET[target]:
            run_script(script)
        run_gradle(target)