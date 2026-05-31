import json
import os

# ПОЛНЫЙ словарь перевода REPO (100% локализация - Часть 2)
# Охватываем все оставшиеся редкие предметы, врагов и технические настройки
translations = {
    # --- МЕНЮ НАСТРОЕК (ПРОДОЛЖЕНИЕ) ---
    "SETTINGS.GRAPHICS.LENS_DISTORTION": "Дисторсия линзы",
    "SETTINGS.GRAPHICS.BLOOM": "Свечение (Bloom)",
    "SETTINGS.GRAPHICS.CHROMATIC_ABERRATION": "Хроматическая аберрация",
    "SETTINGS.GRAPHICS.MOTION_BLUR": "Размытие в движении",
    "SETTINGS.GRAPHICS.GRAIN": "Зернистость",
    "SETTINGS.GRAPHICS.PIXELATION": "Пикселизация",
    "SETTINGS.GRAPHICS.SHADOW_QUALITY": "Качество теней",
    "SETTINGS.GRAPHICS.SHADOW_DISTANCE": "Дальность теней",
    "SETTINGS.GRAPHICS.LIGHT_DISTANCE": "Дальность освещения",
    "SETTINGS.AUDIO.MUSIC_VOLUME": "Громкость музыки",
    "SETTINGS.AUDIO.MASTER_VOLUME": "Мастер-громкость",
    "SETTINGS.AUDIO.SFX_VOLUME": "Громкость эффектов",
    "SETTINGS.AUDIO.PROXIMITY_VOICE_VOLUME": "Громкость голосового чата",
    "SETTINGS.AUDIO.PUSH_TO_TALK": "Рация (Push to Talk)",
    "SETTINGS.CONTROLS.MOVEMENT": "Движение",
    "SETTINGS.CONTROLS.JUMP": "Прыжок",
    "SETTINGS.CONTROLS.SPRINT": "Бег",
    "SETTINGS.CONTROLS.CROUCH": "Присесть",
    "SETTINGS.CONTROLS.INTERACT": "Взаимодействие",
    "SETTINGS.CONTROLS.MAP": "Карта",
    "SETTINGS.CONTROLS.CHAT": "Чат",

    # --- ПРЕДМЕТЫ И ВАЛЮТА (ОСТАТКИ) ---
    "ITEM.GRENADE_DUCT_TAPED": "Связка гранат на изоленте",
    "ITEM.GRENADE_SHOCKWAVE": "Ударная граната",
    "ITEM.MINE_SHOCKWAVE": "Ударная мина",
    "ITEM.MINE_STUN": "Электроловушка",
    "ITEM.ORB_ZERO_GRAVITY": "Сфера антигравитации",
    "ITEM.REVIVE_ITEM": "Дефибриллятор",
    "ITEM.STAFF_VOID": "Посох Бездны",
    "ITEM.STAFF_ZERO_GRAVITY": "Посох антигравитации",
    "ITEM.VEHICLE_SEMISCOOTER": "Грузовоз",
    "ITEM.VEHICLE_SEMISCOOTER_SMALL": "Разведчик",
    "ITEM.WALKIE_TALKIE_BOX": "Ящик с рациями",
    "VALUABLE_BOX.EXTRACT": "Сдать",
    "VALUABLE_BOX.TOO_FULL": "Переполнено",
    "VALUABLE_BOX.TOO_BIG": "Слишком большой",

    # --- ВРАГИ И СУЩЕСТВА (ПОЛНЫЙ СПИСОК) ---
    "ENEMY.OOGLY": "Углик",
    "ENEMY.RUNNER": "Жнец",
    "ENEMY.SHADOW": "Мрак",
    "ENEMY.SLOW_MOUTH": "Плевун",
    "ENEMY.SLOW_WALKER": "Бродяга",
    "ENEMY.SPINNY": "Гамбит",
    "ENEMY.THIN_MAN": "Дитя тени",
    "ENEMY.TICK": "Клещ",
    "ENEMY.TRICYCLE": "Белла",
    "ENEMY.UPSCREAM": "Крикун",
    "ENEMY.VALUABLE_THROWER": "Воришка",
    "ENEMY.CEILING_EYE": "Наблюдатель",
    "ENEMY.DUCK": "Высший хищник",
    "ENEMY.ELSA": "Эльза",
    "ENEMY.GNOME": "Гном",
    "ENEMY.HEAD": "Главарь",
    "ENEMY.ROBE": "Мантия",

    # --- ТЕКСТЫ ОБУЧЕНИЯ (ДЕТАЛЬНО) ---
    "TUTORIAL.CART_HANDLING_1.TEXT": "Это Т.Е.Л.Е.Ж.К.А. Хватайте её за ручку.",
    "TUTORIAL.CART_HANDLING_1.FOCUS_TEXT": "Покатайте Т.Е.Л.Е.Ж.К.У. немного!",
    "TUTORIAL.CART_HANDLING_2.TEXT": "Наполняйте тележки ценностями. Они <b><u>ВАЖНЫ</u></b>, чтобы унести больше добра.",
    "TUTORIAL.EXTRACTION_POINTS.TEXT": "Активируйте и заполняйте <b><u>ТОЧКИ ЭВАКУАЦИИ</u></b> ценностями.",
    "TUTORIAL.FINAL_EXTRACTION.TEXT": "Пора уходить! Грузовик лечит вас и оживляет принесенные головы игроков!",
    "TUTORIAL.MULTIPLE_EXTRACTIONS.TEXT": "На этом уровне несколько <b><u>ТОЧЕК ЭВАКУАЦИИ</u></b>, нужно очистить их все!",
    "TUTORIAL.HEAD_SPECTATE_1.TEXT": "Пока вы мертвы, ваша голова заряжается. Используйте заряд, чтобы ненадолго захватить контроль над ней.",
    "TUTORIAL.HEAD_SPECTATE_2.TEXT": "Управляя головой, удерживайте [jump] для прыжка. Чем дольше держите, тем выше прыжок, но выше и цена.",

    # --- СИСТЕМНЫЕ СООБЩЕНИЯ (LOBBY / POPUP) ---
    "LOBBY.START_GAME": "Начать игру",
    "LOBBY.INVITE": "Пригласить",
    "LOBBY.PLAYER_JOINING": "Игрок подключается...",
    "LOBBY.CHAT_PROMPT": "Нажмите [chat], чтобы написать",
    "POPUP.START_GAME.HEADER": "Начать игру",
    "POPUP.START_GAME.BODY": "Все готовы?\n\nПосле старта новые игроки\nне смогут присоединиться.",
    "POPUP.LEAVE_LOBBY.HEADER": "Покинуть лобби",
    "POPUP.LEAVE_LOBBY.BODY": "Вы уверены?",
    "POPUP.DISCONNECTED.HOST_DISCONNECTED": "Хост разорвал соединение",
    "POPUP.DISCONNECTED.STUCK_LOADING": "Зависло при загрузке",
    "POPUP.SAVE_LIMIT.BUTTON": "Понятно",
    "POPUP.KICKED.BUTTON": "Вот блин",
    "POPUP.DISCONNECTED.BUTTON": "Вот блин",
    "SERVER_LIST.HEADER": "Список серверов",
    "SERVER_LIST.SEARCH": "Поиск",
    "SERVER_LIST.CREATE_NEW": "Создать",
    "SERVER_LIST.BACK": "Назад",
    "SETTINGS.MAX_FPS.UNLIMITED": "Без ограничений",
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
    print(f"Dictionary finalized with {len(translations)} more translations.")
