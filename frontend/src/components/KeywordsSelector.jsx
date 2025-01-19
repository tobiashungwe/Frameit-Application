import React from "react";
import { Box, Typography, Grid2, Checkbox, FormControlLabel } from "@mui/material";

const KeywordsSelector = ({ keywords = [], selectedKeywords, onKeywordSelection, t }) => {
  return (
      <Box mt={4}>
          <Typography variant="h6">{t("labels.generated_keywords")}</Typography>
          <Grid2 container spacing={2}>
              {keywords.map((keyword, index) => (
                  <Grid2 item xs={4} key={index}>
                      <FormControlLabel
                          control={
                              <Checkbox
                                  checked={selectedKeywords.includes(keyword)}
                                  onChange={() => onKeywordSelection(keyword)}
                              />
                          }
                          label={keyword}
                      />
                  </Grid2>
              ))}
          </Grid2>
      </Box>
  );
};


export default KeywordsSelector;
