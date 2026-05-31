import json
import os

# ПОЛНЫЙ словарь перевода REPO (САМЫЙ ФИНАЛЬНЫЙ ЭТАП - Закрываем всё!)
translations = {
    # --- СТРОКИ GAME.TSV ---
    "COSMETIC_SHOP_MACHINE.NEW": "Новинка!",
    "TRUCK_SCREEN.TAXMAN": "Налоговик",
    "TRUCK_SCREEN.DESTROYING_SLACKERS": "Ликвидация бездельников",
    "TRUCK_SCREEN.STARTING_ENGINE": "Запуск двигателя",
    "TRUCK_SCREEN.HITTING_THE_ROAD": "Выезд на объект",

    # --- СТРОКИ HUD.TSV (ТЕКСТЫ ДЕЙСТВИЙ) ---
    "BIG_MESSAGE.EXTRACTION.ACTIVATED": "Точка эвакуации активирована",
    "BIG_MESSAGE.EXTRACTION.COMPLETED": "Эвакуация завершена",
    "FOCUS.EXTRACTION.FIND_NEXT": "Найдите следующую точку эвакуации",
    "TUTORIAL.JUMPING.DUMMY_TEXT": "Нажимайте [jump], пока шкала не заполнится!",
    "TUTORIAL.SNEAKING.DUMMY_TEXT": "Удерживайте [crouch] и двигайтесь, пока шкала не заполнится!",
    "TUTORIAL.HIDING.DUMMY_TEXT": "Спрячьтесь под объектом, пока шкала не заполнится!",
    "TUTORIAL.SPRINTING.DUMMY_TEXT": "Бегите с [sprint], пока шкала не заполнится. Если энергия кончится — подождите.",
    "TUTORIAL.TUMBLING.DUMMY_TEXT": "Бегите с [sprint], прыгайте и жмите [tumble]. Повторяйте до заполнения!",
    "TUTORIAL.GRABBING.DUMMY_TEXT": "Удерживайте [grab] на объекте, пока шкала не заполнится!",
    "TUTORIAL.PUSHING_AND_PULLING.DUMMY_TEXT": "Удерживая предмет [grab], используйте [push], чтобы менять дистанцию!",
    "TUTORIAL.ROTATING.DUMMY_TEXT": "Удерживая предмет [grab], зажмите [grab2] и двигайте мышью для вращения!",
    "TUTORIAL.ITEM_TOGGLING.DUMMY_TEXT": "Схватите предмет и жмите [interact], пока шкала не заполнится!",
    "TUTORIAL.INVENTORY_FILL.DUMMY_TEXT": "С предметом в руках нажмите [inventory1]/[2]/[3]. Заполните все слоты!",
    "TUTORIAL.INVENTORY_EMPTY.DUMMY_TEXT": "Нажимайте [inventory1]/[2]/[3], чтобы выкинуть всё из слотов!",
    "TUTORIAL.MAP.DUMMY_TEXT": "Удерживайте [map], пока шкала не заполнится!",
    "TUTORIAL.CART_HANDLING_1.DUMMY_TEXT": "Схватите тележку за ручку [grab] и покатайте её!",
    "TUTORIAL.CART_HANDLING_2.FOCUS_TEXT": "Наполните тележку ценностями!",
    "TUTORIAL.CART_HANDLING_2.DUMMY_TEXT": "Положите три предмета в тележку.",
    "TUTORIAL.EXTRACTION_POINTS.FOCUS_TEXT": "Сдавайте ценности!",
    "TUTORIAL.EXTRACTION_POINTS.DUMMY_TEXT": "ПРИВЕТ! ЗАПОЛНИ ТОЧКУ ЭВАКУАЦИИ ЦЕННОСТЯМИ!",
    "TUTORIAL.TRUCK.DUMMY_TEXT": "Зайдите в грузовик, схватите и удерживайте область сообщения на экране!",
    "TUTORIAL.EXTRACTION_REMINDER.TEXT": "Заполняйте <b><u>ТОЧКИ ЭВАКУАЦИИ</u></b> ценностями.",
    "LEVEL.HEADER": "Уровень",
    "ENEMY.BOWTIE": "Бабочка",
    "ENEMY.HIDDEN": "Скрытый",
    "UPGRADE_STAND.INTERACT": "Удерживать: Обновить ({cost})",
    "ARENA.WINNER.KING": "Король неудачников!",
    "ARENA.WINNER.LOSERS": "Вы все — неудачники!",
    "ARENA.MESSAGE.LAST_LOSER_STANDING": "Последний выживший неудачник",
    "ARENA.MESSAGE.GAME_OVER": "Игра окончена",
    "SPECTATE_LIST.HEADER": "Сломленные:",
    "ITEM.CART.MODE_STRONG": "Режим: Мощный",
    "ITEM.CART.MODE_WEAK": "Режим: Слабый",

    # --- СТРОКИ MENU.TSV (ИНТЕРФЕЙС И СОХРАНЕНИЯ) ---
    "SAVES.SINGLEPLAYER_MODE": "Одиночный режим",
    "SAVES.MULTIPLAYER_MODE": "Сетевой режим",
    "SAVES.SAVE_INFO.USE_BACKUP": "Бэкап",
    "REGIONS.REGION.CAE": "Канада (Восток)",
    "REGIONS.REGION.HK": "Гонконг",
    "REGIONS.REGION.UAE": "ОАЭ",
    "REGIONS.REGION.USSC: USA South Central": "США (Центр)",
    "SAVES.SAVE_INFO.SORRY": "Упс, простите!",
    "SAVES.SAVE_INFO.PRESS_DELETE": "Нажмите 'Удалить', чтобы стереть \nвсю папку сохранений.",
    "SAVES.SAVE_INFO.CORRUPTED_SAVE_FILE": "Файл поврежден",
    "SAVES.SAVE_FILE.UH_OH": "Ой-ой!",
    "SAVES_RENAME.BACK": "Назад",
    "SAVES_RENAME.CONFIRM": "Ок",
    "COSMETICS.TYPE.BODY_TOP": "Одежда (верх)",
    "COSMETICS.TYPE.BODY_BOTTOM": "Одежда (низ)",
    "PASSWORD.HEADER": "Пароль",
    "PASSWORD.SKIP": "Пропустить",
    "PASSWORD.CONFIRM": "Ок",
    "SAVES.SAVE_INFO.PLAYER_SOLO": "Вы справились в одиночку!",
    "POPUP.VERSION_MISMATCH.BUTTON": "Ясно",
    "POPUP.LOBBY_CLOSED.HEADER": "Лобби закрыто",
    "POPUP.LOBBY_CLOSED.BODY": "Лобби было закрыто.",
    "POPUP.LOBBY_CLOSED.BUTTON": "Понятно",
    "POPUP.DISCONNECTED.CAUSE_PREFIX": "Причина:",
    "POPUP.DISCONNECTED.BANNED_LOBBY": "Вы забанены в этом лобби.",
    "PUBLIC_GAME_CHOICE.HEADER": "Открытая игра",
    "PUBLIC_GAME_CHOICE.RANDOM_MATCHMAKING": "Случайный подбор",
    "PUBLIC_GAME_CHOICE.SERVER_LIST": "Список серверов",
    "PUBLIC_GAME_CHOICE.BACK": "Назад",
    "SETTINGS.MAX_FPS.UNLIMITED": "Без лимита",
    "SETTINGS.GAMEPLAY.INVERT_VERICAL_AIM": "Инверсия по вертикали",
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
    print(f"Dictionary finalized with {len(translations)} absolutely final translations.")
