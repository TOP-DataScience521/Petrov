number = input('Введите цифры на билете: ')

range_1 = number[:3]
range_2 = number[3:]
sum_1 = 0
sum_2 = 0

for n in range_1:
    sum_1 += int(n)
    
for n in range_2:
    sum_2 += int(n)

if sum_1==sum_2:
    print('Да')
else:
    print('Нет')
    
# Введите цифры на билете: 123321
# Да