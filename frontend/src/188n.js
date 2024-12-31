import i18n from "i18next";
import { initReactI18next } from "react-i18next";

i18n.use(initReactI18next).init({
  fallbackLng: "en",
  interpolation: { escapeValue: false }, // React already escapes values
});

export const loadTranslations = async (language) => {
  try {
    const response = await fetch(`http://localhost:8000/translations/${language}`);
    if (!response.ok) {
      throw new Error("Failed to load translations");
    }
    const data = await response.json();
    i18n.addResourceBundle(language, "translation", data.translations, true, true);
    i18n.changeLanguage(language);
  } catch (error) {
    console.error("Error loading translations:", error);
  }
};