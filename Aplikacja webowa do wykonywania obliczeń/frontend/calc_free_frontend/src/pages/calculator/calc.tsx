import React, { useEffect } from "react";
import { Grid, Typography, TextField } from "@mui/material";
import "./calc.css";
import { useState } from "react";
import MyButton from "./myButton";

const Calc = () => {
  const buttonAction = (buttonCode: string) => {
    let answer = "";
    let new_expr = "";
    let expr = expression.replaceAll(",", ".");
    expr = expr.replaceAll("%", "/100.0");
    let len = expression.length;
    if (buttonCode === "=") {
      try {
        let start_brackets = expression.split("(").length - 1;
        let end_brackets = expression.split(")").length - 1;
        for (let i = 0; i < start_brackets - end_brackets; i++) {
          expr = expr + ")";
        }
        answer = eval(expr);
        answer = answer.toString().replaceAll(".", ",");
      } catch (error) {
        answer = "Niepoprawny format";
      }
      setExpression(answer);
      setAnswer("");
    } else {
      let check = false;
      if (buttonCode === "/") {
        if (len > 0) {
          if (
            expression.charAt(len - 1) === ")" ||
            expression.charAt(len - 1) === "%" ||
            (expression.charAt(len - 1) >= "0" &&
              expression.charAt(len - 1) <= "9")
          ) {
            new_expr = expression + "/";
            setExpression(new_expr);
          } else if (
            (expression.charAt(len - 1) === "*" ||
              expression.charAt(len - 1) === "-" ||
              expression.charAt(len - 1) === "+") &&
            expression.charAt(len - 2) !== "("
          ) {
            let temp = expression.substring(0, len - 1);
            new_expr = temp + "/";

            setExpression(new_expr);
          }
        }
      } else if (buttonCode === "*") {
        if (len > 0) {
          if (
            expression.charAt(len - 1) === ")" ||
            expression.charAt(len - 1) === "%" ||
            (expression.charAt(len - 1) >= "0" &&
              expression.charAt(len - 1) <= "9")
          ) {
            new_expr = expression + "*";
            setExpression(new_expr);
          } else if (
            (expression.charAt(len - 1) === "/" ||
              expression.charAt(len - 1) === "-" ||
              expression.charAt(len - 1) === "+") &&
            expression.charAt(len - 2) !== "("
          ) {
            let temp = expression.substring(0, len - 1);
            new_expr = temp + "*";
            setExpression(new_expr);
          }
        }
      } else if (buttonCode === "-") {
        if (len > 0) {
          if (
            expression.charAt(len - 1) === ")" ||
            expression.charAt(len - 1) === "(" ||
            expression.charAt(len - 1) === "%" ||
            (expression.charAt(len - 1) >= "0" &&
              expression.charAt(len - 1) <= "9")
          ) {
            new_expr = expression + "-";
            setExpression(new_expr);
          } else if (
            (expression.charAt(len - 1) === "*" ||
              expression.charAt(len - 1) === "/" ||
              expression.charAt(len - 1) === "+") &&
            expression.charAt(len - 2) !== "("
          ) {
            let temp = expression.substring(0, len - 1);
            new_expr = temp + "-";
            setExpression(new_expr);
          }
        }
      } else if (buttonCode === "+") {
        if (len > 0) {
          if (
            expression.charAt(len - 1) === ")" ||
            expression.charAt(len - 1) === "(" ||
            expression.charAt(len - 1) === "%" ||
            (expression.charAt(len - 1) >= "0" &&
              expression.charAt(len - 1) <= "9")
          ) {
            new_expr = expression + "+";
            setExpression(new_expr);
          } else if (
            (expression.charAt(len - 1) === "*" ||
              expression.charAt(len - 1) === "-" ||
              expression.charAt(len - 1) === "/") &&
            expression.charAt(len - 2) !== "("
          ) {
            let temp = expression.substring(0, len - 1);
            new_expr = temp + "+";
            setExpression(new_expr);
          }
        }
      } else if (buttonCode === "%") {
        if (len > 0) {
          if (
            expression.charAt(len - 1) === ")" ||
            (expression.charAt(len - 1) >= "0" &&
              expression.charAt(len - 1) <= "9")
          ) {
            check = true;
            new_expr = expression + buttonCode;
            setExpression(new_expr);
          }
        }
      } else if (buttonCode === "C") {
        new_expr = "";
        setExpression(new_expr);
        setAnswer("");
      } else if (buttonCode === "()") {
        if (len === 0) {
          new_expr = expression + "(";
          setExpression(new_expr);
        } else {
          let start_brackets = expression.split("(").length - 1;
          let end_brackets = expression.split(")").length - 1;
          if (
            expression.charAt(len - 1) >= "0" &&
            expression.charAt(len - 1) <= "9" &&
            start_brackets > end_brackets
          ) {
            new_expr = expression + ")";
            setExpression(new_expr);
            check = true;
          } else if (
            expression.charAt(len - 1) === "-" ||
            expression.charAt(len - 1) === "+" ||
            expression.charAt(len - 1) === "*" ||
            expression.charAt(len - 1) === "/"
          ) {
            new_expr = expression + "(";
            setExpression(new_expr);
          } else if (
            expression.charAt(len - 1) === ")" &&
            start_brackets > end_brackets
          ) {
            new_expr = expression + ")";
            setExpression(new_expr);
            check = true;
          } else if (expression.charAt(len - 1) === "(") {
            new_expr = expression + "(";
            setExpression(new_expr);
          }
        }
      } else if (buttonCode === "+/-") {
        if (len === 0) {
          new_expr = "(-";
          setExpression(new_expr);
        } else if (
          len === 1 &&
          expression.charAt(0) >= "0" &&
          expression.charAt(0) <= "9"
        ) {
          new_expr = "(-" + expression.charAt(0);
          setExpression(new_expr);
          check = true;
        } else if (
          len === 2 &&
          expression.charAt(0) >= "0" &&
          expression.charAt(0) <= "9" &&
          expression.charAt(1) >= "0" &&
          expression.charAt(1) <= "9"
        ) {
          new_expr = "(-" + expression.charAt(0) + expression.charAt(1);
          setExpression(new_expr);
          check = true;
        } else if (
          len === 2 &&
          expression.charAt(0) === "(" &&
          expression.charAt(1) === "-"
        ) {
          new_expr = "";
          setExpression(new_expr);
        } else if (
          (len > 2 &&
            expression.charAt(len - 1) >= "0" &&
            expression.charAt(len - 1) <= "9") ||
          expression.charAt(len - 1) == ","
        ) {
          let temp = len - 2;
          while (
            (temp >= 0 &&
              expression.charAt(temp) >= "0" &&
              expression.charAt(temp) <= "9") ||
            expression.charAt(temp) == ","
          ) {
            temp--;
          }
          check = true;
          if (temp === -1) {
            new_expr = "(-" + expression;
            setExpression(new_expr);
          } else if (temp === 1) {
            if (expression.charAt(0) === "(" && expression.charAt(1) === "-") {
              new_expr = expression.substring(2, len);
              setExpression(new_expr);
            } else {
              new_expr =
                expression.substring(0, 2) +
                "(-" +
                expression.substring(2, len);
              setExpression(new_expr);
            }
          } else if (temp > 1) {
            if (
              expression.charAt(temp - 1) === "(" &&
              expression.charAt(temp) === "-"
            ) {
              new_expr =
                expression.substring(0, temp - 1) +
                expression.substring(temp + 1, len);
              setExpression(new_expr);
            } else {
              new_expr =
                expression.substring(0, temp + 1) +
                "(-" +
                expression.substring(temp + 1, len);
              setExpression(new_expr);
            }
          }
        } else if (
          len > 2 &&
          expression.charAt(len - 1) === "-" &&
          expression.charAt(len - 2) <= "("
        ) {
          check = true;
          new_expr = expression.substring(0, len - 2);
          setExpression(new_expr);
        } else if (
          expression.charAt(len - 1) === "-" ||
          expression.charAt(len - 1) === "+" ||
          expression.charAt(len - 1) === "*" ||
          expression.charAt(len - 1) === "/"
        ) {
          new_expr = expression + "(-";
          setExpression(new_expr);
        } else if (expression.charAt(len - 1) === "%") {
          new_expr = expression + "*(-";
          setExpression(new_expr);
        }
      } else if (buttonCode === ",") {
        if (
          len > 0 &&
          expression.charAt(len - 1) >= "0" &&
          expression.charAt(len - 1) <= "9"
        ) {
          let temp = len - 2;
          while (
            temp >= 0 &&
            expression.charAt(temp) >= "0" &&
            expression.charAt(temp) <= "9"
          ) {
            temp--;
          }
          if (temp === -1) {
            new_expr = expression + ",";
            setExpression(new_expr);
          } else if (expression.charAt(temp) !== ",") {
            new_expr = expression + ",";
            setExpression(new_expr);
          }
        }
      } else {
        if (
          expression.charAt(len - 1) !== ")" &&
          expression.charAt(len - 1) !== "%"
        ) {
          if (expression.charAt(len - 1) === "0") {
            if (buttonCode === "0") {
              let temp = len - 2;
              while (temp >= 0 && expression.charAt(temp) === "0") {
                temp--;
              }
              if (
                temp >= 0 &&
                expression.charAt(temp) >= "1" &&
                expression.charAt(temp) <= "9"
              ) {
                new_expr = expression + buttonCode;
                setExpression(new_expr);
                check = true;
              }
            } else {
              let temp = len - 2;
              while (temp >= 0 && expression.charAt(temp) === "0") {
                temp--;
              }
              if (
                temp >= 0 &&
                expression.charAt(temp) >= "1" &&
                expression.charAt(temp) <= "9"
              ) {
                new_expr = expression + buttonCode;
                setExpression(new_expr);
                check = true;
              } else {
                new_expr = expression.substring(0, len - 1) + buttonCode;
                setExpression(new_expr);
                check = true;
              }
            }
          } else {
            new_expr = expression + buttonCode;
            setExpression(new_expr);
            check = true;
          }
        }
      }
      if (check === true) {
        answer = "";
        let expr1 = new_expr.replaceAll(",", ".");
        expr1 = expr1.replaceAll("%", "/100.0");
        try {
          let start_brackets = new_expr.split("(").length - 1;
          let end_brackets = new_expr.split(")").length - 1;
          for (let i = 0; i < start_brackets - end_brackets; i++) {
            expr1 = expr1 + ")";
          }
          answer = eval(expr1);
          answer = answer.toString().replaceAll(".", ",");
        } catch (error) {
          answer = "Niepoprawny format";
        }
        setAnswer(answer);
      } else {
        setAnswer("");
      }
    }
  };

  const [expression, setExpression] = useState<string>("");
  const [answer, setAnswer] = useState<string>("");

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return (
    <Grid
      container
      justifyContent="center"
      display="flex"
      flexDirection="column"
      alignItems="center"
      minHeight={830}
    >
      <Grid item marginTop={2} justifyContent="center">
        <Typography fontSize={40} color="#3596FC" textAlign="center">
          Kalkulator
        </Typography>
      </Grid>
      <Grid
        id="all_calculator"
        item
        marginTop={7}
        width={750}
        height={546}
        display="flex"
        flexDirection="column"
        paddingX={2.5}
        paddingY={2.5}
      >
        <Grid item marginTop={1}>
          <TextField
            id="expression"
            fullWidth
            value={expression}
            InputProps={{
              sx: {
                "& input": {
                  textAlign: "end",
                  backgroundColor: "#f7edf0",
                  fontSize: 32,
                },
              },
              readOnly: true,
            }}
          ></TextField>
        </Grid>
        <Grid item marginTop={1}>
          <TextField
            id="answer"
            fullWidth
            value={answer}
            InputProps={{
              sx: {
                "& input": {
                  textAlign: "end",
                  backgroundColor: "#f7edf0",
                  fontSize: 20,
                  color: "#b0a8b9",
                },
              },
              readOnly: true,
            }}
          ></TextField>
        </Grid>
        <Grid item display="flex" flexDirection="row" marginTop={2}>
          <MyButton label="C" buttonAction={buttonAction}></MyButton>
          <MyButton label="()" buttonAction={buttonAction}></MyButton>
          <MyButton label="%" buttonAction={buttonAction}></MyButton>
          <MyButton label="/" buttonAction={buttonAction}></MyButton>
        </Grid>
        <Grid item display="flex" flexDirection="row">
          <MyButton label="7" buttonAction={buttonAction}></MyButton>
          <MyButton label="8" buttonAction={buttonAction}></MyButton>
          <MyButton label="9" buttonAction={buttonAction}></MyButton>
          <MyButton label="*" buttonAction={buttonAction}></MyButton>
        </Grid>
        <Grid item display="flex" flexDirection="row">
          <MyButton label="4" buttonAction={buttonAction}></MyButton>
          <MyButton label="5" buttonAction={buttonAction}></MyButton>
          <MyButton label="6" buttonAction={buttonAction}></MyButton>
          <MyButton label="-" buttonAction={buttonAction}></MyButton>
        </Grid>
        <Grid item display="flex" flexDirection="row">
          <MyButton label="1" buttonAction={buttonAction}></MyButton>
          <MyButton label="2" buttonAction={buttonAction}></MyButton>
          <MyButton label="3" buttonAction={buttonAction}></MyButton>
          <MyButton label="+" buttonAction={buttonAction}></MyButton>
        </Grid>
        <Grid item display="flex" flexDirection="row">
          <MyButton label="+/-" buttonAction={buttonAction}></MyButton>
          <MyButton label="0" buttonAction={buttonAction}></MyButton>
          <MyButton label="," buttonAction={buttonAction}></MyButton>
          <MyButton label="=" buttonAction={buttonAction}></MyButton>
        </Grid>
      </Grid>
    </Grid>
  );
};

export default Calc;
