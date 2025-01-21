import React from "react";
import { Box, Typography, Button, Grid } from "@mui/material";
import { useNavigate } from "react-router-dom";
import frameItLogo from "../../assets/images/FrameIt-logo.jpg";

const MainContent = () => {
  const navigate = useNavigate();

  return (
    <Grid container spacing={6} sx={{ mt: 10 }}>
      {/* Left Content */}
      <Grid item xs={12} md={6}>
        <Typography variant="h3" fontWeight="bold" color="text.primary" gutterBottom>
          An app that creates{" "}
          <Typography
            component="span"
            color="primary"
            fontWeight="bold"
            variant="h3"
            sx={{ display: "inline" }}
          >
            wonderful activities
          </Typography>
        </Typography>
        <Typography variant="body1" color="text.secondary" sx={{ mt: 2, mb: 4 }}>
          A tool that adds fun, customizable narrative layers to sports lessons and
          group activities, boosting engagement and creativity.
        </Typography>
        <Button
          variant="contained"
          size="large"
          color="primary"
          onClick={() => navigate("/home")}
          sx={{
            textTransform: "none",
            fontWeight: "bold",
            borderRadius: "20px",
            px: 5,
          }}
        >
          Start now
        </Button>
      </Grid>

      {/* Right Content */}
      <Grid item xs={12} md={6}>
        <Box
          component="img"
          src={frameItLogo}
          alt="FrameIt Logo"
          sx={{
            width: "100%",
            maxWidth: "350px",
            mx: "auto",
            display: "block",
            borderRadius: "20px",
          }}
        />
      </Grid>
    </Grid>
  );
};

export default MainContent;
