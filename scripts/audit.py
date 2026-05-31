import os
import json
import re

def contains_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))

def audit_translation(source_dir, dictionary_file):
    with open(dictionary_file, "r", encoding="utf-8") as f:
        dictionary = json.load(f)
        
    total_keys = 0
    translated_count = 0
    untranslated = []
    
    for filename in os.listdir(source_dir):
        if filename.endswith(".tsv"):
            filepath = os.path.join(source_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                for line in f:
                    if "\t" in line:
                        total_keys += 1
                        key, original_val = line.strip().split("\t", 1)
                        current_val = dictionary.get(key, "")
                        
                        # Если значение содержит кириллицу - считаем переведенным
                        if contains_cyrillic(current_val):
                            translated_count += 1
                        else:
                            untranslated.append(f"[{filename}] {key}: {current_val}")
                            
    print(f"Total keys: {total_keys}")
    print(f"Translated (with Cyrillic): {translated_count} ({translated_count/total_keys*100:.1f}%)")
    print(f"Remaining (English/Other): {total_keys - translated_count}")
    
    output_path = r"C:\Users\Lecoo\projects\repo-russianlocalization\dictionaries\untranslated.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(untranslated))
    print(f"List of untranslated strings saved to {output_path}")

if __name__ == "__main__":
    source_dir = r"C:\Users\Lecoo\projects\repo-russianlocalization\source"
    dictionary_file = r"C:\Users\Lecoo\projects\repo-russianlocalization\dictionaries\dictionary.json"
    audit_translation(source_dir, dictionary_file)
