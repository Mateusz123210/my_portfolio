from controllers.gestures import Gestures
from controllers.mapping import Mapping
from keras.models import load_model
from keras.layers import Input
from keras.models import Model
from collections import deque
import numpy as np
import cv2
import time


class GestureRecognition():

    def __init__(self, function_getter, sys_controller, camera_controller):
        self.absolute_path = function_getter.get_absolute_path()
        self.position_to_gesture_index = {1: 0, 3: 1, 4: 2, 5: 3, 6: 4, 7: 5, 8: 6, 9: 7, 10: 8, 11: 9, 12: 10, 13: 11, 14: 12,
                                          15: 13, 16: 14, 17: 15, 18: 16, 19: 17, 20: 18, 21: 19, 22: 20, 23: 21, 24: 22, 25: 23, 26: 24}
        self.gestures_list = Gestures(self.absolute_path).get_gestures_list()
        self.recognize = True
        self.cam_controller = camera_controller
        self.gesture_map = Mapping(function_getter, sys_controller)
        self.initialize_recognition()
        self.gesture = None
        self.index = None

    def get_mapping(self):
        return self.gesture_map

    def stop_gesture_recognition(self):
        self.recognize = False

    def initialize_recognition(self):
        self.model = load_model(self.absolute_path +
                                '/trained_models/rgblstm.h5')
        self.model.summary()
        self.rgbinput = Input((150, 100, 3))
        self.x = self.model.layers[1].layer(self.rgbinput)
        for layer in self.model.layers[2:-3]:
            self.x = layer.layer(self.x)
        self.encoder = Model(inputs=self.rgbinput, outputs=self.x)
        self.encoder.summary()
        self.lstminput = Input((10, 1024))
        self.x = self.model.layers[-2](self.lstminput)
        self.x = self.model.layers[-1](self.x)
        self.lstm = Model(inputs=self.lstminput, outputs=self.x)
        self.lstm.summary()
        self.q = deque([np.zeros(1024) for i in range(10)])

    def start_gesture_recognition(self):
        self.recognize = True
        while True:
            if self.recognize is False:
                return
            ret, frame = self.cam_controller.get_camera_image()
            if ret is False:
                time.sleep(0.01)
                continue

            self.q.popleft()
            self.q.append(self.encoder.predict(
                np.array([cv2.resize(frame / 255., (100, 150))]))[0])
            our_values = self.lstm.predict(np.array([self.q]))

            position = 0
            max_value = -10.0
            for i in range(len(our_values[0])):
                if our_values[0][i] > max_value:
                    max_value = our_values[0][i]
                    position = i

            self.index = self.position_to_gesture_index.get(position)
            if self.index is not None:
                self.gesture = self.gestures_list[self.index]
                if max_value > self.gesture.get_gesture_threshold():
                    self.gesture_map.gesture_action(self.gesture)
            time.sleep(0.0001)
