from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QLabel, QPushButton
import threading
import time


class StartApp(QWidget):

    def __init__(self, e):
        super().__init__()
        self.x = 0
        self.y = 0
        self.allow_move = False
        self.end = False
        self.e = e
        self.initUI()

    def start_thread(self):
        self.t2 = threading.Thread(name='daemon', target=self.update_text)
        self.t2.start()
        self.t = threading.Thread(name='daemon', target=self.close_thread)
        self.t.start()

    def close_thread(self):
        self.e.wait()
        self.end = True
        self.t2.join()
        self.close()
        return

    def update_text(self):
        counter = 0
        values = {0: "Loading.", 1: "Loading..", 2: "Loading..."}
        current_value = 1
        while self.end is False:
            if counter == 32:
                current_value = (current_value + 1) % 3
                self.label.setText(values.get(current_value))
                counter = 0
            counter += 1
            time.sleep(0.020)

    def initUI(self):
        self.setWindowTitle('Handy')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(400, 200)
        self.center()
        position = self.pos()
        self.x = position.x()
        self.y = position.y()
        self.allow_move = True
        self.setStyleSheet(
            "background-color: #D7D7D7;border: 1px solid #c4c4c4;")
        self.setAttribute(Qt.WA_StyledBackground)
        self.layout = QVBoxLayout()
        self.handy_label = QLabel("Handy")
        font1 = self.font()
        font1.setPointSize(40)
        font1.setBold(True)
        self.handy_label.setFont(font1)
        self.handy_label.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
        self.handy_label.setStyleSheet("color: #70d345;border:none;")
        self.layout.addWidget(self.handy_label)
        self.label = QLabel("Loading...")
        font2 = self.font()
        font2.setPointSize(12)
        font2.setBold(False)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
        self.label.setStyleSheet("border:none")
        self.layout.addWidget(self.label)
        self.button = QPushButton("close")
        font3 = self.font()
        font3.setPointSize(11)
        font3.setBold(False)
        self.button.setFont(font3)
        self.button.setStyleSheet(
            "background-color: #DFE6F8; text-align: center;border:none;")
        self.button.setFixedSize(200, 30)
        self.layout.addWidget(
            self.button, alignment=Qt.AlignCenter | Qt.AlignBottom)
        self.button.clicked.connect(lambda: self.close())
        self.setLayout(self.layout)
        self.start_thread()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
