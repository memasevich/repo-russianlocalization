import json
import os

# ПОЛНЫЙ словарь перевода REPO (АБСОЛЮТНО ПОСЛЕДНИЙ РЫВОК)
translations = {
    "TUTORIAL.GRABBING.FOCUS_TEXT": "Тащите эту штуку, чтобы заполнить шкалу!",
    "FOCUS.PREFIX": "ЦЕЛЬ",
    "POPUP.MAIN_MENU.OPT1": "Да",
    "POPUP.MAIN_MENU.OPT2": "Нет",
    "POPUP.USE_BACKUP.OPT1": "Да!",
    "POPUP.USE_BACKUP.OPT2": "Нет",
    "REGIONS.REGION.USSC": "США (Юг-Центр)",
    "SAVES.SAVE_FILE.CORRUPTED_SAVE_FILE": "Файл сохранения поврежден",
    "SETTINGS.LANGUAGE.HEADER": "Язык",
    "POPUP.DELETE_PRESET.OPT1": "Да! :')",
    "POPUP.DELETE_PRESET.OPT2": "Нет...",
    "POPUP.COSMETICS_COLOR_ALL.OPT1": "Да! :')",
    "POPUP.COSMETICS_COLOR_ALL.OPT2": "Нет...",
    "POPUP.RESET_GAMEPLAY_SETTINGS.OPT1": "Да!",
    "POPUP.RESET_GAMEPLAY_SETTINGS.OPT2": "Нет",
    "POPUP.RESET_GRAPHICS_SETTINGS.OPT1": "Да!",
    "POPUP.RESET_GRAPHICS_SETTINGS.OPT2": "Нет",
    "POPUP.RESET_AUDIO_SETTINGS.HEADER": "Сброс аудио",
    "POPUP.RESET_AUDIO_SETTINGS.BODY": "Сбросить настройки аудио?",
    "POPUP.RESET_AUDIO_SETTINGS.OPT1": "Да!",
    "POPUP.RESET_AUDIO_SETTINGS.OPT2": "Нет",
    "POPUP.RESET_CONTROLS_SETTINGS.HEADER": "Сброс управления",
    "POPUP.RESET_CONTROLS_SETTINGS.BODY": "Сбросить настройки управления?",
    "POPUP.RESET_CONTROLS_SETTINGS.OPT1": "Да!",
    "POPUP.RESET_CONTROLS_SETTINGS.OPT2": "Нет",
    "LOBBY.SETTINGS": "Настройки",
    "LOBBY.CUSTOMIZE": "Персонаж",
    "POPUP.START_GAME.OPT1": "Да!",
    "POPUP.START_GAME.OPT2": "Подождите!",
    "POPUP.LEAVE_LOBBY.OPT1": "Да",
    "POPUP.LEAVE_LOBBY.OPT2": "Нет",
    "POPUP.NEW_GAME.HEADER": "Новая игра",
    "POPUP.NEW_GAME.BODY": "Начать новую игру?",
    "POPUP.NEW_GAME.OPT1": "Да!",
    "POPUP.NEW_GAME.OPT2": "Нет",
    "POPUP.COSMETICS_RESET_ALL.OPT1": "Да! :')",
    "POPUP.COSMETICS_RESET_ALL.OPT2": "Нет...",
    "POPUP.COSMETICS_RESET_BODY.OPT1": "Да! :')",
    "POPUP.COSMETICS_RESET_BODY.OPT2": "Нет...",
    "POPUP.COSMETICS_RESET_COSMETICS.HEADER": "Очистить",
    "POPUP.COSMETICS_RESET_COSMETICS.BODY": "Снять все косметические предметы?",
    "POPUP.COSMETICS_RESET_COSMETICS.OPT1": "Да! :')",
    "POPUP.COSMETICS_RESET_COSMETICS.OPT2": "Нет...",
    "POPUP.COSMETICS_RANDOMIZE_ALL.OPT1": "Да! :')",
    "POPUP.COSMETICS_RANDOMIZE_ALL.OPT2": "Нет...",
    "POPUP.COSMETICS_RANDOMIZE_BODY.HEADER": "Рандом тела",
    "POPUP.COSMETICS_RANDOMIZE_BODY.BODY": "Случайно выбрать части тела?",
    "POPUP.COSMETICS_RANDOMIZE_BODY.OPT1": "Да! :')",
    "POPUP.COSMETICS_RANDOMIZE_BODY.OPT2": "Нет...",
    "POPUP.COSMETICS_RANDOMIZE_COSMETICS.HEADER": "Рандом одежды",
    "POPUP.COSMETICS_RANDOMIZE_COSMETICS.BODY": "Случайно выбрать одежду?",
    "POPUP.COSMETICS_RANDOMIZE_COSMETICS.OPT1": "Да! :')",
    "POPUP.COSMETICS_RANDOMIZE_COSMETICS.OPT2": "Нет...",
    "POPUP.COSMETICS_COLOR_BODY.HEADER": "Цвет тела",
    "POPUP.COSMETICS_COLOR_BODY.BODY": "Изменить цвет всех частей тела?",
    "POPUP.COSMETICS_COLOR_BODY.OPT1": "Да! :')",
    "POPUP.COSMETICS_COLOR_BODY.OPT2": "Нет...",
    "POPUP.COSMETICS_COLOR_COSMETICS.HEADER": "Цвет одежды",
    "POPUP.COSMETICS_COLOR_COSMETICS.BODY": "Изменить цвет всей одежды?",
    "POPUP.COSMETICS_COLOR_COSMETICS.OPT1": "Да! :')",
    "POPUP.COSMETICS_COLOR_COSMETICS.OPT2": "Нет...",
    "ESC.HEADER": "Меню",
    "ESC.CUSTOMIZE": "Персонаж",
    "MOONS.BACK": "Назад",
    "MOONS.MOON_2.ATTRIBUTE_3": "Лечилка в грузовике теперь восстанавливает 25 здоровья.",
    "MOONS.MOON_4.ATTRIBUTE_3": "Монстры теперь получают еще меньше урона от падений.",
    "LOADING.LEVEL.SHOP": "Магазин",
    "SERVER_LIST_SEARCH.CONFIRM": "Найти",
    "SERVER_LIST_SEARCH.BACK": "Назад",
    "SERVER_LIST_CREATE_NEW.CONFIRM": "Создать",
    "SERVER_LIST_CREATE_NEW.BACK": "Назад",
}

def update_dictionary(dictionary_file, translations):
    with open(dictionary_file, "r", encoding="utf-8") as f:
        dictionary = json.load(f)
    dictionary.update(translations)
    with open(dictionary_file, "w", encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    dict_file = r"C:\Users\Lecoo\projects\repo-russianlocalization\dictionaries\dictionary.json"
    update_dictionary(dict_file, translations)
    print("Dictionary fully finalized.")
