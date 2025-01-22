import React from "react";
import { Snackbar } from "@mui/material";

const SuccessSnackbar = ({ success, onClose }) => {
  return (
    <Snackbar
      open={Boolean(success)}
      onClose={onClose}
      message={success}
      autoHideDuration={6000}
    />
  );
};

export default SuccessSnackbar;
