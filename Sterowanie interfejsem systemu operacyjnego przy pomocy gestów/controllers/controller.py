import sys
sys.path.insert(0, "..")
from gesture_library.gesture_recognition import GestureRecognition
from controllers.camera_controller import CameraController
import threading
from threading import Lock


class Controller():

    def __init__(self, function_getter, sys_controller, win):
        self.mutex = Lock()
        self.win = win
        self.camera_controller = CameraController(win)
        self.system_controller = sys_controller
        self.gesture_recognition = GestureRecognition(function_getter, sys_controller, self.camera_controller)
        self.started = False

    def get_gesture_recognition(self):
        return self.gesture_recognition

    def start_stop_gesture_recognition(self):
        self.mutex.acquire()
        if self.started is False:
            self.t = threading.Thread(name='daemon', target=self.gesture_recognition.start_gesture_recognition)
            self.t.start()
            self.win.set_button_to_stop_mode()
            self.started = True
        else:
            self.system_controller.stop_mouse()
            self.gesture_recognition.stop_gesture_recognition()
            self.t.join()
            self.win.set_button_to_start_mode()
            self.started = False
        self.mutex.release()
    
    def stop_app(self):
        self.mutex.acquire()
        if self.started is True:
            self.system_controller.stop_mouse()
            self.gesture_recognition.stop_gesture_recognition()
            self.t.join()
            self.win.set_button_to_start_mode()
            self.started = False
        self.mutex.release()

    def get_camera_controller(self):
        return self.camera_controller