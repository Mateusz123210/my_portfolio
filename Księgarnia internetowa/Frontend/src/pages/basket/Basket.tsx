import { Button, Grid, Typography } from "@mui/material";
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import Book from "../../models/Book";
import { BasketProduct, clear } from "../../redux/slices/basketSlice";
import { RootState } from "../../redux/store";
import BookService from "../../services/BookService";
import { books } from "../shop/Shop";
import BasketProductView from "./BasketProductView";
import OrderService from "../../services/OrderService";
import { CreateOrder } from "../../services/OrderService";
import { setNotificationMessage, setNotificationType, setNotificationStatus } from "../../redux/slices/notificationSlice";

export interface BasketProductWithDetails {
    product: Book,
    quantity: number
}

const Basket = () => {

    const userDetails = useSelector((state: RootState) => state.user)

    const basketProducts = useSelector((state: RootState) => state.basket).products
    const totalPrice = useSelector((state: RootState) => state.basket).totalPrice as number

    const [basketProductsWithDetails, setBasketProductsWithDetails] = useState<BasketProductWithDetails[]>([])

    const dispatch = useDispatch()

    const navigate = useNavigate()

    useEffect(() => {

        let newBasketProductsWithDetails: BasketProductWithDetails[] = []

        const basketBooksIds = basketProducts.map(item => item.id)

        BookService.getBooksByIds(basketBooksIds)
        .then((response) => {
            const foundBooks = response.data

            basketProducts.forEach((basketProduct: BasketProduct) => {
                const book = foundBooks.filter((book: Book) => book.id == basketProduct.id)[0]
                newBasketProductsWithDetails.push({
                    product: book,
                    quantity: basketProduct.quantity
                });
            })

            setBasketProductsWithDetails(newBasketProductsWithDetails)
        })
        .catch((error) => {
            console.log(error)
        })
    }, [])

    const handleUpdateQuantity = (id: number, quantity: number) => {
        let newBasketProductsWithDetails = [...basketProductsWithDetails]
        const index = basketProductsWithDetails.map(p => p.product.id).indexOf(id)
        newBasketProductsWithDetails[index].quantity = quantity
        setBasketProductsWithDetails(newBasketProductsWithDetails)
    }

    const handleRemove = (id: number) => {
        const index = basketProductsWithDetails.map(p => p.product.id).indexOf(id)
        let newBasketProductsWithDetails = [...basketProductsWithDetails];
        newBasketProductsWithDetails.splice(index, 1)
        setBasketProductsWithDetails(newBasketProductsWithDetails)
    }

    const handleNavigateOrder = () => {

        const checkOrder: CreateOrder = {
            clientId: 1,
            basketItems: basketProducts.map((p: BasketProduct) => ({bookId: p.id, quantity: p.quantity}))
        }

        OrderService.checkOrder(checkOrder)
        .then(() => {
            navigate('/order')
        })
        .catch((error) => {
            dispatch(setNotificationMessage(error.response.data));
            dispatch(setNotificationType("error"));
            dispatch(setNotificationStatus(true));
        })
    }

    return (
        <Grid item xs={10} alignSelf="start" container justifyContent="space-between" marginTop={8}>
            <Grid item xs={6} container direction="column" zIndex={2}>
                <Grid item marginBottom={6}>
                    <Typography variant="h4">
                        Koszyk ({basketProducts.length})
                    </Typography>
                </Grid>
                <Grid item container>
                    {basketProductsWithDetails.map((book: BasketProductWithDetails, index: number) => (
                        <BasketProductView 
                            key={book.product.id} 
                            book={book} 
                            index={index} 
                            handleRemove={handleRemove} 
                            handleUpdateQuantity={handleUpdateQuantity}
                        />
                    ))}
                </Grid>
            </Grid>
            <Grid item xs={5} container justifyContent="center" marginTop={14}>
                <Grid item container direction="column" position="fixed" rowSpacing={4} zIndex={1}>
                    <Grid item container justifyContent="center">
                        <Typography variant="h4" textAlign="end">
                            Łączna kwota: {totalPrice == 0 ? 0 : totalPrice.toFixed(2)} zł
                        </Typography>
                    </Grid>
                    <Grid item container justifyContent="center">
                        {userDetails.isLogged ?
                            basketProducts.length > 0 &&
                                <Button
                                    variant="contained"
                                    color="secondary"
                                    onClick={handleNavigateOrder}
                                >
                                    Złóż zamówienie
                                </Button>
                        :
                            <Button
                                variant="contained"
                                color="secondary"
                                onClick={() => navigate('/login')}
                            >
                                Zaloguj się
                            </Button>
                        }
                    </Grid>
                </Grid>
            </Grid>
        </Grid>
    );
}

export default Basket