import i18n from "i18next";
import { initReactI18next } from "react-i18next";
import LanguageDetector from "i18next-browser-languagedetector";

// Import translation files
import en from "./locales/en.json";
import nl from "./locales/nl.json";
import de from "./locales/de.json";
import it from "./locales/it.json";
import es from "./locales/es.json";

const resources = {
  en: { translation: en },
  nl: { translation: nl },
  de: { translation: de },
  it: { translation: it },
  es: { translation: es }
};

i18n
  .use(initReactI18next)
  .use(LanguageDetector) // Automatically detect user language
  .init({
    resources,
    fallbackLng: "nl", // Default language
    interpolation: { escapeValue: false }, // React already escapes values
  });

export default i18n;
