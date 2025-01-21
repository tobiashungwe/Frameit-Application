import React from "react";
import { TextField, MenuItem } from "@mui/material";
import Grid from '@mui/material/Grid2';
import { useTranslation } from "react-i18next";

const LanguageSelector = ({ language, onChange }) => {
    const { t } = useTranslation();

    return (
        <Grid container justifyContent="flex-end" disableEqualOverflow>
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
        </Grid>
    );
};

export default LanguageSelector;
