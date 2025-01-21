import React from "react";
import { Box, TextField, Button } from "@mui/material";

const AuthForm = ({ fields, buttonLabel, onSubmit }) => {
  return (
    <Box component="form" onSubmit={onSubmit}>
      {fields.map((field, index) => (
        <TextField
          key={index}
          label={field.label}
          variant="outlined"
          type={field.type || "text"}
          fullWidth
          margin="normal"
          value={field.value}
          onChange={field.onChange}
        />
      ))}

      <Button
        type="submit"
        variant="contained"
        color="primary"
        sx={{ mt: 2 }}
        fullWidth
      >
        {buttonLabel}
      </Button>
    </Box>
  );
};

export default AuthForm;
