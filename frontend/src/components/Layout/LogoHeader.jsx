import React from "react";
import { Box, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";
import frameItLogo from "../../assets/images/FrameIt-logo.png";

const LogoHeader = () => {
  const navigate = useNavigate();

  return (
    <Box
      sx={{
        display: "flex",
        alignItems: "center",
        cursor: "pointer",
        gap: 1, // Space between the logo and text
      }}
      onClick={() => navigate("/")}
    >
      <Box
        component="img"
        src={frameItLogo}
        alt="FrameIt Logo"
        sx={{
          width: "40px",
          height: "40px",
          objectFit: "cover",
          borderRadius: "8px", // Optional, for slightly rounded edges
        }}
      />
      <Typography variant="h5" fontWeight="bold" color="text.primary">
        Frame it
      </Typography>
    </Box>
  );
};

export default LogoHeader;
