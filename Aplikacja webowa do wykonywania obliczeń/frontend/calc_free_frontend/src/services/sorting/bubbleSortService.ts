import axios from "axios";
import { address } from "../address";

export interface Numbers {
  allNumbers: string;
  ascending: string;
}

class BubbleSortService {
  bubble_sort(numbers: Numbers) {
    return axios.get(`${address}/bubble-sort/`, {
      params: {
        numbers: numbers.allNumbers,
        ascending: numbers.ascending,
      },
    });
  }
}

export default new BubbleSortService();
