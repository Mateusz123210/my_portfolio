import axios from "axios";
import { address } from "../address";

export interface TriangleSides {
  firstSide: string;
  secondSide: string;
  hypotenuse: string;
}

class TriangleService {
  solveTriangle(triangleSides: TriangleSides) {
    return axios.get(`${address}/triangle/`, {
      params: {
        ...(triangleSides.firstSide.length > 0
          ? { firstSide: triangleSides.firstSide }
          : {}),
        ...(triangleSides.secondSide.length > 0
          ? { secondSide: triangleSides.secondSide }
          : {}),
        ...(triangleSides.hypotenuse.length > 0
          ? { hypotenuse: triangleSides.hypotenuse }
          : {}),
      },
    });
  }
}

export default new TriangleService();
