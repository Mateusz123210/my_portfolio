import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import MainPage from "./pages/start/mainPage";
import SquareEquation from "./pages/equations/squareEquation";
import LinearEquation from "./pages/equations/linearEquation";
import ArithmeticAverage from "./pages/averages/arithmeticAverage";
import WeightedAverage from "./pages/averages/weightedAverage";
import PointsDistance from "./pages/points/pointsDistance";
import BubbleSort from "./pages/sorting/bubbleSort";
import QuickSort from "./pages/sorting/quicksort";
import Calc from "./pages/calculator/calc";
import TriangleCalculations from "./pages/triangle/triangle";
import { createTheme, Grid, ThemeProvider } from "@mui/material";
import AppBar from "./pages/appBar/appBar";
import Footer from "./pages/footer/footer";
import NotFoundPage from "./notFoundPage";

import { useState, useEffect } from "react";

const getWindowDimensions = () => {
  const { innerWidth: width, innerHeight: height } = window;
  return {
    width,
    height,
  };
};

const useWindowDimensions = () => {
  const [windowDimensions, setWindowDimensions] = useState(
    getWindowDimensions()
  );

  useEffect(() => {
    function handleResize() {
      setWindowDimensions(getWindowDimensions());
    }

    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  return windowDimensions;
};

const theme = createTheme({
  components: {
    MuiFormHelperText: {
      styleOverrides: {
        root: {
          color: "red",
        },
      },
    },
  },
});

function App() {
  let a = useWindowDimensions();
  return (
    <React.StrictMode>
      <BrowserRouter>
        <ThemeProvider theme={theme}>
          <Grid
            container
            width={a.width > 1200 ? a.width : 1200}
            justifyContent="center"
            alignItems="center"
          >
            <Grid
              item
              height="100%"
              width={a.width > 1200 ? a.width : 1200}
              justifyContent="center"
              alignItems="center"
            >
              <AppBar />
              <Routes>
                <Route path="/" element={<MainPage />} />
                <Route path="/square-equation" element={<SquareEquation />} />
                <Route path="/linear-equation" element={<LinearEquation />} />
                <Route
                  path="/arithmetic-average"
                  element={<ArithmeticAverage />}
                />
                <Route path="/weighted-average" element={<WeightedAverage />} />
                <Route path="/points-distance" element={<PointsDistance />} />
                <Route path="/bubble-sort" element={<BubbleSort />} />
                <Route path="/quick-sort" element={<QuickSort />} />
                <Route path="/calculator" element={<Calc />} />
                <Route
                  path="/triangle-calculations"
                  element={<TriangleCalculations />}
                />
                <Route path="/*" element={<NotFoundPage />} />
              </Routes>
            </Grid>
            <Footer width={a.width > 1200 ? a.width : 1200} />
          </Grid>
        </ThemeProvider>
      </BrowserRouter>
    </React.StrictMode>
  );
}

export default App;
