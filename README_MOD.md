# Динамический переводчик R.E.P.O. (Russian Localization Mod)

Этот плагин обеспечивает качественный русский перевод для игры REPO, используя динамическую подмену текста и инъекцию шрифтов.

## ✨ Особенности
*   **100% покрытие:** Переводит не только файлы локализации, но и динамические строки, генерируемые кодом.
*   **Исправление шрифтов:** Автоматически заменяет стандартные шрифты Unity на версии с поддержкой кириллицы (SDF), предотвращая появление "квадратов".
*   **Высокая производительность:** Использует `ConcurrentDictionary` для мгновенного поиска переводов без задержек в игре.
*   **Легкое обновление:** Синхронизируется с файлом `dictionary.json`.

## 🚀 Установка

1.  Установите **BepInEx 5.x** (x64) в папку с игрой.
2.  Скачайте `RussianLocalization.dll` и папку `RussianLocalization` из раздела релизов.
3.  Поместите их в папку `REPO/BepInEx/plugins/`.
    *   Путь должен выглядеть так: `REPO/BepInEx/plugins/RussianLocalization/RussianLocalization.dll`
    *   Путь к словарю: `REPO/BepInEx/plugins/RussianLocalization/dictionary.json`
4.  Запустите игру.

## 🛠 Сборка (для разработчиков)

Для компиляции плагина потребуются следующие библиотеки из папки `REPO_Data/Managed/`:
*   `UnityEngine.dll`
*   `UnityEngine.UI.dll`
*   `UnityEngine.AssetBundleModule.dll`
*   `Unity.TextMeshPro.dll`
*   `BepInEx.dll` (из папки BepInEx/core)
*   `0Harmony.dll` (из папки BepInEx/core)

---
*Сделано с помощью Gemini CLI.*
