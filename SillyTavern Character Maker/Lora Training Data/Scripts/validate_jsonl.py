import json
import sys

def validate_jsonl(filepath):
    valid = True
    with open(filepath, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            try:
                json.loads(line)
            except json.JSONDecodeError as e:
                print(f"[Invalid] Line {i}: {e}")
                valid = False
    return valid

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: validate_jsonl.py <file.jsonl>")
        sys.exit(1)

    fname = sys.argv[1]
    ok = validate_jsonl(fname)
    if ok:
        print(f"{fname} is valid JSONL.")
    else:
        print(f"{fname} has errors.")