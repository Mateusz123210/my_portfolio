import axios from "axios";
import { address } from "../address";

export interface Numbers {
  allNumbers: string;
  allWages: string;
}

class WeightedAverageService {
  findWeightedAverage(numbers: Numbers) {
    return axios.get(`${address}/weighted-average/`, {
      params: {
        numbers: numbers.allNumbers,
        wages: numbers.allWages,
      },
    });
  }
}

export default new WeightedAverageService();
