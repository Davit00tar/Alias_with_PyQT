# Alias_with_pyQt

INTRODUCTION
The digital version of the well-known board game, made using Python's library PyQT5.
The programme consists of several files. All the programming is carried out using Python3 and the Python library PYQT5

ABOUT THE APPLICATION
A Graphically generated application allows the user to see the game Alias on a new window, which pops up after they run the code. First, 
appears three buttons: "PLAY", "RULES", and "ADD WORDS".
After the user clicks on either of them the whole layout changes 
based on what they have clicked. Each layout change is a new page.
ADD WORDS allows the user to add words whatever they want 
to the base of words, which will be discussed later. Originally there
are more than 700 English words, which are mainly nouns. After writing
the word, by simply clicking Add button the system automatically adds the word to the base if possible. If the word already exists in the base 
the user gets a message which says that. After pressing the PLAY button,
the user is asked to choose the number of teams, that are going to play 
the game. Then by playing next the user gets to fill in the names of the teams. After they set the Round duration with seconds and the Win-score. After they selected these all things the game is ready to start.

TECHNOLOGIES
The project is carried out using Python3.9 and Python library PyQT5.
https://doc.qt.io/qtforpython/
The core of the programme is the Class MainWindow which inherits its main features from QMainWindow. All the UI is written in __init__ MainWindow function. Which is the reason for it being too long for a single function. In UI the main thing that helps to organize the page-changing
the effect is carried out using QStackedLayout, which allows us to have multiple layouts on the same window. The layout can be changed using the attribute setCurrentIndex.
the InGame words are generated randomly which is carried out using the randint module from Random

GAME RULES
Alias is a team game. You need to guess as many words as possible in the time limit, following the rules of the Game, which are:
1. When explaining words, it is not allowed to use translations or words with the same roots,
2. If the word(s) is (are) guessed, the explainer clicks on it(s) (+1 point).
3. If an unguessed word is clicked, it can be clicked again and the word will become unmarked(unguessed) again. Also during the game, if 
 there is an appeal, you can go back and click on the marked words again to make them unmarked, that is, not guessed.
4. If all the words on the screen are guessed by the participants, observing the rules of the game, and there is still time left, then a new screen is brought up, and the explainer, using the remaining time, can explain the words on the new screen.
Collected points are saved and added up during the game. The winner is the group that first collects the points needed to win.

THE PROJECTS AIM
The project is done for educational purposes.

BEFORE LAUNCH
Before Launch please make sure you have all the necessities, which include the following:
-Python (at least 3.9 version)
     https://www.python.org/downloads/
-PyQt 5 library
     https://pypi.org/project/PyQt5/

HOW TO LOUNCH
If you have all the requirements, in the command line go to the dictionary, and press ''python3 main.py"


