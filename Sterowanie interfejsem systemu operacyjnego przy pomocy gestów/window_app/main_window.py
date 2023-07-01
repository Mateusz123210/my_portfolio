from controllers.system_controller import SystemController
from controllers.functions_getter import FunctionsGetter
from controllers.controller import Controller
from window_app.minimized_camera import MinimizedCamera
from PyQt5.QtGui import QFont, QPixmap, QImage, QColor, QMovie
from PyQt5.QtWidgets import QComboBox, QLabel, QPushButton, QCheckBox, QWidget, QVBoxLayout, \
    QTabWidget, QSizePolicy, QSpacerItem, QGridLayout, QMainWindow, QLayout, QHBoxLayout, QFrame, QScrollArea,\
    QLayout, QDesktopWidget
from PyQt5.QtCore import Qt, QSize, QRect, QThread, pyqtSignal, QCoreApplication, QMetaObject, QTimer, QPoint
import cv2
import time
from PySide2 import QtGui as qtg
from PIL import Image
from numpy import asarray
import sys
from threading import Lock
from screeninfo import get_monitors


class MyComboBox(QComboBox):

    def __init__(self, scrollWidget=None, *args, **kwargs):
        super(QComboBox, self).__init__(*args, **kwargs)
        self.scrollWidget = scrollWidget
        self.setFocusPolicy(Qt.StrongFocus)
        self.reference_to_win = None
        self.setMinimumSize(QSize(0, 30))
        self.textHighlighted.connect(
            lambda: self.clearFocus())
        self.highlighted.connect(
            lambda: self.clearFocus())

    def wheelEvent(self,  event):
        pass

    def keyPressEvent(self, event):
        event.ignore()

    def mouseReleaseEvent(self, event):
        self.clearFocus()


class MyLabel(QLabel, QPushButton):
    def __init__(self, win, parent=None):
        super(MyLabel, self).__init__(parent)
        self.absolute_path = None
        self.win = win
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(223, 230, 248))
        self.setPalette(p)
        self.setMouseTracking(True)
        self.id = -1
        self.name = ""
        self.videoWindow = QMainWindow()

    def set_absolute_path(self, absolute_path):
        self.absolute_path = absolute_path

    def mousePressEvent(self, event) -> None:
        if id != -1:
            self.videoWindow.setFixedSize(290, 500)
            self.videoWindow.wid = QWidget(self.videoWindow)
            self.videoWindow.setCentralWidget(self.videoWindow.wid)
            self.videoWindow.label = QLabel()
            self.videoWindow.label.setFixedSize(270, 480)
            self.videoWindow.layout = QVBoxLayout()
            self.videoWindow.layout.addWidget(self.videoWindow.label)
            self.videoWindow.movie = QMovie(
                self.absolute_path + "/gesture_videos/" + self.name + ".gif")
            self.videoWindow.label.setMovie(self.videoWindow.movie)
            self.videoWindow.movie.start()
            self.videoWindow.wid.setLayout(self.videoWindow.layout)
            self.videoWindow.show()

    def leaveEvent(self, event) -> None:
        if id != -1:
            self.videoWindow.close()

    def mouseMoveEvent(self, event):
        screen = QDesktopWidget().screenGeometry()
        y = screen.height()
        pos = qtg.QCursor().pos()
        pos_y = pos.y()
        if pos_y > y - 600:
            pos_y = y - 600
        self.videoWindow.move(pos.x() + 15, pos_y)

    def set_name(self, name: str):
        self.name = name
        self.id = 0


class MyCheckBox(QCheckBox):
    def __init__(self, parent=None):
        super(MyCheckBox, self).__init__(parent)

    def mouseMoveEvent(self, event) -> None:
        pass

    def wheelEvent(self, event) -> None:
        pass

    def keyPressEvent(self, event) -> None:
        pass


