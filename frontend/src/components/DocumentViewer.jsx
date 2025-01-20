// DocumentViewer.jsx
import React from "react";
import { Box, Typography } from "@mui/material";
import { useTranslation } from "react-i18next";
import CollapsibleCanvas from "./CollapsibleCanvas";

const DocumentViewer = ({ sanitizedContent = "" }) => {
    const { t } = useTranslation();

    // Split sanitized content into lines
    const lines = sanitizedContent ? sanitizedContent.split("\n") : [];

    return (
        <Box mt={4}>
            <Typography variant="h6" component="h2" gutterBottom>

                {t("labels.document_content", "Document Content")}
            </Typography>


            <CollapsibleCanvas minHeight={300} maxHeight={600}>
                {lines.length > 0 ? (
                    lines.map((line, index) => (
                        <Typography key={index} variant="body1" paragraph>
                            {line}
                        </Typography>
                    ))
                ) : (
                    <Typography variant="overline" color="textSecondary">
                        {t("messages.no_content_message", "No content available. Please upload a document.")}
                    </Typography>
                )}
            </CollapsibleCanvas>
        </Box>
    );
};

export default DocumentViewer;
