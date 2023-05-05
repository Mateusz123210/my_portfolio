import { Grid } from "@mui/material";
import './Content.css';

type ContentProps = {
    children: React.ReactNode;
};

const Content = ({ children }: ContentProps) => {
    return (
        <main style={{height: "100%"}}>
            <Grid container justifyContent="center" alignItems="center" sx={{height: "100%"}}>
                {children}
            </Grid>
        </main>
    )
}

export default Content;