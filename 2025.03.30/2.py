# Вариант 1
fruits_list = []

while True:
    fruit = input('Введите фрукт: ')
    if fruit != '':
        fruits_list.append(fruit)
    else:
        result = ', '.join(fruits_list[:-1]) + ' и ' + fruits_list[-1]
        print(result)
        break
        
# Вариант 2
fruits_list = []

while True:
    fruit = input('Введите фрукт: ')
    if fruit != '':
        fruits_list.append(fruit)
    else:
        break

result = ' и '.join(fruits_list)
replace_num = result.count(' и ')-1
result = result.replace(' и ', ', ', replace_num)
print(result)

# Введите фрукт: яблоко
# Введите фрукт: банан
# Введите фрукт:
# яблоко и банан

# Введите фрукт: яблоко
# Введите фрукт: груша
# Введите фрукт: ананас
# Введите фрукт: гранат
# Введите фрукт: вишня
# Введите фрукт:
# яблоко, груша, ананас, гранат и вишня

