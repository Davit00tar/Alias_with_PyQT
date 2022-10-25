import sys
from PyQt5.QtWidgets import *
from base import base_lst
from mainwindow import MainWindow
words = base_lst


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
