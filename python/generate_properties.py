# replacement gradle.properties.template to gradle.properties

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

# configs
with open("python/project_config.json") as f:
    configs = json.load(f)
with open("gradle.properties.template") as f:
    template = f.read()
def replace_config(match):
    key = match.group(1)
    return configs.get(key, "UNKNOWN")
result = re.sub(r"\$\{(mod_\w+)\}", replace_config, template)
with open("gradle.properties", "w") as f:
    f.write(result)

# props
MODL_VERSIONS_URL = os.environ.get("MODL_VERSIONS_URL", "https://github.com/AZO234/MCModFixer/raw/refs/heads/main/modl_versions_21.json")
try:
    versions = load_json(MODL_VERSIONS_URL)
except Exception as e:
    print(f"❌ Failed to load mod loader versions data: {e}")
    sys.exit(1)
if mc_ver not in versions:
    print(f"🛑 Version {mc_ver} not found")
    exit(1)
props = versions[mc_ver]
with open("gradle.properties") as f:
    template = f.read()
def replace_prop(match):
    key = match.group(1)
    return props.get(key, "UNKNOWN")
result = re.sub(r"\$\{(\w+)\}", replace_prop, template)
with open("gradle.properties", "w") as f:
    f.write(result)

print(f"✔️ gradle.properties generated for {mc_ver}")
