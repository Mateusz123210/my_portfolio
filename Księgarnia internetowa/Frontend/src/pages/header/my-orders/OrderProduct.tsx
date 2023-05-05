import { Grid, Typography, IconButton } from "@mui/material";
import CustomImage from "../../../components/common/CustomImage";
import Book from "../../../models/Book";

const OrderProduct = (props: {book: Book, quantity: number}) => {

    const book = props.book

    return (
        <Grid item container border="1px solid black" padding={2} marginBottom={4}>
            <Grid item xs={3} container justifyContent="center" marginRight={6}>
                <CustomImage img={book.avatar}/>
            </Grid>
            <Grid item xs={8} container direction="column">
                <Grid item xs={2} container alignItems="center">
                    <Typography variant="h5">{book.title}</Typography>
                </Grid>
                <Grid item xs={4} marginTop={1.5}>
                    <Typography variant="h6">{book.authors.map((a: any) => a.author.firstname + a.author.surname).join(', ')}</Typography>
                </Grid>
                <Grid item xs={2} container justifyContent="space-between" alignItems="center">
                    <Grid item xs={6} container alignItems="center">
                        <Typography variant="h5">x {props.quantity}</Typography>
                    </Grid>
                    <Grid item xs={6}>
                        <Typography variant="h5" textAlign="end">{book.price} zł</Typography>
                    </Grid>
                </Grid>
            </Grid>
        </Grid>
    )
}

export default OrderProduct;