import { Grid } from "@mui/material";

const Footer = (props: any) => {
  return (
    <Grid
      marginTop={10}
      width={props.width}
      height={80}
      style={{ background: "#f2f9f7" }}
      textAlign="center"
      alignItems="center"
      justifyContent="center"
      paddingTop={1.2}
    >
      <h3>Copyright &copy; Mateusz Urbańczyk. All Rights Reserved</h3>
    </Grid>
  );
};

export default Footer;
