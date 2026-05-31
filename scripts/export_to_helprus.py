import os
import json

def export_all_to_txt(game_source_dir, dictionary_file, output_txt):
    """
    Экспортирует все строки (переведенные и нет) в один удобный текстовый файл.
    Использует данные из игры и подставляет наши переводы из JSON.
    """
    if not os.path.exists(dictionary_file):
        dictionary = {}
    else:
        with open(dictionary_file, "r", encoding="utf-8") as f:
            dictionary = json.load(f)
            
    output_lines = []
    
    # Обрабатываем каждый TSV файл из игры
    for filename in sorted(os.listdir(game_source_dir)):
        if filename.endswith(".tsv"):
            filepath = os.path.join(game_source_dir, filename)
            output_lines.append(f"=== FILE: {filename} ===")
            
            with open(filepath, "r", encoding="utf-8") as f:
                for line in f:
                    if "\t" in line:
                        key, english_val = line.strip().split("\t", 1)
                        # Берем русский перевод если есть, иначе оставляем английский
                        current_val = dictionary.get(key, english_val)
                        output_lines.append(f"{key}: {current_val}")
            
            output_lines.append("") # Пустая строка между файлами
            
    # Сохраняем в файл на рабочем столе
    os.makedirs(os.path.dirname(output_txt), exist_ok=True)
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))
        
    print(f"Successfully exported all texts to {output_txt}")

if __name__ == "__main__":
    game_source = r"D:\steam\steamapps\common\REPO\REPO_Data\StreamingAssets\Localizations\Default"
    working_dict = r"C:\Users\Lecoo\projects\repo-russianlocalization\dictionaries\dictionary.json"
    desktop_output = r"C:\Users\Lecoo\Desktop\HELPRUS\all_gameplay_texts.txt"
    
    export_all_to_txt(game_source, working_dict, desktop_output)
