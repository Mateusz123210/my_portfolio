import { Button, Grid } from "@mui/material";

const MyButton = (props: any) => {
  return (
    <Grid item width={150} margin={2}>
      <Button
        fullWidth
        variant="contained"
        value={props.label}
        onClick={() => {
          props.buttonAction(props.label);
        }}
        style={{ backgroundColor: "#f7edf0", color: "#000000" }}
      >
        {props.label}
      </Button>
    </Grid>
  );
};
export default MyButton;
