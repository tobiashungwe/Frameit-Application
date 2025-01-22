import React from "react";
import { Box, Container } from "@mui/material";
import Header from "../components/LandingPage/Header";
import MainContent from "../components/LandingPage/MainContent"
/*
; to add useful information in main
import Statistics from "../components/LandingPage/Statistics"; to add useful information in statistics
import Footer from "../components/LandingPage/Footer"; to add useful information in footer
*/
/*
<Footer />
<Statistics />
*/
const LandingPage = () => {
  return (
    <Box sx={{ bgcolor: "#f8f9fa", minHeight: "100vh" }}>
      {/* Wrapping content in a centered container */}
      <Container maxWidth="lg" sx={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
        <Header />
        <MainContent />
      </Container>
    </Box>
  );
};

export default LandingPage;
