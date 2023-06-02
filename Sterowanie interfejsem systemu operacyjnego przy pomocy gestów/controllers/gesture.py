

class Gesture:

    def __init__(self, gesture_name, gesture_time, gesture_threshold, gesture_number):
        self.gesture_name = gesture_name
        self.gesture_time = gesture_time
        self.gesture_threshold = gesture_threshold
        self.gesture_number = gesture_number

    def get_gesture_name(self):
        return self.gesture_name

    def get_gesture_time(self):
        return self.gesture_time

    def get_gesture_threshold(self):
        return self.gesture_threshold

    def get_gesture_number(self):
        return self.gesture_number
