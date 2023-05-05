import React from "react";
import { Grid, Typography } from "@mui/material";

const NotFoundPage = () => {
  return (
    <Grid
      container
      height={1200}
      textAlign="center"
      justifyContent="center"
      alignItems="center
    "
    >
      <Typography fontSize={40} color="#E61E1E" textAlign="center">
        Nie znaleziono zasobu! Przejdź do strony głównej.
      </Typography>
    </Grid>
  );
};

export default NotFoundPage;
