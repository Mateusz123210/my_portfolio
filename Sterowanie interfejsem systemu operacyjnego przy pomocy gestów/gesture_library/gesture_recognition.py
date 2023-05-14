from keras.layers import Input
from keras.models import Model
from collections import deque
import numpy as np
import cv2
import time
import sys
import json
sys.path.insert(0,"..")
from controllers.mapping import Mapping
from gesture_library.models import ModelFactory


class GestureRecognition():

    def __init__(self, function_getter, sys_controller, camera_controller):
        self.absolute_path = function_getter.get_absolute_path()
        self.default_thresholds = [0.90 , 0.90 , 0.90, 0.90, 0.70, 0.72, 0.45, 0.50, 0.90, 0.50, 0.50, 0.65, 0.65, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.60
                      , 0.60, 0.90, 0.90, 0.90, 0.90]
        self.thresholds = None
        try:
            with open(self.absolute_path + '/configuration/recognition_threshold_configuration.json') as json_file:
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
        self.recognize = True
        self.cam_controller = camera_controller
        self.gesture_map = Mapping(function_getter, sys_controller)
        self.initialize_recognition()

    def get_mapping(self):
        return self.gesture_map
    
    def stop_gesture_recognition(self):
        self.recognize = False

    def initialize_recognition(self):
        self.model = ModelFactory(self.absolute_path).getModel()
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
        self.lstm = Model(inputs = self.lstminput, outputs = self.x)
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
            self.q.append(self.encoder.predict(np.array([cv2.resize(frame / 255., (100, 150))]))[0])
            our_values = self.lstm.predict(np.array([self.q]))

            position = 0
            max_value = -10.0
            for i in range(len(our_values[0])):
                if our_values[0][i] > max_value:
                    max_value = our_values[0][i]
                    position = i
            
            if max_value > self.thresholds[0] and position == 1:
                self.gesture_map.gesture_action(1)
            elif max_value > self.thresholds[1] and position == 3:
                self.gesture_map.gesture_action(2)
            elif max_value > self.thresholds[2] and position == 4:
                self.gesture_map.gesture_action(3)
            elif max_value > self.thresholds[3] and position == 5:
                self.gesture_map.gesture_action(4)
            elif max_value > self.thresholds[4] and position == 6:
                self.gesture_map.gesture_action(5)
            elif max_value > self.thresholds[5] and position == 7:
                self.gesture_map.gesture_action(6)
            elif max_value > self.thresholds[6] and position == 8:
                self.gesture_map.gesture_action(7)
            elif max_value > self.thresholds[7] and position == 9:
                self.gesture_map.gesture_action(8)
            elif max_value > self.thresholds[8] and position == 10:
                self.gesture_map.gesture_action(9)
            elif max_value > self.thresholds[9] and position == 11:
                self.gesture_map.gesture_action(10)
            elif max_value > self.thresholds[10] and position == 12:
                self.gesture_map.gesture_action(11)
            elif max_value > self.thresholds[11] and position == 13:
                self.gesture_map.gesture_action(12)
            elif max_value > self.thresholds[12] and position == 14:
                self.gesture_map.gesture_action(13)
            elif max_value > self.thresholds[13] and position == 15:
                self.gesture_map.gesture_action(14)
            elif max_value > self.thresholds[14] and position == 16:
                self.gesture_map.gesture_action(15)
            elif max_value > self.thresholds[15] and position == 17:
                self.gesture_map.gesture_action(16)
            elif max_value > self.thresholds[16] and position == 18:
                self.gesture_map.gesture_action(17)
            elif max_value > self.thresholds[17] and position == 19:
                self.gesture_map.gesture_action(18)
            elif max_value > self.thresholds[18] and position == 20:
                self.gesture_map.gesture_action(19)
            elif max_value > self.thresholds[19] and position == 21:
                self.gesture_map.gesture_action(20)
            elif max_value > self.thresholds[20] and position == 22:
                self.gesture_map.gesture_action(21)
            elif max_value > self.thresholds[21] and position == 23:
                self.gesture_map.gesture_action(22)
            elif max_value > self.thresholds[22] and position == 24:
                self.gesture_map.gesture_action(23)
            elif max_value > self.thresholds[23] and position == 25:
                self.gesture_map.gesture_action(24)
            elif max_value > self.thresholds[24] and position == 26:
                self.gesture_map.gesture_action(25)
            time.sleep(0.0002)