from random import randint


def word_adder(word, lst):
    """Returns the Message if the words is added
    or not, adds the word to the list of words and
    to the base file if possible"""
    if not word or not word.isalpha():
        message = "Can't add that word because it's empty!"
    elif (a := word.capitalize()) in lst:
        message = 'Already have that word!'
    else:
        message = 'Added!'
        lst.append(a)
        w = open('base.txt', 'a')
        w.write("\n" + a)
    return message


def word_generator(data):
    """Generates a random value from the given data"""
    return data[randint(0, len(data) - 1)]


def is_odd(num):
    """Checkes if the given number is odd"""
    return True if num % 2 == 1 else False






