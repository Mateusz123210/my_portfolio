import json
from threading import Lock
import time


class Mapping():

    def __init__(self, func_getter, sys_controller, win_reference):
        self.absolute_path = func_getter.get_absolute_path()
        self.win_reference = win_reference
        self.default_gestures_config = {1: "switch window", 2: "escape", 3: "preview of opened windows", 4: "minimize all windows", 5: "space", 6: "page down", 7: "page up", 8: "open action center", 9: "brightness down", 10: "volume down", 11: "volume up", 12: "brightness up",
                                        13: "close window", 14: "scroll down", 15: "scroll left", 16: "scroll right", 17: "scroll up", 18: "screen keyboard", 19: "mouse start", 20: "window right", 21: "window left", 22: "maximize window", 23: "zoom in", 24: "minimize window", 25: "zoom out"}
        self.gesture = {}
        self.end = False
        self.mutex = Lock()
        self.read_configuration_from_file()
        self.controller = sys_controller
        self.function_getter = func_getter
        self.function_getter.set_mapping_reference(self)
        temp = self.function_getter.get_all_functions_names()

        if len(self.gesture) != 25:
            self.gesture = self.default_gestures_config
        else:
            for a in self.gesture.values():
                if not a in temp:
                    self.set_default_config()
                    break
        self.time_before = time.time()
        self.time_now = self.time_before
        self.last_gesture = None

    def get_gestures_list(self):
        self.mutex.acquire()
        dict = {**self.gesture}
        self.mutex.release()
        return dict

    def save_configuration_to_file(self):
        try:
            with open(self.absolute_path + '/configuration/user_configuration.json', 'w') as outfile:
                json.dump(self.gesture, outfile)
        except Exception:
            pass

    def read_configuration_from_file(self):
        self.mutex.acquire()
        try:
            with open(self.absolute_path + '/configuration/user_configuration.json') as json_file:
                data = json.load(json_file)
                self.gesture = {int(k): v for (k, v) in data.items()}
        except Exception:
            self.gesture = self.default_gesture_config
        self.mutex.release()

    def set_default_config(self):
        self.mutex.acquire()
        self.gesture = self.default_gestures_config
        self.mutex.release()
        try:
            self.save_configuration_to_file()
        except:
            pass

    def get_gesture(self, number: int):
        self.mutex.acquire()
        for key in self.gesture.keys():
            if key == number:
                self.mutex.release()
                return True
        self.mutex.release()
        return False

    def set_gesture(self, gesture_action: dict):
        self.mutex.acquire()
        self.gesture = {**gesture_action}
        try:
            self.save_configuration_to_file()
        except:
            pass
        self.mutex.release()

    def set_gestures_without_saving_to_file(self, gesture_action: dict):
        self.mutex.acquire()
        self.gesture = {**gesture_action}
        self.mutex.release()

    def set_time_before(self):
        self.time_before = time.time()

    def reset_last_gesture(self):
        self.last_gesture = None

    def gesture_action(self, recognized_gesture):
        self.time_now = time.time()
        if self.last_gesture == None or self.time_now - self.time_before > self.last_gesture.get_gesture_time():
            self.last_gesture = recognized_gesture
            self.time_before = time.time()
            gesture_number = recognized_gesture.get_gesture_number()
            function = self.gesture.get(gesture_number)
            recognition_message = '''<span style="color:black;">Gesture name<br /></span><span style="color:green;">'''
            recognition_message += recognized_gesture.get_gesture_name()
            recognition_message += '''<br /></span><span style="color:black;">Action name<br /></span><span style="color:green;">'''
            recognition_message += str(self.gesture.get(gesture_number))
            recognition_message += '''<br /></span>'''
            self.win_reference.set_gesture_recognized(
                True, recognition_message)
            if self.get_gesture(gesture_number) == True:
                self.function_getter.call_function(function)
