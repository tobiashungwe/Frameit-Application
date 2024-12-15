import React, { useState } from "react";
import {
  ThemeProvider,
  createTheme,
  Container,
  Box,
  Typography,
  TextField,
  MenuItem,
  Button,
  Grid,
  Autocomplete,
  CircularProgress,
  Checkbox,
  FormControlLabel,
} from "@mui/material";
import { useDropzone } from "react-dropzone";
import { useTranslation } from "react-i18next";

// Create a Material-UI theme
const appTheme = createTheme({
  palette: {
    primary: { main: "#3f51b5" },
    secondary: { main: "#f50057" },
  },
  typography: {
    fontFamily: "Roboto, sans-serif",
  },
});

const staticThemes = ["Mario", "Minions", "Christmas", "Brawl Stars"];
const staticMaterials = ["Hoops", "Balls", "Cones", "Mats", "Tunnels"];
const staticTerrains = ["Indoor Gym", "Grass Field", "Playground", "Beach"];

function App() {
  const { t, i18n } = useTranslation();

  const [language, setLanguage] = useState("nl");
  const [file, setFile] = useState(null);
  const [theme, setTheme] = useState("");
  const [material, setMaterial] = useState("");
  const [terrain, setTerrain] = useState("");
  const [groupCount, setGroupCount] = useState("");
  const [keywords, setKeywords] = useState([]); // Store keywords from Curator Agent
  const [selectedKeywords, setSelectedKeywords] = useState([]); // Store user-selected keywords
  const [isSearching, setIsSearching] = useState(false);

  const onDrop = (acceptedFiles) => setFile(acceptedFiles[0]);

  const { getRootProps, getInputProps } = useDropzone({
    onDrop,
    accept: ".txt, .pdf, .doc, .docx",
  });

  const handleLanguageChange = (event) => {
    const selectedLanguage = event.target.value;
    i18n.changeLanguage(selectedLanguage);
    setLanguage(selectedLanguage);
  };

const handleSearchTheme = async () => {
  if (!theme) return alert(t("messages.enter_theme"));
  setIsSearching(true);

  try {
    const response = await fetch("http://localhost:8000/suggest_keywords", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ theme }),
    });
    const data = await response.json();

    if (response.ok && Array.isArray(data.keywords)) {
      setKeywords(data.keywords); // Populate keywords from backend
    } else {
      console.error("Unexpected keywords format:", data);
      alert(t("messages.no_keywords_found"));
    }
  } catch (error) {
    console.error("Error fetching keywords:", error);
    alert(t("messages.error_fetching_theme"));
  } finally {
    setIsSearching(false);
  }
};

  const handleKeywordSelection = (keyword) => {
    setSelectedKeywords((prev) =>
      prev.includes(keyword)
        ? prev.filter((kw) => kw !== keyword) // Deselect keyword
        : [...prev, keyword] // Select keyword
    );
  };

  const handleStart = () => {
    if (!file || !theme || !groupCount || !terrain || !material) {
      alert(t("messages.all_fields_required"));
      return;
    }
    alert(
      `${t("messages.processing_inputs")}\n${t("labels.theme")}: ${theme}\n${t(
        "labels.selected_keywords"
      )}: ${selectedKeywords.join(", ")}`
    );
  };

  return (
    <ThemeProvider theme={appTheme}>
      <Container maxWidth="md">
        <Box
          sx={{
            mt: 4,
            p: 4,
            bgcolor: "background.paper",
            boxShadow: "0px 8px 20px rgba(0, 0, 0, 0.2)",
            borderRadius: 4,
          }}
        >
          <Grid container justifyContent="flex-end">
            <TextField
              select
              value={language}
              onChange={handleLanguageChange}
              label={t("labels.language")}
              variant="outlined"
              size="small"
            >
              <MenuItem value="nl">Nederlands</MenuItem>
              <MenuItem value="en">English</MenuItem>
              <MenuItem value="de">Deutsch</MenuItem>
              <MenuItem value="it">Italiano</MenuItem>
              <MenuItem value="es">Español</MenuItem>
            </TextField>
          </Grid>

          <Typography variant="h5" align="center" gutterBottom>
            {t("labels.upload_exercise")}
          </Typography>
          <Box
            {...getRootProps()}
            sx={{
              p: 3,
              border: "2px dashed #aaa",
              borderRadius: 2,
              textAlign: "center",
              cursor: "pointer",
              bgcolor: "#eaeaea",
              "&:hover": { bgcolor: "#f5f5f5" },
            }}
          >
            <input {...getInputProps()} />
            <Typography>
              {file ? file.name : t("placeholders.drag_drop_file")}
            </Typography>
          </Box>

          <Box mt={4}>
            <Typography variant="h6">{t("labels.theme")}</Typography>
            <Autocomplete
              options={staticThemes}
              freeSolo
              onInputChange={(e, value) => setTheme(value)}
              renderInput={(params) => (
                <TextField
                  {...params}
                  label={t("placeholders.select_theme")}
                  variant="outlined"
                  fullWidth
                />
              )}
            />
            <Button
              variant="contained"
              color="primary"
              onClick={handleSearchTheme}
              sx={{ mt: 2 }}
              disabled={isSearching}
            >
              {isSearching ? <CircularProgress size={24} /> : t("labels.search")}
            </Button>
          </Box>

          {keywords.length > 0 && (
            <Box mt={4}>
              <Typography variant="h6">{t("labels.generated_keywords")}</Typography>
              <Grid container spacing={2}>
                {keywords.map((keyword, index) => (
                  <Grid item xs={4} key={index}>
                    <FormControlLabel
                      control={
                        <Checkbox
                          checked={selectedKeywords.includes(keyword)}
                          onChange={() => handleKeywordSelection(keyword)}
                        />
                      }
                      label={keyword}
                    />
                  </Grid>
                ))}
              </Grid>
            </Box>
          )}

          <Grid container spacing={2} mt={2}>
            <Grid item xs={6}>
              <Typography variant="h6">{t("labels.groups")}</Typography>
              <TextField
                select
                value={groupCount}
                onChange={(e) => setGroupCount(e.target.value)}
                label={t("placeholders.select_groups")}
                fullWidth
              >
                {staticMaterials.map((group) => (
                  <MenuItem key={group} value={group}>
                    {group}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
            <Grid item xs={6}>
              <Typography variant="h6">{t("labels.terrain")}</Typography>
              <TextField
                select
                value={terrain}
                onChange={(e) => setTerrain(e.target.value)}
                label={t("placeholders.select_terrain")}
                fullWidth
              >
                {staticTerrains.map((terrain) => (
                  <MenuItem key={terrain} value={terrain}>
                    {terrain}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
          </Grid>

          <Box mt={2}>
            <Typography variant="h6">{t("labels.materials")}</Typography>
            <TextField
              select
              value={material}
              onChange={(e) => setMaterial(e.target.value)}
              label={t("placeholders.select_material")}
              fullWidth
            >
              {staticMaterials.map((mat) => (
                <MenuItem key={mat} value={mat}>
                  {mat}
                </MenuItem>
              ))}
            </TextField>
          </Box>

          <Box mt={4} textAlign="center">
            <Button
              variant="contained"
              color="primary"
              onClick={handleStart}
              sx={{ width: "60%" }}
            >
              {t("labels.start")}
            </Button>
          </Box>
        </Box>
      </Container>
    </ThemeProvider>
  );
}

export default App;
