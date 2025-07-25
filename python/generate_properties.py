# replacement gradle.properties.template to gradle.properties

import os, json, re, json

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
with open("python/modl_versions.json") as f:
    versions = json.load(f)
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
