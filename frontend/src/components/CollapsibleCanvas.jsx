// CollapsibleCanvas.jsx
import React, { useState } from "react";
import { Box, Button } from "@mui/material";
import { ExpandLess, ExpandMore } from "@mui/icons-material";

const CollapsibleCanvas = ({ children, minHeight = 300, maxHeight = 600 }) => {
    const [expanded, setExpanded] = useState(false);

    const toggleExpand = () => {
        setExpanded((prev) => !prev);
    };

    return (
        <Box
            sx={{
                position: "relative",
                height: expanded ? maxHeight : minHeight,
                overflow: "auto",
                border: "1px solid #ccc",
                borderRadius: 2,
                transition: "height 0.3s ease-in-out",
                mb: 2,
            }}
        >
            {/* The toggle button in top-right corner */}
            <Button
                variant="text"
                size="small"
                startIcon={expanded ? <ExpandLess /> : <ExpandMore />}
                onClick={toggleExpand}
                sx={{ position: "absolute", top: 8, right: 8, zIndex: 2 }}
            >
                {expanded ? "Minimize" : "Maximize"}
            </Button>

            {/* Canvas Content */}
            <Box sx={{ px: 2, pt: 2, pb: 4 }}>{children}</Box>
        </Box>
    );
};

export default CollapsibleCanvas;
