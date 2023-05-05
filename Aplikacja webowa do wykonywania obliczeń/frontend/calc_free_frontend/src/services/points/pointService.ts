import axios from "axios";
import { address } from "../address";

export interface Point {
  x1: string;
  y1: string;
  x2: string;
  y2: string;
}

class PointService {
  findDistanceBetweenPoints(point: Point) {
    return axios.get(`${address}/points-distance/`, {
      params: {
        firstPoint: point.x1.trimStart() + ";" + point.y1.trimStart(),
        secondPoint: point.x2.trimStart() + ";" + point.y2.trimStart(),
      },
    });
  }
}

export default new PointService();
