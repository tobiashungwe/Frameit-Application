import React from "react";
import { Box, Typography } from "@mui/material";
import { Link } from "react-router-dom";
import frameItLogo from "../../assets/images/FrameIt-logo.png";

const LogoHeader = () => {
  return (
    <Box
      component={Link}
      to="/" // Navigate to the landing page on click
      sx={{
        display: "flex",
        alignItems: "center",
        textDecoration: "none", // Remove underline for the link
        mb: 4, // Add spacing below the header
      }}
    >
      <Box
        component="img"
        src={frameItLogo}
        alt="FrameIt Logo"
        sx={{
          width: "40px", // Adjust size as needed
          height: "40px",
          mr: 1, // Add space between logo and text
        }}
      />
      <Typography variant="h5" fontWeight="bold" color="text.primary">
        Frame it
      </Typography>
    </Box>
  );
};

export default LogoHeader;
