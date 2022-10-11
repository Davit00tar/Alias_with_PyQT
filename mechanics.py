def word_adder(word, lst):
    if word in lst:
        print('Already have that word!')
    elif word == ('' or ' '):
        print('That is not a Word')
    else:
        lst.append(word.capitalize())


