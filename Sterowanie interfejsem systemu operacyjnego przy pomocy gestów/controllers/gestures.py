import json
from controllers.gesture import Gesture


class Gestures:

    def __init__(self, absolute_path):
        self.default_times = [3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.75, 3.25, 3.25, 3.25, 3.25, 3.75,
                              3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25]
        self.times = None
        try:
            with open(absolute_path + '/configuration/gesture_time_configuration.json') as json_file:
                self.times = json.load(json_file)
                self.times = [float(v) for v in self.times.values()]
                if len(self.times) != 25:
                    self.times = self.default_times
                for i in self.times:
                    if i <= 0:
                        self.times = self.default_times
                        break
        except Exception:
            self.times = self.default_times

        self.default_thresholds = [0.90, 0.90, 0.90, 0.90, 0.70, 0.72, 0.45, 0.50, 0.90, 0.50,
                                   0.50, 0.65, 0.65, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.60, 0.51, 0.90, 0.90, 0.90, 0.90]
        self.thresholds = None
        try:
            with open(absolute_path + '/configuration/recognition_threshold_configuration.json') as json_file:
                self.thresholds = json.load(json_file)
                self.thresholds = [float(v) for v in self.thresholds.values()]
                if len(self.thresholds) != 25:
                    self.thresholds = self.default_thresholds
                for i in self.thresholds:
                    if i <= 0 or i >= 1.5:
                        self.thresholds = self.default_thresholds
                        break
        except Exception:
            self.thresholds = self.default_thresholds

        self.gestures_list = []
        self.gestures_list.append(
            Gesture("Drumming fingers", self.times[0], self.thresholds[0], 1))
        self.gestures_list.append(
            Gesture("Pulling hand in", self.times[1], self.thresholds[1], 2))
        self.gestures_list.append(
            Gesture("Pulling two fingers in", self.times[2], self.thresholds[2], 3))
        self.gestures_list.append(
            Gesture("Pushing hand away", self.times[3], self.thresholds[3], 4))
        self.gestures_list.append(
            Gesture("Pushing two fingers away", self.times[4], self.thresholds[4], 5))
        self.gestures_list.append(
            Gesture("Rolling hand backward", self.times[5], self.thresholds[5], 6))
        self.gestures_list.append(
            Gesture("Rolling hand forward", self.times[6], self.thresholds[6], 7))
        self.gestures_list.append(
            Gesture("Shaking hand", self.times[7], self.thresholds[7], 8))
        self.gestures_list.append(
            Gesture("Sliding two fingers down", self.times[8], self.thresholds[8], 9))
        self.gestures_list.append(
            Gesture("Sliding two fingers left", self.times[9], self.thresholds[9], 10))
        self.gestures_list.append(
            Gesture("Sliding two fingers right", self.times[10], self.thresholds[10], 11))
        self.gestures_list.append(
            Gesture("Sliding two fingers up", self.times[11], self.thresholds[11], 12))
        self.gestures_list.append(
            Gesture("Stop sign", self.times[12], self.thresholds[12], 13))
        self.gestures_list.append(
            Gesture("Swiping down", self.times[13], self.thresholds[13], 14))
        self.gestures_list.append(
            Gesture("Swiping left", self.times[14], self.thresholds[14], 15))
        self.gestures_list.append(
            Gesture("Swiping right", self.times[15], self.thresholds[15], 16))
        self.gestures_list.append(
            Gesture("Swiping up", self.times[16], self.thresholds[16], 17))
        self.gestures_list.append(
            Gesture("Thumb down", self.times[17], self.thresholds[17], 18))
        self.gestures_list.append(
            Gesture("Thumb up", self.times[18], self.thresholds[18], 19))
        self.gestures_list.append(
            Gesture("Turning hand clockwise", self.times[19], self.thresholds[19], 20))
        self.gestures_list.append(Gesture(
            "Turning hand counterclockwise", self.times[20], self.thresholds[20], 21))
        self.gestures_list.append(
            Gesture("Zooming in with full hand", self.times[21], self.thresholds[21], 22))
        self.gestures_list.append(
            Gesture("Zooming in with two fingers", self.times[22], self.thresholds[22], 23))
        self.gestures_list.append(
            Gesture("Zooming out with full hand", self.times[23], self.thresholds[23], 24))
        self.gestures_list.append(Gesture(
            "Zooming out with two fingers", self.times[24], self.thresholds[24], 25))

    def get_gestures_list(self):
        return self.gestures_list
