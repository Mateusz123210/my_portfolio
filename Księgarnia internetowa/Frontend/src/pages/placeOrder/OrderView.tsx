import { Grid, Typography, Button } from "@mui/material";
import React from "react";
import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import ValidatedForm from "../../components/common/ValidatedForm";
import Book from "../../models/Book";
import { PersonalData } from "../../models/PersonalData";
import { BasketProduct, clear } from "../../redux/slices/basketSlice";
import { setNotificationMessage, setNotificationType, setNotificationStatus } from "../../redux/slices/notificationSlice";
import { RootState } from "../../redux/store";
import ClientService from "../../services/ClientService";
import FormValidator from "../../services/FormValidator";
import OrderService, { BasicBasketProduct, CreateOrder } from "../../services/OrderService";
import { BasketProductWithDetails } from "../basket/Basket";
import BasketProductView from "../basket/BasketProductView";

interface FormFields {
    name: string;
    surname: string;
    email: string;
    tel: string;
}

const OrderView = () => {

    const basketProducts = useSelector((state: RootState) => state.basket).products

    const [totalPrice, setTotalPrice] = useState<number>(0);
    const [personalData, setPersonalData] = useState<PersonalData | {}>({})

    const initialState: FormFields = {
        name: "",
        surname: "",
        email: "",
        tel: ""
    }

    const [form, setForm] = React.useState<FormFields>(initialState);
    
    const [errors, setErrors] = React.useState<FormFields>(form);

    const dispatch = useDispatch()

    const navigate = useNavigate()

    useEffect(() => {
        ClientService.getClientPersonalData(1)
        .then((response) => {
            setPersonalData(response.data)
        })
    }, [])

    useEffect(() => {

        let newTotalPrice = 0

        basketProducts.forEach((basketProduct: BasketProduct) => {
            newTotalPrice += basketProduct.price * basketProduct.quantity
        })

        setTotalPrice(+newTotalPrice.toFixed(2))
    }, [basketProducts])

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

        let createOrder: any = {
            clientId: 1,
            basketItems: basketProducts.map((p: BasketProduct) => ({bookId: p.id, quantity: p.quantity}))
        }

        if(JSON.stringify(form) !== JSON.stringify(personalData)){
            createOrder.receiverData = form
        }

        OrderService.placeOrder(createOrder)
        .then((response) => {
            dispatch(setNotificationMessage(`Złożono zamówienie nr ${response.data}`));
            dispatch(setNotificationType("success"));
            dispatch(setNotificationStatus(true));
            dispatch(clear())

            navigate('../')
        })
        .catch((error) => {
            dispatch(setNotificationMessage(error.response.data));
            dispatch(setNotificationType("error"));
            dispatch(setNotificationStatus(true));
        })
      };

    return (
        <Grid item xs={8} alignSelf="stretch" container justifyContent="space-between" alignItems="center">
            <Grid item xs={4} container direction="row" justifyContent="center" alignItems="center">
                <ValidatedForm
                    fieldName="Imię"
                    placeholder="Wpisz imię..."
                    value={form.name}
                    error={errors.name}
                    onChange={(value) => setForm({ ...form, name: value })}
                    onErrorChange={(error) => setErrors({ ...errors, name: error })}
                />
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
                <Grid item xs={6} container marginTop={6} justifyContent="center">
                    <Button
                        fullWidth
                        variant="contained"
                        color="secondary"
                        sx={{marginBottom: 4}}
                        onClick={() => {
                            setForm({...form, ...personalData})
                            setErrors(initialState)
                        }}
                    >
                        Użyj swoich danych
                    </Button>
                    <Button
                        fullWidth
                        variant="contained"
                        color="secondary"
                        onClick={() => {
                            setForm(initialState)
                            setErrors(initialState)
                        }}
                    >
                        Wyczyść formularz
                    </Button>
                </Grid>
            </Grid>
            <Grid item xs={5} container direction="column" marginBottom={14} rowSpacing={4}>
                <Grid item container justifyContent="center">
                    <Typography variant="h4" textAlign="end">
                        Łączna kwota: {totalPrice} zł
                    </Typography>
                </Grid>
                <Grid item container justifyContent="center">
                    <Button
                        variant="contained"
                        color="secondary"
                        onClick={handleSubmit}
                    >
                        Złóż zamówienie
                    </Button>
                </Grid>
            </Grid>
        </Grid>
    )
}

export default OrderView;