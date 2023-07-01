import math
import cv2
import mediapipe as mp
import pyautogui
import time
from screeninfo import get_monitors


class GestureMouseSteering:

    def __init__(self, camera, win_reference):
        self.active = True
        self.cam = camera
        self.win_reference = win_reference
        self.sensitivity = 11
        self.recognition_message = '''<br /><span style="color:black;">Action name<br /></span><span style="color:green;">''' + \
            '''mouse stop<br /></span><br />'''
        self.monitors = []
        self.current_monitor_number = 0

    def stop_mouse_steering(self):
        self.active = False

    def start_mouse_steering(self, reference):
        self.get_all_monitors()
        self.current_monitor_number = 0
        self.active = True
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands()
        mp_draw = mp.solutions.drawing_utils
        pyautogui.FAILSAFE = False
        mouse_click_lock = False
        right_mouse_click_lock = False
        mouse_double_click_lock = False
        change_screen_lock = False
        mouse_x_before = 0
        mouse_y_before = 0
        mouse_x = 0
        mouse_y = 0
        while True:
            if self.active is False:
                break
            success, img = self.cam.get_camera_image()
            if success is False:
                time.sleep(0.01)
                continue
            flip_img = cv2.flip(img, 1)
            img_rgb = cv2.cvtColor(flip_img, cv2.COLOR_BGR2RGB)
            results = hands.process(img_rgb)
            points = []
            if results.multi_hand_landmarks:
                for hand_lms in results.multi_hand_landmarks:
                    points.clear()
                    for id, lm in enumerate(hand_lms.landmark):
                        h, w, c = img.shape
                        c_x, c_y = int(lm.x*w), int(lm.y*h)
                        points.append((c_x, c_y))
                        mp_draw.draw_landmarks(
                            flip_img, hand_lms, mp_hands.HAND_CONNECTIONS)
                    if points[8][1] < points[5][1] and points[17][0] > points[1][0]:
                        if points[8][0] >= 200 and points[8][0] <= 400 and points[8][1] >= 150 and points[8][1] <= 350:
                            mouse_x = int(
                                float(points[8][0] - 200) / 200.0 * float(self.monitors[self.current_monitor_number][2])) + self.monitors[self.current_monitor_number][0]
                            mouse_y = int(
                                float(points[8][1] - 150) / 200.0 * float(self.monitors[self.current_monitor_number][3])) + self.monitors[self.current_monitor_number][1]
                            pyautogui.moveTo(mouse_x, mouse_y)
                        if points[2][0] < points[1][0] and points[3][0] < points[2][0] and points[4][0] < points[3][0]:
                            if mouse_click_lock is False:
                                if math.fabs(mouse_x - mouse_x_before) <= self.sensitivity \
                                        and math.fabs(mouse_y - mouse_y_before) <= self.sensitivity:
                                    pyautogui.click()
                                    mouse_click_lock = True
                        else:
                            mouse_click_lock = False
                        if points[10][1] < points[9][1] and points[11][1] < points[10][1] and points[12][1] < points[11][1]:
                            if right_mouse_click_lock is False:
                                if math.fabs(mouse_y - mouse_y_before) <= self.sensitivity \
                                        and math.fabs(mouse_x - mouse_x_before) <= self.sensitivity:
                                    pyautogui.click(button='right')
                                    right_mouse_click_lock = True
                        else:
                            right_mouse_click_lock = False
                        mouse_x_before = mouse_x
                        mouse_y_before = mouse_y
                    elif points[8][1] < points[5][1] and points[17][0] < points[1][0]:
                        if points[8][0] >= 200 and points[8][0] <= 400 and points[8][1] >= 150 and points[8][1] <= 350:
                            mouse_x = int(
                                float(points[8][0] - 200) / 200.0 * float(self.monitors[self.current_monitor_number][2])) + self.monitors[self.current_monitor_number][0]
                            mouse_y = int(
                                float(points[8][1] - 150) / 200.0 * float(self.monitors[self.current_monitor_number][3])) + self.monitors[self.current_monitor_number][1]

                            if points[10][1] < points[9][1] and points[11][1] < points[10][1] and points[12][1] < points[11][1]:
                                pyautogui.dragTo(mouse_x, mouse_y)
                            else:
                                pyautogui.moveTo(mouse_x, mouse_y)
                        if points[2][0] > points[1][0] and points[3][0] > points[2][0] and points[4][0] > points[3][0]:
                            if mouse_double_click_lock is False:
                                if math.fabs(mouse_x - mouse_x_before) <= self.sensitivity \
                                        and math.fabs(mouse_y - mouse_y_before) <= self.sensitivity:
                                    pyautogui.click(clicks=2)
                                    mouse_double_click_lock = True
                        else:
                            mouse_double_click_lock = False
                        mouse_x_before = mouse_x
                        mouse_y_before = mouse_y
                    elif points[0][1] < points[5][1] and points[5][1] < points[8][1] and points[17][0] > points[1][0]:
                        self.win_reference.set_gesture_recognized(
                            True, self.recognition_message)
                        reference.set_time_before()
                        return
                    elif points[5][0] > points[17][0] and points[0][1] > points[9][1]:
                        if points[20][1] < points[19][1] and points[19][1] < points[18][1] and \
                                points[18][1] < points[17][1]:
                            if change_screen_lock is False:
                                self.change_screen()
                                change_screen_lock = True
                        else:
                            change_screen_lock = False
            time.sleep(0.0001)

    def change_screen(self):
        self.get_all_monitors()
        if len(self.monitors) - 1 <= self.current_monitor_number:
            self.current_monitor_number = 0
        else:
            self.current_monitor_number += 1
        mouse_x = int(self.monitors[self.current_monitor_number]
                      [2] / 2) + self.monitors[self.current_monitor_number][0]
        mouse_y = int(self.monitors[self.current_monitor_number]
                      [3] / 2) + self.monitors[self.current_monitor_number][1]
        pyautogui.moveTo(mouse_x, mouse_y)

    def get_all_monitors(self):
        self.monitors.clear()
        for m in get_monitors():
            self.monitors.append([m.x, m.y, m.width, m.height])
