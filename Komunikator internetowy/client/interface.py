import sys
import threading
from multiprocessing.spawn import freeze_support
from PyQt5 import QtWidgets
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QScrollArea, QTextEdit, QComboBox, QLabel, QLineEdit, \
    QMenuBar, QStatusBar
from main import Client
from one_message import OneMessage as om
import ray


class Ui_MainWindow(object):
    def __init__(self, client):
        self.client = client
        client.set_interface_reference(self)
        self.done = False

    def setupUi(self, MainWindow):
        MainWindow.resize(800, 799)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(550, 100, 93, 28))
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(100, 150, 581, 381))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 579, 379))
        self.textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 581, 381))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(140, 110, 371, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 0, 341, 41))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(570, 570, 111, 28))
        self.scrollArea_2 = QScrollArea(self.centralwidget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(100, 650, 581, 81))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 579, 79))
        self.textEdit_2 = QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(0, 0, 581, 87))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea_3 = QScrollArea(self.centralwidget)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(100, 540, 461, 87))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 459, 85))
        self.textEdit_3 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(0, 0, 461, 87))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(140, 60, 371, 22))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(550, 60, 93, 28))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 630, 55, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 40, 55, 16))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(660, 20, 113, 22))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(600, 20, 55, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(140, 90, 121, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(100, 130, 121, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_3.clicked.connect(lambda: self.connect())
        self.pushButton.clicked.connect(lambda: self.get_possible_chatters())
        self.pushButton_2.clicked.connect(lambda: self.send_message())
        self.comboBox.currentIndexChanged.connect(lambda: self.textEdit.clear())
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Communicator", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Communicator", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Your nick", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Your id", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Available chatters", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Message history", None))

    def send_message(self):
        message = self.textEdit_3.toPlainText()
        if len(message) == 0:
            self.textEdit_2.setText("Write message first")
            return
        receiver = self.comboBox.currentText()
        if len(receiver) == 0:
            self.textEdit_2.setText("Choose receiver first")
            return
        nick, id = receiver.split("     ")
        id = id[4:]
        nick = nick[6:]
        msg = om(message, nick, id)
        self.textEdit.setTextColor(QColor( "blue" ) )
        self.textEdit_3.clear()
        self.textEdit_2.clear()
        self.textEdit.append(message)
        self.textEdit.setTextColor(QColor("green"))
        self.client.add_message(msg)

    def connect(self):
        self.textEdit_2.setText(self.client.start(self.lineEdit.text()) + '\n')
        id = self.client.get_id()
        if not (id is None):
            self.lineEdit_2.setText(str(id))
            self.lineEdit.setReadOnly(True)
        self.get_possible_chatters()

    def get_possible_chatters(self):
        ret = self.client.get_possible_chatters_1()
        if ret is None:
            self.comboBox.clear()
            self.textEdit_2.setText("Error occured")
        else:
            self.textEdit_2.clear()
            self.comboBox.clear()
            list1 = ret
            if type(list1) == str:
                if list1 == "There is no available users now":
                    self.textEdit_2.setText(list1)
            else:
                for i in range(0, int(len(list1)-1), 2):
                    self.comboBox.addItem("nick: " + list1[i+1] + "     id: " + list1[i])
            if self.done is False:
                self.done = True
                self.t = threading.Thread(name='daemon', target=self.client.connect_and_chat)
                self.t.start()


@ray.remote
def function1():
    freeze_support()
    c = Client()
    app = QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    window = Ui_MainWindow(c)
    window.setupUi(win)
    win.show()
    app.exec()


if __name__ == '__main__':

    futures = [function1.remote() for a in range(2)]
    all_results = ray.get(futures)
