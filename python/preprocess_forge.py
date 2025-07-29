# preprocess for Forge

import os, json, re, sys, json
import urllib.request

# === Load JSON ===
def load_json(path_or_url):
    if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
        with urllib.request.urlopen(path_or_url) as res:
            return json.load(res)
    else:
        with open(path_or_url, encoding="utf-8") as f:
            return json.load(f)

with open("python/current_mc_version.json") as f:
    mcv = json.load(f)
mc_ver = os.environ.get("MC_VER", mcv["current_mc_version"])

with open("python/project_config.json") as f:
    configs = json.load(f)

MODL_VERSIONS_URL = os.environ.get("MODL_VERSIONS_URL", "https://github.com/AZO234/MCModFixer/raw/refs/heads/main/modl_versions_21.json")

try:
    version_data = load_json(MODL_VERSIONS_URL)
except Exception as e:
    print(f"❌ Failed to load mod loader versions data: {e}")
    sys.exit(1)

props = {**configs, **version_data[mc_ver]}

mod_id = props.get("mod_id", "hellomcworld")
template_dir = "forge/src/main/resources"
targets = {
    f"{template_dir}/META-INF/mods.toml.template": f"{template_dir}/META-INF/mods.toml",
    f"{template_dir}/pack.mcmeta.template": f"{template_dir}/pack.mcmeta"
}

def apply_template(template_path, output_path):
    if not os.path.exists(template_path):
        print(f"⚠️ Template not found: {template_path}")
        return
    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()
    content = re.sub(r"\$\{(\w+)\}", lambda m: props.get(m.group(1), m.group(0)), content)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generated: {output_path}")

for tpl, out in targets.items():
    apply_template(tpl, out)
