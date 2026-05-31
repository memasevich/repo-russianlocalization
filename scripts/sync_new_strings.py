import os
import json

def sync_new_strings(game_dir, dictionary_file):
    """
    Синхронизирует словарь с актуальными файлами игры.
    Находит новые ключи и добавляет их в JSON, сохраняя старые переводы.
    """
    if not os.path.exists(dictionary_file):
        dictionary = {}
    else:
        with open(dictionary_file, "r", encoding="utf-8") as f:
            dictionary = json.load(f)
    
    new_keys_found = 0
    
    for filename in os.listdir(game_dir):
        if filename.endswith(".tsv"):
            filepath = os.path.join(game_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                for line in f:
                    if "\t" in line:
                        key, english_val = line.strip().split("\t", 1)
                        # Если ключа нет в словаре - добавляем его (оригинал)
                        if key not in dictionary:
                            dictionary[key] = english_val
                            new_keys_found += 1
                            print(f"[NEW] {key}: {english_val}")
    
    if new_keys_found > 0:
        with open(dictionary_file, "w", encoding="utf-8") as f:
            json.dump(dictionary, f, ensure_ascii=False, indent=4)
        print(f"\nSynced! Found and added {new_keys_found} new strings to {dictionary_file}")
    else:
        print("\nNo new strings found. Everything is up to date.")

if __name__ == "__main__":
    # Папка с оригинальными файлами игры (Default)
    game_source = r"D:\steam\steamapps\common\REPO\REPO_Data\StreamingAssets\Localizations\Default"
    # Наш рабочий словарь
    working_dict = r"C:\Users\Lecoo\projects\repo-russianlocalization\dictionaries\dictionary.json"
    
    sync_new_strings(game_source, working_dict)
