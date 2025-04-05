number = int(input('Введите натуральное число: '))
a0 = 0
a = 0
b = 1
i = 1
numbers = [1]

while i < number:
    c = a + b
    numbers.append(c)
    a = b
    b = a0+b
    a0 = a
    i += 1
    
for num in numbers:
            print(num, end = ' ')

# Введите натуральное число: 10
# 1 1 2 3 5 8 13 21 34 55



