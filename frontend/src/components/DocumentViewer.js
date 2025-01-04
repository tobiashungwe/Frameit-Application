import React from "react";
import { Box, Typography } from "@mui/material";


const DocumentViewer = ({ sanitizedContent }) => {
  const lines = sanitizedContent.split("\n");

  return (
    <Box mt={4} p={2} bgcolor="background.paper" borderRadius={4}>
      <Typography variant="h6" component="h6">Generated Story</Typography>
      <Box component="div" style={{ whiteSpace: "pre-wrap" }}>
        {lines.map((line, index) => (
          <Typography key={index} variant="body1">
            {line}
          </Typography>
        ))}
      </Box>
    </Box>
  );
};

export default DocumentViewer;