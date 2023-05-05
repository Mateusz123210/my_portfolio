import React, { useEffect } from "react";
import { useState } from "react";
import {
  Grid,
  TextField,
  TextareaAutosize,
  Button,
  Typography,
  IconButton,
} from "@mui/material";
import Validator from "../../validators/validator";
import WeightedAverageService from "../../services/averages/weightedAverageService";
import { OverlayTrigger, Popover } from "react-bootstrap";
import InfoIcon from "@mui/icons-material/Info";

export interface Numbers {
  allNumbers: string;
  allWages: string;
  numbersWagesShow: string;
}

export interface NewNumbers {
  number: string;
  wage: string;
}

export interface Response {
  solution: string;
  hint: string;
  error: string;
}

export interface NumberError {
  numberError: string;
  wageError: string;
  allNumbersError: string;
}

const WeightedAverage = () => {
  const [numbers, setNumbers] = useState<Numbers>({
    allNumbers: "",
    allWages: "",
    numbersWagesShow: "",
  });

  const [newNumbers, setNewNumbers] = useState<NewNumbers>({
    number: "",
    wage: "",
  });

  const [res, setRes] = useState<Response>({
    solution: "",
    hint: "",
    error: "",
  });

  const [errors, setErrors] = useState<NumberError>({
    numberError: "",
    wageError: "",
    allNumbersError: "",
  });

  const [hint, setHint] = useState<boolean>(false);

  const showOrHideHint = () => {
    setHint(!hint);
  };

  const [pop, setPop] = useState<boolean>(false);

  const setPopover = (val: boolean) => {
    setPop(val);
  };

  const addNumbers = () => {
    let newErrorState = { ...errors };
    newErrorState.numberError = "";
    newErrorState.wageError = "";
    newErrorState.allNumbersError = "";
    let valid = true;
    if (!Validator.checkIfIsNotEmpty(newNumbers.number)) {
      newErrorState.numberError = Validator.notNumbersMessage;
      valid = false;
    } else if (!Validator.checkIfIsValidNumber(newNumbers.number)) {
      newErrorState.numberError = Validator.notNumberMessage;
      valid = false;
    }
    if (!Validator.checkIfIsNotEmpty(newNumbers.wage)) {
      newErrorState.wageError = Validator.notNumbersMessage;
      valid = false;
    } else if (!Validator.checkIfIsValidNonNegativeNumber(newNumbers.wage)) {
      newErrorState.wageError = Validator.notNonNegativeNumberMessage;
      valid = false;
    }
    setErrors(newErrorState);
    if (valid === true) {
      let tempString = numbers.numbersWagesShow;
      if (tempString.length > 0) {
        tempString =
          tempString + ";" + newNumbers.number + "(" + newNumbers.wage + ")";
        setNumbers({
          ...numbers,
          numbersWagesShow: tempString,
        });
      } else {
        setNumbers({
          ...numbers,
          numbersWagesShow: newNumbers.number + "(" + newNumbers.wage + ")",
        });
      }
      setNewNumbers({ ...newNumbers, number: "", wage: "" });
    }
  };

  const findWeightedAverage = () => {
    let newErrorState = { ...errors };
    let valid = true;
    newErrorState.numberError = "";
    newErrorState.wageError = "";
    newErrorState.allNumbersError = "";
    if (!Validator.checkIfIsNotEmpty(numbers.numbersWagesShow)) {
      newErrorState.allNumbersError = Validator.emptyListMessage;
      valid = false;
    } else if (
      !Validator.checkIfIsValidWeightedAverageNumbersWagesList(
        numbers.numbersWagesShow
      )
    ) {
      newErrorState.allNumbersError =
        Validator.notValidWeightedAverageListMessage;
      valid = false;
    }
    setErrors(newErrorState);
    if (valid === true) {
      const matches = Validator.getWeightedAverageMatches(
        numbers.numbersWagesShow
      );
      let newNumbers = "";
      let newWages = "";
      let temp = "";
      let t1 = [];
      for (let i = 0; i < matches.length; i++) {
        temp = matches[i].slice(0, matches[i].length - 1);
        t1 = temp.split("(");
        newNumbers = newNumbers + t1[0] + ";";
        newWages = newWages + t1[1] + ";";
      }
      newNumbers = newNumbers.slice(0, newNumbers.length - 1);
      newWages = newWages.slice(0, newWages.length - 1);
      setNumbers({ ...numbers, allNumbers: newNumbers, allWages: newWages });
      let tempNumbers: Numbers = {
        allNumbers: newNumbers,
        allWages: newWages,
        numbersWagesShow: "",
      };

      WeightedAverageService.findWeightedAverage(tempNumbers)
        .then((response) => {
          setRes(response.data);
          if (response.data.error) {
            let newErrorState = { ...errors };
            newErrorState.numberError = "";
            newErrorState.wageError = response.data.error;
            setErrors(newErrorState);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    }
  };

  const clearList = () => {
    setNumbers({
      ...numbers,
      allNumbers: "",
      allWages: "",
      numbersWagesShow: "",
    });
  };

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  const popover = (
    <Grid marginLeft={2}>
      {pop && (
        <Popover
          id="popoverBasic"
          onClick={() => {
            setPopover(false);
          }}
          onMouseLeave={() => {
            setPopover(false);
          }}
        >
          <Grid marginTop={-1}>
            <Popover.Body id="popoverBody">
              Aby obliczyć średnią ważoną liczb należy najpierw
              <br />
              je dodać. Można to zrobić wpisując liczbę i jej
              <br />
              wagę w powyższe pola i kliknąć przycisk
              <br /> "Dodaj liczbę" lub wpisać je samodzielnie w
              <br />
              poniższym polu w formacie liczba(waga);liczba2(waga2).
              <br /> Przykładowy ciąg:
              <br />
              4(5);8(8);43(4);1(2);3(2);8(4);7(9);2(5)
            </Popover.Body>
          </Grid>
        </Popover>
      )}
    </Grid>
  );

  return (
    <Grid
      container
      justifyContent="center"
      display="flex"
      marginTop={2}
      marginBottom={45}
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
              Średnia ważona
            </Typography>
          </Grid>
          <Grid item width={1000} display="flex">
            <Grid item width={790} display="flex">
              <Grid item width={370}>
                <TextField
                  id="number"
                  fullWidth
                  placeholder="Wpisz liczbę..."
                  value={newNumbers.number ? newNumbers.number : ""}
                  onChange={(event) =>
                    setNewNumbers({
                      ...newNumbers,
                      number: event.target.value,
                    })
                  }
                  helperText={errors.numberError ? errors.numberError : ""}
                ></TextField>
              </Grid>
              <Grid item width={370} marginLeft={5}>
                <TextField
                  id="wage"
                  fullWidth
                  placeholder="Wpisz wagę liczby..."
                  value={newNumbers.wage ? newNumbers.wage : ""}
                  onChange={(event) =>
                    setNewNumbers({
                      ...newNumbers,
                      wage: event.target.value,
                    })
                  }
                  helperText={errors.wageError ? errors.wageError : ""}
                ></TextField>
              </Grid>
            </Grid>
            <Grid item marginLeft={2} marginTop={1}>
              <Button
                id="addNumber"
                style={{ background: "#33BCF2" }}
                fullWidth
                variant="contained"
                onClick={() => {
                  addNumbers();
                }}
              >
                Dodaj liczbę
              </Button>
            </Grid>
            <Grid display="flex">
              <Typography fontSize={36}>&nbsp;</Typography>
            </Grid>
          </Grid>
          <Grid item marginTop={2}>
            <Grid item display="flex">
              <Grid item>
                <Typography fontSize={16} color="#2C74B3" textAlign="left">
                  Twoje liczby
                </Typography>
              </Grid>
              <Grid item marginLeft={1} maxHeight={20}>
                <OverlayTrigger
                  trigger="click"
                  rootClose
                  placement="right"
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
            <Grid item display="flex">
              <Grid item>
                <TextareaAutosize
                  id="writtenNumbers"
                  value={
                    numbers.numbersWagesShow ? numbers.numbersWagesShow : ""
                  }
                  style={{ width: 780, resize: "vertical" }}
                  onChange={(event) =>
                    setNumbers({
                      ...numbers,
                      numbersWagesShow: event.target.value,
                    })
                  }
                />
                {errors.allNumbersError.length > 0 && (
                  <Typography
                    marginTop={0.3}
                    fontSize={12}
                    color="red"
                    textAlign="start"
                  >
                    &nbsp;&nbsp;&nbsp;&nbsp;{errors.allNumbersError}
                  </Typography>
                )}
              </Grid>
              <Grid item width={150} marginLeft={2}>
                <Button
                  id="clear"
                  fullWidth
                  style={{ background: "#FF876C" }}
                  variant="contained"
                  onClick={() => {
                    clearList();
                  }}
                >
                  Wyczyść
                </Button>
              </Grid>
            </Grid>
            <Grid item marginTop={2}>
              <Button
                id="solve"
                fullWidth
                variant="contained"
                style={{ background: "#4683E6" }}
                onClick={() => {
                  findWeightedAverage();
                }}
              >
                Oblicz
              </Button>
            </Grid>
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
            minRows={5}
            value={res.solution ? res.solution : ""}
            style={{ width: 1000, resize: "vertical", background: "#D8E8EE" }}
          />
        </Grid>
        <Grid item marginTop={9} width={1000}>
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
        <Grid item marginTop={3}>
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
                minRows={7}
                value={res.hint ? res.hint : ""}
                style={{
                  width: 1000,
                  resize: "vertical",
                  background: "#dcedc8",
                }}
              />
            </Grid>
          )}
        </Grid>
      </Grid>
    </Grid>
  );
};

export default WeightedAverage;
