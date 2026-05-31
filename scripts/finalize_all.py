import json
import os

# ПОЛНЫЙ словарь перевода REPO (ПОСЛЕДНИЙ РЫВОК - Косметика, Обучение, Системные)
translations = {
    # --- КОСМЕТИКА (ДЕТАЛЬНО) ---
    "COSMETICS.TYPE.HEAD_TOP_MESH": "Верх головы",
    "COSMETICS.TYPE.HEAD_BOTTOM_MESH": "Низ головы",
    "COSMETICS.TYPE.BODY_TOP_MESH": "Верх туловища",
    "COSMETICS.TYPE.BODY_BOTTOM_MESH": "Низ туловища",
    "COSMETICS.TYPE.ARM_RIGHT_MESH": "Правое плечо",
    "COSMETICS.TYPE.ARM_LEFT_MESH": "Левое плечо",
    "COSMETICS.TYPE.LEG_RIGHT_MESH": "Правое бедро",
    "COSMETICS.TYPE.LEG_LEFT_MESH": "Левое бедро",
    "COSMETICS.TYPE.GRABBER_MESH": "Захват",
    "COSMETICS.TYPE.EYE_LID_RIGHT_MESH": "Правое веко",
    "COSMETICS.TYPE.EYE_LID_LEFT_MESH": "Левое веко",
    "COSMETICS.TYPE.BODY_TOP_OVERLAY": "Нашивка (верх)",
    "COSMETICS.TYPE.BODY_BOTTOM_OVERLAY": "Нашивка (низ)",
    "COSMETICS.TYPE.HEAD_TOP_OVERLAY": "Покрытие (верх головы)",
    "COSMETICS.TYPE.HEAD_BOTTOM_OVERLAY": "Покрытие (низ головы)",
    "COSMETICS.TYPE.FOOT_RIGHT": "Правая обувь",
    "COSMETICS.TYPE.FOOT_LEFT": "Левая обувь",
    "COSMETICS.TYPE.ARM_RIGHT_OVERLAY": "Наруч (правый)",
    "COSMETICS.TYPE.ARM_LEFT_OVERLAY": "Наруч (левый)",
    "COSMETICS.TYPE.LEG_RIGHT_OVERLAY": "Понож (правый)",
    "COSMETICS.TYPE.LEG_LEFT_OVERLAY": "Понож (левый)",
    "COSMETICS.TYPE.FACE_TOP": "Верх лица",
    "COSMETICS.TYPE.FACE_BOTTOM": "Низ лица",
    "COSMETICS.TYPE.HEAD_BOTTOM": "Лицо (низ)",
    "COSMETICS.CONFIRM": "Подтвердить",
    "COSMETICS.COLOR.HEADER": "Выбор цвета",
    "COSMETICS.COLOR.CONFIRM": "Применить",
    "COSMETICS.PRESET.DELETE": "Удалить",

    # --- ТЕКСТЫ ОБУЧЕНИЯ (СЛОЖНЫЕ) ---
    "TUTORIAL.TUMBLING.TEXT": "Бегите и нажмите [tumble], чтобы красиво упасть. Прыжки тоже помогают!",
    "TUTORIAL.TUMBLING.FOCUS_TEXT": "Бегите, прыгайте и падайте, чтобы заполнить шкалу!",
    "TUTORIAL.PUSHING_AND_PULLING.TEXT": "Используйте [push], чтобы менять дистанцию до удерживаемых объектов.",
    "TUTORIAL.PUSHING_AND_PULLING.FOCUS_TEXT": "Измените дистанцию до предмета!",
    "TUTORIAL.ROTATING.TEXT": "Вращайте удерживаемые объекты с помощью [grab2].",
    "TUTORIAL.ROTATING.FOCUS_TEXT": "Вращайте вещи, чтобы заполнить шкалу!",
    "TUTORIAL.ITEM_TOGGLING.TEXT": "Схватите и нажмите [interact], чтобы включить/выключить предмет.",
    "TUTORIAL.ITEM_TOGGLING.FOCUS_TEXT": "Включите и выключите это!",
    "TUTORIAL.INVENTORY_FILL.TEXT": "Возьмите предмет и используйте [inventory1]/[2]/[3], чтобы положить его в инвентарь.",
    "TUTORIAL.INVENTORY_FILL.FOCUS_TEXT": "Заполните весь инвентарь!",
    "TUTORIAL.INVENTORY_EMPTY.TEXT": "Используйте [inventory1]/[2]/[3], чтобы достать предметы из инвентаря.",
    "TUTORIAL.INVENTORY_EMPTY.FOCUS_TEXT": "Очистите инвентарь!",
    "TUTORIAL.MAP.FOCUS_TEXT": "Проверьте карту!",
    "TUTORIAL.ONLY_ONE_EXTRACTION.TEXT": "Только одна <b><u>ТОЧКА ЭВАКУАЦИИ</u></b> активна за раз. Ищите её на карте!",
    "TUTORIAL.EXPRESSIONS.TEXT": "Используйте клавиши эмоций [1]-[6], чтобы выражать чувства. Можно даже смешивать!",
    "TUTORIAL.OVERCHARGE_2.TEXT": "Если держаться группой, эффект перегрузки ослабевает.",
    "TUTORIAL.COSMETIC_WORLD_OBJECT_1.TEXT": "Это <b><u>КОСМЕТИЧЕСКИЙ ЯЩИК</u></b>. Эвакуируйте его для получения награды.",
    "TUTORIAL.COSMETIC_WORLD_OBJECT_2.TEXT": "Если он поврежден, вы можете <b><u>ПОЛЕЧИТЬ</u></b> его своим здоровьем.",
    "TUTORIAL.COSMETIC_SHOP_MACHINE.TEXT": "Вставляйте <b><u>НАЛОГОВЫЕ ЖЕТОНЫ</u></b> в автомат, чтобы забрать награды.",

    # --- УЛУЧШЕНИЯ И ХАРАКТЕРИСТИКИ ---
    "ITEM.STAFF_TORQUE": "Посох вращения",
    "ITEM.UPGRADE_DEATH_HEAD_BATTERY": "Улучшение: Заряд мертвой головы",
    "ITEM.UPGRADE_MAP_PLAYER_COUNT": "Улучшение: Игроки на карте",
    "ITEM.UPGRADE_PLAYER_CROUCH_REST": "Улучшение: Отдых сидя",
    "ITEM.UPGRADE_PLAYER_ENERGY": "Улучшение: Выносливость",
    "ITEM.UPGRADE_PLAYER_EXTRA_JUMP": "Улучшение: Доп. прыжок",
    "ITEM.UPGRADE_PLAYER_GRAB_RANGE": "Улучшение: Дальность захвата",
    "ITEM.UPGRADE_PLAYER_GRAB_STRENGTH": "Улучшение: Сила захвата",
    "ITEM.UPGRADE_PLAYER_HEALTH": "Улучшение: Здоровье",
    "ITEM.UPGRADE_PLAYER_SPRINT_SPEED": "Улучшение: Скорость бега",
    "ITEM.UPGRADE_PLAYER_TUMBLE_CLIMB": "Улучшение: Подъем из кувырка",
    "ITEM.UPGRADE_PLAYER_TUMBLE_LAUNCH": "Улучшение: Рывок в кувырке",
    "ITEM.UPGRADE_PLAYER_TUMBLE_WINGS": "Улучшение: Крылья кувырка",
    "STATS.UPGRADE.LAUNCH": "Рывок",
    "STATS.UPGRADE.MAP_PLAYER_COUNT": "Игроки на карте",
    "STATS.UPGRADE.TUMBLE_CLIMB": "Подъем",
    "STATS.UPGRADE.TUMBLE_WINGS": "Крылья",

    # --- СИСТЕМНЫЕ ПОПАПЫ (ОКОНЧАТЕЛЬНО) ---
    "POPUP.SELF_DESTRUCT.HEADER": "Самоуничтожение",
    "POPUP.SELF_DESTRUCT.BODY": "Это действительно так?",
    "POPUP.SELF_DESTRUCT.OPT1": "Со мной всё кончено",
    "POPUP.SELF_DESTRUCT.OPT2": "Нет",
    "SAVES.PAGE_INFO.HEADER": "Сохраненные игры",
    "SAVES.PAGE_INFO.DESCRIPTION": "Здесь хранятся все ваши весёлые моменты и возможность продолжить с того же места.",
    "POPUP.DELETE_PRESET.HEADER": "Удалить пресет",
    "POPUP.DELETE_PRESET.BODY": "Вы ДЕЙСТВИТЕЛЬНО УВЕРЕНЫ, что хотите удалить этот пресет НАВСЕГДА?",
    "POPUP.COSMETICS_COLOR_ALL.HEADER": "Смена цвета",
    "POPUP.COSMETICS_COLOR_ALL.BODY": "Это изменит цвета всех частей тела и косметики. Действие необратимо!",
    "POPUP.COSMETICS_RESET_BODY.HEADER": "Очистить тело",
    "POPUP.COSMETICS_RESET_BODY.BODY": "Снять все части тела?",
    "POPUP.COSMETICS_RANDOMIZE_ALL.HEADER": "Рандом",
    "POPUP.COSMETICS_RANDOMIZE_ALL.BODY": "Случайно выбрать все части тела и косметику?",
    "SAVES_RENAME.RENAME_SAVE": "Переименовать",
    "SAVES.SAVE_INFO.CLICK_TO_RENAME": "(Нажмите для переименования)",
    "SETTINGS.SHADOW_DISTANCE.VERY_LOW": "Оч. низкая",
    "SETTINGS.SHADOW_DISTANCE.LOW": "Низкая",
    "SETTINGS.SHADOW_DISTANCE.MEDIUM": "Средняя",
    "SETTINGS.SHADOW_DISTANCE.HIGH": "Высокая",
    "SETTINGS.SHADOW_DISTANCE.VERY_HIGH": "Ультра",
    "REGIONS.REGION.AU": "Австралия",
    "REGIONS.REGION.JP": "Япония",
    "REGIONS.REGION.KR": "Южная Корея",
    "REGIONS.REGION.IN": "Индия",
    "REGIONS.REGION.TR": "Турция",
    "REGIONS.REGION.ZA": "Южная Африка",
    "EXTRACTION.TAX_RETURN": "Налоговая декларация",
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
    print(f"Dictionary finalized with {len(translations)} final translations.")
