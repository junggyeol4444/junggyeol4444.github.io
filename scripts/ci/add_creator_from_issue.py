
import os, re, sys, yaml, pathlib, unicodedata, json

def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = re.sub(r"[^\w\s-]", "", value, flags=re.U).strip().lower()
    value = re.sub(r"[\s_-]+", "-", value, flags=re.U)
    return value

def load_json_env(var):
    s = os.environ.get(var, "")
    if not s:
        print(f"::warning::Missing env {var}")
        return {}
    try:
        return json.loads(s)
    except Exception as e:
        print(f"::error::Invalid JSON in {var}: {e}")
        sys.exit(1)

def ensure_dir(p: pathlib.Path):
    p.mkdir(parents=True, exist_ok=True)

root = pathlib.Path(".")
data_dir = root / "data"
creators_yml = data_dir / "creators.yml"
pages_dir = root / "creators"

info = load_json_env("CREATOR_JSON")

display_name = (info.get("display_name") or "").strip()
if not display_name:
    print("::error::Display name is required")
    sys.exit(1)
platform = (info.get("platform") or "").strip().lower()
channel_url = (info.get("channel_url") or "").strip()
channel_id = (info.get("channel_id") or "").strip()
bio = (info.get("bio") or "").strip()
avatar_url = (info.get("avatar_url") or "").strip()

slug = slugify(display_name)
creator_id = f"{platform}-{slug}" if platform else slug

# Update data/creators.yml (list)
ensure_dir(data_dir)
creators = []
if creators_yml.exists():
    with open(creators_yml, "r", encoding="utf-8") as f:
        try:
            loaded = yaml.safe_load(f) or []
            if isinstance(loaded, list):
                creators = loaded
            else:
                print("::warning::data/creators.yml is not a list; creating a new list")
        except Exception as e:
            print(f"::warning::Failed to parse creators.yml: {e}")

for c in creators:
    if c.get("id") == creator_id or (c.get("name") or "").strip() == display_name:
        print("Creator already exists; skipping append.")
        break
else:
    entry = {
        "id": creator_id,
        "name": display_name,
        "bio": bio or None,
        "avatar_url": avatar_url or None,
        "platforms": [{"platform": platform, "url": channel_url, "channel_id": channel_id or None}]
    }
    creators.append(entry)
    with open(creators_yml, "w", encoding="utf-8") as f:
        yaml.safe_dump(creators, f, allow_unicode=True, sort_keys=False)
    print(f"Added to data/creators.yml: {creator_id}")

# Create creators/<slug>.md (front matter only; no sample body)
ensure_dir(pages_dir)
page_path = pages_dir / f"{slug}.md"
if not page_path.exists():
    lines = ["---",
             "layout: creator",
             f"name: {display_name}",
             f"creator_id: {creator_id}",
             f"slug: {slug}",
             f"permalink: /creators/{slug}/",
             f"platform: {platform}",
             f"channel_url: {channel_url}"]
    if channel_id: lines.append(f"channel_id: {channel_id}")
    if bio: lines.append(f"bio: {bio}")
    if avatar_url: lines.append(f"avatar_url: {avatar_url}")
    lines.append("---")
    with open(page_path, "w", encoding="utf-8") as f:
        f.write("\\n".join(lines)+"\\n")
    print(f"Created page: {page_path}")
else:
    print("Creator page already exists; skipping.")
