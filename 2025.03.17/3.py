year = int(input('Введите год: '))

condition_1 = year % 4
condition_2 = year % 100
condition_3 = year % 400

if condition_3 == 0 or condition_1 == 0 and condition_2 != 0:
    print('да')
else:
    print('нет')

   
# Введите год: 1600
# да

# Введите год: 1700
# нет

# Введите год: 1704
# да