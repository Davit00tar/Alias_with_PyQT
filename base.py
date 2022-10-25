
base = open('Mechanics/base.txt', 'r')
base_lst = base.read().splitlines()
base.close()

game_rules = ''' 
Alias is a team game. You need to guess as many 
words as possible in the time limit,following 
the rules of the Game, which are:
1.When explaining words, it is not allowed to 
 use translations or words with the same roots,
2.If the word(s) is (are) guessed, the 
 explainer clicks on it(s) (+1 point).
3.If an unguessed word is clicked, it can be 
clicked again and the word will become unmarked
 (unguessed) again. Also during the game, if 
 there is an appeal, you can go back and click 
 on the marked words again to make them unmarked,
 that is, not guessed.
4.If all the words on the screen are guessed by 
 the participants, observing the rules of the game,
 and there is still time left, then a new screen 
 is brought up, and the explainer, using the 
 remaining time, can explain the words on the 
 new screen.
Collected points are saved and added up during the 
game. The winner is the group that first collects 
the points needed to win.
'''

