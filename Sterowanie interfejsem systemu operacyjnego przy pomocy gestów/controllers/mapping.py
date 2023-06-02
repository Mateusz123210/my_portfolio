import json
import threading
from threading import Lock
import time
from windows_toasts import WindowsToaster, ToastDuration, ToastAudio, AudioSource, \
    ToastDisplayImage, ToastImageAndText4, ToastScenario


class Mapping():

    def __init__(self, func_getter, sys_controller):
        self.absolute_path = func_getter.get_absolute_path()
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
        self.message_first_line = ""
        self.message_second_line = ""
        self.new_message = False
        self.message_mutex = Lock()
        self.time_before = time.time()
        self.time_now = self.time_before
        self.last_gesture = None
        self.notifications_enabled = False
        t = threading.Thread(name='daemon', target=self.show_message)
        t.start()

    def end_thread(self):
        self.end = True

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

    def set_mouse_end_message(self):
        self.message_mutex.acquire()
        self.message_first_line = "Action name: mouse stop"
        self.message_second_line = ""
        self.new_message = True
        self.message_mutex.release()

    def set_notifications_enabled(self, value: bool):
        if value is True:
            self.message_mutex.acquire()
            self.new_mouse_message = False
            self.new_message = False
            self.message_mutex.release()
        self.notifications_enabled = value

    def show_message(self):
        self.toaster = WindowsToaster('Handy')
        self.newToast = ToastImageAndText4()
        self.newToast.SetGroup("Handy")
        self.newToast.SetHeadline("Gesture detected")
        self.newToast.AddImage(ToastDisplayImage.fromPath(self.absolute_path + '/logo1.ico', large=False,
                                                          circleCrop=False))
        self.newToast.SetAudio(ToastAudio(
            AudioSource.Default, looping=False, silent=True))
        self.newToast.SetDuration(ToastDuration.Short)
        self.newToast.SetScenario(ToastScenario.Alarm)
        while self.end is False:
            if self.notifications_enabled is True:
                self.message_mutex.acquire()
                if self.new_message is True:
                    self.newToast.SetFirstLine(self.message_first_line)
                    self.newToast.SetSecondLine(self.message_second_line)
                    self.toaster.show_toast(self.newToast)
                    self.new_message = False
                self.message_mutex.release()
            time.sleep(0.03)

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

    def set_time_before(self):
        self.time_before = time.time()

    def gesture_action(self, recognized_gesture):
        self.time_now = time.time()
        if self.last_gesture == None or self.time_now - self.time_before > \
                self.last_gesture.get_gesture_time():
            self.last_gesture = recognized_gesture
            self.time_before = time.time()
            gesture_number = recognized_gesture.get_gesture_number()
            self.message_mutex.acquire()
            self.new_message = True
            self.message_first_line = "Gesture name: " + \
                recognized_gesture.get_gesture_name()
            self.message_second_line = "Action name: " + \
                str(self.gesture.get(gesture_number))
            self.message_mutex.release()
            function = self.gesture.get(gesture_number)
            if self.get_gesture(gesture_number) == True:
                self.function_getter.call_function(function)
