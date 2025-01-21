import React from "react";
import { Grid, Typography } from "@mui/material";

const Statistics = () => {
  return (
    <Grid container spacing={4} sx={{ mt: 8 }}>
      {[
        { value: "124K+", description: "Lorem ipsum consectetur" },
        { value: "126", description: "Lorem ipsum consectetur" },
        { value: "78K", description: "Lorem ipsum consectetur" },
      ].map((stat, index) => (
        <Grid item xs={4} key={index}>
          <Typography variant="h5" fontWeight="bold" color="text.primary">
            {stat.value}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            {stat.description}
          </Typography>
        </Grid>
      ))}
    </Grid>
  );
};

export default Statistics;
