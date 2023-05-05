import {
  Button,
  FormControl,
  FormControlLabel,
  FormHelperText,
  FormLabel,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useEffect } from "react";
import BottomNavigation from "../../components/common/BottomNavigation";
import ValidatedForm from "../../components/common/ValidatedForm";
import {
  setNotificationMessage,
  setNotificationType,
  setNotificationStatus,
} from "../../redux/slices/notificationSlice";
import FormValidator from "../../services/FormValidator";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import UserService from "../../services/UserService";
import axios from "axios";
import { login } from "../../redux/slices/userSlice";
import { RootState } from "../../redux/store";

interface FormFields {
  username: string;
  password: string;
}

interface LoggedUserDetails {
  accessToken: string,
  userId: number,
  clientId?: number
}

const Login = () => {

  const useDetails = useSelector((state: RootState) => state.user)

  const [form, setForm] = React.useState<FormFields>({
    username: "",
    password: "",
  });

  const [errors, setErrors] = React.useState<FormFields>(form);

  const navigate = useNavigate();

  const dispatch = useDispatch();

  useEffect(() => {
    if(useDetails.isLogged){
      navigate('../')
    }
  }, [useDetails.isLogged])

  const validateForm = () => {
    let success = true;

    let newErrorsState = { ...errors };

    if (!FormValidator.checkIfIsRequired(form.username)) {
      newErrorsState.username = FormValidator.requiredMessage;
      success = false;
    }

    if (!FormValidator.checkIfIsRequired(form.password)) {
      newErrorsState.password = FormValidator.requiredMessage;
      success = false;
    } else if (!FormValidator.checkMinLength(form.password, 8)) {
      newErrorsState.password = FormValidator.minLengthMessage;
      success = false;
    } else if (!FormValidator.checkContainsSmallLetter(form.password)) {
      newErrorsState.password = FormValidator.smallLetterMessage;
      success = false;
    } else if (!FormValidator.checkContainsUpperLetter(form.password)) {
      newErrorsState.password = FormValidator.upperLetterMessage;
      success = false;
    } else if (!FormValidator.checkContainsDigit(form.password)) {
      newErrorsState.password = FormValidator.digitMessage;
      success = false;
    }

    setErrors(newErrorsState);

    return success;
  };

  const handleSubmit = () => {
    //if (!validateForm()) return;

    UserService.login(form)
    .then((response) => {
      const loggedUserDetails: LoggedUserDetails = response.data
      axios.defaults.headers.common['Authorization'] = `Bearer ${loggedUserDetails.accessToken}`
      dispatch(login({
        userId: loggedUserDetails.userId, clientId: loggedUserDetails.clientId
      }))
      dispatch(setNotificationMessage("Zalogowano pomyślnie"));
      dispatch(setNotificationType("success"));
      dispatch(setNotificationStatus(true));
      navigate('/')
    })
    .catch((error) => {
      dispatch(setNotificationMessage("Login lub hasło są niepoprawne"));
      dispatch(setNotificationType("error"));
      dispatch(setNotificationStatus(true));
    })
  };

  return (
    <Grid item container justifyContent="center" alignItems="center">
      <Grid item xs={12}>
        <Typography variant="h4" textAlign="center">
          Logowanie
        </Typography>
      </Grid>
      <Grid item xs={3} container marginTop={10}>
        <ValidatedForm
          fieldName="Nazwa użytkownika"
          placeholder="Wpisz nazwę użytkownika..."
          value={form.username}
          error={errors.username}
          onChange={(value) => setForm({ ...form, username: value })}
          onErrorChange={(error) => setErrors({ ...errors, username: error })}
        />
        <ValidatedForm
          fieldName="Hasło"
          placeholder="Wpisz hasło..."
          type="password"
          value={form.password}
          error={errors.password}
          onChange={(value) => setForm({ ...form, password: value })}
          onErrorChange={(error) => setErrors({ ...errors, password: error })}
        />
        <Grid item>
          <Button variant="text" color="secondary" sx={{ color: "#1C3CAD" }}>
            Zapomniałem hasła
          </Button>
        </Grid>
        <Grid item xs={6} container marginTop={10} justifyContent="center">
          <Button
            fullWidth
            variant="contained"
            color="secondary"
            onClick={handleSubmit}
          >
            Zaloguj się
          </Button>
        </Grid>
        <Grid item container justifyContent="center" marginTop={3}>
          <Button
            fullWidth
            variant="text"
            color="secondary"
            sx={{ color: "#1C3CAD" }}
            onClick={() => navigate("/register")}
          >
            Nie masz jeszcze konta? Zarejestruj się
          </Button>
        </Grid>
      </Grid>
      <BottomNavigation text={"Wróć do strony głównej"} path="../" />
    </Grid>
  );
};

export default Login;
