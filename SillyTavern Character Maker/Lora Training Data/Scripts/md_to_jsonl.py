import json
import sys
import re
import os

def extract_json_blocks(md_text):
    """Extract JSON blocks from Markdown code fences."""
    pattern = r"```json\s*\n(.*?)```"
    matches = re.findall(pattern, md_text, re.DOTALL | re.IGNORECASE)
    return [m.strip() for m in matches]

def write_jsonl(json_strs, output_dir, base_filename):
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"{base_filename}.jsonl")
    with open(out_path, "w", encoding="utf-8") as f:
        for i, jtext in enumerate(json_strs, start=1):
            try:
                obj = json.loads(jtext)
                f.write(json.dumps(obj, ensure_ascii=False) + "\n")
            except json.JSONDecodeError as e:
                print(f"[Error] Block {i} is not valid JSON: {e}")
    return out_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: md_to_jsonl.py <input.md>")
        sys.exit(1)

    md_file = sys.argv[1]
    with open(md_file, "r", encoding="utf-8") as f:
        md = f.read()

    blocks = extract_json_blocks(md)
    if not blocks:
        print(f"No JSON blocks found in {md_file}.")
        sys.exit(1)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    jsonl_dir = os.path.join(script_dir, "jsonl")
    base_name = os.path.splitext(os.path.basename(md_file))[0]
    out_file = write_jsonl(blocks, jsonl_dir, base_name)

    print(f"Generated JSONL: {out_file}")