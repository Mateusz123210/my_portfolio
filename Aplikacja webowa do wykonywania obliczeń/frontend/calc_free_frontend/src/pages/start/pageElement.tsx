import React from "react";
import { Grid, Typography, Button } from "@mui/material";
import { useNavigate } from "react-router-dom";

const PageElement = (props: any) => {
  const navigate = useNavigate();
  return (
    <Grid
      container
      alignItems="center"
      justifyContent="center"
      display="flex"
      flexDirection="column"
      width={360}
      marginLeft={1}
      marginRight={1}
      marginTop={2}
    >
      <Button
        id={props.id}
        fullWidth
        variant="outlined"
        onClick={() => navigate(props.navigateDirection)}
      >
        <Grid item height={360}>
          <Grid item marginTop={2}>
            <img src={props.image} width={320} height={240} alt={props.label} />
          </Grid>
          <Grid item>
            <Typography fontSize={28} color="#4C87BA" textAlign="center">
              {props.pageName}
            </Typography>
          </Grid>
        </Grid>
      </Button>
    </Grid>
  );
};

export default PageElement;
