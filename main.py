import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from base import base_lst
from mechanics import *
words = base_lst

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('ALIAS')
        self.setGeometry(100, 100, 300, 500)
        self.layout = QStackedLayout()

        ########## START PAGE
        page1 = QWidget()
        page1layout = QVBoxLayout()

        page1layout.addWidget(QPushButton('Play'))
        btn_play_1 = QPushButton("PLAY", self)
        page1layout.addWidget(btn_play_1)
        btn_play_1.clicked.connect(self.clicked_Play_1)

        btn_rules_1 = QPushButton("RULES", self)
        page1layout.addWidget(btn_rules_1)
        btn_rules_1.clicked.connect(self.clicked_Rules_1)

        btn_add_words_1 = QPushButton('ADD WORDS', self)
        page1layout.addWidget(btn_add_words_1)
        btn_add_words_1.clicked.connect(self.clicked_AddWords_1)
        page1.setLayout(page1layout)


        ########## RULES PAGE
        page2 = QWidget()
        page2layout = QVBoxLayout()

        page2layout.addWidget(QLabel('RULES'))
        page2layout.addWidget(QLabel('HERE ARE THE RULES'))
        btn_back_2 = QPushButton('BACK', self)

        page2layout.addWidget(btn_back_2)
        btn_back_2.clicked.connect(self.clicked_Back_to_0)
        page2.setLayout(page2layout)


        ########## ADD WORDS PAGE
        page3 = QWidget()
        page3layout = QVBoxLayout()
        page3layout.addWidget(QLabel('ADD WORDS'))

        self.text_3 = QLineEdit('', self)
        page3layout.addWidget(self.text_3)

        btn_add_3 = QPushButton('ADD', self)
        page3layout.addWidget(btn_add_3)
        btn_add_3.clicked.connect(self.clicked_Add_2)

        btn_back_3 = QPushButton('BACK', self)
        btn_back_3.clicked.connect(self.clicked_Back_to_0)
        page3layout.addWidget(btn_back_3)
        page3.setLayout(page3layout)

        ######## Select Group Numbers
        page4 = QWidget
        page4layout = QVBoxLayout
        btn_back_4 = QPushButton('BACK', self)
        page4layout.addWidget(btn_back_4)
        btn_back_4.clicked.connect(self.clicked_back_to_0)
        page4.setLayout(page4layout)

        ######## Layout Management
        self.layout.addWidget(page1)
        self.layout.addWidget(page2)
        self.layout.addWidget(page3)
        self.layout.addWidget(page4)
        self.layout.setCurrentIndex(0)


        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)


    def clicked_Play_1(self):
        self.layout.setCurrentIndex(3)

    def clicked_Rules_1(self):
        self.layout.setCurrentIndex(1)

    def clicked_AddWords_1(self):
        self.layout.setCurrentIndex(2)

    def clicked_Back_to_0(self):
        self.layout.setCurrentIndex(0)

    def clicked_Add_2(self):
        word_adder(self.text_3.text(), words)








app = QApplication(sys.argv)
window = MainWindow()

window.show()
app.exec_()
