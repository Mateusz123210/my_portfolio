import axios from "axios";
import { address } from "../address";

export interface LinearEquation {
  equation: string;
}

class LinearEquationService {
  private url1 = `https://calcfree.azurewebsites.net`;
  solveLinearEquation(linearEquation: LinearEquation) {
    return axios.get(`${address}/linear-equation/`, {
      params: {
        equation: linearEquation.equation,
      },
    });
  }
}

export default new LinearEquationService();
