square1 = input('Введите координаты для 1 клетки: ')
square2 = input('Введите координаты для 2 клетки: ')

square1_a = square1[0]
square1_b = square1[1]

square2_a = square2[0]
square2_b = square2[1]

if square1_a == square2_a or square1_b == square2_b:
    print('да')
else:
    print('нет')
    
# Введите координаты для 1 клетки: b1
# Введите координаты для 2 клетки: f1
# да

# Введите координаты для 1 клетки: b1
# Введите координаты для 2 клетки: f3
# нет