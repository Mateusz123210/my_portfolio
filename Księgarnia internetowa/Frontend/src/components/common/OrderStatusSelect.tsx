import { OrderStatus } from "../../models/OrderStatus";
import { Grid, Typography, FormControl, Select, MenuItem, SelectChangeEvent } from "@mui/material";
import { useState, useEffect } from "react";
import OrderStatusService from "../../services/OrderStatusService";

export interface OrderStatusSelectProps {
    status?: OrderStatus,
    canBeEmpty?: boolean,
    setStatus: (status: OrderStatus) => void
}

const OrderStatusSelect = (props: OrderStatusSelectProps) => {

    const [orderStatuses, setOrderStatuses] = useState<OrderStatus[]>([])
    const [selectedStatus, setSelectedStatus] = useState<OrderStatus | undefined>(props.status)

    useEffect(() => {
        OrderStatusService.getAll()
        .then((response) => {
            setOrderStatuses(response.data)
        })
    }, [])

    const handleUpdateStatus = (event: SelectChangeEvent) => {
        const orderStatusId: number = +event.target.value
        const newStatus = orderStatuses.filter((status: OrderStatus) => status.id == orderStatusId)[0]
        setSelectedStatus(newStatus);
        props.setStatus(newStatus)
    }

    return (
        <Grid container alignItems="center" marginTop={2}>
            <Grid item xs={6}>
                <Typography variant="h6">
                    Status zamówienia:
                </Typography>
            </Grid>
            <Grid item xs={6}>
                <FormControl fullWidth>
                    <Select
                        value={selectedStatus ? selectedStatus?.id.toString() : undefined}
                        onChange={handleUpdateStatus}
                    >
                        {props.canBeEmpty &&
                            <MenuItem key={0} value={0}>-</MenuItem>
                        }
                        {orderStatuses.map((status: OrderStatus) => (
                            <MenuItem key={status.id} value={status.id.toString()}>{status.name}</MenuItem>
                        ))}
                    </Select>
                </FormControl>
            </Grid>
        </Grid>
    )
}

export default OrderStatusSelect;