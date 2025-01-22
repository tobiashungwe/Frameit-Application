import React from "react";
import { Button, Box } from "@mui/material";

const SaveButton = ({ onSave }) => {
  return (
    <Box sx={{ mt: 2, textAlign: "right" }}>
      <Button
        onClick={onSave}
        variant="contained"
        color="primary"
        sx={{ borderRadius: 2 }}
      >
        Save changes
      </Button>
    </Box>
  );
};

export default SaveButton;
