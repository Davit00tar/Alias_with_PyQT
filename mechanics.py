from random import randint


def word_adder(word, lst):
    if not word:
        message = "Can't add that word because it's empty!"
    elif (a := word.capitalize()) in lst:
        message = 'Already have that word!'
    else:
        message = ''
        lst.append(a)
        w = open('base.txt', 'a')
        w.write("\n" + a)
    return message


def word_generator(data):
    return data[randint(0, len(data) - 1)]


def is_odd(num):
    return True if num % 2 == 1 else False






