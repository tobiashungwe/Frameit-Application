// SanitizedContentViewer.jsx
import React from "react";
import { Box, Typography } from "@mui/material";

const SanitizedContentViewer = ({ sanitizedContent, t, children }) => {
  return (
    <Box mt={4} p={2} bgcolor="background.paper" borderRadius={4}>
      {/* Note the component="div" here so it won't produce a <p> tag */}
      <Typography variant="h6" component="div">
        {t("labels.sanitized_content")}
      </Typography>
      {React.cloneElement(children, { sanitizedContent: sanitizedContent.data })}
    </Box>
  );
};

export default SanitizedContentViewer;
