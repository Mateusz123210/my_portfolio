import { Grid } from "@mui/material";
import React, { useEffect } from "react";
import Order from "../../../models/Order";
import { OrderStatus } from "../../../models/OrderStatus";
import { OrderWithDetails } from "../../../models/OrderWithDetails";
import OrderService from "../../../services/OrderService";
import { books } from "../../shop/Shop";
import OrderDetails from "./OrderDetails";

const MyOrders = () => {

    const [orders, setOrders] = React.useState<OrderWithDetails[]>([])

    useEffect(() => {
        OrderService.getByClientId(1)
        .then((response) => {
            setOrders(response.data)
        })
        .catch((error) => {
            console.log(error)
        })
    }, [])
    
    return (
        <Grid item xs={10} container justifyContent="center" marginTop={10}>
            {orders.length == 0 ? "Brak zamówień" : orders.map((orderWithDetails: OrderWithDetails, index: number) => (
                <OrderDetails key={orderWithDetails.id} index={index} orderWithDetails={orderWithDetails}/>
            ))}
        </Grid>
    );
}

export default MyOrders;