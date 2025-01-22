import React from "react";
import { Box } from "@mui/material";
import Header from "../LandingPage/Header";

const AuthLayout = ({ title, children }) => {
  return (
    <Box>
      {/* Add Header */}
      <Header />
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          minHeight: "calc(100vh - 80px)", // Adjust to exclude header height
          p: 4,
        }}
      >
        <Box
          sx={{
            width: "100%",
            maxWidth: "400px",
            boxShadow: 3,
            borderRadius: 2,
            bgcolor: "background.paper",
            p: 3,
          }}
        >
          <h1 style={{ textAlign: "center" }}>{title}</h1>
          {children}
        </Box>
      </Box>
    </Box>
  );
};

export default AuthLayout;
