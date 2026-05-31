using System;
using System.IO;
using System.Text;
using System.Collections.Generic;
using System.Collections.Concurrent;
using System.Reflection;
using System.Text.RegularExpressions;
using BepInEx;
using HarmonyLib;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

namespace RepoRussianLocalization
{
    [BepInPlugin("com.gemini.repo.rus", "REPO Russian Localization", "1.0.0")]
    public class RussianLocalization : BaseUnityPlugin
    {
        private static ConcurrentDictionary<string, string> Dictionary = new ConcurrentDictionary<string, string>();
        private static TMP_FontAsset RussianFont;
        private static bool FontInitialized = false;

        void Awake()
        {
            Log("Инициализация динамического переводчика...");
            LoadDictionary();
            
            var harmony = new Harmony("com.gemini.repo.rus");
            harmony.PatchAll();
            
            Log("Патчи Harmony применены успешно.");
        }

        private void LoadDictionary()
        {
            string path = Path.Combine(Paths.PluginPath, "RussianLocalization", "dictionary.json");
            if (!File.Exists(path))
            {
                LogWarning($"Словарь не найден по пути: {path}");
                return;
            }

            try
            {
                string json = File.ReadAllText(path, Encoding.UTF8);
                // Простая загрузка JSON (для минимизации зависимостей можно использовать встроенный JsonUtility или простую логику)
                // Здесь предполагается наличие словаря в формате {"Key": "Value"}
                var matches = Regex.Matches(json, "\"([^\"]+)\":\\s*\"([^\"]+)\"");
                foreach (Match match in matches)
                {
                    Dictionary[match.Groups[1].Value] = match.Groups[2].Value.Replace("\\n", "\n");
                }
                Log($"Загружено {Dictionary.Count} строк из словаря.");
            }
            catch (Exception e)
            {
                LogError($"Ошибка при загрузке словаря: {e.Message}");
            }
        }

        // --- Патчи для замены текста ---

        [HarmonyPatch(typeof(TMP_Text), "text", MethodType.Setter)]
        class PatchTMPText
        {
            static void Prefix(TMP_Text __instance, ref string value)
            {
                if (string.IsNullOrEmpty(value)) return;
                
                if (Dictionary.TryGetValue(value, out string translated))
                {
                    value = translated;
                }
                
                // Принудительная замена шрифта для кириллицы
                TryFixFont(__instance);
            }
        }

        [HarmonyPatch(typeof(Text), "text", MethodType.Setter)]
        class PatchUnityText
        {
            static void Prefix(Text __instance, ref string value)
            {
                if (string.IsNullOrEmpty(value)) return;

                if (Dictionary.TryGetValue(value, out string translated))
                {
                    value = translated;
                }
            }
        }

        // --- Патч для шрифтов ---

        private static void TryFixFont(TMP_Text textComponent)
        {
            if (!FontInitialized)
            {
                // Ищем встроенный в Unity шрифт, поддерживающий кириллицу (Liberation Sans или Arial)
                var fonts = Resources.FindObjectsOfTypeAll<TMP_FontAsset>();
                foreach (var font in fonts)
                {
                    if (font.name.Contains("Liberation Sans") || font.name.Contains("Arial"))
                    {
                        RussianFont = font;
                        FontInitialized = true;
                        break;
                    }
                }
            }

            if (RussianFont != null && textComponent.font != RussianFont)
            {
                textComponent.font = RussianFont;
            }
        }

        private static void Log(string message) => BepInEx.Logging.Logger.CreateLogSource("REPO_RUS").LogInfo(message);
        private static void LogWarning(string message) => BepInEx.Logging.Logger.CreateLogSource("REPO_RUS").LogWarning(message);
        private static void LogError(string message) => BepInEx.Logging.Logger.CreateLogSource("REPO_RUS").LogError(message);
    }
}
