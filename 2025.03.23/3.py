num = int(input('Введите натуральное число: '))
divisors = []
sum_divisors = 0

iterations = range(1, num+1)
for n in iterations:
    if num % n == 0:
        divisors.append(n)
        sum_divisors += n
print('Сумма делителей: ', sum_divisors)

# Введите натуральное число: 48
# Сумма делителей:  124