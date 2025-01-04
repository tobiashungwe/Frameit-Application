import React from "react";
import { Container, Box } from "@mui/material";

const MainLayout = ({ children }) => {
  return (
    <Container maxWidth="md">
      <Box
        sx={{
          mt: 4,
          p: 4,
          bgcolor: "background.paper",
          boxShadow: "0px 8px 20px rgba(0, 0, 0, 0.2)",
          borderRadius: 4,
        }}
      >
        {children}
      </Box>
    </Container>
  );
};

export default MainLayout;
