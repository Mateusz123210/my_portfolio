import axios from "axios";
import { address } from "../address";

export interface Numbers {
  allNumbers: string;
  ascending: string;
}

class QuickSortService {
  quick_sort(numbers: Numbers) {
    return axios.get(`${address}/quick-sort/`, {
      params: {
        numbers: numbers.allNumbers,
        ascending: numbers.ascending,
      },
    });
  }
}

export default new QuickSortService();
