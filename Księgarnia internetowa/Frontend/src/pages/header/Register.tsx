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
import React from "react";
import {useEffect} from "react";
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
import UserService, { Credentials } from "../../services/UserService";
import { PersonalData } from "../../models/PersonalData";
import { RootState } from "../../redux/store";

interface FormFields {
  name: string;
  username: string;
  password: string;
  passwordRepeat: string;
  surname: string;
  email: string;
  tel: string;
}

const Register = () => {

  const useDetails = useSelector((state: RootState) => state.user)

  const [form, setForm] = React.useState<FormFields>({
    name: "",
    username: "",
    password: "",
    passwordRepeat: "",
    surname: "",
    email: "",
    tel: "",
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
    if (!FormValidator.checkIfIsRequired(form.name)) {
      newErrorsState.name = FormValidator.requiredMessage;
      success = false;
    } else if (!FormValidator.checkMinLength(form.name, 3)) {
      newErrorsState.name = FormValidator.minLengthMessage;
      success = false;
    } else if (!FormValidator.checkOnlyLetters(form.name)) {
      newErrorsState.name = FormValidator.onlyLettersMessage;
    }
    if (!FormValidator.checkIfIsRequired(form.username)) {
      newErrorsState.username = FormValidator.requiredMessage;
      success = false;
    } else if (!FormValidator.checkMinLength(form.username, 3)) {
      newErrorsState.username = FormValidator.minLengthMessage;
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
    if (!FormValidator.checkIfIsRequired(form.passwordRepeat)) {
      newErrorsState.passwordRepeat = FormValidator.requiredMessage;
      success = false;
    } else if (form.password !== form.passwordRepeat) {
      newErrorsState.passwordRepeat = "Hasła się nie zgadzają";
      success = false;
    }
    if (!FormValidator.checkIfIsRequired(form.surname)) {
      newErrorsState.surname = FormValidator.requiredMessage;
      success = false;
    } else if (!FormValidator.checkMinLength(form.surname, 3)) {
      newErrorsState.surname = FormValidator.minLengthMessage;
      success = false;
    } else if (!FormValidator.checkOnlyLetters(form.surname)) {
      newErrorsState.surname = FormValidator.onlyLettersMessage;
    }
    if (!FormValidator.checkIfIsRequired(form.email)) {
      newErrorsState.email = FormValidator.requiredMessage;
      success = false;
    } else if (!FormValidator.checkEmail(form.email)) {
      newErrorsState.email = FormValidator.emailMessage;
      success = false;
    }
    if (!FormValidator.checkIfIsRequired(form.tel)) {
      newErrorsState.tel = FormValidator.requiredMessage;
      success = false;
    } else if (!FormValidator.checkMinLength(form.tel, 3)) {
      newErrorsState.tel = FormValidator.minLengthMessage;
      success = false;
    }

    setErrors(newErrorsState);

    return success;
  };

  const handleSubmit = () => {
    if (!validateForm()) return;

    const credentials: Credentials = {
      username: form.username,
      password: form.password
    }

    const personalData: PersonalData = {
      name: form.name,
      surname: form.surname,
      email: form.email,
      tel: form.tel
    }

    UserService.register(credentials, personalData)
    .then((response) => {
      dispatch(setNotificationMessage("Zarejestrowano pomyślnie"));
      dispatch(setNotificationType("success"));
      dispatch(setNotificationStatus(true));
    })
    .catch((error) => {
      dispatch(setNotificationMessage(error.response.data));
      dispatch(setNotificationType("error"));
      dispatch(setNotificationStatus(true));
    })
  };

  return (
    <Grid item container justifyContent="center" alignItems="center">
      <Grid item xs={12}>
        <Typography variant="h4" textAlign="center">
          Rejestracja
        </Typography>
      </Grid>
      <Grid item xs={12} container marginTop={10} justifyContent="center">
        <Grid item xs={3} marginRight={20}>
          <ValidatedForm
            fieldName="Imię"
            placeholder="Wpisz imię..."
            value={form.name}
            error={errors.name}
            onChange={(value) => setForm({ ...form, name: value })}
            onErrorChange={(error) => setErrors({ ...errors, name: error })}
          />
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
          <ValidatedForm
            fieldName="Powtórz hasło"
            placeholder="Powtórz hasło..."
            type="password"
            value={form.passwordRepeat}
            error={errors.passwordRepeat}
            onChange={(value) => setForm({ ...form, passwordRepeat: value })}
            onErrorChange={(error) =>
              setErrors({ ...errors, passwordRepeat: error })
            }
          />
        </Grid>
        <Grid item xs={3}>
          <ValidatedForm
            fieldName="Nazwisko"
            placeholder="Wpisz nazwisko..."
            value={form.surname}
            error={errors.surname}
            onChange={(value) => setForm({ ...form, surname: value })}
            onErrorChange={(error) => setErrors({ ...errors, surname: error })}
          />
          <ValidatedForm
            fieldName="E-mail"
            placeholder="Wpisz e-mail..."
            value={form.email}
            error={errors.email}
            onChange={(value) => setForm({ ...form, email: value })}
            onErrorChange={(error) => setErrors({ ...errors, email: error })}
          />
          <ValidatedForm
            fieldName="Numer telefonu"
            placeholder="Wpisz nr telefonu..."
            value={form.tel}
            error={errors.tel}
            onChange={(value) => setForm({ ...form, tel: value })}
            onErrorChange={(error) => setErrors({ ...errors, tel: error })}
          />
        </Grid>
      </Grid>
      <Grid
        item
        xs={1.5}
        container
        marginTop={10}
        justifyContent="center"
      >
        <Button
          fullWidth
          variant="contained"
          color="secondary"
          onClick={handleSubmit}
        >
          Zarejestruj się
        </Button>
      </Grid>
      <Grid item container justifyContent="center" marginTop={3}>
        <Button
          fullWidth
          variant="text"
          color="secondary"
          sx={{ color: "#1C3CAD" }}
          onClick={() => navigate("/login")}
        >
          Masz już konto? Zaloguj się
        </Button>
      </Grid>
      <BottomNavigation text={"Wróć do strony głównej"} path="../" />
    </Grid>
  );
};

export default Register;
