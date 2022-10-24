from PyQt5.QtWidgets import *
from base import base_lst
from mechanics import *

words = base_lst


class GuessWord(QWidget):
    def __init__(self, *args, **kwargs):
        super(GuessWord, self).__init__(*args, **kwargs)

        self.times_clicked = 0
        self.is_guessed = False
        self.setFixedSize(200, 50)
        self.word_layout = QHBoxLayout()
        self.setLayout(self.word_layout)

        self.btn_guess = QPushButton(word_generator(words))
        self.word_layout.addWidget(self.btn_guess)
        self.btn_guess.clicked.connect(self.clicked_btn_guess)

        self.color = QWidget()
        self.color.setFixedSize(50, 20)
        self.word_layout.addWidget(self.color)
        self.btn_guess.clicked.connect(self.color_adder)

    def clicked_btn_guess(self):
        if is_odd(self.times_clicked):
            self.is_guessed = False
        else:
            self.is_guessed = True
        self.times_clicked += 1

    def color_adder(self):
        if self.is_guessed:
            self.color.setStyleSheet("""background: green;""")
        else:
            self.color.setStyleSheet("""background: red;""")


class WordPage(QWidget):
    def __init__(self, *args, **kwargs):
        super(WordPage, self).__init__(*args, **kwargs)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.word1 = GuessWord()
        self.word2 = GuessWord()
        self.word3 = GuessWord()
        self.word4 = GuessWord()
        self.word5 = GuessWord()

        self.layout.addWidget(self.word1)
        self.layout.addWidget(self.word2)
        self.layout.addWidget(self.word3)
        self.layout.addWidget(self.word4)
        self.layout.addWidget(self.word5)



    def is_all_guessed(self):
        return True if (self.word1.is_guessed and self.word2.is_guessed and self.word3.is_guessed and
            self.word4.is_guessed and self.word5.is_guessed) else False


    def new_words(self):
        self.word1.btn_guess.setText(word_generator(words))
        self.word2.btn_guess.setText(word_generator(words))
        self.word3.btn_guess.setText(word_generator(words))
        self.word4.btn_guess.setText(word_generator(words))
        self.word5.btn_guess.setText(word_generator(words))

        self.word1.is_guessed = False
        self.word1.times_clicked = 0
        self.word1.color.setStyleSheet("""background: red;""")
        self.word2.is_guessed = False
        self.word2.color.setStyleSheet("""background: red;""")
        self.word2.times_clicked = 0
        self.word2.color.setStyleSheet("""background: red;""")
        self.word3.is_guessed = False
        self.word3.color.setStyleSheet("""background: red;""")
        self.word3.times_clicked = 0
        self.word4.color.setStyleSheet("""background: red;""")
        self.word4.is_guessed = False
        self.word4.times_clicked = 0
        self.word5.color.setStyleSheet("""background: red;""")
        self.word5.is_guessed = False
        self.word5.times_clicked = 0

    def change_words(self):
        if self.is_all_guessed():
            self.new_words()
        else:
            pass
