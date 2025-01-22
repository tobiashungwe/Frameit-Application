import React from "react";
import { Box, Typography, Button, Grid, Container } from "@mui/material";
import { useNavigate } from "react-router-dom";
import frameItLogo from "../../assets/images/FrameIt-logo.png";
import howestLogo from "../../assets/images/howest-logo.png";

const Header = () => {
  const navigate = useNavigate();

  return (
    <Container maxWidth="lg">
      <Grid container alignItems="center" justifyContent="space-between">
        {/* App Title with FrameIt Logo */}
        <Box display="flex" alignItems="center" gap={1} onClick={() => navigate("/")}>
          <Box
            component="img"
            src={frameItLogo}
            alt="FrameIt Logo"
            sx={{
              width: "40px",
              height: "40px",
              objectFit: "contain",
              cursor: "pointer",
            }}
          />
          <Typography
            variant="h4"
            fontWeight="bold"
            color="text.primary"
            sx={{ cursor: "pointer" }}
          >
            Frame it
          </Typography>
        </Box>

        {/* Login Button and Howest Logo */}
        <Box display="flex" alignItems="center" gap={2}>
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
          <Box
            component="img"
            src={howestLogo}
            alt="Howest Logo"
            sx={{
              width: "50px",
              height: "50px",
              borderRadius: "50%",
              objectFit: "cover",
            }}
          />
        </Box>
      </Grid>
    </Container>
  );
};

export default Header;
