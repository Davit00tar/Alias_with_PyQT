import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *




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
        btn_back_2.clicked.connect(self.clicked_Back_2)
        page2.setLayout(page2layout)

        ########## ADD WORDS PAGE
        page3 = QWidget()
        page3layout = QVBoxLayout()
        page3layout.addWidget(QLabel('ADD WORDS'))
        text_3 = QLineEdit('', self)
        page3layout.addWidget(text_3)
        btn_add_3 = QPushButton('ADD', self)
        page3layout.addWidget(btn_add_3)
        btn_back_3 = QPushButton('BACK', self)
        btn_back_3.clicked.connect(self.clicked_Back_2)
        page3layout.addWidget(btn_back_3)
        page3.setLayout(page3layout)

        self.layout.addWidget(page1)
        self.layout.addWidget(page2)
        self.layout.addWidget(page3)
        self.layout.setCurrentIndex(0)


        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)


    def clicked_Rules_1(self):
        self.layout.setCurrentIndex(1)

    def clicked_AddWords_1(self):
        self.layout.setCurrentIndex(2)

    def clicked_Back_2(self):
        self.layout.setCurrentIndex(0)





app = QApplication(sys.argv)
window = MainWindow()

window.show()
app.exec_()
