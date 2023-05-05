import { Grid, Typography, Button, FormControl, MenuItem, Select } from "@mui/material"
import moment from "moment"
import React, { useEffect, useState } from "react"
import { useDispatch } from "react-redux"
import { useParams } from "react-router-dom"
import XCloeasableDialog from "../../../components/common/XCloeasableDialog"
import { OrderBookDetails } from "../../../models/OrderBookDetails"
import { OrderWithDetails } from "../../../models/OrderWithDetails"
import { setNotificationMessage, setNotificationType, setNotificationStatus } from "../../../redux/slices/notificationSlice"
import OrderService from "../../../services/OrderService"
import { DataRow } from "../../book-details/BookDetails"
import OrderProduct from "../my-orders/OrderProduct"
import { OrderStatus } from "../../../models/OrderStatus"
import { SelectChangeEvent } from "@mui/material"
import OrderStatusSelect from "../../../components/common/OrderStatusSelect"

const OrderData = () => {

    let orderId: any = useParams().orderId
    const [order, setOrder] = useState<OrderWithDetails>()

    const [showAllProducts, setShowAllProducts] = React.useState<boolean>(false)

    const dispatch = useDispatch()

    useEffect(() => {
        OrderService.getById(+orderId)
        .then((response) => {
            setOrder(response.data)
        })
        .catch((error) => {
            dispatch(setNotificationMessage(error.message.data));
            dispatch(setNotificationType("error"));
            dispatch(setNotificationStatus(true));
        })
    }, [])

    if(!order){
        return <div>Ładowanie...</div>
    }

    const handleUpdateOrder = (status: OrderStatus) => {
        OrderService.updateOrder(orderId, status)
        .then((response) => {
            setOrder({...order, status: response.data.status, fullfillmentDate: response.data.fullfillmentDate, totalPrice: response.data.totalPrice})
        })
    }

    return (
        <Grid item container xs={10} justifyContent="space-between" alignSelf="start" marginBottom={4}  marginTop={8} rowSpacing={2}>
            <Grid item xs={12} marginBottom={4}>
                <Typography variant="h3">
                    Zamówienie {order.id}
                </Typography>
            </Grid>
            <Grid item xs={5.4} marginBottom={5}>
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
            <Grid item xs={5.4} container alignSelf="start" justifyContent="center">
                <Grid item xs={4} container justifyContent="center" rowSpacing={2} marginBottom={10} position="fixed">
                    <Typography variant="h4" textAlign="center" marginBottom={2}>
                        Dane zamówienia
                    </Typography>
                    <DataRow title="Data utworzenia:" value={moment(order.creationDate).format("DD.MM.YYYY").toLocaleString()}/>
                    {order.fullfillmentDate && <DataRow title="Data odbioru:" value={moment(order.creationDate).format("DD.MM.YYYY").toLocaleString()}/>}
                    <DataRow title="Łączna kwota:" value={`${order.totalPrice} zł`}/>
                    <OrderStatusSelect 
                        status={order.status} 
                        setStatus={handleUpdateOrder}
                    />
                    <Typography variant="h4" textAlign="center" marginTop={5} marginBottom={2}>
                        Dane odbiorcy
                    </Typography>
                    <DataRow title="Imię:" value={order.receiverData.name}/>
                    <DataRow title="Nazwisko:" value={order.receiverData.surname}/>
                    <DataRow title="E-mail:" value={order.receiverData.email}/>
                    <DataRow title="Telefon:" value={order.receiverData.tel ? order.receiverData.tel : ''}/>
                </Grid>
            </Grid>
        </Grid>
    );
}

export default OrderData;