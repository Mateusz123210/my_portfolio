import { Button, Grid, IconButton, Typography } from "@mui/material";
import moment from "moment";
import React from "react";
import { useDispatch } from "react-redux";
import CustomImage from "../../../components/common/CustomImage";
import XCloeasableDialog from "../../../components/common/XCloeasableDialog";
import Book from "../../../models/Book";
import Order from "../../../models/Order";
import { OrderBookDetails } from "../../../models/OrderBookDetails";
import { OrderStatus } from "../../../models/OrderStatus";
import { OrderWithDetails } from "../../../models/OrderWithDetails";
import { removeProduct, updateProductQuantity } from "../../../redux/slices/basketSlice";
import { setNotificationMessage, setNotificationType, setNotificationStatus } from "../../../redux/slices/notificationSlice";
import OrderService from "../../../services/OrderService";
import { DataRow } from "../../book-details/BookDetails";
import OrderProduct from "./OrderProduct";

export interface OrderDetailsProps {
    index: number,
    orderWithDetails: OrderWithDetails
}

const OrderDetails = (props: OrderDetailsProps) => {

    const [order, setOrder] = React.useState<OrderWithDetails>(props.orderWithDetails)

    const [showAllProducts, setShowAllProducts] = React.useState<boolean>(false)

    const dispatch = useDispatch()

    console.log(order)

    const handleRollbackOrder = () => {

        OrderService.rollbackOrder(order.id)
        .then((response) => {
            setOrder({...props.orderWithDetails, status: response.data})
            dispatch(setNotificationMessage(`Wycofano zamówienie`));
            dispatch(setNotificationType("success"));
            dispatch(setNotificationStatus(true));
        })
        .catch((error) => {
            dispatch(setNotificationMessage(error.message.data));
            dispatch(setNotificationType("error"));
            dispatch(setNotificationStatus(true));
        })
    }

    return (
        <Grid item container xs={10} justifyContent="space-between" marginBottom={4} rowSpacing={2}>
            <Grid item xs={12}>
                <Typography variant="h4">
                    Zamowienie {props.index+1}
                </Typography>
            </Grid>
            <Grid item xs={6}>
                {!showAllProducts ?
                    <OrderProduct book={order.books[0].book} quantity={order.books[0].quantity}/>
                :
                    order.books.map((bookDetails: OrderBookDetails) => (
                        <OrderProduct key={bookDetails.book.id} book={bookDetails.book} quantity={bookDetails.quantity}/>
                    ))
                }
                {order.books.length > 1 && 
                    <Button
                        variant="contained"
                        color="secondary"
                        onClick={() => setShowAllProducts(!showAllProducts)}
                    >
                        {!showAllProducts ? "Pokaż więcej produktów" : "Ukryj produkty"}
                    </Button>
                }
            </Grid>
            <Grid item xs={4} container direction="column" justifyContent="center" rowSpacing={2} marginBottom={10}>
                <DataRow title="Data utworzenia:" value={moment(order.creationDate).format("DD.MM.YYYY").toLocaleString()}/>
                {order.fullfillmentDate && <DataRow title="Data odbioru:" value={moment(order.creationDate).format("DD.MM.YYYY").toLocaleString()}/>}
                <DataRow title="Łączna kwota:" value={`${order.totalPrice} zł`}/>
                <DataRow title="Status zamówienia:" value={order.status.name}/>
                <Grid item container justifyContent="center" marginTop={2}>
                    <Grid item xs={6}>
                        <XCloeasableDialog
                            title={`Dane odbiorcy zamówienia nr ${props.index+1}`}
                            buttonTitle="Dane odbiorcy"
                            showButton={true}
                            form={
                                <Grid item xs={8} container alignSelf="center" justifyContent="center" alignItems="center" rowSpacing={2}>
                                    <DataRow title="Imię:" value={order.receiverData.name}/>
                                    <DataRow title="Nazwisko:" value={order.receiverData.surname}/>
                                    <DataRow title="E-mail:" value={order.receiverData.email}/>
                                    <DataRow title="Telefon:" value={order.receiverData.tel ? order.receiverData.tel : ''}/>
                                </Grid>
                            }
                        />
                    </Grid>
                </Grid>
                {order.status.name === "Utworzone" &&
                    <Grid item container justifyContent="center" marginTop={2}>
                        <Button
                            variant="contained"
                            color="error"
                            onClick={handleRollbackOrder}
                        >
                            Wycofaj
                        </Button>
                    </Grid>
                }
            </Grid>
        </Grid>
    );
}

export default OrderDetails;

//<DataRow title="Data utworzena:" value={moment(order.creationDate).format("DD.MM.YYYY").toLocaleString()}/>
//{order.creationDate && <DataRow title="Data realizacji:" value={moment(order.creationDate).format("DD.MM.YYYY").toLocaleString()}/>}