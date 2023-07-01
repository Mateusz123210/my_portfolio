import platform
import ctypes
import pyautogui
from gesture_library.mouse_steering import GestureMouseSteering
import screen_brightness_control as sbc
from ctypes import wintypes as w
import time


class SystemController:

    _scroll_speed = 320

    def __init__(self, absolute_path, win_reference):
        self.absolute_path = absolute_path
        self.win_reference = win_reference
        self.operating_system_name = platform.system()
        self.camera = None
        self.mouse_steering = None
        self.sound_values = []

    def set_reference(self, function_getter):
        self.function_getter = function_getter

    def set_camera_reference(self, camera):
        self.camera = camera
        self.mouse_steering = GestureMouseSteering(camera, self.win_reference)

    def minimize_window(self):
        user32 = ctypes.WinDLL('user32')
        user32.GetForegroundWindow.argtypes = ()
        user32.GetForegroundWindow.restype = w.HWND
        user32.ShowWindow.argtypes = w.HWND, w.BOOL
        user32.ShowWindow.restype = w.BOOL
        SW_MINIMIZE = 6
        hWnd = user32.GetForegroundWindow()
        user32.ShowWindow(hWnd, SW_MINIMIZE)

    def maximize_window(self):
        user32 = ctypes.WinDLL('user32')
        user32.GetForegroundWindow.argtypes = ()
        user32.GetForegroundWindow.restype = w.HWND
        user32.ShowWindow.argtypes = w.HWND, w.BOOL
        user32.ShowWindow.restype = w.BOOL
        SW_MAXIMIZE = 3
        hWnd = user32.GetForegroundWindow()
        user32.ShowWindow(hWnd, SW_MAXIMIZE)

    def close_window(self):
        user32 = ctypes.WinDLL('user32')
        user32.GetForegroundWindow.argtypes = ()
        user32.GetForegroundWindow.restype = w.HWND
        user32.ShowWindow.argtypes = w.HWND, w.BOOL
        user32.ShowWindow.restype = w.BOOL
        hWnd = user32.GetForegroundWindow()
        user32.ShowWindow(hWnd, 0)

    @property
    def scroll_speed(self):
        return self._scroll_speed

    @scroll_speed.setter
    def scroll_speed(self, speed):
        self._scroll_speed = speed

    def scroll_up(self, speed=_scroll_speed):
        pyautogui.scroll(self.scroll_speed)

    def scroll_down(self, speed=_scroll_speed):
        pyautogui.scroll(-self.scroll_speed)

    def volume_up(self):
        pyautogui.press('volumeup')

    def volume_down(self):
        pyautogui.press('volumedown')

    def zoom_in(self):
        pyautogui.keyDown('ctrl')
        pyautogui.press('+')
        pyautogui.keyUp('ctrl')

    def zoom_out(self):
        pyautogui.keyDown('ctrl')
        pyautogui.press('-')
        pyautogui.keyUp('ctrl')

    def brightness_up(self):
        current_brightness = sbc.get_brightness()
        brightness = current_brightness[0] + 5
        if brightness > 100:
            brightness = 100
        sbc.set_brightness(brightness)

    def brightness_down(self):
        current_brightness = sbc.get_brightness()
        brightness = current_brightness[0] - 5
        if brightness < 0:
            brightness = 0
        sbc.set_brightness(brightness)

    def scroll_right(self):
        pyautogui.press('right')

    def scroll_left(self):
        pyautogui.press('left')

    def switch_window(self):
        time.sleep(0.1)
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')

    def mouse_start(self):
        self.mouse_steering.start_mouse_steering(self.function_getter)
        self.function_getter.set_time_before()

    def stop_mouse(self):
        self.mouse_steering.stop_mouse_steering()

    def window_left(self):
        pyautogui.keyDown('win')
        pyautogui.press('left')
        pyautogui.keyUp('win')

    def window_right(self):
        pyautogui.keyDown('win')
        pyautogui.press('right')
        pyautogui.keyUp('win')

    def escape(self):
        pyautogui.press('esc')

    def do_nothing(self):
        pass

    def minimize_all_windows(self):
        pyautogui.keyDown('win')
        pyautogui.press('d')
        pyautogui.keyUp('win')

    def preview_of_opened_windows(self):
        pyautogui.keyDown('win')
        pyautogui.press('tab')
        pyautogui.keyUp('win')

    def open_action_center(self):
        pyautogui.keyDown('win')
        pyautogui.press('a')
        pyautogui.keyUp('win')

    def page_up(self):
        pyautogui.press('pageup')

    def page_down(self):
        pyautogui.press('pagedown')

    def space(self):
        pyautogui.press('space')

    def screen_keyboard(self):
        pyautogui.keyDown('win')
        pyautogui.keyDown('ctrl')
        pyautogui.press('o')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('win')

    def set_controller_reference(self, cont):
        self.controller_reference = cont
