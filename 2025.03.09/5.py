number1 = str(input('Введите целое число миль: '))
number2 = str(input('Введите дробное число миль: '))

mile_all = round(float(number1+'.'+number2), 2)
km_all = round(mile_all*1.61, 1)

print(f'{mile_all} миль = {km_all} км.')

# Введите целое число миль: 30
# Введите дробное число миль: 55555
# 30.56 миль = 49.2 км.

