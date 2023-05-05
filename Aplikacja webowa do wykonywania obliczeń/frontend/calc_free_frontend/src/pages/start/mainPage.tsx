import React from "react";
import { Grid } from "@mui/material";
import PageElement from "./pageElement";
import ExampleLinear from "../../assets/example_linear.png";
import ExampleSquare from "../../assets/example_square.png";
import ExampleDistance from "../../assets/example_distance.png";
import ExampleCalculator from "../../assets/example_calculator.png";
import ExampleArithmeticAverage from "../../assets/example_arithmetic_average.png";
import ExampleWeightedAverage from "../../assets/example_weighted_average.png";
import ExampleBubbleSort from "../../assets/example_bubble_sort.png";
import ExampleQuickSort from "../../assets/example_quick_sort.png";
import ExampleTriangle from "../../assets/example_triangle.png";

const MainPage = () => {
  return (
    <Grid
      container
      alignItems="center"
      display="flex"
      flexDirection="column"
      marginTop={2}
    >
      <Grid
        item
        justifyContent="center"
        alignItems="center"
        display="flex"
        flexDirection="row"
      >
        <PageElement
          id="linearEquation"
          image={ExampleLinear}
          label="Rysunek"
          pageName="Równanie liniowe"
          navigateDirection="/linear-equation"
        />
        <PageElement
          id="squareEquation"
          image={ExampleSquare}
          label="Rysunek"
          pageName="Równanie kwadratowe"
          navigateDirection="/square-equation"
        />
        <PageElement
          id="calculator"
          image={ExampleCalculator}
          label="Rysunek"
          pageName="Kalkulator"
          navigateDirection="/calculator"
        />
      </Grid>
      <Grid
        item
        justifyContent="center"
        alignItems="center"
        display="flex"
        flexDirection="row"
      >
        <PageElement
          id="arithmeticAverage"
          image={ExampleArithmeticAverage}
          label="Rysunek"
          pageName="Średnia arytmetyczna"
          navigateDirection="/arithmetic-average"
        />
        <PageElement
          id="weightedAverage"
          image={ExampleWeightedAverage}
          label="Rysunek"
          pageName="Średnia ważona"
          navigateDirection="/weighted-average"
        />
        <PageElement
          id="bubbleSort"
          image={ExampleBubbleSort}
          label="Rysunek"
          pageName="Sortowanie bąbelkowe"
          navigateDirection="/bubble-sort"
        />
      </Grid>
      <Grid
        item
        justifyContent="center"
        alignItems="center"
        display="flex"
        flexDirection="row"
      >
        <PageElement
          id="quickSort"
          image={ExampleQuickSort}
          label="Rysunek"
          pageName="Sortowanie szybkie"
          navigateDirection="/quick-sort"
        />
        <PageElement
          id="pointsDistance"
          image={ExampleDistance}
          label="Rysunek"
          pageName="Odległość między punktami"
          navigateDirection="/points-distance"
        />
        <PageElement
          id="triangleCalculations"
          image={ExampleTriangle}
          label="Rysunek"
          pageName="Boki i kąty trójkąta prostokątnego"
          navigateDirection="/triangle-calculations"
        />
      </Grid>
    </Grid>
  );
};

export default MainPage;
