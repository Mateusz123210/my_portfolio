import React, { useEffect } from "react";
import { useState } from "react";
import {
  Grid,
  TextField,
  TextareaAutosize,
  Button,
  Typography,
  IconButton,
  Checkbox,
  FormControlLabel,
} from "@mui/material";
import Validator from "../../validators/validator";
import QuickSortService from "../../services/sorting/quickSortService";
import { OverlayTrigger, Popover } from "react-bootstrap";
import InfoIcon from "@mui/icons-material/Info";

export interface Numbers {
  allNumbers: string;
  ascending: string;
}

export interface NewNumbers {
  newWrittenNumbers: string;
}

export interface Distance {
  solution: string;
  hint: string;
}

export interface NumberError {
  numbersError: string;
}

const QuickSort = () => {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  const [numbers, setNumbers] = useState<Numbers>({
    allNumbers: "",
    ascending: "yes",
  });
  const [newNumbers, setNewNumbers] = useState<NewNumbers>({
    newWrittenNumbers: "",
  });
  const [res, setRes] = useState<Distance>({
    solution: "",
    hint: "",
  });

  const [errors, setErrors] = useState<NumberError>({
    numbersError: "",
  });

  const [hint, setHint] = useState<boolean>(false);

  const [checked, setChecked] = useState<boolean>(true);

  const showOrHideHint = () => {
    setHint(!hint);
  };

  const [pop, setPop] = useState<boolean>(false);

  const setPopover = (val: boolean) => {
    setPop(val);
  };

  const addNumbers = () => {
    let newErrorState = { ...errors };
    newErrorState.numbersError = "";
    let valid = true;
    if (!Validator.checkIfIsNotEmpty(newNumbers.newWrittenNumbers)) {
      newErrorState.numbersError = Validator.notNumbersMessage;
      valid = false;
    } else if (
      !Validator.checkIfIsValidListOfNumbers(newNumbers.newWrittenNumbers)
    ) {
      newErrorState.numbersError = Validator.notValidListOfNumbersMessage;
      valid = false;
    }
    setErrors(newErrorState);
    if (valid === true) {
      let temp = numbers.allNumbers;
      if (temp.length > 0) {
        temp = temp + ";" + newNumbers.newWrittenNumbers;
        if (temp.split(";").length <= 30) {
          setNumbers({ ...numbers, allNumbers: temp });
          setNewNumbers({ ...newNumbers, newWrittenNumbers: "" });
        } else {
          let newErrorState = { ...errors };
          newErrorState.numbersError = "Zbyt dużo liczb";
          setErrors(newErrorState);
        }
      } else {
        if (newNumbers.newWrittenNumbers.split(";").length <= 30) {
          setNumbers({ ...numbers, allNumbers: newNumbers.newWrittenNumbers });
          setNewNumbers({ ...newNumbers, newWrittenNumbers: "" });
        } else {
          let newErrorState = { ...errors };
          newErrorState.numbersError = "Zbyt dużo liczb";
          setErrors(newErrorState);
        }
      }
    }
  };

  const quick_sort = () => {
    if (numbers.allNumbers && numbers.allNumbers.length > 0) {
      QuickSortService.quick_sort(numbers)
        .then((response) => {
          setRes(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    } else {
      setErrors({ ...errors, numbersError: "Dodaj liczby najpierw" });
    }
  };

  const clearList = () => {
    setNumbers({ ...numbers, allNumbers: "" });
  };

  const handleCheckboxChange = () => {
    if (checked === true) {
      setNumbers({ ...numbers, ascending: "no" });
      setChecked(false);
    } else {
      setNumbers({ ...numbers, ascending: "yes" });
      setChecked(true);
    }
  };

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
          <Popover.Header as="h3" color="#cccccc">
            Jak dodać liczby?
          </Popover.Header>
          <Popover.Body id="popoverBody">
            Liczby należy wpisywać, rozdzielając je
            <br />
            średnikiem. Liczby te pojawią się w polu
            <br />
            "Twoje liczby". Maksymalnie można dodać 30 liczb.
            <br />
            Aby posortować liczby, należy kliknąć
            <br />
            przycisk "Sortuj". Przykładowe listy liczb:
            <br />
            5;7;9;12;15,25
            <br />
            3,5;4;7;8;12
            <br />
            -6
            <br />
            5,5;6;3;4
          </Popover.Body>
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
              Sortowanie szybkie (quicksort)
            </Typography>
          </Grid>
          <Grid item width={1000} display="flex">
            <Grid item width={790}>
              <TextField
                id="numbers"
                fullWidth
                placeholder="Wpisz liczby.."
                value={
                  newNumbers.newWrittenNumbers
                    ? newNumbers.newWrittenNumbers
                    : ""
                }
                onChange={(event) =>
                  setNewNumbers({
                    ...newNumbers,
                    newWrittenNumbers: event.target.value,
                  })
                }
                helperText={errors.numbersError ? errors.numbersError : ""}
              ></TextField>
            </Grid>
            <Grid item width={150} marginLeft={2} marginTop={1}>
              <Button
                id="addNumbers"
                fullWidth
                variant="contained"
                style={{ background: "#33BCF2" }}
                onClick={() => {
                  addNumbers();
                }}
              >
                Dodaj liczby
              </Button>
            </Grid>
            <Grid display="flex">
              <Typography fontSize={36}>&nbsp;</Typography>
              <OverlayTrigger
                trigger="click"
                rootClose
                placement="left"
                overlay={popover}
              >
                <IconButton
                  id="popoverButton"
                  onClick={() => {
                    setPopover(true);
                  }}
                >
                  <InfoIcon />
                </IconButton>
              </OverlayTrigger>
            </Grid>
          </Grid>
          <Grid item marginTop={2}>
            <Grid item>
              <Typography fontSize={16} color="#2C74B3" textAlign="left">
                Twoje liczby
              </Typography>
            </Grid>
            <Grid item display="flex">
              <Grid item>
                <TextareaAutosize
                  id="writtenNumbers"
                  readOnly={true}
                  value={numbers.allNumbers ? numbers.allNumbers : ""}
                  style={{ width: 780, resize: "vertical" }}
                />
              </Grid>
              <Grid item width={150} marginLeft={2}>
                <Button
                  id="clear"
                  fullWidth
                  variant="contained"
                  style={{ background: "#FF876C" }}
                  onClick={() => {
                    clearList();
                  }}
                >
                  Wyczyść
                </Button>
              </Grid>
            </Grid>
            <Grid item>
              <FormControlLabel
                control={
                  <Checkbox checked={checked} onChange={handleCheckboxChange} />
                }
                label="Niemalejąco"
              />
            </Grid>
            <Grid item marginTop={2}>
              <Button
                id="sort"
                fullWidth
                variant="contained"
                style={{ background: "#4683E6" }}
                onClick={() => {
                  quick_sort();
                }}
              >
                Sortuj
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
                minRows={7}
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

export default QuickSort;
