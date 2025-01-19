import React from "react";
import { Box, Typography } from "@mui/material";
import { useTranslation } from "react-i18next";

const DocumentViewer = ({ sanitizedContent = "" }) => {
    const { t } = useTranslation(); // Hook for translations

    // Split sanitized content into lines or provide an empty array if content is empty
    const lines = sanitizedContent ? sanitizedContent.split("\n") : [];

    return (
        <Box mt={4} p={2} bgcolor="background.paper" borderRadius={4}>
            <Typography variant="h6" component="h6">
                {t("labels.generated_story", "Generated Story")}
            </Typography>
            <Box component="div" style={{ whiteSpace: "pre-wrap" }}>
                {lines.length > 0 ? (
                    lines.map((line, index) => (
                        <Typography key={index} variant="body1">
                            {line}
                        </Typography>
                    ))
                ) : (
                    <Typography variant="overline" color="textSecondary">
                        {t("messages.no_content_message", "No content available. Please upload a document.")}
                    </Typography>
                )}
            </Box>
        </Box>
    );
};

export default DocumentViewer;
