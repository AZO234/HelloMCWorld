import os, json, re, sys
import urllib.request

with open("python/current_mc_version.json") as f:
    mcv = json.load(f)
mc_ver = os.environ.get("MC_VER", mcv["current_mc_version"])

# === Config ===
DIFF_API_URL = os.environ.get("DIFF_API_URL", "python/diff_api_21.json")
PROJECT_CONFIG_PATH = os.environ.get("PROJECT_CONFIG", "python/project_config.json")

# === Load JSON ===
def load_json(path_or_url):
    if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
        with urllib.request.urlopen(path_or_url) as res:
            return json.load(res)
    else:
        with open(path_or_url, encoding="utf-8") as f:
            return json.load(f)

# === Inherit resolution ===
def resolve_inherit(ver, versions, visited=None):
    if visited is None:
        visited = set()
    if ver in visited:
        raise ValueError(f"Circular inheritance at version '{ver}'")
    visited.add(ver)

    entry = versions.get(ver)
    if entry is None:
        return None

    base_ver = entry.get("inherit")
    if not base_ver:
        return entry

    base_entry = resolve_inherit(base_ver, versions, visited)
    if base_entry is None:
        return entry

    merged = dict(base_entry)
    merged.update({k: v for k, v in entry.items() if k != "diff"})
    merged["diff"] = base_entry.get("diff", []) + entry.get("diff", [])
    return merged

# === Variable substitution ===
def replace_vars(text, substitutions):
    for k, v in substitutions.items():
        text = text.replace(k, v)
    return text

# === Main process ===
try:
    all_diffs = load_json(DIFF_API_URL)
    project_config = load_json(PROJECT_CONFIG_PATH)
except Exception as e:
    print(f"❌ Failed to load config or diff data: {e}")
    sys.exit(1)

group_path = project_config["mod_group_id"].replace(".", "/")
class_name = project_config["mod_classname"]
substitutions = {
    "${mod_group_id}": group_path,
    "${mod_classname}": class_name
}

processed = 0
skipped = 0

for entry in all_diffs:
    modloader = entry.get("modloader") or entry.get("mocloader")
    if not modloader:
        continue

    version_map = entry.get("versions") or {
        k: v for k, v in entry.items() if re.match(r"^\d+\.\d+(\.\d+)?$", k)
    }

    diff_entry = resolve_inherit(mc_ver, version_map)
    if diff_entry is None:
        print(f"⚠️  No entry for {modloader} {mc_ver}")
        skipped += 1
        continue

    if not diff_entry.get("diff"):
        print(f"✔ No diff needed for {modloader} {mc_ver}")
        skipped += 1
        continue

    template_path = replace_vars(diff_entry["template"], substitutions)
    locate_path = replace_vars(diff_entry["locate"], substitutions)

    try:
        with open(template_path, encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Template not found for {modloader}: {template_path}")
        skipped += 1
        continue

    for patch in diff_entry["diff"]:
        content = re.sub(patch["pattern"], patch["replacement"], content)

    os.makedirs(os.path.dirname(locate_path), exist_ok=True)
    with open(locate_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ {modloader} {mc_ver} → {locate_path}")
    processed += 1

print(f"\n📝 Done. {processed} modified, {skipped} skipped.")
