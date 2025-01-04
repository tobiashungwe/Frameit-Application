import React, { useState, useEffect } from "react";
import { Box, Typography, Button, CircularProgress, Autocomplete, TextField } from "@mui/material";
import { useTranslation } from "react-i18next";
import KeywordsSelector from "./KeywordsSelector";

const ThemeSearch = ({
  theme,
  onThemeChange,
  keywords = [],
  selectedKeywords,
  onKeywordToggle,
  onSearch,
  isSearching,
  hasSearched,
}) => {
  const { t } = useTranslation();
  const [themeOptions, setThemeOptions] = useState([]);
  const [isLoadingThemes, setIsLoadingThemes] = useState(false);

  useEffect(() => {
    const fetchThemes = async () => {
      setIsLoadingThemes(true);
      try {
        const response = await fetch("http://localhost:8000/api/themes/");
        if (!response.ok) {
          throw new Error("Failed to fetch themes");
        }
        const data = await response.json();
        setThemeOptions(data);
      } catch (error) {
        console.error("Error fetching themes:", error);
        setThemeOptions([]);
      } finally {
        setIsLoadingThemes(false);
      }
    };

    fetchThemes();
  }, []);

  return (
    <>
      <Box mt={4}>
        <Typography variant="h6">{t("labels.theme")}</Typography>
        {isLoadingThemes ? (
          <CircularProgress />
        ) : (
          <Autocomplete
            options={themeOptions.map((theme) => theme.title)} // Assuming themes have a `title` field
            freeSolo
            onInputChange={(e, value) => {
              onThemeChange(value);
            }}
            renderInput={(params) => (
              <TextField
                {...params}
                label={t("placeholders.select_theme")}
                variant="outlined"
                fullWidth
              />
            )}
          />
        )}
        <Button
          variant="contained"
          color="primary"
          onClick={onSearch}
          sx={{ mt: 2 }}
          disabled={isSearching}
        >
          {isSearching ? <CircularProgress size={24} /> : t("labels.search")}
        </Button>
      </Box>

      {keywords.length > 0 && (
        <Box mt={4}>
          <KeywordsSelector
            keywords={keywords}
            selectedKeywords={selectedKeywords}
            onKeywordSelection={onKeywordToggle}
            t={t}
          />
        </Box>
      )}

      {keywords.length === 0 && !isSearching && hasSearched && (
        <Box mt={4}>
          <Typography variant="body1">{t("messages.no_keywords_found")}</Typography>
        </Box>
      )}
    </>
  );
};

export default ThemeSearch;
