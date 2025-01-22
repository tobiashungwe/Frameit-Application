import React from "react";
import { Box, Button, Typography } from "@mui/material";

const HistoryPanel = ({ stories, onSelect }) => {
  return (
    <Box
      sx={{
        width: "20%",
        bgcolor: "#f5f5f5",
        p: 2,
        display: "flex",
        flexDirection: "column",
        gap: 2,
      }}
    >
      <Typography variant="h6" fontWeight="bold">
        History
      </Typography>
      {stories.map((story, index) => (
        <Button
          key={index}
          onClick={() => onSelect(story)}
          variant="outlined"
          fullWidth
          sx={{ justifyContent: "flex-start" }}
        >
          {story}
        </Button>
      ))}
    </Box>
  );
};

export default HistoryPanel;
