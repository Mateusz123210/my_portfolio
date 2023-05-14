import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from window_app.start_app import StartApp
from PyQt5.QtGui import QIcon
from multiprocessing import Process, Event, Value, freeze_support
import os


class Handy:

    def __init__(self):
        self.absolute_path = os.path.realpath(os.path.dirname(__file__))
        self.absolute_path = self.absolute_path.replace("\\", "/")
        self.ui = None
        self.start_app = None
        self.start_app_widget = None
        self.app = None
        self.started = False
        self.start()

    def end_application(self):
        self.ui.close_application()
    
    def start_application(self):
        from window_app.main_window import Ui_main_window as win 
        self.app = QtWidgets.QApplication(sys.argv)
        QtWidgets.QApplication.setWindowIcon(QIcon(self.absolute_path + '/logo.png'))
        self.app.setQuitOnLastWindowClosed(False)
        self.app.lastWindowClosed.connect(self.end_application)
        self.MainWindow = QtWidgets.QMainWindow()
        if self.v.value == 1:
            return
        self.ui = win(self.absolute_path)
        self.ui.setupUi(self.MainWindow)
        if self.v.value == 1:
            self.MainWindow.close()
            self.ui.close_application()
            return
        self.started = True
        self.e.set()    
        try:
            self.p.terminate()
        except Exception:
            pass
        self.MainWindow.showMaximized()
        sys.exit(self.app.exec_())

    def start(self):
        self.v = Value('i', 0)
        self.e = Event()
        self.p = Process(target=self.start_temp_app, args=(self.e, self.v))
        self.p.daemon = True
        self.p.start()
        self.start_application()
    
    def assign(self, v):
        v.value = 1

    def start_temp_app(self, e, v):
        self.start_app = QApplication(sys.argv)
        self.start_app.setQuitOnLastWindowClosed(False)
        self.start_app.lastWindowClosed.connect(lambda: self.assign(v))
        QApplication.setWindowIcon(QIcon(self.absolute_path + '/logo.png'))
        self.start_app_widget = StartApp(e)
        sys.exit(self.start_app.exec_())      


if __name__ == '__main__':
    freeze_support()
    if sys.stdout is None:
        sys.stdout = open(os.devnull, "w")
    if sys.stderr is None:
        sys.stderr = open(os.devnull, "w")
    Handy()
