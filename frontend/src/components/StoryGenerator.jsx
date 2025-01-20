import React from "react";
import { Box, Button, CircularProgress, Typography } from "@mui/material";
import { useTranslation } from "react-i18next";

const StoryGenerator = ({ onGenerate, isGenerating, story }) => {
  const { t } = useTranslation();

  return (
    <>
      <Box mt={4}>
        <Button
          variant="contained"
          color="primary"
          onClick={onGenerate}
          disabled={isGenerating}
          fullWidth
        >
          {isGenerating ? <CircularProgress size={24} /> : t("labels.document_content")}
        </Button>
      </Box>

      {story && (
        <Box mt={4} p={2} bgcolor="background.paper" borderRadius={4}>
          <Typography variant="h6" component="h6">{t("labels.document_content")}</Typography>
          <Typography component="div">{story}</Typography>
        </Box>
      )}
    </>
  );
};

export default StoryGenerator;
