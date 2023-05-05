import { Grid, Typography } from "@mui/material";

const NotFound = () => {
    return (
        <Grid item xs={12} container alignItems="center" justifyContent="center" alignSelf="stretch">
            <Typography variant="h4">
                Błąd 404 - Nie znaleziono zasobu
            </Typography>
        </Grid>
    )
}

export default NotFound;