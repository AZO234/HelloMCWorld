# preprocess for Fabric

import os, json, re, json

with open("python/current_mc_version.json") as f:
    mcv = json.load(f)

with open("python/project_config.json") as f:
    configs = json.load(f)

mc_ver = os.environ.get("MC_VER", mcv["current_mc_version"])
with open("python/modl_versions_21.json") as f:
    versions = json.load(f)
version_data = versions.get(mc_ver, {})

props = {**configs, **version_data}

mod_id = props.get("mod_id", "hellomcworld")
template_dir = "fabric/src/main/resources"
targets = {
    f"{template_dir}/fabric.mod.json.template": f"{template_dir}/fabric.mod.json",
    f"{template_dir}/{mod_id}.mixins.json.template": f"{template_dir}/{mod_id}.mixins.json"
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
