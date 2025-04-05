count = int(input('Введите кол-во для подсчета: '))
numbers_all = []
sum_total = 0

while count > 0:
    try:
        number = int(input('Число: '))
    except ValueError:
        print('Это не целое число')
        break
    else:
        numbers_all.append(number)
        if number > 0:
            sum_total += number
    count = count - 1
else: 
    print(f'Сумма положительных чисел: {sum_total}')
    
# Введите кол-во для подсчета: 6
# Число: 0
# Число: -1
# Число: 5
# Число: 2
# Число: 3
# Число: -1
# Сумма положительных чисел: 10