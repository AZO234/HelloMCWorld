import os
import shutil
import argparse

CLEAN_PATHS = [
    ".gradle",
    ".idea",
    ".kotlin",
    "build",
    "common/build",
    "fabric/.gradle",
    "fabric/build",
    "fabricw/build",
    "forge/build",
    "forgew/build",
    "neoforge/build",
    "neoforge/run",
    "neoforgew/build",
]

def remove_path(path):
    if os.path.isdir(path):
        shutil.rmtree(path, ignore_errors=True)
        print(f"🧹 Removed directory: {path}")
    elif os.path.isfile(path):
        os.remove(path)
        print(f"🗑️ Removed file: {path}")
    else:
        print(f"⚠️ Skipped (not found): {path}")

def main():
    parser = argparse.ArgumentParser(description="Clean build artifacts.")
    parser.add_argument("-g", "--gradle_cache", action="store_true", help="Also delete global Gradle cache (~/.gradle)")
    args = parser.parse_args()

    for path in CLEAN_PATHS:
        remove_path(path)

    if args.gradle_cache:
        gradle_cache = os.path.expanduser("~/.gradle")
        remove_path(gradle_cache)

if __name__ == "__main__":
    main()