class MainWindow(QMainWindow):
    def __init__(self, absolute_path, app, temp_ref):
        self.absolute_path = absolute_path
        self.app = app
        self.temp_ref = temp_ref
        super().__init__()
        self.minimized_camera_checkbox_disabled = False
        self.disable_gesture_combobox_event = False
        self.recognition_message = ""
        self.gesture_recognized = False
        self.close_time = False
        self.sys_cont = SystemController(self.absolute_path, self)
        self.func_get = FunctionsGetter(self.sys_cont, self.absolute_path)
        self.cont = Controller(self.func_get, self.sys_cont, self)
        self.sys_cont.set_camera_reference(self.cont.get_camera_controller())
        self.gesture_recognized_lock = Lock()

    def set_gesture_recognized(self, value, message):
        self.gesture_recognized_lock.acquire()
        self.gesture_recognized = value
        self.recognition_message = message
        self.gesture_recognized_lock.release()

    def get_gesture_recognized(self):
        self.gesture_recognized_lock.acquire()
        temp = self.gesture_recognized, self.recognition_message
        self.gesture_recognized_lock.release()
        return temp

    def get_geometry(self):
        return self.geometry()

    def get_position(self):
        return self.pos()

    def refresh_camera_list(self):
        temp = self.cont.get_camera_controller().refresh_camera_list()
        self.camera_combo_box.clear()
        if len(temp) > 0:
            for a in temp:
                self.camera_combo_box.addItem("Camera " + str(a))
            self.camera_combo_box.setCurrentText("Camera 0")

    def set_camera(self):
        camera_text = self.camera_combo_box.currentText()
        camera_number = int(camera_text[-1])
        temp = self.cont.get_camera_controller(
        ).set_used_camera_number(camera_number)
        if temp >= 0:
            self.camera_combo_box.setCurrentText("Camera " + str(temp))
        self.camera_combo_box.clearFocus()

    def set_cameras_combo_box(self, lst):
        self.camera_combo_box.clear()
        for a in lst:
            self.camera_combo_box.addItem("Camera " + str(a))

    def get_config(self):
        config = self.cont.get_gesture_recognition().get_mapping().get_gestures_list()
        self.action1_comboBox.setCurrentText(config.get(1))
        self.action2_comboBox.setCurrentText(config.get(2))
        self.action3_comboBox.setCurrentText(config.get(3))
        self.action4_comboBox.setCurrentText(config.get(4))
        self.action5_comboBox.setCurrentText(config.get(5))
        self.action6_comboBox.setCurrentText(config.get(6))
        self.action7_comboBox.setCurrentText(config.get(7))
        self.action8_comboBox.setCurrentText(config.get(8))
        self.action9_comboBox.setCurrentText(config.get(9))
        self.action10_comboBox.setCurrentText(config.get(10))
        self.action11_comboBox.setCurrentText(config.get(11))
        self.action12_comboBox.setCurrentText(config.get(12))
        self.action13_comboBox.setCurrentText(config.get(13))
        self.action14_comboBox.setCurrentText(config.get(14))
        self.action15_comboBox.setCurrentText(config.get(15))
        self.action16_comboBox.setCurrentText(config.get(16))
        self.action17_comboBox.setCurrentText(config.get(17))
        self.action18_comboBox.setCurrentText(config.get(18))
        self.action20_comboBox.setCurrentText(config.get(20))
        self.action21_comboBox.setCurrentText(config.get(21))
        self.action22_comboBox.setCurrentText(config.get(22))
        self.action23_comboBox.setCurrentText(config.get(23))
        self.action24_comboBox.setCurrentText(config.get(24))
        self.action25_comboBox.setCurrentText(config.get(25))

    def get_default_config(self):
        self.cont.get_gesture_recognition().get_mapping(
        ).set_default_config()
        self.get_config()

    def set_test_gesture_config(self):
        if self.test_gestures_button.text() == 'Test gestures':
            dict1 = {}
            for i in range(1, 19):
                dict1[i] = "do nothing"
            dict1[19] = "mouse start"
            for i in range(20, 26):
                dict1[i] = "do nothing"
            self.cont.get_gesture_recognition().get_mapping(
            ).set_gestures_without_saving_to_file(dict1)
            self.test_gestures_button.setText("Stop test mode")
            self.test_gestures_button.setStyleSheet("border-style:outset;\n"
                                                    "border-radius:8px;\n"
                                                    "background-color: rgb(255, 0, 0);\n"
                                                    "color:white;\n"
                                                    "")
        else:
            self.test_gestures_button.setText("Test gestures")
            self.test_gestures_button.setStyleSheet("border-style:outset;\n"
                                                    "border-radius:8px;\n"
                                                    "background-color: rgb(22, 155, 213);\n"
                                                    "color:white;\n"
                                                    "")
            self.cont.get_gesture_recognition().get_mapping().read_configuration_from_file()
        self.disable_gesture_combobox_event = True
        self.get_config()
        self.disable_gesture_combobox_event = False

    def set_config(self):
        if self.disable_gesture_combobox_event is False:
            dict = {}
            dict[1] = self.action1_comboBox.currentText()
            dict[2] = self.action2_comboBox.currentText()
            dict[3] = self.action3_comboBox.currentText()
            dict[4] = self.action4_comboBox.currentText()
            dict[5] = self.action5_comboBox.currentText()
            dict[6] = self.action6_comboBox.currentText()
            dict[7] = self.action7_comboBox.currentText()
            dict[8] = self.action8_comboBox.currentText()
            dict[9] = self.action9_comboBox.currentText()
            dict[10] = self.action10_comboBox.currentText()
            dict[11] = self.action11_comboBox.currentText()
            dict[12] = self.action12_comboBox.currentText()
            dict[13] = self.action13_comboBox.currentText()
            dict[14] = self.action14_comboBox.currentText()
            dict[15] = self.action15_comboBox.currentText()
            dict[16] = self.action16_comboBox.currentText()
            dict[17] = self.action17_comboBox.currentText()
            dict[18] = self.action18_comboBox.currentText()
            dict[19] = "mouse start"
            dict[20] = self.action20_comboBox.currentText()
            dict[21] = self.action21_comboBox.currentText()
            dict[22] = self.action22_comboBox.currentText()
            dict[23] = self.action23_comboBox.currentText()
            dict[24] = self.action24_comboBox.currentText()
            dict[25] = self.action25_comboBox.currentText()
            self.cont.get_gesture_recognition().get_mapping().set_gesture(dict)

    def get_controller(self):
        return self.cont

    def get_close_time(self):
        return self.close_time

    def close_application(self):
        self.close_time = True
        self.cont.get_camera_controller().release_camera()
        self.cont.stop_app()
        self.small_camera_widget.close()
        time.sleep(0.1)
        sys.exit(0)

    def set_button_to_start_mode(self):
        self.start_button.setStyleSheet("border-style:outset;\n"
                                        "border-radius:8px;\n"
                                        "background-color: rgb(22, 155, 213);\n"
                                        "color:white;\n"
                                        "")
        self.start_button.setText("Start")

    def set_button_to_stop_mode(self):
        self.start_button.setStyleSheet("border-style:outset;\n"
                                        "border-radius:8px;\n"
                                        "background-color: rgb(255, 0, 0);\n"
                                        "color:white;\n"
                                        "")
        self.start_button.setText("Stop")

    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1287, 1000)
        main_window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.aplication_tab_widget = QTabWidget(self.centralwidget)
        self.aplication_tab_widget.setStyleSheet(
            "background-color: rgb(215, 215, 215);")
        self.aplication_tab_widget.setTabShape(QTabWidget.Rounded)
        self.aplication_tab_widget.setElideMode(Qt.ElideLeft)
        self.aplication_tab_widget.setTabsClosable(False)
        self.aplication_tab_widget.setTabBarAutoHide(False)
        self.aplication_tab_widget.setObjectName("aplication_tab_widget")
        self.camera_tab = QWidget()
        self.camera_tab.setObjectName("camera_tab")
        self.gridLayout = QGridLayout(self.camera_tab)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        spacerItem2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 5, 1, 1)
        self.gesture_message_label = QLabel()
        self.gesture_message_label.setMinimumSize(QSize(500, 125))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gesture_message_label.setFont(font)
        self.gesture_message_label.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.gesture_message_label, 5, 10, 1, 1)
        self.big_camera_label = QLabel()
        self.gridLayout.addWidget(self.big_camera_label, 4, 10, 1, 1)
        spacerItem3 = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 11, 1, 1)
        spacerItem4 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 12, 1, 1)
        self.vertical_line = QFrame(self.camera_tab)
        self.vertical_line.setMinimumSize(QSize(0, 300))
        self.vertical_line.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.vertical_line.setFont(font)
        self.vertical_line.setStyleSheet(
            "background-color: rgb(171, 171, 171);")
        self.vertical_line.setFrameShadow(QFrame.Raised)
        self.vertical_line.setFrameShape(QFrame.VLine)
        self.vertical_line.setObjectName("vertical_line")
        self.gridLayout.addWidget(self.vertical_line, 4, 6, 2, 1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem5 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.select_camera_label = QLabel(self.camera_tab)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.select_camera_label.setFont(font)
        self.select_camera_label.setObjectName("select_camera_label")
        self.verticalLayout_3.addWidget(self.select_camera_label)
        self.camera_combo_box = MyComboBox(self.camera_tab)
        sizePolicy = QSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.camera_combo_box.sizePolicy().hasHeightForWidth())
        self.camera_combo_box.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.camera_combo_box.setFont(font)
        self.camera_combo_box.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "outline-color: black;")
        self.camera_combo_box.setObjectName("camera_combo_box")
        self.verticalLayout_3.addWidget(self.camera_combo_box)
        self.refresh_cameras_button = QPushButton(self.camera_tab)
        self.refresh_cameras_button.setMinimumSize(QSize(0, 40))
        self.refresh_cameras_button.setMaximumSize(
            QSize(16777215, 16777209))
        font = QFont()
        font.setPointSize(10)
        self.refresh_cameras_button.setFont(font)
        self.refresh_cameras_button.setStyleSheet("background-color:white;\n"
                                                  "border-style:outset;\n"
                                                  "border-radius:8px;\n"
                                                  "outline-color: black;\n"
                                                  "border: 1px solid grey;")
        self.refresh_cameras_button.setObjectName("refresh_cameras_button")
        self.verticalLayout_3.addWidget(self.refresh_cameras_button)
        spacerItem6 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem6)
        font = QFont()
        font.setPointSize(10)
        font.setWeight(60)
        self.show_minimized_camera_check_box = MyCheckBox(self.camera_tab)
        self.show_minimized_camera_check_box.setFont(font)
        self.show_minimized_camera_check_box.setStyleSheet("")
        self.show_minimized_camera_check_box.setObjectName(
            "show_minimized_camera_check_box")
        self.verticalLayout_3.addWidget(self.show_minimized_camera_check_box)
        spacerItem7 = QSpacerItem(
            20, 35, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem7)
        self.modify_gestures_button = QPushButton(self.camera_tab)
        sizePolicy = QSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.modify_gestures_button.sizePolicy().hasHeightForWidth())
        self.modify_gestures_button.setSizePolicy(sizePolicy)
        self.modify_gestures_button.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(10)
        self.modify_gestures_button.setFont(font)
        self.modify_gestures_button.setStyleSheet("background-color:white;\n"
                                                  "border-style:outset;\n"
                                                  "border-radius:8px;\n"
                                                  "outline-color: black;\n"
                                                  "border: 1px solid grey;")
        self.modify_gestures_button.setObjectName("modify_gestures_button")
        self.verticalLayout_3.addWidget(self.modify_gestures_button)
        spacerItem8 = QSpacerItem(
            20, 120, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.start_button = QPushButton(self.camera_tab)
        sizePolicy = QSizePolicy(
            QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        self.start_button.setMinimumSize(QSize(230, 80))
        font = QFont()
        font.setPointSize(16)
        self.start_button.setFont(font)
        self.start_button.setFocusPolicy(Qt.WheelFocus)
        self.start_button.setLayoutDirection(Qt.LeftToRight)
        self.start_button.setStyleSheet("border-style:outset;\n"
                                        "border-radius:8px;\n"
                                        "background-color: rgb(22, 155, 213);\n"
                                        "color:white;\n"
                                        "")
        self.start_button.setAutoRepeat(False)
        self.start_button.setAutoExclusive(False)
        self.start_button.setAutoDefault(False)
        self.start_button.setDefault(False)
        self.start_button.setFlat(False)
        self.start_button.setObjectName("start_button")
        self.verticalLayout_3.addWidget(self.start_button)
        spacerItem9 = QSpacerItem(
            20, 120, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem9)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.minimize_window_button = QPushButton(self.camera_tab)
        sizePolicy = QSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.minimize_window_button.sizePolicy().hasHeightForWidth())
        self.minimize_window_button.setSizePolicy(sizePolicy)
        self.minimize_window_button.setMinimumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(10)
        self.minimize_window_button.setFont(font)
        self.minimize_window_button.setStyleSheet("background-color:white;\n"
                                                  "border-radius:10px;\n"
                                                  "border-style:outset;\n"
                                                  "border-radius:8px;\n"
                                                  "border: 1px solid grey;\n"
                                                  "")
        self.minimize_window_button.setObjectName("help_button")
        self.horizontalLayout_9.addWidget(self.minimize_window_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        spacerItem0 = QSpacerItem(
            20, 50, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem0)
        self.gridLayout.addLayout(self.verticalLayout_3, 4, 1, 1, 3)
        spacerItem10 = QSpacerItem(
            80, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 4, 8, 1, 1)
        self.aplication_tab_widget.addTab(self.camera_tab, "")
        self.gesture_tab = QWidget()
        self.gesture_tab.setObjectName("gesture_tab")
        self.verticalLayout_4 = QVBoxLayout(self.gesture_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gestures_scroll_area = QScrollArea(self.gesture_tab)
        sizePolicy = QSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.gestures_scroll_area.sizePolicy().hasHeightForWidth())
        self.gestures_scroll_area.setSizePolicy(sizePolicy)
        self.gestures_scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOn)
        self.gestures_scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        self.gestures_scroll_area.setWidgetResizable(True)
        self.gestures_scroll_area.setObjectName("gestures_scroll_area")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(
            QRect(0, -973, 1224, 1685))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QGridLayout(
            self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.steering_gestures_label1 = QLabel("Gestures for special actions")
        self.steering_gestures_label1.setFont(font)
        self.steering_gestures_label1.setStyleSheet("margin: 10px;")
        self.gridLayout_4.addWidget(self.steering_gestures_label1, 0, 1, 1, 5)

        self.mouse_steering_gestures_label1 = QLabel(
            "Gestures for mouse steering")
        self.mouse_steering_gestures_label1.setStyleSheet("margin: 10px;")
        self.mouse_steering_gestures_label1.setFont(font)
        self.gridLayout_4.addWidget(
            self.mouse_steering_gestures_label1, 6, 1, 1, 5)

        self.mouse_right_button_vertical_layout = QVBoxLayout()
        self.mouse_right_button_vertical_layout.setContentsMargins(
            -1, -1, 0, -1)
        self.mouse_right_button_vertical_layout.setSpacing(0)
        self.mouse_right_button_vertical_layout.setObjectName(
            "mouse_right_button_vertical_layout")
        self.mouse_right_button_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.mouse_right_button_image_label.set_absolute_path(
            self.absolute_path)
        self.mouse_right_button_image_label.set_name("mouse_right_click")
        self.mouse_right_button_image_label.setMinimumSize(
            QSize(120, 200))
        self.mouse_right_button_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.mouse_right_button_image_label.setText("")
        self.mouse_right_button_image_label.setTextFormat(Qt.AutoText)
        self.mouse_right_button_image_label.setPixmap(QPixmap
                                                      (self.absolute_path + "/gesture_images/mouse_stering_gestures/click_right_button.png"))
        self.mouse_right_button_image_label.setScaledContents(True)
        self.mouse_right_button_image_label.setObjectName(
            "mouse_right_button_image_label")
        self.mouse_right_button_vertical_layout.addWidget(
            self.mouse_right_button_image_label)
        self.mouse_right_button_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mouse_right_button_name_label.sizePolicy().hasHeightForWidth())
        self.mouse_right_button_name_label.setSizePolicy(sizePolicy)
        self.mouse_right_button_name_label.setMinimumSize(QSize(0, 50))
        self.mouse_right_button_name_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.mouse_right_button_name_label.setFont(font)
        self.mouse_right_button_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.mouse_right_button_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.mouse_right_button_name_label.setAlignment(Qt.AlignCenter)
        self.mouse_right_button_name_label.setObjectName(
            "mouse_right_button_name_label")
        self.mouse_right_button_vertical_layout.addWidget(
            self.mouse_right_button_name_label)
        self.gridLayout_4.addLayout(
            self.mouse_right_button_vertical_layout, 7, 4, 1, 1)

        self.mouse_drag1_vertical_layout = QVBoxLayout()
        self.mouse_drag1_vertical_layout.setContentsMargins(
            -1, -1, 0, -1)
        self.mouse_drag1_vertical_layout.setSpacing(0)
        self.mouse_drag1_vertical_layout.setObjectName(
            "mouse_drag1_vertical_layout")
        self.mouse_drag1_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.mouse_drag1_image_label.set_absolute_path(
            self.absolute_path)
        self.mouse_drag1_image_label.set_name("mouse_drag")
        self.mouse_drag1_image_label.setMinimumSize(
            QSize(120, 200))
        self.mouse_drag1_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.mouse_drag1_image_label.setText("")
        self.mouse_drag1_image_label.setTextFormat(Qt.AutoText)
        self.mouse_drag1_image_label.setPixmap(QPixmap
                                               (self.absolute_path + "/gesture_images/mouse_stering_gestures/drag.png"))
        self.mouse_drag1_image_label.setScaledContents(True)
        self.mouse_drag1_image_label.setObjectName(
            "mouse_drag1_image_label")
        self.mouse_drag1_vertical_layout.addWidget(
            self.mouse_drag1_image_label)
        self.mouse_drag1_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mouse_drag1_name_label.sizePolicy().hasHeightForWidth())
        self.mouse_drag1_name_label.setSizePolicy(sizePolicy)
        self.mouse_drag1_name_label.setMinimumSize(QSize(0, 50))
        self.mouse_drag1_name_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.mouse_drag1_name_label.setFont(font)
        self.mouse_drag1_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.mouse_drag1_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.mouse_drag1_name_label.setAlignment(Qt.AlignCenter)
        self.mouse_drag1_name_label.setObjectName(
            "mouse_drag1_name_label")
        self.mouse_drag1_vertical_layout.addWidget(
            self.mouse_drag1_name_label)
        self.gridLayout_4.addLayout(
            self.mouse_drag1_vertical_layout, 7, 5, 1, 1)

        self.mouse_double_click1_vertical_layout = QVBoxLayout()
        self.mouse_double_click1_vertical_layout.setContentsMargins(
            -1, -1, 0, -1)
        self.mouse_double_click1_vertical_layout.setSpacing(0)
        self.mouse_double_click1_vertical_layout.setObjectName(
            "mouse_double_click1_vertical_layout")
        self.mouse_double_click1_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.mouse_double_click1_image_label.set_absolute_path(
            self.absolute_path)
        self.mouse_double_click1_image_label.set_name("mouse_double_click")
        self.mouse_double_click1_image_label.setMinimumSize(
            QSize(120, 200))
        self.mouse_double_click1_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.mouse_double_click1_image_label.setText("")
        self.mouse_double_click1_image_label.setTextFormat(Qt.AutoText)
        self.mouse_double_click1_image_label.setPixmap(QPixmap
                                                       (self.absolute_path + "/gesture_images/mouse_stering_gestures/double_click.png"))
        self.mouse_double_click1_image_label.setScaledContents(True)
        self.mouse_double_click1_image_label.setObjectName(
            "mouse_double_click1_image_label")
        self.mouse_double_click1_vertical_layout.addWidget(
            self.mouse_double_click1_image_label)
        self.mouse_double_click1_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mouse_double_click1_name_label.sizePolicy().hasHeightForWidth())
        self.mouse_double_click1_name_label.setSizePolicy(sizePolicy)
        self.mouse_double_click1_name_label.setMinimumSize(QSize(0, 50))
        self.mouse_double_click1_name_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.mouse_double_click1_name_label.setFont(font)
        self.mouse_double_click1_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.mouse_double_click1_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.mouse_double_click1_name_label.setAlignment(Qt.AlignCenter)
        self.mouse_double_click1_name_label.setObjectName(
            "mouse_double_click1_name_label")
        self.mouse_double_click1_vertical_layout.addWidget(
            self.mouse_double_click1_name_label)
        self.gridLayout_4.addLayout(
            self.mouse_double_click1_vertical_layout, 8, 1, 1, 1)

        self.mouse_change_screen_vertical_layout = QVBoxLayout()
        self.mouse_change_screen_vertical_layout.setContentsMargins(
            -1, -1, 0, -1)
        self.mouse_change_screen_vertical_layout.setSpacing(0)
        self.mouse_change_screen_vertical_layout.setObjectName(
            "mouse_change_screen_vertical_layout")
        self.mouse_change_screen_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.mouse_change_screen_image_label.set_absolute_path(
            self.absolute_path)
        self.mouse_change_screen_image_label.set_name("mouse_change_screen")
        self.mouse_change_screen_image_label.setMinimumSize(
            QSize(120, 200))
        self.mouse_change_screen_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.mouse_change_screen_image_label.setText("")
        self.mouse_change_screen_image_label.setTextFormat(Qt.AutoText)
        self.mouse_change_screen_image_label.setPixmap(QPixmap
                                                       (self.absolute_path + "/gesture_images/mouse_stering_gestures/change_screen.png"))
        self.mouse_change_screen_image_label.setScaledContents(True)
        self.mouse_change_screen_image_label.setObjectName(
            "mouse_change_screen_image_label")
        self.mouse_change_screen_vertical_layout.addWidget(
            self.mouse_change_screen_image_label)
        self.mouse_change_screen_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mouse_change_screen_name_label.sizePolicy().hasHeightForWidth())
        self.mouse_change_screen_name_label.setSizePolicy(sizePolicy)
        self.mouse_change_screen_name_label.setMinimumSize(QSize(0, 50))
        self.mouse_change_screen_name_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.mouse_change_screen_name_label.setFont(font)
        self.mouse_change_screen_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.mouse_change_screen_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.mouse_change_screen_name_label.setAlignment(Qt.AlignCenter)
        self.mouse_change_screen_name_label.setObjectName(
            "mouse_change_screen_name_label")
        self.mouse_change_screen_vertical_layout.addWidget(
            self.mouse_change_screen_name_label)
        self.gridLayout_4.addLayout(
            self.mouse_change_screen_vertical_layout, 8, 2, 1, 1)

        self.mouse_left_button_vertical_layout = QVBoxLayout()
        self.mouse_left_button_vertical_layout.setSizeConstraint(
            QLayout.SetDefaultConstraint)
        self.mouse_left_button_vertical_layout.setContentsMargins(
            -1, -1, 0, -1)
        self.mouse_left_button_vertical_layout.setSpacing(0)
        self.mouse_left_button_vertical_layout.setObjectName(
            "mouse_left_button_vertical_layout")
        self.mouse_left_button_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.mouse_left_button_image_label.set_absolute_path(
            self.absolute_path)
        self.mouse_left_button_image_label.set_name("mouse_left_click")
        self.mouse_left_button_image_label.setMinimumSize(
            QSize(120, 200))
        self.mouse_left_button_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.mouse_left_button_image_label.setText("")
        self.mouse_left_button_image_label.setTextFormat(Qt.AutoText)
        self.mouse_left_button_image_label.setPixmap(QPixmap
                                                     (self.absolute_path + "/gesture_images/mouse_stering_gestures/click_left_button.png"))
        self.mouse_left_button_image_label.setScaledContents(True)
        self.mouse_left_button_image_label.setObjectName(
            "mouse_left_button_image_label")
        self.mouse_left_button_vertical_layout.addWidget(
            self.mouse_left_button_image_label)
        self.mouse_left_button_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mouse_left_button_name_label.sizePolicy().hasHeightForWidth())
        self.mouse_left_button_name_label.setSizePolicy(sizePolicy)
        self.mouse_left_button_name_label.setMinimumSize(QSize(0, 50))
        self.mouse_left_button_name_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.mouse_left_button_name_label.setFont(font)
        self.mouse_left_button_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.mouse_left_button_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.mouse_left_button_name_label.setAlignment(Qt.AlignCenter)
        self.mouse_left_button_name_label.setObjectName(
            "mouse_left_button_name_label")
        self.mouse_left_button_vertical_layout.addWidget(
            self.mouse_left_button_name_label)
        self.gridLayout_4.addLayout(
            self.mouse_left_button_vertical_layout, 7, 3, 1, 1)
        self.turning_hand_counter_vertical_layout = QVBoxLayout()
        self.turning_hand_counter_vertical_layout.setSpacing(0)
        self.turning_hand_counter_vertical_layout.setObjectName(
            "turning_hand_counter_vertical_layout")
        self.turning_hand_counter_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.turning_hand_counter_image_label.set_absolute_path(
            self.absolute_path)
        self.turning_hand_counter_image_label.set_name(
            "turning_hand_counterclockwise")
        self.turning_hand_counter_image_label.setMinimumSize(
            QSize(0, 200))
        self.turning_hand_counter_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.turning_hand_counter_image_label.setText("")
        self.turning_hand_counter_image_label.setTextFormat(Qt.AutoText)
        self.turning_hand_counter_image_label.setPixmap(QPixmap
                                                        (self.absolute_path + "/gesture_images/turning_hand_counterclockwise.png"))
        self.turning_hand_counter_image_label.setScaledContents(True)
        self.turning_hand_counter_image_label.setObjectName(
            "turning_hand_counter_image_label")
        self.turning_hand_counter_vertical_layout.addWidget(
            self.turning_hand_counter_image_label)
        self.turning_hand_counter_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.turning_hand_counter_name_label.sizePolicy().hasHeightForWidth())
        self.turning_hand_counter_name_label.setSizePolicy(sizePolicy)
        self.turning_hand_counter_name_label.setMinimumSize(
            QSize(0, 50))
        self.turning_hand_counter_name_label.setSizeIncrement(
            QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.turning_hand_counter_name_label.setFont(font)
        self.turning_hand_counter_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.turning_hand_counter_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.turning_hand_counter_name_label.setAlignment(
            Qt.AlignCenter)
        self.turning_hand_counter_name_label.setObjectName(
            "turning_hand_counter_name_label")
        self.turning_hand_counter_vertical_layout.addWidget(
            self.turning_hand_counter_name_label)
        self.action21_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action21_comboBox.setFont(font)
        self.action21_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "outline-color: black;")
        self.action21_comboBox.setObjectName("action21_comboBox")
        self.turning_hand_counter_vertical_layout.addWidget(
            self.action21_comboBox)
        self.gridLayout_4.addLayout(
            self.turning_hand_counter_vertical_layout, 5, 2, 1, 1)
        self.mouse_exit_vertical_layout = QVBoxLayout()
        self.mouse_exit_vertical_layout.setContentsMargins(-1, -1, 0, -1)
        self.mouse_exit_vertical_layout.setSpacing(0)
        self.mouse_exit_vertical_layout.setObjectName(
            "mouse_exit_vertical_layout")
        self.mouse_exit_image_label = MyLabel(self.scrollAreaWidgetContents)
        self.mouse_exit_image_label.set_absolute_path(self.absolute_path)
        self.mouse_exit_image_label.set_name("mouse_stop")
        self.mouse_exit_image_label.setMinimumSize(QSize(120, 200))
        self.mouse_exit_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.mouse_exit_image_label.setText("")
        self.mouse_exit_image_label.setTextFormat(Qt.AutoText)
        self.mouse_exit_image_label.setPixmap(QPixmap
                                              (self.absolute_path + "/gesture_images/mouse_stering_gestures/stop_mouse_mode.png"))
        self.mouse_exit_image_label.setScaledContents(True)
        self.mouse_exit_image_label.setObjectName("mouse_exit_image_label")
        self.mouse_exit_vertical_layout.addWidget(self.mouse_exit_image_label)
        self.mouse_exit_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mouse_exit_name_label.sizePolicy().hasHeightForWidth())
        self.mouse_exit_name_label.setSizePolicy(sizePolicy)
        self.mouse_exit_name_label.setMinimumSize(QSize(0, 50))
        self.mouse_exit_name_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.mouse_exit_name_label.setFont(font)
        self.mouse_exit_name_label.setLayoutDirection(Qt.LeftToRight)
        self.mouse_exit_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.mouse_exit_name_label.setAlignment(Qt.AlignCenter)
        self.mouse_exit_name_label.setObjectName("mouse_exit_name_label")
        self.mouse_exit_vertical_layout.addWidget(self.mouse_exit_name_label)
        self.gridLayout_4.addLayout(
            self.mouse_exit_vertical_layout, 8, 3, 1, 1)
        spacerItem12 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem12, 2, 6, 1, 1)
        self.mouse_steering_vertical_layout = QVBoxLayout()
        self.mouse_steering_vertical_layout.setContentsMargins(-1, -1, 0, -1)
        self.mouse_steering_vertical_layout.setSpacing(0)
        self.mouse_steering_vertical_layout.setObjectName(
            "mouse_steering_vertical_layout")
        self.mouse_steering_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.mouse_steering_image_label.set_absolute_path(self.absolute_path)
        self.mouse_steering_image_label.set_name("mouse_steering")
        self.mouse_steering_image_label.setMinimumSize(QSize(180, 200))
        self.mouse_steering_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.mouse_steering_image_label.setText("")
        self.mouse_steering_image_label.setTextFormat(Qt.AutoText)
        self.mouse_steering_image_label.setPixmap(QPixmap
                                                  (self.absolute_path + "/gesture_images/mouse_stering_gestures/mouse_stering.png"))
        self.mouse_steering_image_label.setScaledContents(True)
        self.mouse_steering_image_label.setObjectName(
            "mouse_steering_image_label")
        self.mouse_steering_vertical_layout.addWidget(
            self.mouse_steering_image_label)
        self.mouse_sterring_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mouse_sterring_name_label.sizePolicy().hasHeightForWidth())
        self.mouse_sterring_name_label.setSizePolicy(sizePolicy)
        self.mouse_sterring_name_label.setMinimumSize(QSize(0, 50))
        self.mouse_sterring_name_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.mouse_sterring_name_label.setFont(font)
        self.mouse_sterring_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.mouse_sterring_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.mouse_sterring_name_label.setAlignment(Qt.AlignCenter)
        self.mouse_sterring_name_label.setObjectName(
            "mouse_sterring_name_label")
        self.mouse_steering_vertical_layout.addWidget(
            self.mouse_sterring_name_label)
        self.gridLayout_4.addLayout(
            self.mouse_steering_vertical_layout, 7, 2, 1, 1)
        self.thumb_up_vertical_layout = QVBoxLayout()
        self.thumb_up_vertical_layout.setSpacing(0)
        self.thumb_up_vertical_layout.setObjectName("thumb_up_vertical_layout")
        self.thumb_up_image_label = MyLabel(self.scrollAreaWidgetContents)
        self.thumb_up_image_label.set_absolute_path(self.absolute_path)
        self.thumb_up_image_label.set_name("thumb_up")
        self.thumb_up_image_label.setMinimumSize(QSize(180, 0))
        self.thumb_up_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.thumb_up_image_label.setText("")
        self.thumb_up_image_label.setTextFormat(Qt.AutoText)
        self.thumb_up_image_label.setPixmap(QPixmap
                                            (self.absolute_path + "/gesture_images/thumb_up.png"))
        self.thumb_up_image_label.setScaledContents(True)
        self.thumb_up_image_label.setObjectName("thumb_up_image_label")
        self.thumb_up_vertical_layout.addWidget(self.thumb_up_image_label)
        self.start_mouse_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.start_mouse_name_label.sizePolicy().hasHeightForWidth())
        self.start_mouse_name_label.setSizePolicy(sizePolicy)
        self.start_mouse_name_label.setMinimumSize(QSize(0, 50))
        self.start_mouse_name_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.start_mouse_name_label.setFont(font)
        self.start_mouse_name_label.setLayoutDirection(Qt.LeftToRight)
        self.start_mouse_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.start_mouse_name_label.setAlignment(Qt.AlignCenter)
        self.start_mouse_name_label.setObjectName("start_mouse_name_label")
        self.thumb_up_vertical_layout.addWidget(self.start_mouse_name_label)
        self.gridLayout_4.addLayout(self.thumb_up_vertical_layout, 7, 1, 1, 1)
        spacerItem13 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem13, 1, 0, 1, 1)
        self.druming_fingers_vertical_layout = QVBoxLayout()
        self.druming_fingers_vertical_layout.setSpacing(0)
        self.druming_fingers_vertical_layout.setObjectName(
            "druming_fingers_vertical_layout")
        self.druming_fingers_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.druming_fingers_image_label.set_absolute_path(self.absolute_path)
        self.druming_fingers_image_label.set_name("drumming_fingers")
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.druming_fingers_image_label.sizePolicy().hasHeightForWidth())
        self.druming_fingers_image_label.setSizePolicy(sizePolicy)
        self.druming_fingers_image_label.setMinimumSize(QSize(0, 200))
        self.druming_fingers_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.druming_fingers_image_label.setText("")
        self.druming_fingers_image_label.setTextFormat(Qt.AutoText)
        self.druming_fingers_image_label.setPixmap(QPixmap
                                                   (self.absolute_path + "/gesture_images/drumming_fingers.png"))
        self.druming_fingers_image_label.setScaledContents(True)
        self.druming_fingers_image_label.setObjectName(
            "druming_fingers_image_label")
        self.druming_fingers_vertical_layout.addWidget(
            self.druming_fingers_image_label)
        self.druming_fingers_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.druming_fingers_name_label.sizePolicy().hasHeightForWidth())
        self.druming_fingers_name_label.setSizePolicy(sizePolicy)
        self.druming_fingers_name_label.setMinimumSize(QSize(0, 50))
        self.druming_fingers_name_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.druming_fingers_name_label.setFont(font)
        self.druming_fingers_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.druming_fingers_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.druming_fingers_name_label.setAlignment(Qt.AlignCenter)
        self.druming_fingers_name_label.setObjectName(
            "druming_fingers_name_label")
        self.druming_fingers_vertical_layout.addWidget(
            self.druming_fingers_name_label)
        self.action1_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action1_comboBox.setFont(font)
        self.action1_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "outline-color: black;")
        self.action1_comboBox.setObjectName("action1_comboBox")
        self.druming_fingers_vertical_layout.addWidget(self.action1_comboBox)
        self.gridLayout_4.addLayout(
            self.druming_fingers_vertical_layout, 1, 5, 1, 1)
        self.swiping_up_vertical_layout = QVBoxLayout()
        self.swiping_up_vertical_layout.setSpacing(0)
        self.swiping_up_vertical_layout.setObjectName(
            "swiping_up_vertical_layout")
        self.swiping_up_image_label = MyLabel(self.scrollAreaWidgetContents)
        self.swiping_up_image_label.set_absolute_path(self.absolute_path)
        self.swiping_up_image_label.set_name("swiping_up")
        self.swiping_up_image_label.setMinimumSize(QSize(0, 200))
        self.swiping_up_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.swiping_up_image_label.setText("")
        self.swiping_up_image_label.setTextFormat(Qt.AutoText)
        self.swiping_up_image_label.setPixmap(QPixmap
                                              (self.absolute_path + "/gesture_images/swiping_up.png"))
        self.swiping_up_image_label.setScaledContents(True)
        self.swiping_up_image_label.setObjectName("swiping_up_image_label")
        self.swiping_up_vertical_layout.addWidget(self.swiping_up_image_label)
        self.swiping_up_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.swiping_up_name_label.sizePolicy().hasHeightForWidth())
        self.swiping_up_name_label.setSizePolicy(sizePolicy)
        self.swiping_up_name_label.setMinimumSize(QSize(0, 50))
        self.swiping_up_name_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.swiping_up_name_label.setFont(font)
        self.swiping_up_name_label.setLayoutDirection(Qt.LeftToRight)
        self.swiping_up_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.swiping_up_name_label.setAlignment(Qt.AlignCenter)
        self.swiping_up_name_label.setObjectName("swiping_up_name_label")
        self.swiping_up_vertical_layout.addWidget(self.swiping_up_name_label)
        self.action17_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action17_comboBox.setFont(font)
        self.action17_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "outline-color: black;")
        self.action17_comboBox.setObjectName("action17_comboBox")
        self.swiping_up_vertical_layout.addWidget(self.action17_comboBox)
        self.gridLayout_4.addLayout(
            self.swiping_up_vertical_layout, 2, 1, 1, 1)
        self.swiping_down_vertical_layout = QVBoxLayout()
        self.swiping_down_vertical_layout.setSpacing(0)
        self.swiping_down_vertical_layout.setObjectName(
            "swiping_down_vertical_layout")
        self.swiping_down_image_label = MyLabel(self.scrollAreaWidgetContents)
        self.swiping_down_image_label.set_absolute_path(self.absolute_path)
        self.swiping_down_image_label.set_name("swiping_down")
        self.swiping_down_image_label.setMinimumSize(QSize(0, 200))
        self.swiping_down_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.swiping_down_image_label.setText("")
        self.swiping_down_image_label.setTextFormat(Qt.AutoText)
        self.swiping_down_image_label.setPixmap(QPixmap
                                                (self.absolute_path + "/gesture_images/swiping_down.png"))
        self.swiping_down_image_label.setScaledContents(True)
        self.swiping_down_image_label.setObjectName("swiping_down_image_label")
        self.swiping_down_vertical_layout.addWidget(
            self.swiping_down_image_label)
        self.swiping_down_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.swiping_down_name_label.sizePolicy().hasHeightForWidth())
        self.swiping_down_name_label.setSizePolicy(sizePolicy)
        self.swiping_down_name_label.setMinimumSize(QSize(0, 50))
        self.swiping_down_name_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.swiping_down_name_label.setFont(font)
        self.swiping_down_name_label.setLayoutDirection(Qt.LeftToRight)
        self.swiping_down_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.swiping_down_name_label.setAlignment(Qt.AlignCenter)
        self.swiping_down_name_label.setObjectName("swiping_down_name_label")
        self.swiping_down_vertical_layout.addWidget(
            self.swiping_down_name_label)
        self.action14_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action14_comboBox.setFont(font)
        self.action14_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "outline-color: black;")
        self.action14_comboBox.setObjectName("action14_comboBox")
        self.swiping_down_vertical_layout.addWidget(self.action14_comboBox)
        self.gridLayout_4.addLayout(
            self.swiping_down_vertical_layout, 2, 2, 1, 1)
        self.rolling_hand_vertical_layout = QVBoxLayout()
        self.rolling_hand_vertical_layout.setSpacing(0)
        self.rolling_hand_vertical_layout.setObjectName(
            "rolling_hand_vertical_layout")
        self.rolling_hand_image_label = MyLabel(self.scrollAreaWidgetContents)
        self.rolling_hand_image_label.set_absolute_path(self.absolute_path)
        self.rolling_hand_image_label.set_name("rolling_hand_backward")
        self.rolling_hand_image_label.setMinimumSize(QSize(0, 200))
        self.rolling_hand_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.rolling_hand_image_label.setText("")
        self.rolling_hand_image_label.setTextFormat(Qt.AutoText)
        self.rolling_hand_image_label.setPixmap(QPixmap
                                                (self.absolute_path + "/gesture_images/rolling_hand_backward.png"))
        self.rolling_hand_image_label.setScaledContents(True)
        self.rolling_hand_image_label.setObjectName("rolling_hand_image_label")
        self.rolling_hand_vertical_layout.addWidget(
            self.rolling_hand_image_label)
        self.rolling_hand_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.rolling_hand_name_label.sizePolicy().hasHeightForWidth())
        self.rolling_hand_name_label.setSizePolicy(sizePolicy)
        self.rolling_hand_name_label.setMinimumSize(QSize(0, 50))
        self.rolling_hand_name_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.rolling_hand_name_label.setFont(font)
        self.rolling_hand_name_label.setLayoutDirection(Qt.LeftToRight)
        self.rolling_hand_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.rolling_hand_name_label.setAlignment(Qt.AlignCenter)
        self.rolling_hand_name_label.setObjectName("rolling_hand_name_label")
        self.rolling_hand_vertical_layout.addWidget(
            self.rolling_hand_name_label)
        self.action6_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action6_comboBox.setFont(font)
        self.action6_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "outline-color: black;")
        self.action6_comboBox.setObjectName("action6_comboBox")
        self.rolling_hand_vertical_layout.addWidget(self.action6_comboBox)
        self.gridLayout_4.addLayout(
            self.rolling_hand_vertical_layout, 5, 4, 1, 1)
        self.swiping_left_vertical_layout = QVBoxLayout()
        self.swiping_left_vertical_layout.setSpacing(0)
        self.swiping_left_vertical_layout.setObjectName(
            "swiping_left_vertical_layout")
        self.swiping_left_image_label = MyLabel(self.scrollAreaWidgetContents)
        self.swiping_left_image_label.set_absolute_path(self.absolute_path)
        self.swiping_left_image_label.set_name("swiping_left")
        self.swiping_left_image_label.setMinimumSize(QSize(0, 200))
        self.swiping_left_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.swiping_left_image_label.setText("")
        self.swiping_left_image_label.setTextFormat(Qt.AutoText)
        self.swiping_left_image_label.setPixmap(QPixmap
                                                (self.absolute_path + "/gesture_images/swiping_left.png"))
        self.swiping_left_image_label.setScaledContents(True)
        self.swiping_left_image_label.setObjectName("swiping_left_image_label")
        self.swiping_left_vertical_layout.addWidget(
            self.swiping_left_image_label)
        self.swiping_left_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.swiping_left_name_label.sizePolicy().hasHeightForWidth())
        self.swiping_left_name_label.setSizePolicy(sizePolicy)
        self.swiping_left_name_label.setMinimumSize(QSize(0, 50))
        self.swiping_left_name_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.swiping_left_name_label.setFont(font)
        self.swiping_left_name_label.setLayoutDirection(Qt.LeftToRight)
        self.swiping_left_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.swiping_left_name_label.setAlignment(Qt.AlignCenter)
        self.swiping_left_name_label.setObjectName("swiping_left_name_label")
        self.swiping_left_vertical_layout.addWidget(
            self.swiping_left_name_label)
        self.action15_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action15_comboBox.setFont(font)
        self.action15_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "outline-color: black;")
        self.action15_comboBox.setObjectName("action15_comboBox")
        self.swiping_left_vertical_layout.addWidget(self.action15_comboBox)
        self.gridLayout_4.addLayout(
            self.swiping_left_vertical_layout, 2, 3, 1, 1)
        self.rolling_hand_forward_vertical_layout = QVBoxLayout()
        self.rolling_hand_forward_vertical_layout.setSpacing(0)
        self.rolling_hand_forward_vertical_layout.setObjectName(
            "rolling_hand_forward_vertical_layout")
        self.rolling_hand_forward_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.rolling_hand_forward_image_label.set_absolute_path(
            self.absolute_path)
        self.rolling_hand_forward_image_label.set_name("rolling_hand_forward")
        self.rolling_hand_forward_image_label.setMinimumSize(
            QSize(0, 200))
        self.rolling_hand_forward_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.rolling_hand_forward_image_label.setText("")
        self.rolling_hand_forward_image_label.setTextFormat(Qt.AutoText)
        self.rolling_hand_forward_image_label.setPixmap(QPixmap
                                                        (self.absolute_path + "/gesture_images/rolling_hand_forward.png"))
        self.rolling_hand_forward_image_label.setScaledContents(True)
        self.rolling_hand_forward_image_label.setObjectName(
            "rolling_hand_forward_image_label")
        self.rolling_hand_forward_vertical_layout.addWidget(
            self.rolling_hand_forward_image_label)
        self.rolling_hand_forward_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.rolling_hand_forward_name_label.sizePolicy().hasHeightForWidth())
        self.rolling_hand_forward_name_label.setSizePolicy(sizePolicy)
        self.rolling_hand_forward_name_label.setMinimumSize(
            QSize(0, 50))
        self.rolling_hand_forward_name_label.setSizeIncrement(
            QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.rolling_hand_forward_name_label.setFont(font)
        self.rolling_hand_forward_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.rolling_hand_forward_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.rolling_hand_forward_name_label.setAlignment(
            Qt.AlignCenter)
        self.rolling_hand_forward_name_label.setObjectName(
            "rolling_hand_forward_name_label")
        self.rolling_hand_forward_vertical_layout.addWidget(
            self.rolling_hand_forward_name_label)
        self.action7_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action7_comboBox.setFont(font)
        self.action7_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "outline-color: black;")
        self.action7_comboBox.setObjectName("action7_comboBox")
        self.rolling_hand_forward_vertical_layout.addWidget(
            self.action7_comboBox)
        self.gridLayout_4.addLayout(
            self.rolling_hand_forward_vertical_layout, 5, 3, 1, 1)
        self.swiping_right_vertical_layout = QVBoxLayout()
        self.swiping_right_vertical_layout.setSpacing(0)
        self.swiping_right_vertical_layout.setObjectName(
            "swiping_right_vertical_layout")
        self.swiping_right_image_label = MyLabel(self.scrollAreaWidgetContents)
        self.swiping_right_image_label.set_absolute_path(self.absolute_path)
        self.swiping_right_image_label.set_name("swiping_right")
        self.swiping_right_image_label.setMinimumSize(QSize(0, 200))
        self.swiping_right_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.swiping_right_image_label.setText("")
        self.swiping_right_image_label.setTextFormat(Qt.AutoText)
        self.swiping_right_image_label.setPixmap(QPixmap
                                                 (self.absolute_path + "/gesture_images/swiping_right.png"))
        self.swiping_right_image_label.setScaledContents(True)
        self.swiping_right_image_label.setObjectName(
            "swiping_right_image_label")
        self.swiping_right_vertical_layout.addWidget(
            self.swiping_right_image_label)
        self.swiping_right_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.swiping_right_name_label.sizePolicy().hasHeightForWidth())
        self.swiping_right_name_label.setSizePolicy(sizePolicy)
        self.swiping_right_name_label.setMinimumSize(QSize(0, 50))
        self.swiping_right_name_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.swiping_right_name_label.setFont(font)
        self.swiping_right_name_label.setLayoutDirection(Qt.LeftToRight)
        self.swiping_right_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.swiping_right_name_label.setAlignment(Qt.AlignCenter)
        self.swiping_right_name_label.setObjectName("swiping_right_name_label")
        self.swiping_right_vertical_layout.addWidget(
            self.swiping_right_name_label)
        self.action16_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action16_comboBox.setFont(font)
        self.action16_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "outline-color: black;")
        self.action16_comboBox.setObjectName("action16_comboBox")
        self.swiping_right_vertical_layout.addWidget(self.action16_comboBox)
        self.gridLayout_4.addLayout(
            self.swiping_right_vertical_layout, 2, 4, 1, 1)
        self.stop_sign_vertical_layout = QVBoxLayout()
        self.stop_sign_vertical_layout.setSpacing(0)
        self.stop_sign_vertical_layout.setObjectName(
            "stop_sign_vertical_layout")
        self.stop_sign_image_label = MyLabel(self.scrollAreaWidgetContents)
        self.stop_sign_image_label.set_absolute_path(self.absolute_path)
        self.stop_sign_image_label.set_name("stop_sign")
        self.stop_sign_image_label.setMinimumSize(QSize(0, 200))
        self.stop_sign_image_label.setAutoFillBackground(False)
        self.stop_sign_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.stop_sign_image_label.setText("")
        self.stop_sign_image_label.setTextFormat(Qt.AutoText)
        self.stop_sign_image_label.setPixmap(QPixmap
                                             (self.absolute_path + "/gesture_images/stop_sign.png"))
        self.stop_sign_image_label.setScaledContents(True)
        self.stop_sign_image_label.setObjectName("stop_sign_image_label")
        self.stop_sign_vertical_layout.addWidget(self.stop_sign_image_label)
        self.stop_sign_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.stop_sign_name_label.sizePolicy().hasHeightForWidth())
        self.stop_sign_name_label.setSizePolicy(sizePolicy)
        self.stop_sign_name_label.setMinimumSize(QSize(0, 50))
        self.stop_sign_name_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.stop_sign_name_label.setFont(font)
        self.stop_sign_name_label.setLayoutDirection(Qt.LeftToRight)
        self.stop_sign_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.stop_sign_name_label.setAlignment(Qt.AlignCenter)
        self.stop_sign_name_label.setObjectName("stop_sign_name_label")
        self.stop_sign_vertical_layout.addWidget(self.stop_sign_name_label)
        self.action13_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action13_comboBox.setFont(font)
        self.action13_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "outline-color: black;")
        self.action13_comboBox.setObjectName("action13_comboBox")
        self.stop_sign_vertical_layout.addWidget(self.action13_comboBox)
        self.gridLayout_4.addLayout(self.stop_sign_vertical_layout, 3, 5, 1, 1)
        self.thumb_down_vertical_layout = QVBoxLayout()
        self.thumb_down_vertical_layout.setSpacing(0)
        self.thumb_down_vertical_layout.setObjectName(
            "thumb_down_vertical_layout")
        self.thumb_down_image_label = MyLabel(self.scrollAreaWidgetContents)
        self.thumb_down_image_label.set_absolute_path(self.absolute_path)
        self.thumb_down_image_label.set_name("thumb_down")
        self.thumb_down_image_label.setMinimumSize(QSize(0, 200))
        self.thumb_down_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.thumb_down_image_label.setText("")
        self.thumb_down_image_label.setTextFormat(Qt.AutoText)
        self.thumb_down_image_label.setPixmap(QPixmap
                                              (self.absolute_path + "/gesture_images/thumb_down.png"))
        self.thumb_down_image_label.setScaledContents(True)
        self.thumb_down_image_label.setObjectName("thumb_down_image_label")
        self.thumb_down_vertical_layout.addWidget(self.thumb_down_image_label)
        self.thumb_down_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.thumb_down_name_label.sizePolicy().hasHeightForWidth())
        self.thumb_down_name_label.setSizePolicy(sizePolicy)
        self.thumb_down_name_label.setMinimumSize(QSize(0, 50))
        self.thumb_down_name_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.thumb_down_name_label.setFont(font)
        self.thumb_down_name_label.setLayoutDirection(Qt.LeftToRight)
        self.thumb_down_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.thumb_down_name_label.setAlignment(Qt.AlignCenter)
        self.thumb_down_name_label.setObjectName("thumb_down_name_label")
        self.thumb_down_vertical_layout.addWidget(self.thumb_down_name_label)
        self.action18_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action18_comboBox.setFont(font)
        self.action18_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "outline-color: black;")
        self.action18_comboBox.setObjectName("action18_comboBox")
        self.thumb_down_vertical_layout.addWidget(self.action18_comboBox)
        self.gridLayout_4.addLayout(
            self.thumb_down_vertical_layout, 2, 5, 1, 1)
        self.sliding_two_fingers_down_vertical_layout_2 = QVBoxLayout()
        self.sliding_two_fingers_down_vertical_layout_2.setSpacing(0)
        self.sliding_two_fingers_down_vertical_layout_2.setObjectName(
            "sliding_two_fingers_down_vertical_layout_2")
        self.shaking_hand_image_label = MyLabel(self.scrollAreaWidgetContents)
        self.shaking_hand_image_label.set_absolute_path(self.absolute_path)
        self.shaking_hand_image_label.set_name("shaking_hand")
        self.shaking_hand_image_label.setMinimumSize(QSize(0, 200))
        self.shaking_hand_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.shaking_hand_image_label.setText("")
        self.shaking_hand_image_label.setTextFormat(Qt.AutoText)
        self.shaking_hand_image_label.setPixmap(QPixmap
                                                (self.absolute_path + "/gesture_images/shaking_hand.png"))
        self.shaking_hand_image_label.setScaledContents(True)
        self.shaking_hand_image_label.setObjectName("shaking_hand_image_label")
        self.sliding_two_fingers_down_vertical_layout_2.addWidget(
            self.shaking_hand_image_label)
        self.shaking_hand_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.shaking_hand_name_label.sizePolicy().hasHeightForWidth())
        self.shaking_hand_name_label.setSizePolicy(sizePolicy)
        self.shaking_hand_name_label.setMinimumSize(QSize(0, 50))
        self.shaking_hand_name_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.shaking_hand_name_label.setFont(font)
        self.shaking_hand_name_label.setLayoutDirection(Qt.LeftToRight)
        self.shaking_hand_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.shaking_hand_name_label.setAlignment(Qt.AlignCenter)
        self.shaking_hand_name_label.setObjectName("shaking_hand_name_label")
        self.sliding_two_fingers_down_vertical_layout_2.addWidget(
            self.shaking_hand_name_label)
        self.action8_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action8_comboBox.setFont(font)
        self.action8_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "outline-color: black;")
        self.action8_comboBox.setObjectName("action8_comboBox")
        self.sliding_two_fingers_down_vertical_layout_2.addWidget(
            self.action8_comboBox)
        self.gridLayout_4.addLayout(
            self.sliding_two_fingers_down_vertical_layout_2, 4, 1, 1, 1)
        self.zooming_out_with_full_hand_vertical_layout = QVBoxLayout()
        self.zooming_out_with_full_hand_vertical_layout.setSpacing(0)
        self.zooming_out_with_full_hand_vertical_layout.setObjectName(
            "zooming_out_with_fiull_hand_vertical_layout")
        self.zooming_out_with_fiull_hand_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.zooming_out_with_fiull_hand_image_label.set_absolute_path(
            self.absolute_path)
        self.zooming_out_with_fiull_hand_image_label.set_name(
            "zooming_out_with_full_hand")
        self.zooming_out_with_fiull_hand_image_label.setMinimumSize(
            QSize(0, 200))
        self.zooming_out_with_fiull_hand_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.zooming_out_with_fiull_hand_image_label.setText("")
        self.zooming_out_with_fiull_hand_image_label.setTextFormat(
            Qt.AutoText)
        self.zooming_out_with_fiull_hand_image_label.setPixmap(QPixmap
                                                               (self.absolute_path + "/gesture_images/zooming_out_with_full_hand.png"))
        self.zooming_out_with_fiull_hand_image_label.setScaledContents(True)
        self.zooming_out_with_fiull_hand_image_label.setObjectName(
            "zooming_out_with_fiull_hand_image_label")
        self.zooming_out_with_full_hand_vertical_layout.addWidget(
            self.zooming_out_with_fiull_hand_image_label)
        self.zooming_out_with_full_hand_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.zooming_out_with_full_hand_name_label.sizePolicy().hasHeightForWidth())
        self.zooming_out_with_full_hand_name_label.setSizePolicy(sizePolicy)
        self.zooming_out_with_full_hand_name_label.setMinimumSize(
            QSize(0, 50))
        self.zooming_out_with_full_hand_name_label.setSizeIncrement(
            QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.zooming_out_with_full_hand_name_label.setFont(font)
        self.zooming_out_with_full_hand_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.zooming_out_with_full_hand_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.zooming_out_with_full_hand_name_label.setAlignment(
            Qt.AlignCenter)
        self.zooming_out_with_full_hand_name_label.setObjectName(
            "zooming_out_with_fiull_hand_name_label")
        self.zooming_out_with_full_hand_vertical_layout.addWidget(
            self.zooming_out_with_full_hand_name_label)
        self.action24_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action24_comboBox.setFont(font)
        self.action24_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "outline-color: black;")
        self.action24_comboBox.setObjectName("action24_comboBox")
        self.zooming_out_with_full_hand_vertical_layout.addWidget(
            self.action24_comboBox)
        self.gridLayout_4.addLayout(
            self.zooming_out_with_full_hand_vertical_layout, 1, 4, 1, 1)
        self.zooming_in_with_full_hand_vertical_layout = QVBoxLayout()
        self.zooming_in_with_full_hand_vertical_layout.setSpacing(0)
        self.zooming_in_with_full_hand_vertical_layout.setObjectName(
            "zooming_in_with_full_hand_vertical_layout")
        self.zooming_in_with_full_hand_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.zooming_in_with_full_hand_image_label.set_absolute_path(
            self.absolute_path)
        self.zooming_in_with_full_hand_image_label.set_name(
            "zooming_in_with_full_hand")
        self.zooming_in_with_full_hand_image_label.setMinimumSize(
            QSize(0, 200))
        self.zooming_in_with_full_hand_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.zooming_in_with_full_hand_image_label.setText("")
        self.zooming_in_with_full_hand_image_label.setTextFormat(
            Qt.AutoText)
        self.zooming_in_with_full_hand_image_label.setPixmap(QPixmap
                                                             (self.absolute_path + "/gesture_images/zooming_in_with_full_hand.png"))
        self.zooming_in_with_full_hand_image_label.setScaledContents(True)
        self.zooming_in_with_full_hand_image_label.setObjectName(
            "zooming_in_with_full_hand_image_label")
        self.zooming_in_with_full_hand_vertical_layout.addWidget(
            self.zooming_in_with_full_hand_image_label)
        self.zooming_in_with_full_hand_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.zooming_in_with_full_hand_name_label.sizePolicy().hasHeightForWidth())
        self.zooming_in_with_full_hand_name_label.setSizePolicy(sizePolicy)
        self.zooming_in_with_full_hand_name_label.setMinimumSize(
            QSize(0, 50))
        self.zooming_in_with_full_hand_name_label.setSizeIncrement(
            QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.zooming_in_with_full_hand_name_label.setFont(font)
        self.zooming_in_with_full_hand_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.zooming_in_with_full_hand_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.zooming_in_with_full_hand_name_label.setAlignment(
            Qt.AlignCenter)
        self.zooming_in_with_full_hand_name_label.setObjectName(
            "zooming_in_with_full_hand_name_label")
        self.zooming_in_with_full_hand_vertical_layout.addWidget(
            self.zooming_in_with_full_hand_name_label)
        self.action22_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action22_comboBox.setFont(font)
        self.action22_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "outline-color: black;")
        self.action22_comboBox.setObjectName("action22_comboBox")
        self.zooming_in_with_full_hand_vertical_layout.addWidget(
            self.action22_comboBox)
        self.gridLayout_4.addLayout(
            self.zooming_in_with_full_hand_vertical_layout, 1, 3, 1, 1)
        self.zooming_in_with_two_fing_vertical_layout = QVBoxLayout()
        self.zooming_in_with_two_fing_vertical_layout.setSpacing(0)
        self.zooming_in_with_two_fing_vertical_layout.setObjectName(
            "zooming_in_with_two_fing_vertical_layout")
        self.zooming_in_with_two_fing_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.zooming_in_with_two_fing_image_label.set_absolute_path(
            self.absolute_path)
        self.zooming_in_with_two_fing_image_label.set_name(
            "zooming_in_with_two_fingers")
        self.zooming_in_with_two_fing_image_label.setMinimumSize(
            QSize(0, 200))
        self.zooming_in_with_two_fing_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.zooming_in_with_two_fing_image_label.setText("")
        self.zooming_in_with_two_fing_image_label.setTextFormat(
            Qt.AutoText)
        self.zooming_in_with_two_fing_image_label.setPixmap(QPixmap
                                                            (self.absolute_path + "/gesture_images/zooming_in_with_two_fingers.png"))
        self.zooming_in_with_two_fing_image_label.setScaledContents(True)
        self.zooming_in_with_two_fing_image_label.setObjectName(
            "zooming_in_with_two_fing_image_label")
        self.zooming_in_with_two_fing_vertical_layout.addWidget(
            self.zooming_in_with_two_fing_image_label)
        self.zooming_in_with_two_fing_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.zooming_in_with_two_fing_name_label.sizePolicy().hasHeightForWidth())
        self.zooming_in_with_two_fing_name_label.setSizePolicy(sizePolicy)
        self.zooming_in_with_two_fing_name_label.setMinimumSize(
            QSize(0, 50))
        self.zooming_in_with_two_fing_name_label.setSizeIncrement(
            QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.zooming_in_with_two_fing_name_label.setFont(font)
        self.zooming_in_with_two_fing_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.zooming_in_with_two_fing_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.zooming_in_with_two_fing_name_label.setAlignment(
            Qt.AlignCenter)
        self.zooming_in_with_two_fing_name_label.setObjectName(
            "zooming_in_with_two_fing_name_label")
        self.zooming_in_with_two_fing_vertical_layout.addWidget(
            self.zooming_in_with_two_fing_name_label)
        self.action23_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action23_comboBox.setFont(font)
        self.action23_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "outline-color: black;")
        self.action23_comboBox.setObjectName("action23_comboBox")
        self.zooming_in_with_two_fing_vertical_layout.addWidget(
            self.action23_comboBox)
        self.gridLayout_4.addLayout(
            self.zooming_in_with_two_fing_vertical_layout, 1, 1, 1, 1)
        self.zooming_out_with_two_fing_vertical_layout = QVBoxLayout()
        self.zooming_out_with_two_fing_vertical_layout.setSpacing(0)
        self.zooming_out_with_two_fing_vertical_layout.setObjectName(
            "zooming_out_with_two_fing_vertical_layout")
        self.zooming_out_with_two_fing_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.zooming_out_with_two_fing_image_label.set_absolute_path(
            self.absolute_path)
        self.zooming_out_with_two_fing_image_label.set_name(
            "zooming_out_with_two_fingers")
        self.zooming_out_with_two_fing_image_label.setMinimumSize(
            QSize(0, 200))
        self.zooming_out_with_two_fing_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.zooming_out_with_two_fing_image_label.setText("")
        self.zooming_out_with_two_fing_image_label.setTextFormat(
            Qt.AutoText)
        self.zooming_out_with_two_fing_image_label.setPixmap(QPixmap
                                                             (self.absolute_path + "/gesture_images/zooming_out_with_2_fingers.png"))
        self.zooming_out_with_two_fing_image_label.setScaledContents(True)
        self.zooming_out_with_two_fing_image_label.setObjectName(
            "zooming_out_with_two_fing_image_label")
        self.zooming_out_with_two_fing_vertical_layout.addWidget(
            self.zooming_out_with_two_fing_image_label)
        self.zooming_out_with_two_fing_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.zooming_out_with_two_fing_name_label.sizePolicy().hasHeightForWidth())
        self.zooming_out_with_two_fing_name_label.setSizePolicy(sizePolicy)
        self.zooming_out_with_two_fing_name_label.setMinimumSize(
            QSize(0, 50))
        self.zooming_out_with_two_fing_name_label.setSizeIncrement(
            QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.zooming_out_with_two_fing_name_label.setFont(font)
        self.zooming_out_with_two_fing_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.zooming_out_with_two_fing_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.zooming_out_with_two_fing_name_label.setAlignment(
            Qt.AlignCenter)
        self.zooming_out_with_two_fing_name_label.setObjectName(
            "zooming_out_with_two_fing_name_label")
        self.zooming_out_with_two_fing_vertical_layout.addWidget(
            self.zooming_out_with_two_fing_name_label)
        self.action25_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action25_comboBox.setFont(font)
        self.action25_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "outline-color: black;")
        self.action25_comboBox.setObjectName("action25_comboBox")
        self.zooming_out_with_two_fing_vertical_layout.addWidget(
            self.action25_comboBox)
        self.gridLayout_4.addLayout(
            self.zooming_out_with_two_fing_vertical_layout, 1, 2, 1, 1)
        self.turrning_hand_clock_vertical_layout = QVBoxLayout()
        self.turrning_hand_clock_vertical_layout.setSpacing(0)
        self.turrning_hand_clock_vertical_layout.setObjectName(
            "turrning_hand_clock_vertical_layout")
        self.turrning_hand_clock_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.turrning_hand_clock_image_label.set_absolute_path(
            self.absolute_path)
        self.turrning_hand_clock_image_label.set_name("turning_hand_clockwise")
        self.turrning_hand_clock_image_label.setMinimumSize(
            QSize(0, 200))
        self.turrning_hand_clock_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.turrning_hand_clock_image_label.setText("")
        self.turrning_hand_clock_image_label.setTextFormat(Qt.AutoText)
        self.turrning_hand_clock_image_label.setPixmap(QPixmap
                                                       (self.absolute_path + "/gesture_images/turning_hand_clockwise.png"))
        self.turrning_hand_clock_image_label.setScaledContents(True)
        self.turrning_hand_clock_image_label.setObjectName(
            "turrning_hand_clock_image_label")
        self.turrning_hand_clock_vertical_layout.addWidget(
            self.turrning_hand_clock_image_label)
        self.turrning_hand_clock_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.turrning_hand_clock_name_label.sizePolicy().hasHeightForWidth())
        self.turrning_hand_clock_name_label.setSizePolicy(sizePolicy)
        self.turrning_hand_clock_name_label.setMinimumSize(QSize(0, 50))
        self.turrning_hand_clock_name_label.setSizeIncrement(
            QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.turrning_hand_clock_name_label.setFont(font)
        self.turrning_hand_clock_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.turrning_hand_clock_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.turrning_hand_clock_name_label.setAlignment(Qt.AlignCenter)
        self.turrning_hand_clock_name_label.setObjectName(
            "turrning_hand_clock_name_label")
        self.turrning_hand_clock_vertical_layout.addWidget(
            self.turrning_hand_clock_name_label)
        self.action20_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action20_comboBox.setFont(font)
        self.action20_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "outline-color: black;")
        self.action20_comboBox.setObjectName("action20_comboBox")
        self.turrning_hand_clock_vertical_layout.addWidget(
            self.action20_comboBox)
        self.gridLayout_4.addLayout(
            self.turrning_hand_clock_vertical_layout, 5, 1, 1, 1)
        self.pulling_hand_in_vertical_layout = QVBoxLayout()
        self.pulling_hand_in_vertical_layout.setSpacing(0)
        self.pulling_hand_in_vertical_layout.setObjectName(
            "pulling_hand_in_vertical_layout")
        self.pulling_hand_in_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.pulling_hand_in_image_label.set_absolute_path(self.absolute_path)
        self.pulling_hand_in_image_label.set_name("pulling_hand_in")
        self.pulling_hand_in_image_label.setMinimumSize(QSize(0, 200))
        self.pulling_hand_in_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.pulling_hand_in_image_label.setText("")
        self.pulling_hand_in_image_label.setTextFormat(Qt.AutoText)
        self.pulling_hand_in_image_label.setPixmap(QPixmap
                                                   (self.absolute_path + "/gesture_images/pulling_hand_in.png"))
        self.pulling_hand_in_image_label.setScaledContents(True)
        self.pulling_hand_in_image_label.setObjectName(
            "pulling_hand_in_image_label")
        self.pulling_hand_in_vertical_layout.addWidget(
            self.pulling_hand_in_image_label)
        self.pulling_hand_in_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pulling_hand_in_name_label.sizePolicy().hasHeightForWidth())
        self.pulling_hand_in_name_label.setSizePolicy(sizePolicy)
        self.pulling_hand_in_name_label.setMinimumSize(QSize(0, 50))
        self.pulling_hand_in_name_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pulling_hand_in_name_label.setFont(font)
        self.pulling_hand_in_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.pulling_hand_in_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.pulling_hand_in_name_label.setAlignment(Qt.AlignCenter)
        self.pulling_hand_in_name_label.setObjectName(
            "pulling_hand_in_name_label")
        self.pulling_hand_in_vertical_layout.addWidget(
            self.pulling_hand_in_name_label)
        self.action2_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action2_comboBox.setFont(font)
        self.action2_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "outline-color: black;")
        self.action2_comboBox.setObjectName("action2_comboBox")
        self.pulling_hand_in_vertical_layout.addWidget(self.action2_comboBox)
        self.gridLayout_4.addLayout(
            self.pulling_hand_in_vertical_layout, 4, 4, 1, 1)
        self.pushing_hand_away_vertical_layout = QVBoxLayout()
        self.pushing_hand_away_vertical_layout.setSpacing(0)
        self.pushing_hand_away_vertical_layout.setObjectName(
            "pushing_hand_away_vertical_layout")
        self.pushing_hand_away_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.pushing_hand_away_image_label.set_absolute_path(
            self.absolute_path)
        self.pushing_hand_away_image_label.set_name("pushing_hand_away")
        self.pushing_hand_away_image_label.setMinimumSize(QSize(0, 200))
        self.pushing_hand_away_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.pushing_hand_away_image_label.setText("")
        self.pushing_hand_away_image_label.setTextFormat(Qt.AutoText)
        self.pushing_hand_away_image_label.setPixmap(QPixmap
                                                     (self.absolute_path + "/gesture_images/pushing_hand_away.png"))
        self.pushing_hand_away_image_label.setScaledContents(True)
        self.pushing_hand_away_image_label.setObjectName(
            "pushing_hand_away_image_label")
        self.pushing_hand_away_vertical_layout.addWidget(
            self.pushing_hand_away_image_label)
        self.pushing_hand_away_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushing_hand_away_name_label.sizePolicy().hasHeightForWidth())
        self.pushing_hand_away_name_label.setSizePolicy(sizePolicy)
        self.pushing_hand_away_name_label.setMinimumSize(QSize(0, 50))
        self.pushing_hand_away_name_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushing_hand_away_name_label.setFont(font)
        self.pushing_hand_away_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.pushing_hand_away_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.pushing_hand_away_name_label.setAlignment(Qt.AlignCenter)
        self.pushing_hand_away_name_label.setObjectName(
            "pushing_hand_away_name_label")
        self.pushing_hand_away_vertical_layout.addWidget(
            self.pushing_hand_away_name_label)
        self.action4_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action4_comboBox.setFont(font)
        self.action4_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "outline-color: black;")
        self.action4_comboBox.setObjectName("action4_comboBox")
        self.pushing_hand_away_vertical_layout.addWidget(self.action4_comboBox)
        self.gridLayout_4.addLayout(
            self.pushing_hand_away_vertical_layout, 4, 5, 1, 1)
        self.pulling_two_fingers_in_vertical_layout = QVBoxLayout()
        self.pulling_two_fingers_in_vertical_layout.setSpacing(0)
        self.pulling_two_fingers_in_vertical_layout.setObjectName(
            "pulling_two_fingers_in_vertical_layout")
        self.pulling_two_fingers_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.pulling_two_fingers_image_label.set_absolute_path(
            self.absolute_path)
        self.pulling_two_fingers_image_label.set_name("pulling_two_fingers_in")
        self.pulling_two_fingers_image_label.setMinimumSize(
            QSize(0, 200))
        self.pulling_two_fingers_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.pulling_two_fingers_image_label.setText("")
        self.pulling_two_fingers_image_label.setTextFormat(Qt.AutoText)
        self.pulling_two_fingers_image_label.setPixmap(QPixmap
                                                       (self.absolute_path + "/gesture_images/pulling_two_fingers_in.png"))
        self.pulling_two_fingers_image_label.setScaledContents(True)
        self.pulling_two_fingers_image_label.setObjectName(
            "pulling_two_fingers_image_label")
        self.pulling_two_fingers_in_vertical_layout.addWidget(
            self.pulling_two_fingers_image_label)
        self.pulling_two_fingers_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pulling_two_fingers_name_label.sizePolicy().hasHeightForWidth())
        self.pulling_two_fingers_name_label.setSizePolicy(sizePolicy)
        self.pulling_two_fingers_name_label.setMinimumSize(QSize(0, 50))
        self.pulling_two_fingers_name_label.setSizeIncrement(
            QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pulling_two_fingers_name_label.setFont(font)
        self.pulling_two_fingers_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.pulling_two_fingers_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.pulling_two_fingers_name_label.setAlignment(Qt.AlignCenter)
        self.pulling_two_fingers_name_label.setObjectName(
            "pulling_two_fingers_name_label")
        self.pulling_two_fingers_in_vertical_layout.addWidget(
            self.pulling_two_fingers_name_label)
        self.action3_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action3_comboBox.setFont(font)
        self.action3_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "outline-color: black;")
        self.action3_comboBox.setObjectName("action3_comboBox")
        self.pulling_two_fingers_in_vertical_layout.addWidget(
            self.action3_comboBox)
        self.gridLayout_4.addLayout(
            self.pulling_two_fingers_in_vertical_layout, 4, 2, 1, 1)
        self.pushing_two_fingers_away_vertical_layout = QVBoxLayout()
        self.pushing_two_fingers_away_vertical_layout.setSpacing(0)
        self.pushing_two_fingers_away_vertical_layout.setObjectName(
            "pushing_two_fingers_away_vertical_layout")
        self.pushing_two_fingers_away_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.pushing_two_fingers_away_image_label.set_absolute_path(
            self.absolute_path)
        self.pushing_two_fingers_away_image_label.set_name(
            "pushing_two_fingers_away")
        self.pushing_two_fingers_away_image_label.setMinimumSize(
            QSize(0, 200))
        self.pushing_two_fingers_away_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.pushing_two_fingers_away_image_label.setText("")
        self.pushing_two_fingers_away_image_label.setTextFormat(
            Qt.AutoText)
        self.pushing_two_fingers_away_image_label.setPixmap(QPixmap
                                                            (self.absolute_path + "/gesture_images/pushing_two_finger_away.png"))
        self.pushing_two_fingers_away_image_label.setScaledContents(True)
        self.pushing_two_fingers_away_image_label.setObjectName(
            "pushing_two_fingers_away_image_label")
        self.pushing_two_fingers_away_vertical_layout.addWidget(
            self.pushing_two_fingers_away_image_label)
        self.pushing_two_fingers_away_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushing_two_fingers_away_name_label.sizePolicy().hasHeightForWidth())
        self.pushing_two_fingers_away_name_label.setSizePolicy(sizePolicy)
        self.pushing_two_fingers_away_name_label.setMinimumSize(
            QSize(0, 50))
        self.pushing_two_fingers_away_name_label.setSizeIncrement(
            QSize(0, 0))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushing_two_fingers_away_name_label.setFont(font)
        self.pushing_two_fingers_away_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.pushing_two_fingers_away_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.pushing_two_fingers_away_name_label.setAlignment(
            Qt.AlignCenter)
        self.pushing_two_fingers_away_name_label.setObjectName(
            "pushing_two_fingers_away_name_label")
        self.pushing_two_fingers_away_vertical_layout.addWidget(
            self.pushing_two_fingers_away_name_label)
        self.action5_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action5_comboBox.setFont(font)
        self.action5_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "outline-color: black;")
        self.action5_comboBox.setObjectName("action5_comboBox")
        self.pushing_two_fingers_away_vertical_layout.addWidget(
            self.action5_comboBox)
        self.gridLayout_4.addLayout(
            self.pushing_two_fingers_away_vertical_layout, 4, 3, 1, 1)
        self.sliding_two_fingers_left_vertical_layout = QVBoxLayout()
        self.sliding_two_fingers_left_vertical_layout.setSpacing(0)
        self.sliding_two_fingers_left_vertical_layout.setObjectName(
            "sliding_two_fingers_left_vertical_layout")
        self.sliding_two_fingers_left_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.sliding_two_fingers_left_image_label.set_absolute_path(
            self.absolute_path)
        self.sliding_two_fingers_left_image_label.set_name(
            "sliding_two_fingers_left")
        self.sliding_two_fingers_left_image_label.setMinimumSize(
            QSize(0, 200))
        self.sliding_two_fingers_left_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.sliding_two_fingers_left_image_label.setText("")
        self.sliding_two_fingers_left_image_label.setTextFormat(
            Qt.AutoText)
        self.sliding_two_fingers_left_image_label.setPixmap(QPixmap
                                                            (self.absolute_path + "/gesture_images/sliding_two_finger_left.png"))
        self.sliding_two_fingers_left_image_label.setScaledContents(True)
        self.sliding_two_fingers_left_image_label.setObjectName(
            "sliding_two_fingers_left_image_label")
        self.sliding_two_fingers_left_vertical_layout.addWidget(
            self.sliding_two_fingers_left_image_label)
        self.sliding_two_fingers_left_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sliding_two_fingers_left_name_label.sizePolicy().hasHeightForWidth())
        self.sliding_two_fingers_left_name_label.setSizePolicy(sizePolicy)
        self.sliding_two_fingers_left_name_label.setMinimumSize(
            QSize(0, 50))
        self.sliding_two_fingers_left_name_label.setSizeIncrement(
            QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.sliding_two_fingers_left_name_label.setFont(font)
        self.sliding_two_fingers_left_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.sliding_two_fingers_left_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.sliding_two_fingers_left_name_label.setAlignment(
            Qt.AlignCenter)
        self.sliding_two_fingers_left_name_label.setObjectName(
            "sliding_two_fingers_left_name_label")
        self.sliding_two_fingers_left_vertical_layout.addWidget(
            self.sliding_two_fingers_left_name_label)
        self.action10_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action10_comboBox.setFont(font)
        self.action10_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "outline-color: black;")
        self.action10_comboBox.setObjectName("action10_comboBox")
        self.sliding_two_fingers_left_vertical_layout.addWidget(
            self.action10_comboBox)
        self.gridLayout_4.addLayout(
            self.sliding_two_fingers_left_vertical_layout, 3, 1, 1, 1)
        self.sliding_two_fingers_right_vertical_layout = QVBoxLayout()
        self.sliding_two_fingers_right_vertical_layout.setSpacing(0)
        self.sliding_two_fingers_right_vertical_layout.setObjectName(
            "sliding_two_fingers_right_vertical_layout")
        self.sliding_two_fingers_right_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.sliding_two_fingers_right_image_label.set_absolute_path(
            self.absolute_path)
        self.sliding_two_fingers_right_image_label.set_name(
            "sliding_two_fingers_right")
        self.sliding_two_fingers_right_image_label.setMinimumSize(
            QSize(0, 200))
        self.sliding_two_fingers_right_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.sliding_two_fingers_right_image_label.setText("")
        self.sliding_two_fingers_right_image_label.setTextFormat(
            Qt.AutoText)
        self.sliding_two_fingers_right_image_label.setPixmap(QPixmap
                                                             (self.absolute_path + "/gesture_images/sliding_two_finger_right.png"))
        self.sliding_two_fingers_right_image_label.setScaledContents(True)
        self.sliding_two_fingers_right_image_label.setObjectName(
            "sliding_two_fingers_right_image_label")
        self.sliding_two_fingers_right_vertical_layout.addWidget(
            self.sliding_two_fingers_right_image_label)
        self.sliding_two_fingers_right_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sliding_two_fingers_right_name_label.sizePolicy().hasHeightForWidth())
        self.sliding_two_fingers_right_name_label.setSizePolicy(sizePolicy)
        self.sliding_two_fingers_right_name_label.setMinimumSize(
            QSize(0, 50))
        self.sliding_two_fingers_right_name_label.setSizeIncrement(
            QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.sliding_two_fingers_right_name_label.setFont(font)
        self.sliding_two_fingers_right_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.sliding_two_fingers_right_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.sliding_two_fingers_right_name_label.setAlignment(
            Qt.AlignCenter)
        self.sliding_two_fingers_right_name_label.setObjectName(
            "sliding_two_fingers_right_name_label")
        self.sliding_two_fingers_right_vertical_layout.addWidget(
            self.sliding_two_fingers_right_name_label)
        self.action11_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action11_comboBox.setFont(font)
        self.action11_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "outline-color: black;")
        self.action11_comboBox.setObjectName("action11_comboBox")
        self.sliding_two_fingers_right_vertical_layout.addWidget(
            self.action11_comboBox)
        self.gridLayout_4.addLayout(
            self.sliding_two_fingers_right_vertical_layout, 3, 2, 1, 1)
        self.sliding_two_fingers_down_vertical_layout = QVBoxLayout()
        self.sliding_two_fingers_down_vertical_layout.setSpacing(0)
        self.sliding_two_fingers_down_vertical_layout.setObjectName(
            "sliding_two_fingers_down_vertical_layout")
        self.sliding_two_fingers_down_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.sliding_two_fingers_down_image_label.set_absolute_path(
            self.absolute_path)
        self.sliding_two_fingers_down_image_label.set_name(
            "sliding_two_fingers_down")
        self.sliding_two_fingers_down_image_label.setMinimumSize(
            QSize(0, 200))
        self.sliding_two_fingers_down_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.sliding_two_fingers_down_image_label.setText("")
        self.sliding_two_fingers_down_image_label.setTextFormat(
            Qt.AutoText)
        self.sliding_two_fingers_down_image_label.setPixmap(QPixmap
                                                            (self.absolute_path + "/gesture_images/sliding_two_fingers_down.png"))
        self.sliding_two_fingers_down_image_label.setScaledContents(True)
        self.sliding_two_fingers_down_image_label.setObjectName(
            "sliding_two_fingers_down_image_label")
        self.sliding_two_fingers_down_vertical_layout.addWidget(
            self.sliding_two_fingers_down_image_label)
        self.sliding_two_fingers_down_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sliding_two_fingers_down_name_label.sizePolicy().hasHeightForWidth())
        self.sliding_two_fingers_down_name_label.setSizePolicy(sizePolicy)
        self.sliding_two_fingers_down_name_label.setMinimumSize(
            QSize(0, 50))
        self.sliding_two_fingers_down_name_label.setSizeIncrement(
            QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.sliding_two_fingers_down_name_label.setFont(font)
        self.sliding_two_fingers_down_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.sliding_two_fingers_down_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.sliding_two_fingers_down_name_label.setAlignment(
            Qt.AlignCenter)
        self.sliding_two_fingers_down_name_label.setObjectName(
            "sliding_two_fingers_down_name_label")
        self.sliding_two_fingers_down_vertical_layout.addWidget(
            self.sliding_two_fingers_down_name_label)
        self.action9_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action9_comboBox.setFont(font)
        self.action9_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "outline-color: black;")
        self.action9_comboBox.setObjectName("action9_comboBox")
        self.sliding_two_fingers_down_vertical_layout.addWidget(
            self.action9_comboBox)
        self.gridLayout_4.addLayout(
            self.sliding_two_fingers_down_vertical_layout, 3, 4, 1, 1)
        self.sliding_two_fingers_up_vertical_layout = QVBoxLayout()
        self.sliding_two_fingers_up_vertical_layout.setSpacing(0)
        self.sliding_two_fingers_up_vertical_layout.setObjectName(
            "sliding_two_fingers_up_vertical_layout")
        self.sliding_two_fingers_up_image_label = MyLabel(
            self.scrollAreaWidgetContents)
        self.sliding_two_fingers_up_image_label.set_absolute_path(
            self.absolute_path)
        self.sliding_two_fingers_up_image_label.set_name(
            "sliding_two_fingers_up")
        self.sliding_two_fingers_up_image_label.setMinimumSize(
            QSize(0, 200))
        self.sliding_two_fingers_up_image_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.sliding_two_fingers_up_image_label.setText("")
        self.sliding_two_fingers_up_image_label.setTextFormat(
            Qt.AutoText)
        self.sliding_two_fingers_up_image_label.setPixmap(QPixmap
                                                          (self.absolute_path + "/gesture_images/sliding_two_fingers_up.png"))
        self.sliding_two_fingers_up_image_label.setScaledContents(True)
        self.sliding_two_fingers_up_image_label.setObjectName(
            "sliding_two_fingers_up_image_label")
        self.sliding_two_fingers_up_vertical_layout.addWidget(
            self.sliding_two_fingers_up_image_label)
        self.sliding_two_fingers_up_name_label = QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sliding_two_fingers_up_name_label.sizePolicy().hasHeightForWidth())
        self.sliding_two_fingers_up_name_label.setSizePolicy(sizePolicy)
        self.sliding_two_fingers_up_name_label.setMinimumSize(
            QSize(0, 50))
        self.sliding_two_fingers_up_name_label.setSizeIncrement(
            QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.sliding_two_fingers_up_name_label.setFont(font)
        self.sliding_two_fingers_up_name_label.setLayoutDirection(
            Qt.LeftToRight)
        self.sliding_two_fingers_up_name_label.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.sliding_two_fingers_up_name_label.setAlignment(
            Qt.AlignCenter)
        self.sliding_two_fingers_up_name_label.setObjectName(
            "sliding_two_fingers_up_name_label")
        self.sliding_two_fingers_up_vertical_layout.addWidget(
            self.sliding_two_fingers_up_name_label)
        self.action12_comboBox = MyComboBox(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(12)
        self.action12_comboBox.setFont(font)
        self.action12_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "outline-color: black;")
        self.action12_comboBox.setObjectName("action12_comboBox")
        self.sliding_two_fingers_up_vertical_layout.addWidget(
            self.action12_comboBox)
        self.gridLayout_4.addLayout(
            self.sliding_two_fingers_up_vertical_layout, 3, 3, 1, 1)
        self.gestures_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.gestures_scroll_area, 0, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.aply_and_restore_box_layout = QHBoxLayout()
        self.aply_and_restore_box_layout.setObjectName(
            "aply_and_restore_box_layout")
        sizePolicy = QSizePolicy(
            QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        font = QFont()
        font.setPointSize(11)
        self.restore_button = QPushButton(self.gesture_tab)
        sizePolicy = QSizePolicy(
            QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.restore_button.sizePolicy().hasHeightForWidth())
        self.restore_button.setSizePolicy(sizePolicy)
        self.restore_button.setMinimumSize(QSize(180, 40))
        font = QFont()
        font.setPointSize(11)
        self.restore_button.setFont(font)
        self.restore_button.setStyleSheet("background-color:white;\n"
                                          "border-radius:10px;\n"
                                          "border-style:outset;\n"
                                          "border-radius:8px;\n"
                                          "border: 1px solid grey;\n"
                                          "")
        self.restore_button.setObjectName("restore_button")
        self.aply_and_restore_box_layout.addWidget(self.restore_button)
        spacerItem14 = QSpacerItem(
            100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.aply_and_restore_box_layout.addItem(spacerItem14)
        self.test_gestures_button = QPushButton(self.gesture_tab)
        sizePolicy = QSizePolicy(
            QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.test_gestures_button.sizePolicy().hasHeightForWidth())
        self.test_gestures_button.setSizePolicy(sizePolicy)
        self.test_gestures_button.setMinimumSize(QSize(150, 40))
        font = QFont()
        font.setPointSize(11)
        self.test_gestures_button.setFont(font)
        self.test_gestures_button.setStyleSheet("border-style:outset;\n"
                                                "border-radius:8px;\n"
                                                "background-color: rgb(22, 155, 213);\n"
                                                "color:white;\n"
                                                "")
        self.test_gestures_button.setObjectName("test_gestures_button")
        self.aply_and_restore_box_layout.addWidget(self.test_gestures_button)
        self.verticalLayout_4.addLayout(self.aply_and_restore_box_layout)
        self.aplication_tab_widget.addTab(self.gesture_tab, "")
        self.verticalLayout.addWidget(self.aplication_tab_widget)
        self.instruction_tab = QWidget()
        self.instruction_tab.setObjectName("instruction_tab")
        self.gridLayout30 = QGridLayout(self.instruction_tab)
        self.gridLayout30.setObjectName("gridLayout30")
        self.instruction_scroll_area = QScrollArea(self.instruction_tab)
        sizePolicy = QSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.instruction_scroll_area.sizePolicy().hasHeightForWidth())
        self.instruction_scroll_area.setSizePolicy(sizePolicy)
        self.instruction_scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOn)
        self.instruction_scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        self.instruction_scroll_area.setWidgetResizable(True)
        self.instruction_scroll_area.setMinimumWidth(1625)
        self.instructionWidget = QWidget()
        self.instruction_inner_grid_layout = QGridLayout(
            self.instructionWidget)
        self.instruction_inner_grid_layout.setAlignment(Qt.AlignCenter)
        self.instruction_label = QLabel(self.instructionWidget)
        self.instruction_label.setMinimumSize(QSize(1583, 880))
        self.instruction_label.setPixmap(
            QPixmap(self.absolute_path + "/other/instruction.png"))
        self.instruction_inner_grid_layout.addWidget(
            self.instruction_label, 0, 0, 1, 1)
        self.instruction_label_2 = QLabel(self.instructionWidget)
        self.instruction_label_2.setMinimumSize(QSize(1583, 880))
        self.instruction_label_2.setPixmap(
            QPixmap(self.absolute_path + "/other/instruction_2.png"))
        self.instruction_inner_grid_layout.addWidget(
            self.instruction_label_2, 1, 0, 1, 1)
        self.instruction_label_3 = QLabel(self.instructionWidget)
        self.instruction_label_3.setMinimumSize(QSize(1583, 880))
        self.instruction_label_3.setPixmap(
            QPixmap(self.absolute_path + "/other/instruction_3.png"))
        self.instruction_inner_grid_layout.addWidget(
            self.instruction_label_3, 2, 0, 1, 1)
        self.instruction_scroll_area.setWidget(self.instructionWidget)
        self.gridLayout30.addWidget(self.instruction_scroll_area, 0, 0, 1, 1)
        self.aplication_tab_widget.addTab(self.instruction_tab, "Instruction")
        spacerItem15 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem15)
        main_window.setCentralWidget(self.centralwidget)
        self.retranslateUi(main_window)
        self.aplication_tab_widget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(main_window)
        action_names = self.cont.get_gesture_recognition(
        ).get_mapping().function_getter.get_all_functions_names()
        for i in action_names:
            self.action1_comboBox.addItem(i)
            self.action2_comboBox.addItem(i)
            self.action3_comboBox.addItem(i)
            self.action4_comboBox.addItem(i)
            self.action5_comboBox.addItem(i)
            self.action6_comboBox.addItem(i)
            self.action7_comboBox.addItem(i)
            self.action8_comboBox.addItem(i)
            self.action9_comboBox.addItem(i)
            self.action10_comboBox.addItem(i)
            self.action11_comboBox.addItem(i)
            self.action12_comboBox.addItem(i)
            self.action13_comboBox.addItem(i)
            self.action14_comboBox.addItem(i)
            self.action15_comboBox.addItem(i)
            self.action16_comboBox.addItem(i)
            self.action17_comboBox.addItem(i)
            self.action18_comboBox.addItem(i)
            self.action20_comboBox.addItem(i)
            self.action21_comboBox.addItem(i)
            self.action22_comboBox.addItem(i)
            self.action23_comboBox.addItem(i)
            self.action24_comboBox.addItem(i)
            self.action25_comboBox.addItem(i)
        self.get_config()
        arr = self.cont.get_camera_controller().get_all_cameras()
        for i in arr:
            self.camera_combo_box.addItem("Camera "+str(i))
        self.refresh_cameras_button.clicked.connect(
            lambda: self.refresh_camera_list())
        self.minimize_window_button.clicked.connect(
            lambda: self.minimize_window())
        self.camera_combo_box.activated.connect(
            lambda: self.set_camera())
        self.start_button.clicked.connect(
            lambda: self.start_or_stop_gesture_recognition())
        self.test_gestures_button.clicked.connect(
            lambda: self.set_test_gesture_config())
        self.restore_button.clicked.connect(lambda: self.get_default_config())
        self.show_minimized_camera_check_box.stateChanged.connect(
            lambda: self.show_camera(self.show_minimized_camera_check_box.isChecked()))
        self.modify_gestures_button.clicked.connect(
            lambda: self.aplication_tab_widget.setCurrentIndex(1))
        self.action1_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action2_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action3_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action4_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action5_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action6_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action7_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action8_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action9_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action10_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action11_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action12_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action13_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action14_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action15_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action16_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action17_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action18_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action20_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action21_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action22_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action23_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action24_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.action25_comboBox.currentIndexChanged.connect(
            lambda: self.set_config())
        self.aplication_tab_widget.currentChanged.connect(
            lambda: self.scroll_up())
        self.Worker1 = Worker1(self.cont, self, self.absolute_path)
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.small_camera_widget = MinimizedCamera(
            self, self.Worker1, self.app, self.absolute_path)

    def retranslateUi(self, main_window):
        _translate = QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Handy"))
        self.select_camera_label.setText(
            _translate("main_window", "Select camera"))
        self.refresh_cameras_button.setText(
            _translate("main_window", "Refresh Cameras"))
        self.show_minimized_camera_check_box.setText(
            _translate("main_window", "Show small camera window"))
        self.modify_gestures_button.setText(
            _translate("main_window", "Modify gestures"))
        self.start_button.setText(_translate("main_window", "Start"))
        self.minimize_window_button.setText(
            _translate("main_window", "Minimize window"))
        self.aplication_tab_widget.setTabText(self.aplication_tab_widget.indexOf(
            self.camera_tab), _translate("main_window", "Camera"))
        self.mouse_right_button_name_label.setText(
            _translate("main_window", "Right mouse button"))
        self.mouse_drag1_name_label.setText(
            _translate("main_window", "Mouse drag"))
        self.mouse_double_click1_name_label.setText(
            _translate("main_window", "Mouse double click"))
        self.mouse_change_screen_name_label.setText(
            _translate("main_window", "Change mouse screen"))
        self.mouse_left_button_name_label.setText(
            _translate("main_window", "Left mouse button"))
        self.turning_hand_counter_name_label.setText(
            _translate("main_window", "Turning hand counterclockwise"))
        self.mouse_exit_name_label.setText(
            _translate("main_window", "Stop mouse control"))
        self.mouse_sterring_name_label.setText(
            _translate("main_window", "Mouse move"))
        self.start_mouse_name_label.setText(
            _translate("main_window", "Start mouse control"))
        self.druming_fingers_name_label.setText(
            _translate("main_window", "Drumming fingers"))
        self.swiping_up_name_label.setText(
            _translate("main_window", "Swiping up"))
        self.swiping_down_name_label.setText(
            _translate("main_window", "Swiping down"))
        self.rolling_hand_name_label.setText(
            _translate("main_window", "Rolling hand backward"))
        self.swiping_left_name_label.setText(
            _translate("main_window", "Swiping left"))
        self.rolling_hand_forward_name_label.setText(
            _translate("main_window", "Rolling hand forward"))
        self.swiping_right_name_label.setText(
            _translate("main_window", "Swiping right"))
        self.stop_sign_name_label.setText(
            _translate("main_window", "Stop sign"))
        self.thumb_down_name_label.setText(
            _translate("main_window", "Thumb down"))
        self.shaking_hand_name_label.setText(
            _translate("main_window", "Shaking hand"))
        self.zooming_out_with_full_hand_name_label.setText(
            _translate("main_window", "Zooming out with full hand"))
        self.zooming_in_with_full_hand_name_label.setText(
            _translate("main_window", "Zooming in with full hand"))
        self.zooming_in_with_two_fing_name_label.setText(
            _translate("main_window", "Zooming in with two fingers"))
        self.zooming_out_with_two_fing_name_label.setText(
            _translate("main_window", "Zooming out with two fingers"))
        self.turrning_hand_clock_name_label.setText(
            _translate("main_window", "Turning hand clockwise"))
        self.pulling_hand_in_name_label.setText(
            _translate("main_window", "Pulling hand in"))
        self.pushing_hand_away_name_label.setText(
            _translate("main_window", "Pushing hand away"))
        self.pulling_two_fingers_name_label.setText(
            _translate("main_window", "Pulling two fingers in"))
        self.pushing_two_fingers_away_name_label.setText(
            _translate("main_window", "Pushing two fingers away"))
        self.sliding_two_fingers_left_name_label.setText(
            _translate("main_window", "Sliding two fingers left"))
        self.sliding_two_fingers_right_name_label.setText(
            _translate("main_window", "Sliding two fingers right"))
        self.sliding_two_fingers_down_name_label.setText(
            _translate("main_window", "Sliding two fingers down"))
        self.sliding_two_fingers_up_name_label.setText(
            _translate("main_window", "Sliding two fingers up"))
        self.restore_button.setText(_translate(
            "main_window", "Restore default settings"))
        self.test_gestures_button.setText(
            _translate("main_window", "Test gestures"))
        self.aplication_tab_widget.setTabText(self.aplication_tab_widget.indexOf(
            self.gesture_tab), _translate("main_window", "Gestures"))

    def scroll_up(self):
        self.gestures_scroll_area.verticalScrollBar().setValue(0)
        self.instruction_scroll_area.verticalScrollBar().setValue(0)

    def start_or_stop_gesture_recognition(self):
        self.small_camera_widget.show_if_recognition_started_on_interface(
            not (self.cont.get_started()))
        self.cont.start_stop_gesture_recognition()

    def minimize_window(self):
        self.temp_ref.showMinimized()

    def uncheck_minimized_camera_checkbox(self):
        self.minimized_camera_checkbox_disabled = True
        self.show_minimized_camera_check_box.setChecked(False)
        self.minimized_camera_checkbox_disabled = False

    def is_camera_checkbox_checked(self):
        return self.show_minimized_camera_check_box.isChecked()

    def show_camera(self, is_checked):
        if self.minimized_camera_checkbox_disabled is False:
            if is_checked is True:
                position = self.camera_tab.mapToGlobal(QPoint(0, 0))
                camera_tab_size = self.camera_tab.size()
                x_position = position.x() + camera_tab_size.width() - 320
                y_position = position.y() + camera_tab_size.height() - 240
                if x_position < 0:
                    x_position = 0
                if y_position < 0:
                    y_position = 0
                if self.check_if_on_screen(x_position, y_position) is False:
                    x_position = 10
                    y_position = 10
                self.small_camera_widget.move(x_position, y_position)
                self.small_camera_widget.show_navigation_label()
                self.small_camera_widget.unset_entered_before_delete_label_time()
                self.small_camera_widget.delete_label_thread_is_active_up()
                QTimer.singleShot(3000, self.small_camera_widget.on_timeout)
                self.small_camera_widget.show()
            else:
                self.small_camera_widget.hide()

    def check_if_on_screen(self, x, y):
        monitors = []
        for m in get_monitors():
            monitors.append([m.x, m.y, m.width, m.height])
        for m in monitors:
            if x >= m[0] and y >= m[1] and m[0] + m[2] >= x + 320 and m[1] + m[3] >= y + 240:
                return True
        return False

    def ImageUpdateSlot(self, Image):
        recognition_status, recognition_message = self.get_gesture_recognized()
        if recognition_status is True:
            self.gesture_message_label.setText(recognition_message)
        else:
            self.gesture_message_label.setText("")
        self.big_camera_label.setPixmap(QPixmap.fromImage(Image))

    def is_active(self):
        return self.camera_tab.isVisible()


