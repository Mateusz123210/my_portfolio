import React, { useEffect } from "react";
import { useState } from "react";
import {
  Grid,
  TextField,
  TextareaAutosize,
  Button,
  Typography,
} from "@mui/material";
import { emptyDrawing } from "../../assets/graphImage";
import PointService from "../../services/points/pointService";
import Validator from "../../validators/validator";

export interface Point {
  x1: string;
  y1: string;
  x2: string;
  y2: string;
}

export interface Distance {
  solution: string;
  hint: string;
  graph: string;
}

export interface PointError {
  x1: string;
  y1: string;
  x2: string;
  y2: string;
}

const PointsDistance = () => {
  const [point, setPoint] = useState<Point>({
    x1: "",
    y1: "",
    x2: "",
    y2: "",
  });
  const [dis, setDis] = useState<Distance>({
    solution: "",
    hint: "",
    graph: emptyDrawing,
  });

  const [errors, setErrors] = useState<PointError>({
    x1: "",
    y1: "",
    x2: "",
    y2: "",
  });

  const [hint, setHint] = useState<boolean>(false);

  const showOrHideHint = () => {
    setHint(!hint);
  };

  const findDistanceBetweenPoints = () => {
    let newErrorState = { ...errors };
    newErrorState.x1 = "";
    newErrorState.y1 = "";
    newErrorState.x2 = "";
    newErrorState.y2 = "";
    let valid = true;
    if (!Validator.checkIfIsNotEmpty(point.x1)) {
      newErrorState.x1 = Validator.emptyX;
      valid = false;
    } else if (!Validator.checkIfIsValidNumber(point.x1)) {
      newErrorState.x1 = Validator.notNumberMessage;
      valid = false;
    }
    if (!Validator.checkIfIsNotEmpty(point.y1)) {
      newErrorState.y1 = Validator.emptyY;
      valid = false;
    } else if (!Validator.checkIfIsValidNumber(point.y1)) {
      newErrorState.y1 = Validator.notNumberMessage;
      valid = false;
    }
    if (!Validator.checkIfIsNotEmpty(point.x2)) {
      newErrorState.x2 = Validator.emptyX;
      valid = false;
    } else if (!Validator.checkIfIsValidNumber(point.x2)) {
      newErrorState.x2 = Validator.notNumberMessage;
      valid = false;
    }
    if (!Validator.checkIfIsNotEmpty(point.y2)) {
      newErrorState.y2 = Validator.emptyY;
      valid = false;
    } else if (!Validator.checkIfIsValidNumber(point.y2)) {
      newErrorState.y2 = Validator.notNumberMessage;
      valid = false;
    }
    setErrors(newErrorState);
    if (valid === true) {
      PointService.findDistanceBetweenPoints(point)
        .then((response) => {
          setDis(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    }
  };

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return (
    <Grid
      container
      justifyContent="center"
      display="flex"
      alignItems="center"
      marginTop={2}
    >
      <Grid item width={1000}>
        <Grid item>
          <Grid
            item
            justifyContent="center"
            alignItems="center"
            paddingBottom={2}
            marginTop={0}
            paddingTop={0}
          >
            <Typography fontSize={40} color="#3596FC" textAlign="center">
              Odległość pomiędzy punktami
            </Typography>
          </Grid>
          <Grid item width={1000} display="flex">
            <Typography
              fontSize={36}
              color="#3760FA"
              textAlign="center"
              marginTop={4.8}
            >
              p1&nbsp;=&nbsp;
            </Typography>
            <Grid item width={400} display="column">
              <Grid item>
                <TextField
                  id="x1"
                  fullWidth
                  placeholder="Wpisz x1..."
                  value={point.x1 ? point.x1 : ""}
                  onChange={(event) =>
                    setPoint({ ...point, x1: event.target.value })
                  }
                  helperText={errors.x1 ? errors.x1 : ""}
                ></TextField>
              </Grid>
              <Grid item marginTop={3}>
                <TextField
                  id="y1"
                  fullWidth
                  placeholder="Wpisz y1..."
                  value={point.y1 ? point.y1 : ""}
                  onChange={(event) =>
                    setPoint({ ...point, y1: event.target.value })
                  }
                  helperText={errors.y1 ? errors.y1 : ""}
                ></TextField>
              </Grid>
            </Grid>
            <Typography
              fontSize={36}
              color="#3760FA"
              textAlign="center"
              marginTop={4.8}
            >
              &nbsp;&nbsp;&nbsp;p2&nbsp;=&nbsp;
            </Typography>
            <Grid item width={400} display="column">
              <Grid item>
                <TextField
                  id="x2"
                  fullWidth
                  placeholder="Wpisz x2..."
                  value={point.x2 ? point.x2 : ""}
                  onChange={(event) =>
                    setPoint({ ...point, x2: event.target.value })
                  }
                  helperText={errors.x2 ? errors.x2 : ""}
                ></TextField>
              </Grid>
              <Grid item marginTop={3}>
                <TextField
                  id="y2"
                  fullWidth
                  placeholder="Wpisz y2..."
                  value={point.y2 ? point.y2 : ""}
                  onChange={(event) =>
                    setPoint({ ...point, y2: event.target.value })
                  }
                  helperText={errors.y2 ? errors.y2 : ""}
                ></TextField>
              </Grid>
            </Grid>
          </Grid>
          <Grid item marginTop={2}>
            <Button
              id="solve"
              fullWidth
              variant="contained"
              style={{ background: "#4683E6" }}
              onClick={() => {
                findDistanceBetweenPoints();
              }}
            >
              Rozwiąż
            </Button>
          </Grid>
        </Grid>
        <Grid item marginTop={3}>
          <Grid item>
            <Typography fontSize={16} color="#2C74B3" textAlign="left">
              Wynik
            </Typography>
          </Grid>
          <TextareaAutosize
            id="result"
            readOnly={true}
            minRows={2}
            value={dis.solution ? dis.solution : ""}
            style={{ width: 1000, resize: "vertical", background: "#D8E8EE" }}
          />
        </Grid>
        <Grid item marginTop={3} width={1000}>
          <Button
            id="hintButton"
            style={{
              backgroundColor: "#21b6ae",
            }}
            fullWidth
            variant="contained"
            onClick={() => {
              showOrHideHint();
            }}
          >
            {hint ? "Ukryj wskazówkę" : "Pokaż wskazówkę"}
          </Button>
        </Grid>
        <Grid item marginTop={2}>
          {hint && (
            <Grid item>
              <Grid item>
                <Typography fontSize={16} color="#2C74B3" textAlign="left">
                  Wskazówka
                </Typography>
              </Grid>
              <TextareaAutosize
                id="hint"
                readOnly={true}
                minRows={2}
                value={dis.hint ? dis.hint : ""}
                style={{
                  width: 1000,
                  resize: "vertical",
                  background: "#dcedc8",
                }}
              />
            </Grid>
          )}
        </Grid>
        <Grid item marginTop={2} width={1000} marginLeft={21}>
          <img
            id="image"
            src={`data:image/jpeg;base64,${dis.graph}`}
            alt="Rysunek"
          />
        </Grid>
      </Grid>
    </Grid>
  );
};

export default PointsDistance;
