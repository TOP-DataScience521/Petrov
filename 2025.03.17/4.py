try:
    num = float(input('Введите число: '))
    
except ValueError:
    print('Не является числом')
    
else:
    result = 2 ** num
    if result % 2 == 0 or result == 1:
        print('да')
    else:
        print('нет')
        

# Введите число: 0
# да

# Введите число: 7
# да

# Введите число: -9
# нет

# Введите число: 5.5
# нет

# Введите число: dsjv
# Не является числом