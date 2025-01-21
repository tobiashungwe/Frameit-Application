import React from "react";
import { Container, Box, Typography } from "@mui/material";

/**
 * AuthLayout: A simple layout for auth pages 
 * with consistent styles & structure.
 */
const AuthLayout = ({ title, children }) => {
  return (
    <Container maxWidth="sm">
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          minHeight: "100vh",
          justifyContent: "center",
        }}
      >
        <Typography variant="h4" gutterBottom>
          {title}
        </Typography>
        <Box
          sx={{
            width: "100%",
            mt: 2,
            p: 3,
            boxShadow: 3,
            borderRadius: 2,
            bgcolor: "background.paper",
          }}
        >
          {children}
        </Box>
      </Box>
    </Container>
  );
};

export default AuthLayout;