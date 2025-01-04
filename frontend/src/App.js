import React, { useState, useEffect } from "react";
import { ThemeProvider, createTheme, Container, Box } from "@mui/material";
import { useTranslation } from "react-i18next";
import "./i18n";

// Import child components
import LanguageSelector from "./components/LanguageSelector";
import FileUploader from "./components/FileUploader";
import SanitizedContentViewer from "./components/SanitizedContentViewer";
import ThemeSearch from "./components/ThemeSearch";
import ParameterSelector from "./components/ParameterSelector";
import StoryGenerator from "./components/StoryGenerator";
import DocumentViewer from "./components/DocumentViewer";

// Import hooks`
import useFileUpload from "./hooks/useFileUpload";
import useStoryGeneration from "./hooks/useStoryGeneration";
import useSearchTheme from "./hooks/useSearchTheme";


//Functions 
const fetchTranslations = async (language) => {
  try {
    const response = await fetch(`http://localhost:8000/api/translations/${language}`);
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
// ===================================================

const appTheme = createTheme({
  palette: {
    primary: { main: "#3f51b5" },
    secondary: { main: "#f50057" },
  },
  typography: {
    fontFamily: "Roboto, sans-serif",
  },
});

// Some static data (if needed)
const staticMaterials = ["Hoops", "Balls", "Cones", "Mats", "Tunnels"];
const staticTerrains = ["Indoor Gym", "Grass Field", "Playground", "Beach"];
const staticGroups = ["Small Group", "Medium Group", "Large Group"];
const defaultLanguage = "nl";

function App() {
  const { t, i18n } = useTranslation();

  // Global states
  const [language, setLanguage] = useState(defaultLanguage);
  const [file, setFile] = useState(null);
  const [sanitizedContent, setSanitizedContent] = useState("");

  const [theme, setTheme] = useState("");
  const [selectedKeywords, setSelectedKeywords] = useState([]); // user-selected
  const [groupCount, setGroupCount] = useState("");
  const [terrain, setTerrain] = useState("");
  const [material, setMaterial] = useState("");
  const [story, setStory] = useState("");

  // Loading states
  const [isGenerating, setIsGenerating] = useState(false);

   // Hooks
   const { handleUploadFile } = useFileUpload({ t });
   const { handleGenerateStory } = useStoryGeneration({ t });
   const { keywords, isSearching, hasSearched, handleSearchTheme } = useSearchTheme({ t });

  useEffect(() => {
    loadLanguage(language);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [language]);

  const loadLanguage = async (lang) => {
    try {
      const translations = await fetchTranslations(lang);
      i18n.addResourceBundle(lang, "translation", translations, true, true);
      await i18n.changeLanguage(lang);
      setLanguage(lang);
    } catch (error) {
      console.error("Error loading language:", error);
    }
  };

  // =====================
  // HANDLERS
  // =====================

  const handleLanguageChange = (event) => {
    const selectedLanguage = event.target.value;
    setLanguage(selectedLanguage);
  };

  
  const handleKeywordSelection = (keyword) => {
    setSelectedKeywords((prev) =>
      prev.includes(keyword)
        ? prev.filter((kw) => kw !== keyword)
        : [...prev, keyword]
    );
  };

  

  return (
    <ThemeProvider theme={appTheme}>
      <Container maxWidth="md">
        <Box sx={{ mt: 4, p: 4, bgcolor: "background.paper", boxShadow: "0px 8px 20px rgba(0, 0, 0, 0.2)", borderRadius: 4, }}>
          
          <LanguageSelector language={language} onChange={handleLanguageChange} t={t} />

          
          <FileUploader
            file={file}
            onUploadFile={(selectedFile) => {
              setFile(selectedFile);
              handleUploadFile(selectedFile, setSanitizedContent);
            }}
            t={t}
          />

          {sanitizedContent && (
            <SanitizedContentViewer sanitizedContent={sanitizedContent} t={t} >
              <DocumentViewer />
            </SanitizedContentViewer>
          )}

          <ThemeSearch 
                theme={theme}
                onThemeChange={setTheme}
                keywords={keywords}
                selectedKeywords={selectedKeywords}
                onKeywordToggle={handleKeywordSelection}
                onSearch={() => handleSearchTheme(theme)} // Ensure this is correctly assigned
                isSearching={isSearching}
                hasSearched={hasSearched}
            />

          <ParameterSelector groupCount={groupCount}
            setGroupCount={setGroupCount}
            terrain={terrain}
            setTerrain={setTerrain}
            material={material}
            setMaterial={setMaterial}
            staticGroups={staticGroups || []}
            staticTerrains={staticTerrains || []}
            staticMaterials={staticMaterials || []}
            t={t}
          />

          <StoryGenerator
            onGenerate={() =>
              handleGenerateStory({
                theme,
                file,
                selectedKeywords,
                sanitizedContent,
                groupCount,
                terrain,
                material,
                language,
                setStory,
                setIsGenerating,
              })
            }
            isGenerating={isGenerating}
            story={story}
            t={t}
          />
        </Box>
      </Container>
    </ThemeProvider>
  );
}

export default App;
