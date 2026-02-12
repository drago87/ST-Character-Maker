import json
import os
import sys

def get_jsonl_files(paths, recursive=False):
    all_files = []
    for path in paths:
        if os.path.isdir(path):
            if recursive:
                for root, _, files in os.walk(path):
                    for f in files:
                        if f.lower().endswith(".jsonl"):
                            all_files.append(os.path.join(root, f))
            else:
                for f in os.listdir(path):
                    if f.lower().endswith(".jsonl"):
                        all_files.append(os.path.join(path, f))
        elif os.path.isfile(path) and path.lower().endswith(".jsonl"):
            all_files.append(path)
    return all_files

def combine_jsonl(paths, output_folder="Dataset", output_filename="CMC Lora Training Data.jsonl"):
    files = get_jsonl_files(paths)
    if not files:
        print("No JSONL files found in the provided paths.")
        return

    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, output_filename)
    total_lines = 0

    with open(output_path, "w", encoding="utf-8") as outfile:
        for f in files:
            with open(f, "r", encoding="utf-8") as infile:
                for line in infile:
                    line = line.strip()
                    if line:
                        try:
                            json.loads(line)
                            outfile.write(line + "\n")
                            total_lines += 1
                        except json.JSONDecodeError as e:
                            print(f"[Error] Skipping invalid JSON in {f}: {e}")

    print(f"Combined {total_lines} lines from {len(files)} files into '{output_path}'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: combine_jsonl.py <file_or_folder1> [file_or_folder2 ...]")
        sys.exit(1)

    paths = sys.argv[1:]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_folder = os.path.join(script_dir, "Dataset")
    combine_jsonl(paths, output_folder=dataset_folder)