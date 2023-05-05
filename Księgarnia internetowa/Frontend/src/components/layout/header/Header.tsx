import { Toolbar, Box, Typography, Grid, AppBar, Button } from "@mui/material";
import { Link } from "react-router-dom";
import logo from "../../../assets/logo.png";
import basket from "../../../assets/basket.png";
import "./Header.css";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { RootState } from "../../../redux/store";
import { logout } from "../../../redux/slices/userSlice";
import { setNotificationMessage, setNotificationType, setNotificationStatus } from "../../../redux/slices/notificationSlice";

const Header = () => {

  const userDetails = useSelector((state: RootState) => state.user)
  const dispatch = useDispatch()

  const navigate = useNavigate();

  return (
    <Grid container component="nav" alignItems="center">
      <Grid item xs={5} justifySelf="start">
        <Link to="/" className="nice-link">
          <img src={logo} width="100" alt="logo" />
        </Link>
      </Grid>
      <Grid
        item
        xs={2}
        justifySelf="center"
        container
        justifyContent="center"
        alignSelf="center"
      >
        <Typography component="h4" id="name" textAlign="center">
          Bookshop
        </Typography>
      </Grid>
      <Grid
        item
        xs={5}
        justifySelf="end"
        container
        alignItems="center"
        justifyContent="end"
        columnSpacing={3}
      >
        {userDetails.isLogged ? (
          <React.Fragment>
            {userDetails.clientId ?
              <Grid item>
                <Button variant="contained" color="secondary"
                  onClick={() => navigate('/my-orders')}
                >
                  Moje zamówienia
                </Button>
              </Grid>
              :
              <Grid item>
                <Button
                  variant="contained"
                  color="secondary"
                  onClick={() => navigate("/all-orders")}
                >
                  Zarządzaj zamówieniami
                </Button>
              </Grid>
            }
            <Grid item>
              <Button
                variant="contained"
                color="secondary"
                onClick={() => {
                  dispatch(logout())
                  dispatch(setNotificationMessage("Wylogowano pomyślnie"));
                  dispatch(setNotificationType("success"));
                  dispatch(setNotificationStatus(true));
                  navigate('/')
                }}
              >
                Wyloguj się
              </Button>
            </Grid>
          </React.Fragment>
        ) : (
          <React.Fragment>    
            <Grid item>
              <Button
                variant="contained"
                color="secondary"
                onClick={() => navigate("/register")}
              >
                Zarejestruj się
              </Button>
            </Grid>
            <Grid item>
              <Button
                variant="contained"
                color="secondary"
                onClick={() => navigate("/login")}
              >
                Zaloguj się
              </Button>
            </Grid>
          </React.Fragment>
        )}
        {!(userDetails.isLogged && !userDetails.clientId) &&
          <Grid item>
            <Link to="/basket" className="nice-link">
              <img src={basket} width="60" alt="koszyk"/>
            </Link>
          </Grid>
        }
      </Grid>
    </Grid>
  );
};

export default Header;
