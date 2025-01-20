// SanitizedContentViewer.jsx
import React from "react";
import { Box, Typography } from "@mui/material";

const SanitizedContentViewer = ({ sanitizedContent, t, children }) => {
    return (
        <Box mt={4} p={2} bgcolor="background.paper" borderRadius={4}>
            <Typography variant="h6" component="div" gutterBottom>
                {t("labels.cleaned_document_preview", "Cleaned Document Preview")}
            </Typography>

            {/* Pass sanitizedContent down to children (the DocumentViewer) */}
            {React.cloneElement(children, { sanitizedContent: sanitizedContent.data })}
        </Box>
    );
};

export default SanitizedContentViewer;
