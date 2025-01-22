import React from "react";
import { Box, Container } from "@mui/material";
import Header from "../components/LandingPage/Header";
import MainContent from "../components/LandingPage/MainContent";
import Statistics from "../components/LandingPage/Statistics";
import Footer from "../components/LandingPage/Footer";

const LandingPage = () => {
  return (
    <Box sx={{ bgcolor: "#f8f9fa", minHeight: "100vh" }}>
      {/* Wrapping content in a centered container */}
      <Container maxWidth="lg" sx={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
        <Header />
        <MainContent />
        {/*<Statistics />*/}
      </Container>
      {/*<Footer />*/}
    </Box>
  );
};

export default LandingPage;
