import { Grid, Typography } from "@mui/material";

const Forbidden = () => {
    return (
        <Grid item xs={12} container alignItems="center" justifyContent="center" alignSelf="stretch">
            <Typography variant="h4">
                Błąd 403 - Brak dostępu do zasobu
            </Typography>
        </Grid>
    )
}

export default Forbidden;