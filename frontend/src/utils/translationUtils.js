import config from "../config";

export const fetchTranslations = async (language) => {
    try {
      const response = await fetch(`${config.API_BASE_URL}/api/translations/${language}`);
      if (!response.ok) {
        throw new Error("Failed to load translations");
      }
      const data = await response.json();
      return data.translations;
    } catch (error) {
      console.error("Error fetching translations:", error);
      return {};
    }
  };
  