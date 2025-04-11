square1 = input('Введите координаты для 1 клетки: ')
square2 = input('Введите координаты для 2 клетки: ')

horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

square1_horizontal = horizontal.index(square1[0])
square1_vertical = int(square1[1])
square2_horizontal = horizontal.index(square2[0])
square2_vertical = int(square2[1])

if (abs(square2_horizontal-square1_horizontal) <= 1 and 
    abs(square2_vertical-square1_vertical) <= 1):
    print('да')
else:
    print('нет')
    
# Введите координаты для 1 клетки: b2
# Введите координаты для 2 клетки: c3
# да

# Введите координаты для 1 клетки: b2
# Введите координаты для 2 клетки: f2
# нет