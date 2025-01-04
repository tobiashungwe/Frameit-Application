import { useState } from "react";

const useSearchTheme = ({ t }) => {
  const [isSearching, setIsSearching] = useState(false);
  const [hasSearched, setHasSearched] = useState(false);
  const [keywords, setKeywords] = useState([]);

  const handleSearchTheme = async (theme) => {
    if (!theme) {
      alert(t("messages.enter_theme"));
      return;
    }

    setIsSearching(true);
    setHasSearched(true);
    try {
      const response = await fetch("http://localhost:8000/api/stories/generate_keywords", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ theme }),
      });

      const data = await response.json();

      if (response.ok) {
        setKeywords(Array.isArray(data.suggestions) ? data.suggestions : []);
      } else {
        console.error("Error fetching keywords:", data);
        setKeywords([]); // Reset to an empty array
        alert(t("messages.no_keywords_found"));
      }
    } catch (error) {
      console.error("Error fetching keywords:", error);
      setKeywords([]); // Reset to an empty array
      alert(t("messages.error_fetching_theme"));
    } finally {
      setIsSearching(false);
    }
  };

  return { keywords, isSearching, hasSearched, handleSearchTheme };
};

export default useSearchTheme;
