numbers = []

while True:
    number = int(input('Введите число: '))
    if number % 7 == 0:
        numbers.append(number)
    else:
        result = numbers[::-1]
        for num in result:
            print(num, end = ' ')
        break
           
# Введите число: 7
# Введите число: 7
# Введите число: 21
# Введите число: 35
# Введите число: 28
# Введите число: 5
# 28 35 21 7 7