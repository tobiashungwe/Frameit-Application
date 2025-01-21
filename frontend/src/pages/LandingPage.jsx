// src/pages/LandingPage.js
import React from "react";
import { Box, Typography, Button, Container, Grid } from "@mui/material";
import { useNavigate } from "react-router-dom";

const LandingPage = () => {
  const navigate = useNavigate();

  return (
    <Box sx={{ bgcolor: "#f8f9fa", minHeight: "100vh", pt: 4 }}>
      {/* Header Section */}
      <Container maxWidth="lg">
        <Grid container alignItems="center" justifyContent="space-between">
          <Typography variant="h4" fontWeight="bold" color="text.primary">
            Frame it
          </Typography>
          <Button
            variant="outlined"
            onClick={() => navigate("/login")}
            sx={{
              textTransform: "none",
              fontWeight: "bold",
              borderRadius: "20px",
              px: 3,
            }}
          >
            Login
          </Button>
        </Grid>
      </Container>

      {/* Main Content Section */}
      <Container maxWidth="lg" sx={{ mt: 10 }}>
        <Grid container spacing={6}>
          {/* Left Content */}
          <Grid item xs={12} md={6}>
            <Typography variant="h3" fontWeight="bold" color="text.primary" gutterBottom>
              An app that creates{" "}
              <Typography
                component="span"
                color="primary"
                fontWeight="bold"
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
              src="/path/to/logo-image.png" // Replace with your actual logo path
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

        {/* Statistics Section */}
        <Grid container spacing={4} sx={{ mt: 8 }}>
          <Grid item xs={4}>
            <Typography variant="h5" fontWeight="bold" color="text.primary">
              124K+
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Lorem ipsum consectetur
            </Typography>
          </Grid>
          <Grid item xs={4}>
            <Typography variant="h5" fontWeight="bold" color="text.primary">
              126
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Lorem ipsum consectetur
            </Typography>
          </Grid>
          <Grid item xs={4}>
            <Typography variant="h5" fontWeight="bold" color="text.primary">
              78K
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Lorem ipsum consectetur
            </Typography>
          </Grid>
        </Grid>
      </Container>

      {/* Footer Section */}
      <Box sx={{ mt: 10, py: 4, bgcolor: "#ffffff" }}>
        <Container maxWidth="lg">
          <Grid container spacing={3}>
            <Grid item xs={4}>
              <Typography variant="body2" color="text.secondary">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Faucibus in
                libero risus.
              </Typography>
            </Grid>
            <Grid item xs={4}>
              <Typography variant="body2" color="text.secondary">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Faucibus in
                libero risus.
              </Typography>
            </Grid>
            <Grid item xs={4}>
              <Typography variant="body2" color="text.secondary">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Faucibus in
                libero risus.
              </Typography>
            </Grid>
          </Grid>
        </Container>
      </Box>
    </Box>
  );
};

export default LandingPage;
