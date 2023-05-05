import React, { useEffect } from "react";
import {
  TextField,
  Typography,
  Grid,
  TextareaAutosize,
  Button,
  IconButton,
} from "@mui/material";
import { useState } from "react";
import TriangleService from "../../services/triangle/triangleService";
import { TriangleSides } from "../../services/triangle/triangleService";
import Triangle from "../../assets/triangle.png";
import Validator from "../../validators/validator";
import { OverlayTrigger, Popover } from "react-bootstrap";
import InfoIcon from "@mui/icons-material/Info";

export interface Response {
  error?: string;
  firstSide?: string;
  secondSide?: string;
  hypotenuse?: string;
  sinL?: string;
  cosL?: string;
  tgL?: string;
  ctgL?: string;
  hint?: string;
}

const TriangleCalculations = () => {
  const [res, setRes] = useState<Response>({
    error: "",
    firstSide: "",
    secondSide: "",
    hypotenuse: "",
    sinL: "",
    cosL: "",
    tgL: "",
    ctgL: "",
    hint: "",
  });

  const [sides, setSides] = useState<TriangleSides>({
    firstSide: "",
    secondSide: "",
    hypotenuse: "",
  });

  const [errors, setErrors] = useState<TriangleSides>({
    firstSide: "",
    secondSide: "",
    hypotenuse: "",
  });

  const [hint, setHint] = useState<boolean>(false);

  const showOrHideHint = () => {
    setHint(!hint);
  };

  const [pop, setPop] = useState<boolean>(false);

  const setPopover = (val: boolean) => {
    setPop(val);
  };
  const popover = (
    <Grid marginLeft={2}>
      {pop && (
        <Popover
          id="popover-basic"
          onClick={() => {
            setPopover(false);
          }}
          onMouseLeave={() => {
            setPopover(false);
          }}
        >
          <Grid marginTop={-1}>
            <Popover.Body id="popover-body">
              Wymagane jest podanie długości minimum dwóch
              <br />
              boków trójkąta
            </Popover.Body>
          </Grid>
        </Popover>
      )}
    </Grid>
  );

  const getTriangleProperties = () => {
    let newErrorState = { ...errors };
    newErrorState.firstSide = "";
    newErrorState.secondSide = "";
    newErrorState.hypotenuse = "";
    let valid = true;
    if (!Validator.checkIfIsNotEmpty(sides.firstSide)) {
      if (
        Validator.checkIfIsNotEmpty(sides.secondSide) &&
        Validator.checkIfIsNotEmpty(sides.hypotenuse)
      ) {
        if (!Validator.checkIfISValidPositiveNumber(sides.secondSide)) {
          newErrorState.secondSide = Validator.notValidPositiveNumberMessage;
          valid = false;
        }
        if (!Validator.checkIfISValidPositiveNumber(sides.hypotenuse)) {
          newErrorState.hypotenuse = Validator.notValidPositiveNumberMessage;
          valid = false;
        }
      } else {
        newErrorState.hypotenuse = Validator.notEnoughNumbersMessage;
        valid = false;
      }
    } else if (!Validator.checkIfIsNotEmpty(sides.secondSide)) {
      if (
        Validator.checkIfIsNotEmpty(sides.firstSide) &&
        Validator.checkIfIsNotEmpty(sides.hypotenuse)
      ) {
        if (!Validator.checkIfISValidPositiveNumber(sides.firstSide)) {
          newErrorState.firstSide = Validator.notValidPositiveNumberMessage;
          valid = false;
        }
        if (!Validator.checkIfISValidPositiveNumber(sides.hypotenuse)) {
          newErrorState.hypotenuse = Validator.notValidPositiveNumberMessage;
          valid = false;
        }
      } else {
        newErrorState.hypotenuse = Validator.notEnoughNumbersMessage;
        valid = false;
      }
    } else if (!Validator.checkIfIsNotEmpty(sides.hypotenuse)) {
      if (
        Validator.checkIfIsNotEmpty(sides.firstSide) &&
        Validator.checkIfIsNotEmpty(sides.secondSide)
      ) {
        if (!Validator.checkIfISValidPositiveNumber(sides.firstSide)) {
          newErrorState.firstSide = Validator.notValidPositiveNumberMessage;
          valid = false;
        }
        if (!Validator.checkIfISValidPositiveNumber(sides.secondSide)) {
          newErrorState.secondSide = Validator.notValidPositiveNumberMessage;
          valid = false;
        }
      } else {
        newErrorState.hypotenuse = Validator.notEnoughNumbersMessage;
        valid = false;
      }
    } else {
      if (!Validator.checkIfISValidPositiveNumber(sides.firstSide)) {
        newErrorState.firstSide = Validator.notValidPositiveNumberMessage;
        valid = false;
      }
      if (!Validator.checkIfISValidPositiveNumber(sides.secondSide)) {
        newErrorState.secondSide = Validator.notValidPositiveNumberMessage;
        valid = false;
      }
      if (!Validator.checkIfISValidPositiveNumber(sides.hypotenuse)) {
        newErrorState.hypotenuse = Validator.notValidPositiveNumberMessage;
        valid = false;
      }
    }

    setErrors(newErrorState);
    if (valid === true) {
      TriangleService.solveTriangle(sides)
        .then((response) => {
          setRes(response.data);
          if (response.data.firstSide) {
            setSides({ ...sides, firstSide: response.data.firstSide });
          }
          if (response.data.secondSide) {
            setSides({ ...sides, secondSide: response.data.secondSide });
          }
          if (response.data.hypotenuse) {
            setSides({ ...sides, hypotenuse: response.data.hypotenuse });
          }
          if (response.data.error) {
            setErrors({ ...errors, hypotenuse: response.data.error });
          }
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
        <Grid
          item
          justifyContent="center"
          alignItems="center"
          paddingBottom={2}
          marginTop={0}
          paddingTop={0}
        >
          <Typography fontSize={40} color="#3596FC" textAlign="center">
            Boki i kąty trójkąta prostokątnego
          </Typography>
        </Grid>
        <Grid item marginTop={3}>
          <Grid item display="flex" flexDirection="row">
            <Grid item>
              <img src={Triangle} width={700} alt="Trójkąt" />
            </Grid>
            <Grid item display="flex" flexDirection="column">
              <Grid item display="flex" flexDirection="row" marginTop={2}>
                <Typography fontSize={24} marginTop={1}>
                  a&nbsp;=&nbsp;
                </Typography>
                <TextField
                  id="a"
                  fullWidth
                  value={sides.firstSide ? sides.firstSide : ""}
                  onChange={(event) =>
                    setSides({ ...sides, firstSide: event.target.value })
                  }
                  helperText={errors.firstSide ? errors.firstSide : ""}
                  InputProps={{
                    sx: {
                      "& input": {
                        textAlign: "end",
                        fontSize: 20,
                      },
                    },
                  }}
                ></TextField>
              </Grid>

              <Grid item display="flex" flexDirection="row" marginTop={2}>
                <Typography fontSize={24} marginTop={1}>
                  b&nbsp;=&nbsp;
                </Typography>
                <TextField
                  id="b"
                  fullWidth
                  value={sides.secondSide ? sides.secondSide : ""}
                  onChange={(event) =>
                    setSides({ ...sides, secondSide: event.target.value })
                  }
                  helperText={errors.secondSide ? errors.secondSide : ""}
                  InputProps={{
                    sx: {
                      "& input": {
                        textAlign: "end",
                        fontSize: 20,
                      },
                    },
                  }}
                ></TextField>
              </Grid>
              <Grid item display="flex" flexDirection="row" marginTop={2}>
                <Typography fontSize={24} marginTop={1}>
                  c&nbsp;=&nbsp;
                </Typography>
                <TextField
                  id="c"
                  fullWidth
                  value={sides.hypotenuse ? sides.hypotenuse : ""}
                  onChange={(event) =>
                    setSides({ ...sides, hypotenuse: event.target.value })
                  }
                  helperText={errors.hypotenuse ? errors.hypotenuse : ""}
                  InputProps={{
                    sx: {
                      "& input": {
                        textAlign: "end",
                        fontSize: 20,
                      },
                    },
                  }}
                ></TextField>
              </Grid>
            </Grid>
          </Grid>
          <Grid item marginTop={2} display="flex" flexDirection="row">
            <Grid item width={960}>
              <Button
                id="solve"
                fullWidth
                variant="contained"
                style={{ background: "#4683E6" }}
                onClick={() => {
                  getTriangleProperties();
                }}
              >
                Rozwiąż
              </Button>
            </Grid>
            <Grid item marginLeft={1}>
              <OverlayTrigger
                trigger="click"
                rootClose
                placement="left"
                overlay={popover}
              >
                <IconButton
                  id="popoverButton"
                  style={{ height: "100%" }}
                  onClick={() => {
                    setPopover(true);
                  }}
                >
                  <InfoIcon />
                </IconButton>
              </OverlayTrigger>
            </Grid>
          </Grid>
          <Grid
            item
            marginTop={3}
            display="flex"
            flexDirection="row"
            justifyContent="space-between"
          >
            <Grid item display="flex" flexDirection="column">
              <Grid
                item
                display="flex"
                flexDirection="row"
                justifyContent="space-between"
              >
                <Typography fontSize={24} marginTop={1}>
                  sin(L)&nbsp;=&nbsp;&nbsp;
                </Typography>
                <Grid item width={280}>
                  <TextField
                    id="sinL"
                    style={{ background: "#D8E8EE" }}
                    fullWidth
                    value={res.sinL ? res.sinL : ""}
                    InputProps={{
                      sx: {
                        "& input": {
                          textAlign: "end",
                          fontSize: 20,
                        },
                      },
                      readOnly: true,
                    }}
                  ></TextField>
                </Grid>
              </Grid>
              <Grid
                item
                display="flex"
                flexDirection="row"
                marginTop={1}
                justifyContent="space-between"
              >
                <Typography fontSize={24} marginTop={1}>
                  cos(L)&nbsp;=&nbsp;
                </Typography>
                <Grid item width={280}>
                  <TextField
                    id="cosL"
                    style={{ background: "#D8E8EE" }}
                    fullWidth
                    value={res.cosL ? res.cosL : ""}
                    InputProps={{
                      sx: {
                        "& input": {
                          textAlign: "end",
                          fontSize: 20,
                        },
                      },
                      readOnly: true,
                    }}
                  ></TextField>
                </Grid>
              </Grid>
              <Grid
                item
                display="flex"
                flexDirection="row"
                marginTop={1}
                justifyContent="space-between"
              >
                <Typography fontSize={24} marginTop={1}>
                  tg(L)&nbsp;=&nbsp;&nbsp;&nbsp;
                </Typography>
                <Grid item width={280}>
                  <TextField
                    id="tgL"
                    style={{ background: "#D8E8EE" }}
                    fullWidth
                    value={res.tgL ? res.tgL : ""}
                    InputProps={{
                      sx: {
                        "& input": {
                          textAlign: "end",
                          fontSize: 20,
                        },
                      },
                      readOnly: true,
                    }}
                  ></TextField>
                </Grid>
              </Grid>
              <Grid item display="flex" flexDirection="row" marginTop={1}>
                <Typography fontSize={24} marginTop={1}>
                  ctg(L)&nbsp;=&nbsp;&nbsp;
                </Typography>
                <Grid item width={280}>
                  <TextField
                    id="ctgL"
                    style={{ background: "#D8E8EE" }}
                    fullWidth
                    value={res.ctgL ? res.ctgL : ""}
                    InputProps={{
                      sx: {
                        "& input": {
                          textAlign: "end",
                          fontSize: 20,
                        },
                      },
                      readOnly: true,
                    }}
                  ></TextField>
                </Grid>
              </Grid>
            </Grid>
            <Grid item display="flex" flexDirection="column">
              <Grid
                item
                display="flex"
                flexDirection="row"
                justifyContent="space-between"
              >
                <Typography fontSize={24} marginTop={1}>
                  sin(B)&nbsp;=&nbsp;&nbsp;
                </Typography>
                <Grid item width={280}>
                  <TextField
                    id="sinB"
                    fullWidth
                    style={{ background: "#D8E8EE" }}
                    value={res.cosL ? res.cosL : ""}
                    InputProps={{
                      sx: {
                        "& input": {
                          textAlign: "end",
                          fontSize: 20,
                        },
                      },
                      readOnly: true,
                    }}
                  ></TextField>
                </Grid>
              </Grid>
              <Grid
                item
                display="flex"
                flexDirection="row"
                marginTop={1}
                justifyContent="space-between"
              >
                <Typography fontSize={24} marginTop={1}>
                  cos(B)&nbsp;=&nbsp;
                </Typography>
                <Grid item width={280}>
                  <TextField
                    id="cosB"
                    style={{ background: "#D8E8EE" }}
                    fullWidth
                    value={res.sinL ? res.sinL : ""}
                    InputProps={{
                      sx: {
                        "& input": {
                          textAlign: "end",
                          fontSize: 20,
                        },
                      },
                      readOnly: true,
                    }}
                  ></TextField>
                </Grid>
              </Grid>
              <Grid
                item
                display="flex"
                flexDirection="row"
                marginTop={1}
                justifyContent="space-between"
              >
                <Typography fontSize={24} marginTop={1}>
                  tg(B)&nbsp;=&nbsp;&nbsp;&nbsp;&nbsp;
                </Typography>
                <Grid item width={280}>
                  <TextField
                    id="tgB"
                    style={{ background: "#D8E8EE" }}
                    fullWidth
                    value={res.ctgL ? res.ctgL : ""}
                    InputProps={{
                      sx: {
                        "& input": {
                          textAlign: "end",
                          fontSize: 20,
                        },
                      },
                      readOnly: true,
                    }}
                  ></TextField>
                </Grid>
              </Grid>
              <Grid
                item
                display="flex"
                flexDirection="row"
                marginTop={1}
                justifyContent="space-between"
              >
                <Typography fontSize={24} marginTop={1}>
                  ctg(B)&nbsp;=&nbsp;&nbsp;
                </Typography>
                <Grid item width={280}>
                  <TextField
                    id="ctgB"
                    style={{ background: "#D8E8EE" }}
                    fullWidth
                    value={res.tgL ? res.tgL : ""}
                    InputProps={{
                      sx: {
                        "& input": {
                          textAlign: "end",
                          fontSize: 20,
                        },
                      },
                      readOnly: true,
                    }}
                  ></TextField>
                </Grid>
              </Grid>
            </Grid>
          </Grid>
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
        <Grid item marginTop={3} width={1000}>
          {hint && (
            <Grid item>
              <Grid item>
                <Typography fontSize={16} color="#2C74B3" textAlign="left">
                  Wskazówka
                </Typography>
              </Grid>
              <TextareaAutosize
                id="hint"
                minRows={3}
                value={res.hint ? res.hint : ""}
                style={{
                  width: 1000,
                  resize: "vertical",
                  background: "#dcedc8",
                }}
                readOnly={true}
              />
            </Grid>
          )}
        </Grid>
      </Grid>
    </Grid>
  );
};

export default TriangleCalculations;
