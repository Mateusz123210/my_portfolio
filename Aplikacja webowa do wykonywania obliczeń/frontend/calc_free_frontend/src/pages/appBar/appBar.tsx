import React from "react";
import { Grid, Typography } from "@mui/material";
import "./appBar.css";
import Logo from "../../assets/Logo.png";
import { useNavigate } from "react-router-dom";

const AppBar = () => {
  const navigate = useNavigate();

  return (
    <Grid container component="nav" display="flex" alignItems="center">
      <Grid item xs={4.5} justifySelf="start">
        <img
          id="logo"
          src={Logo}
          width={70}
          alt="Logo"
          onClick={() => navigate("/")}
        />
      </Grid>
      <Grid
        item
        xs={3}
        paddingTop={1.4}
        justifySelf="center"
        alignSelf="center"
        justifyContent="center"
      >
        <Typography
          id="pageName"
          variant="h2"
          color="#4C87BA"
          textAlign="center"
          onClick={() => navigate("/")}
        >
          CalcFree
        </Typography>
      </Grid>
    </Grid>
  );
};

export default AppBar;