class Worker1(QThread):

    def __init__(self, controller, win, absolute_path):
        self.absolute_path = absolute_path
        super().__init__()
        self.controller = controller
        self.win = win
        self.camera = self.controller.get_camera_controller()
    MinimizedImageUpdate = pyqtSignal(QImage)
    ImageUpdate = pyqtSignal(QImage)

    def run(self):
        img = Image.open(self.absolute_path + '/other/no_camera_picture.png')
        no_cam = asarray(img)
        ConvertToQtFormat = QImage(no_cam.data, no_cam.shape[1], no_cam.shape[0],
                                   QImage.Format_RGB888)
        no_cam_picture = ConvertToQtFormat.scaled(
            800, 640, Qt.KeepAspectRatio)
        no_cam_picture_minimized = ConvertToQtFormat.scaled(
            320, 240, Qt.KeepAspectRatio)
        frame_counter = 0
        while self.win.get_close_time() is False:
            gesture_recognized, message = self.win.get_gesture_recognized()
            if gesture_recognized is True:
                if frame_counter >= 75:
                    self.win.set_gesture_recognized(False, "")
                    frame_counter = 0
                frame_counter += 1
            if self.win.is_active():
                ret, frame = self.camera.get_camera_image()
                if ret is True:
                    Image1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    FlippedImage = cv2.flip(Image1, 1)
                    ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0],
                                               QImage.Format_RGB888)
                    if self.win.is_camera_checkbox_checked():
                        self.ImageUpdate.emit(no_cam_picture)
                    else:
                        picture = ConvertToQtFormat.scaled(
                            800, 640, Qt.KeepAspectRatio)
                        self.ImageUpdate.emit(picture)
                    minimized_camera_picture = ConvertToQtFormat.scaled(
                        320, 240, Qt.KeepAspectRatio)
                    self.MinimizedImageUpdate.emit(minimized_camera_picture)
                else:
                    self.ImageUpdate.emit(no_cam_picture)
                    self.MinimizedImageUpdate.emit(no_cam_picture_minimized)
            else:
                ret, frame = self.camera.get_camera_image()
                if ret is True:
                    Image1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    FlippedImage = cv2.flip(Image1, 1)
                    ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0],
                                               QImage.Format_RGB888)
                    minimized_camera_picture = ConvertToQtFormat.scaled(
                        320, 240, Qt.KeepAspectRatio)
                    self.MinimizedImageUpdate.emit(minimized_camera_picture)
                else:
                    self.MinimizedImageUpdate.emit(no_cam_picture_minimized)

            time.sleep(0.02)
