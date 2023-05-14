import json


class GestureTimer():
    
    def __init__(self, absolute_path):
        self.default_times = [3.96 , 3.79 , 4.57, 4.22, 3.92, 4.06, 4.06, 4.23, 2.90, 3.74, 4.07, 4.10, 3.95, 3.84, 3.50, 3.57,
                               4.10, 4.02, 3.39, 3.77, 3.97, 4.26, 4.28, 3.99, 3.75]
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

    def get_time(self, number: int):
        return self.times[number - 1]