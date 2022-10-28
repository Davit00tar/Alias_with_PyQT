from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from base import base_lst, game_rules
from mechanics import *
from word_class import WordPage
words = base_lst

########


class MainWindow(QMainWindow):
    """
    The main window class for Alias, All the UI elements are here.
    And overall the main code is in this class. The MainWindow Object
    is only called once in the programme, ano only uses its atribute
    inherited from Parent Class: QMainWindow, which is .show()
    """
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('ALIAS')
        self.setGeometry(100, 100, 300, 500)
        self.layout = QStackedLayout()

        self.team1score = 0
        self.team2score = 0
        self.team3score = 0
        self.current_score = 0

        self.play_time = 30
        self.win_score = 50

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.timing)
        self.timer.start(1000)
        self.start_timer = False
        self.second = 0

        self.turn = -1
        self.playing_team = [1]

        # START PAGE   0

        page1 = QWidget()
        page1layout = QVBoxLayout()

        btn_play_1 = QPushButton("PLAY", self)
        page1layout.addWidget(btn_play_1)
        btn_play_1.clicked.connect(self.clicked_play_1)

        btn_rules_1 = QPushButton("RULES", self)
        page1layout.addWidget(btn_rules_1)
        btn_rules_1.clicked.connect(self.clicked_rules_1)

        btn_add_words_1 = QPushButton('ADD WORDS', self)
        page1layout.addWidget(btn_add_words_1)
        btn_add_words_1.clicked.connect(self.clicked_add_words_1)
        page1.setLayout(page1layout)


        # RULES PAGE    1
        page2 = QWidget()
        page2layout = QVBoxLayout()

        page2layout.addWidget(QLabel('RULES'))
        rules = QLabel(game_rules)
        rules.setFixedSize(300, 450)
        page2layout.addWidget(rules)
        btn_back_2 = QPushButton('BACK', self)

        page2layout.addWidget(btn_back_2)
        btn_back_2.clicked.connect(self.clicked_back_to_0)
        page2.setLayout(page2layout)


        # ADD WORDS PAGE    2
        page3 = QWidget()
        page3layout = QVBoxLayout()
        page3layout.addWidget(QLabel('ADD WORDS'))

        self.message = QLabel()
        page3layout.addWidget(self.message)

        self.text_3 = QLineEdit('', self)
        page3layout.addWidget(self.text_3)

        btn_add_3 = QPushButton('ADD', self)
        page3layout.addWidget(btn_add_3)
        btn_add_3.clicked.connect(self.clicked_add_2)

        btn_back_3 = QPushButton('BACK', self)
        btn_back_3.clicked.connect(self.clicked_back_to_0)
        page3layout.addWidget(btn_back_3)
        page3.setLayout(page3layout)

        # Select Group Numbers   4
        page4 = QWidget()
        page4layout = QVBoxLayout()

        page4layout.addWidget(QLabel('SELECT TEAM NUMBER'))
        self.team_select = QComboBox()

        self.team_select.addItems(['Two', 'Three'])
        page4layout.addWidget(self.team_select)
        self.team_select.setCurrentIndex(0)

        btn_next_4 = QPushButton('NEXT')
        page4layout.addWidget(btn_next_4)
        btn_next_4.clicked.connect(self.clicked_next_4)

        btn_back_4 = QPushButton('BACK')
        page4layout.addWidget(btn_back_4)
        btn_back_4.clicked.connect(self.clicked_back_to_0)
        page4.setLayout(page4layout)


        # 1GROUP NAMES    5
        page5 = QWidget()
        page5layout = QVBoxLayout()

        team1 = QWidget()
        team1layout = QHBoxLayout()
        team1layout.addWidget(QLabel('TEAM 1 Name'))
        self.team1name = QLineEdit('TEAM 1')
        team1layout.addWidget(self.team1name)
        team1.setLayout(team1layout)
        page5layout.addWidget(team1)

        btn_next_5 = QPushButton('NEXT')
        page5layout.addWidget(btn_next_5)
        btn_next_5.clicked.connect(self.clicked_next_5)
        btn_back_5 = QPushButton('BACK')
        page5layout.addWidget(btn_back_5)
        btn_back_5.clicked.connect(self.clicked_back_5)

        page5.setLayout(page5layout)


        # 2GROUP NAME   6
        page6 = QWidget()
        page6layout = QVBoxLayout()
        team2 = QWidget()
        team2layout = QHBoxLayout()
        team2layout.addWidget(QLabel('TEAM 2 name'))
        self.team2name = QLineEdit('TEAM 2')
        team2layout.addWidget(self.team2name)
        team2.setLayout(team2layout)
        page6layout.addWidget(team2)
        page6.setLayout(page6layout)

        btn_next_6 = QPushButton('NEXT')
        page6layout.addWidget(btn_next_6)
        btn_next_6.clicked.connect(self.clicked_next_6)

        btn_back_6 = QPushButton('BACK')
        page6layout.addWidget(btn_back_6)
        btn_back_6.clicked.connect(self.clicked_back_6)


        # 3GROUP NAME  7
        page7 = QWidget()
        page7layout = QVBoxLayout()
        team3 = QWidget()
        team3layout = QHBoxLayout()
        team3layout.addWidget(QLabel('TEAM 3 name'))
        self.team3name = QLineEdit('TEAM 3')
        team3layout.addWidget(self.team3name)
        team3.setLayout(team3layout)
        page7layout.addWidget(team3)
        page7.setLayout(page7layout)
        btn_next_7 = QPushButton('NEXT')
        page7layout.addWidget(btn_next_7)
        btn_next_7.clicked.connect(self.clicked_next_7)

        btn_back_7 = QPushButton('BACK')
        page7layout.addWidget(btn_back_7)
        btn_back_7.clicked.connect(self.clicked_back_7)


        # TIME AND SCORE SELECTION PAGE  8
        page8 = QWidget()
        page8layout = QVBoxLayout()
        page8.setLayout(page8layout)

        page8layout.addWidget(QLabel('SELECT ROUND DURATION (SECONDS)'))
        page8layout.addWidget(QLabel('Must be at least 30 seconds'))
        self.time_select = QLineEdit('30')
        page8layout.addWidget(self.time_select)

        page8layout.addWidget(QLabel('SELECT WIN SCORE'))
        page8layout.addWidget(QLabel('Must be at least 50 pts'))
        self.score_select = QLineEdit('50')
        page8layout.addWidget(self.score_select)

        btn_next_8 = QPushButton('NEXT')
        page8layout.addWidget(btn_next_8)
        btn_next_8.clicked.connect(self.clicked_next_8)

        btn_back_8 = QPushButton('BACK')
        page8layout.addWidget(btn_back_8)
        btn_back_8.clicked.connect(self.clicked_back_8)


        # SCORE ONE TEAM 9
        page9 = QWidget()
        page9layout = QVBoxLayout()
        page9.setLayout(page9layout)

        self.label1_9 = QLabel()
        page9layout.addWidget(self.label1_9)
        self.label2_9 = QLabel(str(self.team1score))
        page9layout.addWidget(self.label2_9)

        self.label_score_9 = QLabel()
        page9layout.addWidget(self.label_score_9)

        btn_next_9 = QPushButton('START')
        page9layout.addWidget(btn_next_9)
        btn_next_9.clicked.connect(self.clicked_start_game)

        btn_back_9 = QPushButton('BACK')
        page9layout.addWidget(btn_back_9)
        btn_back_9.clicked.connect(self.clicked_back_to_7)

        #  SCORE TWO TEAMS 10
        page10 = QWidget()
        page10layout = QVBoxLayout()
        page10.setLayout(page10layout)

        team1score_10 = QWidget()
        team1score_layout_10 = QVBoxLayout()
        team1score_10.setLayout(team1score_layout_10)

        self.label1_10 = QLabel()
        team1score_layout_10.addWidget(self.label1_10)
        self.label2_10 = QLabel(str(self.team1score))
        team1score_layout_10.addWidget(self.label2_10)

        team2score_10 = QWidget()
        team2score_layout_10 = QVBoxLayout()
        team2score_10.setLayout(team2score_layout_10)

        self.label3_10 = QLabel()
        team2score_layout_10.addWidget(self.label3_10)
        self.label4_10 = QLabel(str(self.team2score))
        team2score_layout_10.addWidget(self.label4_10)

        horizontal10 = QWidget()
        horizontal10layout = QHBoxLayout()
        horizontal10.setLayout(horizontal10layout)
        horizontal10layout.addWidget(team1score_10)
        horizontal10layout.addWidget(team2score_10)
        page10layout.addWidget(horizontal10)
        self.label_score_10 = QLabel()
        page10layout.addWidget(self.label_score_10)

        btn_start_10 = QPushButton('START')
        page10layout.addWidget(btn_start_10)
        btn_start_10.clicked.connect(self.clicked_start_game)

        btn_back_10 = QPushButton('BACK')
        page10layout.addWidget(btn_back_10)
        btn_back_10.clicked.connect(self.clicked_back_to_7)

        #  SCORE THREE TEAMS 11
        page11 = QWidget()
        page11layout = QVBoxLayout()
        page11.setLayout(page11layout)

        team1score_11 = QWidget()
        team1score_layout_11 = QVBoxLayout()
        team1score_11.setLayout(team1score_layout_11)

        self.label1_11 = QLabel()
        team1score_layout_11.addWidget(self.label1_11)
        self.label2_11 = QLabel(str(self.team1score))
        team1score_layout_11.addWidget(self.label2_11)

        team2score_11 = QWidget()
        team2score_layout_11 = QVBoxLayout()
        team2score_11.setLayout(team2score_layout_11)

        self.label3_11 = QLabel()
        team2score_layout_11.addWidget(self.label3_11)
        self.label4_11 = QLabel(str(self.team2score))
        team2score_layout_11.addWidget(self.label4_11)

        team3score_11 = QWidget()
        team3score_layout_11 = QVBoxLayout()
        team3score_11.setLayout(team3score_layout_11)

        self.label5_11 = QLabel()
        team3score_layout_11.addWidget(self.label5_11)
        self.label6_11 = QLabel(str(self.team3score))
        team3score_layout_11.addWidget(self.label6_11)


        horizontal11 = QWidget()
        horizontal11layout = QHBoxLayout()
        horizontal11.setLayout(horizontal11layout)

        horizontal11layout.addWidget(team1score_11)
        horizontal11layout.addWidget(team2score_11)
        horizontal11layout.addWidget(team3score_11)
        page11layout.addWidget(horizontal11)

        self.label_score_11 = QLabel()
        page11layout.addWidget(self.label_score_11)
        btn_start_11 = QPushButton('START')
        page11layout.addWidget(btn_start_11)
        btn_start_11.clicked.connect(self.clicked_start_game)

        btn_back_11 = QPushButton('BACK')
        page11layout.addWidget(btn_back_11)
        btn_back_11.clicked.connect(self.clicked_back_to_7)

        # TEAM 1 GAME_PAGE 12
        page12 = QWidget()
        page12layout = QVBoxLayout()
        page12.setLayout(page12layout)
        self.label1_12 = QLabel()
        page12layout.addWidget(self.label1_12)

        page12hlayout = QHBoxLayout()
        page12h = QWidget()
        page12h.setLayout(page12hlayout)
        page12layout.addWidget(page12h)
        self.page12score = QLabel(str(self.current_score))
        page12hlayout.addWidget(self.page12score)

        self.show_time12 = QLabel('//TIME//')
        page12hlayout.addWidget(self.show_time12)
        self.words12 = WordPage()
        page12layout.addWidget(self.words12)


        # TEAM 2 GAME PAGE 13
        page13 = QWidget()
        page13layout = QVBoxLayout()
        page13.setLayout(page13layout)
        self.label1_13 = QLabel()
        page13layout.addWidget(self.label1_13)

        page13h = QWidget()
        page13hlayout = QHBoxLayout()
        page13h.setLayout(page13hlayout)
        page13layout.addWidget(page13h)
        self.page13score = QLabel(str(self.team2score))
        page13hlayout.addWidget(self.page13score)
        self.show_time13 = QLabel('//TIME//')
        page13hlayout.addWidget(self.show_time13)
        self.words13 = WordPage()
        page13layout.addWidget(self.words13)


        # TEAM 3 GAME PAGE 14
        page14 = QWidget()
        page14layout = QVBoxLayout()
        page14.setLayout(page14layout)
        self.label1_14 = QLabel()
        page14layout.addWidget(self.label1_14)

        page14h = QWidget()
        page14hlayout = QHBoxLayout()
        page14h.setLayout(page14hlayout)
        page14layout.addWidget(page14h)
        self.page14score = QLabel(str(self.team3score))
        page14hlayout.addWidget(self.page14score)

        self.show_time14 = QLabel('//TIME//')
        page14hlayout.addWidget(self.show_time14)
        self.words14 = WordPage()
        page14layout.addWidget(self.words14)

        self.score_connect()


        # GAME OVER SCREEN 15
        page15 = QWidget()
        page15layout = QVBoxLayout()
        page15.setLayout(page15layout)

        label1_15 = QLabel('CONGRATULATIONS!!!!')
        page15layout.addWidget(label1_15)
        self.label3_15 = QLabel()
        page15layout.addWidget(self.label3_15)
        self.label4_15 = QLabel()
        page15layout.addWidget(self.label4_15)

        # Layout Management
        self.layout.addWidget(page1)
        self.layout.addWidget(page2)
        self.layout.addWidget(page3)
        self.layout.addWidget(page4)
        self.layout.addWidget(page5)
        self.layout.addWidget(page6)
        self.layout.addWidget(page7)
        self.layout.addWidget(page8)
        self.layout.addWidget(page9)
        self.layout.addWidget(page10)
        self.layout.addWidget(page11)
        self.layout.addWidget(page12)
        self.layout.addWidget(page13)
        self.layout.addWidget(page14)
        self.layout.addWidget(page15)
        self.layout.setCurrentIndex(0)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def clicked_play_1(self):
        """Connected to a QPushButton object
            changes the main layout Index"""
        self.layout.setCurrentIndex(3)

    def clicked_rules_1(self):
        """Connected to a QPushButton object
            changes the main layout Index"""
        self.layout.setCurrentIndex(1)

    def clicked_add_words_1(self):
        """Connected to a QPushButton object
            changes the main layout Index"""
        self.layout.setCurrentIndex(2)

    def clicked_back_to_0(self):
        """Connected to a QPushButton object
            changes the main layout Index"""
        self.layout.setCurrentIndex(0)

    def clicked_add_2(self):
        """Connected to a QPushButton object
            Raises a message when pressed Button ADD and adds the word if possible"""
        self.message.setText(word_adder(self.text_3.text(), words))

    def clicked_next_4(self):
        """Connected to a QPushButton object
            changes the main layout Index"""
        if self.team_select.currentIndex() == 0:
            self.playing_team = [1, 2]
        elif self.team_select.currentIndex() == 1:
            self.playing_team = [1, 2, 3]

        self.layout.setCurrentIndex(4)

    def team_number(self):
        """returns the number of teams selected"""
        number = self.team_select.currentIndex() + 1
        return number

    def clicked_back_5(self):
        """Connected to a QPushButton object
            changes the main layout Index"""
        self.layout.setCurrentIndex(3)

    def clicked_next_5(self):
        """Connected to a QPushButton object
        changes the main layout Index
        considering the number of teams selected"""
        self.layout.setCurrentIndex(5)


    def clicked_back_6(self):
        """Connected to a QPushButton object
        changes the main layout Index"""
        self.layout.setCurrentIndex(4)

    def clicked_next_6(self):
       if self.team_select.currentIndex() == 1:
           self.layout.setCurrentIndex(6)
       else:
           self.layout.setCurrentIndex(7)

    def clicked_next_7(self):
        """Connected to a QPushButton object
            changes the main layout Index"""
        self.layout.setCurrentIndex(7)

    def clicked_back_7(self):
        """Connected to a QPushButton object
            changes the main layout Index"""
        self.layout.setCurrentIndex(5)

    def clicked_back_8(self):
        """Connected to a QPushButton object
                changes the main layout Index
                considering the number of teams selected"""
        if self.team_select.currentIndex() == 0:
            self.layout.setCurrentIndex(4)
        elif self.team_select.currentIndex() == 1:
            self.layout.setCurrentIndex(5)
        else:
            self.layout.setCurrentIndex(6)

    def clicked_next_8(self):
        """Connected to a QPushButton object,
         sets the chosen time and win socre for
         the game, sets the Team names for the
         Game score page, changes the main layout index
         """
        if int(self.score_select.text()) > 50:
            self.win_score = int(self.score_select.text())
        else:
            self.win_score = 50
        self.time_select.text()
        self.play_time = self.time_select.text()
        self.label1_9.setText(self.team1name.text())
        self.label1_10.setText(self.team1name.text())
        self.label1_11.setText(self.team1name.text())
        self.label3_10.setText(self.team2name.text())
        self.label3_11.setText(self.team2name.text())
        self.label5_11.setText(self.team3name.text())
        self.turn += 1
        if self.team_select.currentIndex() == 0:
            self.label_score_10.setText(f" ITS {self.turn +1}'s TURN")
            self.layout.setCurrentIndex(9)
        elif self.team_select.currentIndex() == 1:
            self.label_score_11.setText(f" ITS {self.turn + 1}'s TURN")
            self.layout.setCurrentIndex(10)
        else:
            self.label_score_11.setText(f" ITS {self.turn + 1}'s TURN")
            self.layout.setCurrentIndex(10)

    def clicked_back_to_7(self):
        """Connected to a QPushButton object
        Changes the main layout index and
        gives all the variables their default values"""
        self.turn = -1
        self.layout.setCurrentIndex(3)
        self.team1score = 0
        self.team2score = 0
        self.team3score = 0
        self.time_select.setText('30')
        self.score_select.setText('50')
        self.label2_9.setText(str(self.team1score))
        self.label2_10.setText(str(self.team1score))
        self.label2_11.setText(str(self.team1score))
        self.label4_10.setText(str(self.team2score))
        self.label4_11.setText(str(self.team2score))
        self.label6_11.setText(str(self.team3score))
        self.team1name.setText('TEAM 1')
        self.team2name.setText('TEAM 2')
        self.team3name.setText('TEAM 3')


    def score_connect(self):
        """Connects every IN-GAME BUTTON to score adder function passing it the specific parametrs
        of every single button"""
        self.words12.word1.btn_guess.clicked.connect(lambda x: self.score_adder(self.words12.word1,
                                                    self.words12, self.page12score))
        self.words12.word2.btn_guess.clicked.connect(lambda x: self.score_adder(self.words12.word2,
                                                    self.words12, self.page12score))
        self.words12.word3.btn_guess.clicked.connect(lambda x: self.score_adder(self.words12.word3,
                                                    self.words12, self.page12score))
        self.words12.word4.btn_guess.clicked.connect(lambda x: self.score_adder(self.words12.word4,
                                                    self.words12, self.page12score))
        self.words12.word5.btn_guess.clicked.connect(lambda x: self.score_adder(self.words12.word5,
                                                    self.words12, self.page12score))

        self.words13.word1.btn_guess.clicked.connect(lambda x: self.score_adder(self.words13.word1,
                                                    self.words13, self.page13score))
        self.words13.word2.btn_guess.clicked.connect(lambda x: self.score_adder(self.words13.word2,
                                                    self.words13, self.page13score))
        self.words13.word3.btn_guess.clicked.connect(lambda x: self.score_adder(self.words13.word3,
                                                    self.words13, self.page13score))
        self.words13.word4.btn_guess.clicked.connect(lambda x: self.score_adder(self.words13.word4,
                                                    self.words13, self.page13score))
        self.words13.word5.btn_guess.clicked.connect(lambda x: self.score_adder(self.words13.word5,
                                                    self.words13, self.page13score))

        self.words14.word1.btn_guess.clicked.connect(lambda x: self.score_adder(self.words14.word1,
                                                    self.words14, self.page14score))
        self.words14.word2.btn_guess.clicked.connect(lambda x: self.score_adder(self.words14.word2,
                                                    self.words14, self.page14score))
        self.words14.word3.btn_guess.clicked.connect(lambda x: self.score_adder(self.words14.word3,
                                                    self.words14, self.page14score))
        self.words14.word4.btn_guess.clicked.connect(lambda x: self.score_adder(self.words14.word4,
                                                    self.words14, self.page14score))
        self.words14.word5.btn_guess.clicked.connect(lambda x: self.score_adder(self.words14.word5,
                                                    self.words14, self.page14score))

    def clicked_start_game(self):
        """Connected to a QPushButton object
        Starts the game, generates new words
        starts the timer countdown, defines
        which team must play the round"""
        self.words12.new_words()
        self.words13.new_words()
        self.words14.new_words()

        if self.turn >= len(self.playing_team):
            self.turn = 0
        if self.turn == 0:
            self.label1_12.setText(self.team1name.text())
            self.layout.setCurrentIndex(11)
        elif self.turn == 1:
            self.label1_13.setText(self.team2name.text())
            self.layout.setCurrentIndex(12)
        else:
            self.label1_14.setText(self.team3name.text())
            self.layout.setCurrentIndex(13)
        self.start_timer = True

        # For Easy Test, Comment this part.
        # if int(self.play_time) > 30:
        #     self.second = int(self.play_time)
        # else:
        #     self.second = 30

        # And Run This Line
        self.second = int(self.play_time)


    def score_adder(self, word, words, score_lbl):
        """Connected to a QPushButton object
        when clicked IN-GAME button chekces if
        the button is guessed adds the current
        score, otherwise reduses the current
        score"""
        if word.is_guessed:
            self.current_score += 1
        else:
            self.current_score -= 1
        words.change_words()
        score_lbl.setText(str(self.current_score))


    def timing(self):
        """Connected to QTimer object
        the main function that makes the timer work
        and shows the remaining time on a label"""
        if self.start_timer:
            self.second = self.second - 1
            self.show_time12.setText(str(self.second))
            self.show_time13.setText(str(self.second))
            self.show_time14.setText(str(self.second))

        if self.second == 0 and self.start_timer:
            self.end_time()

    def end_time(self):
        """Connected to Timer when the remaining time reaches 0
        addes the surrent score to the playing team's score
        Checked if any team has reached the win score changes the
        game layout to Win Page, if there are no winners yet
        gives the playing teams' score to labels to show,
        changes the layout index
        """
        if self.turn == 0:
            self.team1score += self.current_score
            if self.team1score >= self.win_score:
                self.game_over(self.team1score, self.team1name.text())
                self.layout.setCurrentIndex(15)
                return 0
        elif self.turn == 1:
            self.team2score += self.current_score
            if self.team2score >= self.win_score:
                self.game_over(self.team2score, self.team2name.text())
                self.layout.setCurrentIndex(15)
                return 0
        else:
            self.team3score += self.current_score
            if self.team3score >= self.win_score:
                self.game_over(self.team3score, self.team3name. text())
                self.layout.setCurrentIndex(15)
                return 0
        self.turn += 1
        self.current_score = 0
        self.page12score.setText(str(0))
        self.label2_9.setText(str(self.team1score))
        self.label2_10.setText(str(self.team1score))
        self.label2_11.setText(str(self.team1score))
        self.label4_10.setText(str(self.team2score))
        self.label4_11.setText(str(self.team2score))
        self.label6_11.setText(str(self.team3score))

        if self.turn >= len(self.playing_team):
            self.turn = 0
        if self.team_select.currentIndex() == 0:
            self.label_score_10.setText(f" ITS {self.turn +1}'s TURN")
            self.layout.setCurrentIndex(9)
        elif self.team_select.currentIndex() == 1:
            self.label_score_11.setText(f" ITS {self.turn + 1}'s TURN")
            self.layout.setCurrentIndex(10)
        else:
            self.label_score_11.setText(f" ITS {self.turn + 1}'s TURN")

        if self.team_select.currentIndex() == 0:
            self.layout.setCurrentIndex(9)
        elif self.team_select.currentIndex() == 1:
            self.layout.setCurrentIndex(10)
        else:
            self.layout.setCurrentIndex(10)

    def game_over(self, score, name):
        """When this function is called it means the game is over and
        there is a winner. It gives tee winner name and teh score
        they won the game, changes the layout index"""
        self.label3_15.setText(f" {name} WON THE GAME!")
        self.label4_15.setText(f"WITH A SCORE OF {score}")
        self.layout.setCurrentIndex(14)
