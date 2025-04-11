square1 = input('Введите координаты для 1 клетки: ')
square2 = input('Введите координаты для 2 клетки: ')

horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
vertical = range(1,9)

color_white = []
color_black = []

horizontal_range = range(1, len(horizontal)+1)

for i in vertical:
    for j in horizontal_range:
        if (i+j) % 2 == 1:
            code = horizontal[j-1]+str(i)
            color_white.append(code)
        else:
            code = horizontal[j-1]+str(i)
            color_black.append(code)
            
if square1 in color_white and square2 in color_white:
    print('да')
elif square1 in color_black and square2 in color_black:
    print('да')
else:
    print('нет')
    
# Введите координаты для 1 клетки: b1
# Введите координаты для 2 клетки: f3
# да

# Введите координаты для 1 клетки: b2
# Введите координаты для 2 клетки: c4
# нет
            
        

