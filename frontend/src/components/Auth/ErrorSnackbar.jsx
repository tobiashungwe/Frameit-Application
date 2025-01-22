import React from "react";
import { Snackbar } from "@mui/material";

const ErrorSnackbar = ({ error, onClose }) => {
  return (
    <Snackbar
      open={Boolean(error)}
      onClose={onClose}
      message={error}
      autoHideDuration={6000}
    />
  );
};

export default ErrorSnackbar;
