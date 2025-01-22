import React from "react";
import { Box, Typography, TextField, IconButton } from "@mui/material";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";

const StoryEditor = ({ story, onEdit, onDelete }) => {
  return (
    <Box
      sx={{
        flexGrow: 1,
        p: 2,
        display: "flex",
        flexDirection: "column",
        gap: 2,
        border: "1px solid #ccc",
        borderRadius: 2,
      }}
    >
      <Typography variant="h6" fontWeight="bold">
        Gegenereerde verhaal
      </Typography>
      <TextField
        fullWidth
        multiline
        minRows={8}
        value={story}
        onChange={onEdit}
        variant="outlined"
        sx={{ bgcolor: "#f5f5f5" }}
      />
      <Box sx={{ display: "flex", justifyContent: "flex-end", gap: 1 }}>
        <IconButton onClick={onDelete}>
          <DeleteIcon />
        </IconButton>
        <IconButton>
          <EditIcon />
        </IconButton>
      </Box>
    </Box>
  );
};

export default StoryEditor;
