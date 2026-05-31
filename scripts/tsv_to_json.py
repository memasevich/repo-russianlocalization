import os
import json

def convert_tsv_to_json(source_dir, output_file):
    dictionary = {}
    for filename in os.listdir(source_dir):
        if filename.endswith(".tsv"):
            filepath = os.path.join(source_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                for line in f:
                    if "\t" in line:
                        key, value = line.strip().split("\t", 1)
                        dictionary[key] = value
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    source_dir = r"C:\Users\Lecoo\projects\repo-russianlocalization\source"
    output_file = r"C:\Users\Lecoo\projects\repo-russianlocalization\dictionaries\dictionary.json"
    convert_tsv_to_json(source_dir, output_file)
    print(f"Created dictionary at {output_file}")
