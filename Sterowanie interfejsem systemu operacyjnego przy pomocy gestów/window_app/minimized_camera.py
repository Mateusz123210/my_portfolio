from PyQt5.QtWidgets import QWidget, QLabel, QGraphicsOpacityEffect
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap, QFont
from threading import Lock


class MinimizedCamera(QWidget):

    def __init__(self, parent, update_thread, start_app, absolute_path):
        self.parent = parent
        super().__init__(self.parent)
        self.absolute_path = absolute_path
        self.update_thread = update_thread
        self.start_app = start_app
        self.oldPos = None
        self.entered_before_delete_label_time = False
        self.delete_label_thread_is_active_counter = 0
        self.mouse_released_before_hide = True
        self.screen = self.start_app.screenAt(self.pos())
        self.geometry = self.screen.geometry()
        self.initUI()
        self.delete_label_mutex = Lock()

    def set_mouse_released_before_hide(self, value):
        self.mouse_released_before_hide = value

    def unset_entered_before_delete_label_time(self):
        self.entered_before_delete_label_time = False

    def delete_label_thread_is_active_up(self):
        self.delete_label_mutex.acquire()
        self.delete_label_thread_is_active_counter += 1
        self.delete_label_mutex.release()

    def delete_label_thread_is_active_down(self):
        self.delete_label_mutex.acquire()
        self.delete_label_thread_is_active_counter -= 1
        self.delete_label_mutex.release()

    def get_delete_label_thread_is_active(self):
        self.delete_label_mutex.acquire()
        temp = self.delete_label_thread_is_active_counter
        self.delete_label_mutex.release()
        return temp

    def resizeEvent(self, e):
        pass

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.oldPos != None:
            new_mouse_position = event.globalPos()
            delta = QPoint(new_mouse_position - self.oldPos)
            new_x = self.pos().x() + delta.x()
            new_y = self.pos().y() + delta.y()
            if new_x >= 0 and new_y >= 0:
                self.move(new_x, new_y)
                self.oldPos = new_mouse_position

    def leaveEvent(self, e) -> None:
        self.navigation_label.hide()
        self.clickable_label.hide()
        return super().leaveEvent(e)

    def enterEvent(self, e) -> None:
        self.entered_before_delete_label_time = True
        self.clickable_label.show()
        return super().enterEvent(e)

    def on_timeout(self):
        self.delete_label_thread_is_active_down()
        if self.entered_before_delete_label_time is False and self.get_delete_label_thread_is_active() == 0:
            self.navigation_label.hide()

    def initUI(self):
        self.setWindowTitle('Handy')
        self.setWindowFlags(Qt.Tool | Qt. FramelessWindowHint |
                            Qt.WindowDoesNotAcceptFocus | Qt.WindowStaysOnTopHint)
        self.setFixedSize(320, 240)
        self.label = QLabel(self)
        self.label.setStyleSheet("border: 2px solid #BBBBBB;")
        self.label.setFixedSize(320, 240)
        self.label.setGeometry(0, 0, 320, 240)
        self.clickable_label = ClickableLabel(self)
        self.clickable_label.hide()
        self.clickable_label.setFixedSize(40, 40)
        self.clickable_label.move(140, 185)
        self.clickable_label.setPixmap(QPixmap
                                       (self.absolute_path + "/other/close_button.png"))
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.35)
        self.clickable_label.setGraphicsEffect(self.opacity_effect)
        self.update_thread.MinimizedImageUpdate.connect(self.update_image)
        self.start_label = ClickableLabelForTurningOnOffRecognition(self)

        self.start_label.setStyleSheet("background-color: #FC4008;"
                                       "border :1px solid #FC4008;"
                                       "border-top-left-radius :5px;"
                                       " border-top-right-radius : 5px; "
                                       "border-bottom-left-radius : 5px; "
                                       "border-bottom-right-radius : 5px")
        self.start_label.resize(10, 10)
        self.start_label.move(10, 220)
        self.navigation_label = QLabel(self)
        self.navigation_label.setFixedSize(65, 65)
        self.navigation_label.move(10, 10)
        self.navigation_label.setPixmap(QPixmap
                                        (self.absolute_path + "/other/navigation_image.png"))
        self.message_label = MyLabel(self)
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.setFixedSize(300, 90)
        self.message_label.move(10, 85)
        self.message_label.setStyleSheet("background-color: #BBBBBB;")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.message_label.setFont(font)

    def update_image(self, Image):
        recognition_status, recognition_message = self.parent.get_gesture_recognized()
        if recognition_status is True:
            self.label.setStyleSheet("border: 2px solid #70d345;")
            self.message_label.setText(
                recognition_message)
            self.message_label.show()
        else:
            if self.mouse_released_before_hide is True:
                self.message_label.hide()
            self.label.setStyleSheet("border: 2px solid #BBBBBB;")
        self.label.setPixmap(QPixmap.fromImage(Image))

    def close_using_button(self):
        self.hide()
        self.parent.uncheck_minimized_camera_checkbox()

    def show_if_recognition_started_on_interface(self, started):
        if started is True:
            self.start_label.setStyleSheet("background-color: #29FC08;"
                                           "border :1px solid #29FC08;"
                                           "border-top-left-radius :5px;"
                                           " border-top-right-radius : 5px; "
                                           "border-bottom-left-radius : 5px; "
                                           "border-bottom-right-radius : 5px")
        else:
            self.start_label.setStyleSheet("background-color: #FC4008;"
                                           "border :1px solid #FC4008;"
                                           "border-top-left-radius :5px;"
                                           " border-top-right-radius : 5px; "
                                           "border-bottom-left-radius : 5px; "
                                           "border-bottom-right-radius : 5px")

    def get_parent(self):
        return self.parent

    def show_navigation_label(self):
        self.navigation_label.show()


class ClickableLabel(QLabel):

    def __init__(self, parent):
        self.parent = parent
        super().__init__(self.parent)

    def mousePressEvent(self, e):
        if (20 - e.pos().x()) ** 2 + (20 - e.pos().y()) ** 2 <= 400:
            self.parent.close_using_button()
        return super().mousePressEvent(e)


class ClickableLabelForTurningOnOffRecognition(QLabel):

    def __init__(self, parent):
        self.parent = parent
        super().__init__(self.parent)

    def mousePressEvent(self, e):
        self.parent.get_parent().start_or_stop_gesture_recognition()


class MyLabel(QLabel):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(self.parent)

    def mousePressEvent(self, e):
        self.parent.set_mouse_released_before_hide(False)
        e.ignore()

    def mouseMoveEvent(self, e):
        e.ignore()

    def mouseReleaseEvent(self, e):
        self.parent.set_mouse_released_before_hide(True)
