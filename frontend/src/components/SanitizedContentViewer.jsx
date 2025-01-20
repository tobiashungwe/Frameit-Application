// SanitizedContentViewer.jsx
import React from "react";
import { Box, Typography } from "@mui/material";

const SanitizedContentViewer = ({ sanitizedContent, t, children }) => {
    return (
        <Box mt={4} bgcolor="background.paper" borderRadius={4}>


            {/* Pass sanitizedContent down to children (the DocumentViewer) */}
            {React.cloneElement(children, { sanitizedContent: sanitizedContent.data })}
        </Box>
    );
};

export default SanitizedContentViewer;
