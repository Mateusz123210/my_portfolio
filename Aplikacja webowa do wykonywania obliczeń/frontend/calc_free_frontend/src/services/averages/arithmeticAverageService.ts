import axios from "axios";
import { address } from "../address";

export interface Numbers {
  allNumbers: string;
}

class ArithmeticAverageService {
  findArithmeticAverage(numbers: Numbers) {
    return axios.get(`${address}/arithmetic-average/`, {
      params: {
        numbers: numbers.allNumbers,
      },
    });
  }
}

export default new ArithmeticAverageService();
