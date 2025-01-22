import React from "react";
import { Box, Typography, Container, Grid } from "@mui/material";

const Footer = () => {
  return (
    <Box sx={{ mt: 10, py: 4, bgcolor: "#ffffff" }}>
      <Container maxWidth="lg">
        <Grid container spacing={3}>
          {[...Array(3)].map((_, index) => (
            <Grid item xs={4} key={index}>
              <Typography variant="body2" color="text.secondary">
              </Typography>
            </Grid>
          ))}
        </Grid>
      </Container>
    </Box>
  );
};

export default Footer;
