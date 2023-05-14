from controllers.gesture_name_mapper import NameMapper
import json
from win10toast import ToastNotifier as tn
import threading
from threading import Lock
import time
from window_app.action_name_mapper import ActionNameMapper
from controllers.gesture_timer import GestureTimer as gt


class Mapping():

    def __init__(self, func_getter, sys_controller):
        self.absolute_path = func_getter.get_absolute_path()
        self.nm = ActionNameMapper()
        self.gesture = {}
        self.end = False
        self.name_mapper = NameMapper()
        self.read_configuration_from_file()
        self.controller = sys_controller
        self.function_getter = func_getter
        self.function_getter.set_mapping_reference(self)
        self.mutex = Lock()
        temp =  self.function_getter.get_all_functions_names()
        for a in self.gesture.values():
            if not a in temp:
                self.read_default_configuration_from_file()
                break
        self.toaster = tn()
        self.message = 1
        self.new_message = False
        self.new_mouse_message = False
        self.message_mutex = Lock()
        self.time_before = time.time()
        self.time_now = self.time_before
        self.gesture_timer = gt(self.absolute_path)
        self.last_gesture_number = -1
        self.notifications_enabled = False
        t = threading.Thread(name='daemon',target=self.show_message)
        t.start()

    def end_thread(self):
        self.end = True

    def get_gestures_list(self):
        self.mutex.acquire()
        dict = {**self.gesture}
        self.mutex.release()
        return dict

    def save_configuration_to_file(self):
        with open(self.absolute_path + '/configuration/user_configuration.json', 'w') as outfile:
            json.dump(self.gesture, outfile)

    def read_configuration_from_file(self):
        with open(self.absolute_path + '/configuration/user_configuration.json') as json_file:
            data = json.load(json_file)
            self.gesture = {int(k): v for (k, v) in data.items()}

    def read_default_configuration_from_file(self):
        self.mutex.acquire()
        with open(self.absolute_path + '/configuration/default_configuration.json') as json_file:
            data = json.load(json_file)
            self.gesture.clear()
            self.gesture = {int(k): v for (k, v) in data.items()}
        self.mutex.release()
        try:
            self.save_configuration_to_file()
        except:
            pass

    def set_mouse_end_message(self):
        self.message_mutex.acquire()
        self.new_mouse_message = True
        self.message_mutex.release()

    def set_notifications_enabled(self,value: bool):
        if value is True:
            self.message_mutex.acquire()
            self.new_mouse_message = False
            self.new_message = False
            self.message_mutex.release()
        self.notifications_enabled = value

    def show_message(self):
        temp_logo = self.absolute_path + '/logo1.ico'
        while self.end is False:
            if self.notifications_enabled is True:
                self.message_mutex.acquire()                
                if self.new_mouse_message is True:
                    self.new_mouse_message = False
                    self.toaster.show_toast("Gesture detected",
                                            "Action name: mouse stop\n",
                                            duration=1.7, icon_path=temp_logo, threaded=True)
                elif self.new_message is True:
                    self.toaster.show_toast("Gesture detected",
                                            "Gesture name: " + self.name_mapper.get_gesture_name(self.message) + "\n"
                                            + "Action name: " + self.nm.get_user_friendly_action_name(
                                                str(self.gesture.get(self.message))),
                               duration=1.7, icon_path=temp_logo, threaded=True)
                    self.new_message = False
                self.message_mutex.release()
            time.sleep(0.02)

    def get_gesture(self, number: int):
        self.mutex.acquire()
        for key in self.gesture.keys():
            if key == number:
                self.mutex.release()
                return True
        self.mutex.release()
        return False

    def set_gesture(self,gesture_action: dict):
        self.mutex.acquire()
        self.gesture = {**gesture_action}
        try:
            self.save_configuration_to_file()
        except:
            pass
        self.mutex.release()

    def set_time_before(self):
        self.time_before = time.time()

    def gesture_action(self, number):
        self.time_now = time.time()
        if self.last_gesture_number == -1 or self.time_now - self.time_before > \
                self.gesture_timer.get_time(self.last_gesture_number):
            self.last_gesture_number = number
            self.time_before = time.time()
            self.message_mutex.acquire()
            self.new_message = True
            self.message = number
            function = self.gesture.get(number)
            self.message_mutex.release()
            if self.get_gesture(number)  == True:
                return self.function_getter.call_function(function)
            else:
                return False
        else:
            return False