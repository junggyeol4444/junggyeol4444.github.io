
import sys, os, json, yaml
from jsonschema import Draft202012Validator

ROOT = os.path.dirname(os.path.dirname(__file__))

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []

def load_schema(name):
    p = os.path.join(ROOT, "schemas", f"{name}.schema.json")
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_data(data, schema):
    validator = Draft202012Validator(schema)
    return sorted(validator.iter_errors(data), key=lambda e: e.path)

def main():
    print("::group::Schema validation")
    ok = True
    checks = [
        ("data/schedule.yml","schedule"),
        ("data/creators.yml","creators"),
        ("data/clips.yml","clips"),
    ]
    for rel, schema_name in checks:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            print(f"[warn] {rel} not found — skipping")
            continue
        try:
            data = load_yaml(path)
            schema = load_schema(schema_name)
            errs = validate_data(data, schema)
            if errs:
                ok = False
                print(f"::error file={rel}::Schema validation failed:")
                for e in errs:
                    print(f"  - {list(e.path)}: {e.message}")
            else:
                print(f"[ok] {schema_name}")
        except Exception as ex:
            ok = False
            print(f"::error file={rel}::Exception: {ex}")
    print("::endgroup::")
    if not ok:
        sys.exit(1)

if __name__ == "__main__":
    main()
