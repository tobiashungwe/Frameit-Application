import React from "react";
import { Box, Typography, Grid, Checkbox, FormControlLabel } from "@mui/material";

const KeywordsSelector = ({ keywords = [], selectedKeywords, onKeywordSelection, t }) => {
  return (
      <Box mt={4}>
          <Typography variant="h6">{t("labels.generated_keywords")}</Typography>
          <Grid container spacing={2}>
              {keywords.map((keyword, index) => (
                  <Grid item xs={4} key={index}>
                      <FormControlLabel
                          control={
                              <Checkbox
                                  checked={selectedKeywords.includes(keyword)}
                                  onChange={() => onKeywordSelection(keyword)}
                              />
                          }
                          label={keyword}
                      />
                  </Grid>
              ))}
          </Grid>
      </Box>
  );
};


export default KeywordsSelector;
