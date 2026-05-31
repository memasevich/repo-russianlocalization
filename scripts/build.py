import os
import json

def build_translation(source_dir, dictionary_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    with open(dictionary_file, "r", encoding="utf-8") as f:
        dictionary = json.load(f)
        
    for filename in os.listdir(source_dir):
        if filename.endswith(".tsv"):
            source_path = os.path.join(source_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            translated_lines = []
            with open(source_path, "r", encoding="utf-8") as f:
                for line in f:
                    if "\t" in line:
                        key, original_value = line.strip().split("\t", 1)
                        # Используем перевод из словаря, если он там есть и отличается от ключа
                        # (или если мы уже перевели его в JSON)
                        translated_value = dictionary.get(key, original_value)
                        translated_lines.append(f"{key}\t{translated_value}")
                    else:
                        translated_lines.append(line.strip())
            
            with open(output_path, "w", encoding="utf-8") as f:
                f.write("\n".join(translated_lines) + "\n")

if __name__ == "__main__":
    source_dir = r"C:\Users\Lecoo\projects\repo-russianlocalization\source"
    dictionary_file = r"C:\Users\Lecoo\projects\repo-russianlocalization\dictionaries\dictionary.json"
    output_dir = r"C:\Users\Lecoo\projects\repo-russianlocalization\translation"
    build_translation(source_dir, dictionary_file, output_dir)
    print(f"Built translations in {output_dir}")
