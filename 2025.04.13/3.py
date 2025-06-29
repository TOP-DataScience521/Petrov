from random import randrange

def tree_generator():
    # Ограничил количество дочерних элементов (веток) до 3 на одном уровне вложенности 
    branchs = randrange(1, 4) 
    result = []
    for _ in range(branchs):
        selection = randrange(0, 2)  
        if selection == 0:
            result.append(tree_generator())
        else:
            result.append('leaf')
    return result


# >>> tree_generator()
# [[[['leaf', 'leaf'], 'leaf'], [[[['leaf', 'leaf', 'leaf'], ['leaf'], ['leaf', 'leaf']]], 'leaf'], 'leaf']]
# >>> tree_generator()
# [['leaf', ['leaf', ['leaf', 'leaf', ['leaf']]], 'leaf']]

