import React from "react";
import { TextField, MenuItem, Grid2 } from "@mui/material";
import { useTranslation } from "react-i18next";

const LanguageSelector = ({ language, onChange }) => {
  const { t } = useTranslation();

  return (
    <Grid2 container justifyContent="flex-end">
      <TextField
        select
        value={language}
        onChange={onChange}
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
    </Grid2>
  );
};

export default LanguageSelector;
