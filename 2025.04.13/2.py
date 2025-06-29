def deck():
    suits = ['черви', 'бубны', 'пики', 'трефы']
    nominals = list(range(2, 15))
    
    for suit in suits:
        for nominal in nominals:
            yield (nominal, suit)

deck_obj = deck()
            
# >>> list(deck())[12::13]
# [(14, 'черви'), (14, 'бубны'), (14, 'пики'), (14, 'трефы')]

# >>> list(deck())[11:15]
# [(13, 'черви'), (14, 'черви'), (2, 'бубны'), (3, 'бубны')]

# >>> deck_obj.__next__()
# (2, 'черви')
# >>> deck_obj.__next__()
# (3, 'черви')
# >>> deck_obj.__next__()
# (4, 'черви')
# >>> deck_obj.__next__()
# (5, 'черви')

