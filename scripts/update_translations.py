import json
import os

# ПОЛНЫЙ словарь перевода REPO (100% локализация)
translations = {
    # --- ГЛАВНОЕ МЕНЮ И ИНТЕРФЕЙС ---
    "MAIN.PRIVATE_GAME": "Закрытая игра",
    "MAIN.PUBLIC_GAME": "Открытая игра",
    "MAIN.JOIN_FRIEND": "Присоединиться к другу",
    "MAIN.SINGLEPLAYER": "Одиночная игра",
    "MAIN.TUTORIAL": "Обучение",
    "MAIN.SETTINGS": "Настройки",
    "MAIN.QUIT_GAME": "Выход",
    "MAIN.CUSTOMIZE": "Кастомизация",
    "LOADING.LOADING": "Загрузка...",
    "LOBBY.HEADER": "Лобби",
    "LOBBY.START_GAME": "Начать игру",
    "LOBBY.LEAVE": "Покинуть",
    "ESC.CONTINUE": "Продолжить",
    "ESC.SETTINGS": "Настройки",
    "ESC.MAIN_MENU": "Главное меню",
    "ESC.QUIT_GAME": "Выйти из игры",
    "ESC.ACTIVE_MOONS": "Активные луны",
    "ESC.SELF_DESTRUCT": "Самоуничтожение",

    # --- ПРЕДМЕТЫ (ITEM) ---
    "ITEM.GRENADE_EXPLOSIVE": "Осколочная граната",
    "ITEM.GRENADE_STUN": "Шоковая граната",
    "ITEM.GUN_HANDGUN": "Пистолет",
    "ITEM.GUN_LASER": "Фотонный бластер",
    "ITEM.GUN_SHOTGUN": "Дробовик",
    "ITEM.HEALTH_PACK_SMALL": "Малая аптечка (25)",
    "ITEM.HEALTH_PACK_MEDIUM": "Средняя аптечка (50)",
    "ITEM.HEALTH_PACK_LARGE": "Большая аптечка (100)",
    "ITEM.RUBBER_DUCK": "Резиновая уточка",
    "ITEM.POWER_CRYSTAL": "Энергокристалл",
    "ITEM.REVIVE_ITEM": "Дефибриллятор",
    "ITEM.WALKIE_TALKIE": "Рация Semibot",
    "ITEM.CART_MEDIUM": "Тележка C.A.R.T.",
    "ITEM.CART_SMALL": "Карманная C.A.R.T.",
    "ITEM.LEAF_BLOWER": "Воздуходувка",
    "ITEM.MELEE_BASEBALL_BAT": "Бейсбольная бита",
    "ITEM.MELEE_FRYING_PAN": "Сковорода",
    "ITEM.MELEE_INFLATABLE_HAMMER": "Надувной молот",
    "ITEM.MELEE_SLEDGE_HAMMER": "Кувалда",
    "ITEM.MELEE_STUN_BATON": "Электрошокер",
    "ITEM.MELEE_SWORD": "Меч",
    "ITEM.MINE_EXPLOSIVE": "Взрывная мина",
    "ITEM.MINE_SHOCKWAVE": "Ударная мина",
    "ITEM.MINE_STUN": "Электроловушка",
    "ITEM.PHASE_BRIDGE": "Фазовый мост",
    "ITEM.VALUABLE_TRACKER": "Детектор ценностей",
    "ITEM.EXTRACTION_TRACKER": "Трекер эвакуации",
    "ITEM.DRONE_BATTERY": "Дрон-зарядник",
    "ITEM.DRONE_FEATHER": "Дрон-перо",
    "ITEM.DRONE_INDESTRUCTIBLE": "Неуязвимый дрон",
    "ITEM.DRONE_TORQUE": "Дрон-катун",
    "ITEM.DRONE_ZERO_GRAVITY": "Гравидрон",
    "ITEM.DUCK_BUCKET": "Ведро с уточками",

    # --- ВРАГИ (ENEMY) ---
    "ENEMY.ANIMAL": "Зверь",
    "ENEMY.BANG": "Громила",
    "ENEMY.BEAMER": "Клоун",
    "ENEMY.BIRTHDAY_BOY": "Именинник",
    "ENEMY.BOMB_THROWER": "Ликвидатор",
    "ENEMY.CEILING_EYE": "Наблюдатель",
    "ENEMY.DUCK": "Высший хищник",
    "ENEMY.ELSA": "Эльза",
    "ENEMY.GNOME": "Гном",
    "ENEMY.HEAD": "Главарь",
    "ENEMY.HUNTER": "Охотник",
    "ENEMY.RUNNER": "Жнец",
    "ENEMY.SHADOW": "Мрак",
    "ENEMY.THIN_MAN": "Дитя тени",
    "ENEMY.TUMBLER": "Повар",
    "ENEMY.FLOATER": "Менталист",
    "ENEMY.HEAD_GRABBER": "Хватоглав",
    "ENEMY.HEART_HUGGER": "Сердцеед",
    "ENEMY.SLOW_MOUTH": "Плевун",
    "ENEMY.SLOW_WALKER": "Бродяга",
    "ENEMY.SPINNY": "Гамбит",
    "ENEMY.VALUABLE_THROWER": "Мелкий воришка",
    "ENEMY.ROBE": "Мантия",
    "ENEMY.TICK": "Клещ",

    # --- ОБУЧЕНИЕ И ИНСТРУКЦИИ (TUTORIAL / FOCUS) ---
    "TUTORIAL.TRANSITION_TEXT": "Отличная работа!",
    "TUTORIAL.MOVEMENT.TEXT": "Используйте [move] для перемещения.",
    "TUTORIAL.MOVEMENT.FOCUS_TEXT": "Двигайтесь, чтобы заполнить шкалу прогресса!",
    "TUTORIAL.MOVEMENT.DUMMY_TEXT": "Используйте [move] на клавиатуре, пока шкала не заполнится!",
    "TUTORIAL.JUMPING.TEXT": "Нажмите [jump] для прыжка.",
    "TUTORIAL.JUMPING.FOCUS_TEXT": "Прыгайте, чтобы заполнить шкалу!",
    "TUTORIAL.SNEAKING.TEXT": "Нажмите [crouch], чтобы красться. Так монстрам сложнее вас заметить.",
    "TUTORIAL.SNEAKING.FOCUS_TEXT": "Крадитесь, чтобы заполнить шкалу!",
    "TUTORIAL.SPRINTING.TEXT": "Удерживайте [sprint] для бега. Это расходует выносливость.",
    "TUTORIAL.SPRINTING.FOCUS_TEXT": "Бегите, чтобы заполнить шкалу!",
    "TUTORIAL.GRABBING.TEXT": "Хватайте объекты, используя [grab].",
    "TUTORIAL.MAP.TEXT": "Используйте [map], чтобы открыть карту. Карта <b><u>КРИТИЧЕСКИ ВАЖНА</u></b> для навигации.",
    "TUTORIAL.TRUCK.TEXT": "Зайдите в <b><u>ГРУЗОВИК</u></b> и отправьте сообщение боссу, чтобы покинуть уровень.",
    "TUTORIAL.TRUCK.FOCUS_TEXT": "Зайдите в грузовик и отправьте сообщение!",
    "TUTORIAL.HEALING.TEXT": "Делитесь здоровьем с другими игроками, хватая их за шеи!",
    "TUTORIAL.REVIVING.TEXT": "Оживляйте павших товарищей, извлекая их головы!",
    "TUTORIAL.CHARGING_STATION.TEXT": "Покупайте <b><u>ЭНЕРГОКРИСТАЛЛЫ</u></b> для <b><u>ЗАРЯДНОЙ СТАНЦИИ</u></b>, чтобы чинить и заряжать снаряжение!",
    "TUTORIAL.CHAT.TEXT": "Нажмите [chat], чтобы открыть чат! Это весело!",
    "TUTORIAL.SHOP.TEXT": "Это <b><u>МАГАЗИН</u></b>. Сдавайте предметы для покупок. Здесь вы в безопасности!",
    "TUTORIAL.OVERCHARGE_1.TEXT": "Захват монстра вызывает перегрузку. Когда шкала заполнится, произойдет взрыв.",
    "TUTORIAL.ENEMY_ELSA.TEXT": "ПОГЛАДЬ СОБАКУ!",
    "FOCUS.EXTRACTION.FILL_VALUABLES": "Заполните точку эвакуации ценностями",
    "FOCUS.EXTRACTION.AVOID_GRENADES": "Осторожно, гранаты!",
    "FOCUS.EXTRACTION.BACK_TO_TRUCK": "Возвращайтесь к грузовику!",
    "FOCUS.SHOP.INTRO": "Купите что-нибудь полезное в магазине",
    "FOCUS.TRUCK.INTRO": "Наслаждайтесь поездкой, заряжайтесь и ГОТОВЬТЕСЬ!",
    "COSMETIC_SHOP_MACHINE.INFO_TEXT": "Нажмите [interact], чтобы вставить жетон",
    "MOON_UI.SKIP": "[menu], чтобы пропустить",

    # --- НАСТРОЙКИ (SETTINGS) ---
    "SETTINGS.HEADER": "Настройки",
    "SETTINGS.GAMEPLAY": "Геймплей",
    "SETTINGS.GRAPHICS": "Графика",
    "SETTINGS.AUDIO": "Звук",
    "SETTINGS.CONTROLS": "Управление",
    "SETTINGS.LANGUAGE": "Язык",
    "SETTINGS.BACK": "Назад",
    "SETTINGS.BOOL.ON": "Вкл",
    "SETTINGS.BOOL.OFF": "Выкл",
    "SETTINGS.GAMEPLAY.PHOTOSENSITIVITY": "Светочувствительность",
    "SETTINGS.GAMEPLAY.ARACHNOPHOBIA": "Арахнофобия",
    "SETTINGS.GAMEPLAY.AIM_SENSITIVITY": "Чувствительность прицела",
    "SETTINGS.GRAPHICS.WINDOW_MODE": "Оконный режим",
    "SETTINGS.GRAPHICS.VSYNC": "Вертикальная синхронизация",
    "SETTINGS.GRAPHICS.GAMMA": "Гамма",
    "SETTINGS.GRAPHICS.MAX_FPS": "Макс. FPS",
    "SETTINGS.AUDIO.MASTER_VOLUME": "Общая громкость",
    "SETTINGS.AUDIO.MUSIC_VOLUME": "Громкость музыки",
    "SETTINGS.AUDIO.SFX_VOLUME": "Громкость эффектов",

    # --- СОХРАНЕНИЯ (SAVES) ---
    "SAVES.HEADER": "Сохранения",
    "SAVES.NEW_GAME": "Новая игра",
    "SAVES.GO_BACK": "< Назад",
    "SAVES.SAVE_INFO.TOTAL_HAUL": "Общий улов:",
    "SAVES.SAVE_INFO.CURRENT_MOON": "Текущая луна:",
    "SAVES.SAVE_INFO.DELETE_SAVE": "Удалить",
    "SAVES.SAVE_INFO.LOAD_SAVE": "Загрузить",

    # --- ЛОКАЦИИ (LEVEL) ---
    "LEVEL.NAME.SHOP": "Сервисная станция",
    "LEVEL.NAME.ARENA": "Арена утилизации",
    "LEVEL.NAME.ARCTIC": "Станция Мак-Джаннек",
    "LEVEL.NAME.MANOR": "Поместье старосты",
    "LEVEL.NAME.MUSEUM": "Музей человеческого искусства",
    "LEVEL.NAME.WIZARD": "Академия Свифтбрум",

    # --- ЭВАКУАЦИЯ (EXTRACTION) ---
    "EXTRACTION.READY": "Готово",
    "EXTRACTION.ACTIVE": "Активно",
    "EXTRACTION.EXTRACTING": "Эвакуация...",
    "EXTRACTION.COMPLETED": "Завершено",
    "EXTRACTION.LOCKED": "Заблокировано",

    # --- ЛУНЫ / МУТАТОРЫ (MOONS) ---
    "MOONS.HEADER": "Активные луны",
    "MOONS.MOON_1.NAME": "Растущая луна",
    "MOONS.MOON_1.ATTRIBUTE_1": "Лечилка в грузовике теперь восстанавливает 35 здоровья.",
    "MOONS.MOON_1.ATTRIBUTE_2": "Монстров теперь сложнее сбить с ног ценными вещами.",
    "MOONS.MOON_2.NAME": "Полумесяц",
    "MOONS.MOON_2.ATTRIBUTE_1": "Монстры теперь перегружают ваш захват.",
    "MOONS.MOON_2.ATTRIBUTE_2": "Монстры получают тяжелый урон от падения в ямы, но могут выжить.",
    "MOONS.MOON_3.NAME": "Полнолуние",
    "MOONS.MOON_3.ATTRIBUTE_1": "Монстры перегружают ваш захват на 25% быстрее.",
    "MOONS.MOON_3.ATTRIBUTE_2": "Монстры получают меньше урона от падений.",
    "MOONS.MOON_4.NAME": "Суперлуние",
    "MOONS.MOON_4.ATTRIBUTE_1": "Вражеские сферы теперь взрываются при уничтожении.",
    "MOONS.MOON_4.ATTRIBUTE_2": "Монстры перегружают ваш захват на 50% быстрее.",

    # --- СИСТЕМНЫЕ ПОПАПЫ ---
    "POPUP.QUIT_GAME.HEADER": "Выход",
    "POPUP.QUIT_GAME.BODY": "Закрыть приложение?",
    "POPUP.QUIT_GAME.OPT1": "Да",
    "POPUP.QUIT_GAME.OPT2": "Нет",
    "POPUP.VERSION_MISMATCH.HEADER": "Разные версии игры",
    "POPUP.VERSION_MISMATCH.BODY": "В лобби используется версия:\n{version}",
    "POPUP.DISCONNECTED.HEADER": "Соединение разорвано",
    "POPUP.KICKED.HEADER": "Вы исключены",
    "POPUP.KICKED.BODY": "Вас выгнал хост.",
    "POPUP.SAVE_LIMIT.HEADER": "Лимит сохранений",
    "POPUP.SAVE_LIMIT.BODY": "Вы достигли лимита в {limit} сохранений.",

    # --- УЛУЧШЕНИЯ (UPGRADES) ---
    "STATS.UPGRADE.HEALTH": "Здоровье",
    "STATS.UPGRADE.STAMINA": "Выносливость",
    "STATS.UPGRADE.SPEED": "Скорость бега",
    "STATS.UPGRADE.RANGE": "Дальность захвата",
    "STATS.UPGRADE.STRENGTH": "Сила захвата",
    "STATS.UPGRADE.EXTRA_JUMP": "Доп. прыжок",
    "STATS.UPGRADE.CROUCH_REST": "Отдых сидя",
    "STATS.UPGRADE.DEATH_HEAD_BATTERY": "Заряд головы",
}

def update_dictionary(dictionary_file, translations):
    if not os.path.exists(dictionary_file):
        dictionary = {}
    else:
        with open(dictionary_file, "r", encoding="utf-8") as f:
            dictionary = json.load(f)
    
    dictionary.update(translations)
    
    with open(dictionary_file, "w", encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    dict_file = r"C:\Users\Lecoo\projects\repo-russianlocalization\dictionaries\dictionary.json"
    update_dictionary(dict_file, translations)
    print(f"Dictionary updated with {len(translations)} high-quality translations.")
