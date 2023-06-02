

class FunctionsGetter():

    def __init__(self, controller, absolute_path):
        self.absolute_path = absolute_path
        self.controller = controller
        self.controller.set_reference(self)
        self.dct = {"zoom in": self.controller.zoom_in,
                    "zoom out": self.controller.zoom_out,
                    "scroll up": self.controller.scroll_up,
                    "scroll down": self.controller.scroll_down,
                    "page up": self.controller.page_up,
                    "page down": self.controller.page_down,
                    "scroll left": self.controller.scroll_left,
                    "scroll right": self.controller.scroll_right,
                    "volume up": self.controller.volume_up,
                    "volume down": self.controller.volume_down,
                    "mouse start": self.controller.mouse_start,
                    "screen keyboard": self.controller.screen_keyboard,
                    "brightness up": self.controller.brightness_up,
                    "brightness down": self.controller.brightness_down,
                    "maximize window": self.controller.maximize_window,
                    "minimize window": self.controller.minimize_window,
                    "minimize all windows": self.controller.minimize_all_windows,
                    "close window": self.controller.close_window,
                    "switch window": self.controller.switch_window,
                    "preview of opened windows": self.controller.preview_of_opened_windows,
                    "window left": self.controller.window_left,
                    "window right": self.controller.window_right,
                    "open action center": self.controller.open_action_center,
                    "escape": self.controller.escape,
                    "space": self.controller.space,
                    "do nothing": self.controller.do_nothing
                    }

    def call_function(self, name):
        try:
            self.dct.get(name)()
        except:
            pass

    def get_all_functions_names(self):
        return self.dct.keys()

    def get_absolute_path(self):
        return self.absolute_path

    def set_mapping_reference(self, ref):
        self.map_ref = ref

    def set_time_before(self):
        self.map_ref.set_time_before()

    def set_end_mouse_message(self):
        self.map_ref.set_mouse_end_message()
