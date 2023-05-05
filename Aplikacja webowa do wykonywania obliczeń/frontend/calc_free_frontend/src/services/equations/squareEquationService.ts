import axios from "axios";
import { address } from "../address";

export interface SquareEquation {
  equation: string;
}

class SquareEquationService {
  solveSquareEquation(squareEquation: SquareEquation) {
    return axios.get(`${address}/square-equation/`, {
      params: {
        equation: squareEquation.equation,
      },
    });
  }
}

export default new SquareEquationService();
