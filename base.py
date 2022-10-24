
base = open('base.txt', 'r')
base_lst = base.read().splitlines()
base.close()



def tester(lst, target):
    return target in lst

game_rules = ''' 
The .currentIndexChanged signal is triggered when the
currently selected item is updated, by default passing the index of the 
selected item in the list. However, when connecting to the signal you can also
request an alternative version of the signal by appending [str] (think of the signal
as a dict). This alternative interface instead provides the label of the currently 
selected item, which is often more useful.'''

