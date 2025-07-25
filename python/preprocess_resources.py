# preprocess resources

import os, shutil

resource_src_dir = "python/resources"
resource_targets = [
    f"fabric/src/main/resources",
    f"forge/src/main/resources",
    f"neoforge/src/main/resources"
]

def copy_resource_directory(src_dir, dest_dir):
    print(f"🔁 Copying {src_dir} → {dest_dir}")
    shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)
    print(f"✅ Done copying to: {dest_dir}")

for target_dir in resource_targets:
    copy_resource_directory(resource_src_dir, target_dir)
