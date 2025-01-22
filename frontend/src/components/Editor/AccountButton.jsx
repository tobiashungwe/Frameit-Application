import React from "react";
import { Box, Button } from "@mui/material";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";

const AccountButton = ({ onClick }) => {
  return (
    <Box sx={{ mt: "auto", p: 2 }}>
      <Button
        startIcon={<AccountCircleIcon />}
        onClick={onClick}
        variant="outlined"
        fullWidth
      >
        View account
      </Button>
    </Box>
  );
};

export default AccountButton;
