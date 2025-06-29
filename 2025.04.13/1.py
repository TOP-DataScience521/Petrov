tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']]

def tree_leaves(argument)-> int:
    count_result = 0
    for elem in argument:
        if type(elem) == str:
            count_result += 1
        else:
            count_result += tree_leaves(elem)
    return count_result
    
# >>> tree_leaves(tree)
# 38

