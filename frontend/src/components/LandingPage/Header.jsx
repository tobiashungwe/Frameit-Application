import React from "react";
import { Box, Typography, Button, Grid, Container } from "@mui/material";
import { useNavigate } from "react-router-dom";
import howestLogo from "../../assets/images/howest-logo.png";

const Header = () => {
  const navigate = useNavigate();

  return (
    <Container maxWidth="lg">
      <Grid container alignItems="center" justifyContent="space-between">
        {/* App Title */}
        <Typography variant="h4" fontWeight="bold" color="text.primary">
          Frame it
        </Typography>

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
