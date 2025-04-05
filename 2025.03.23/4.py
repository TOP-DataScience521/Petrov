num = int(input('Введите натуральное число: '))
limit1 = int('1'+'0'*(num-1))
limit2 = int('9'*num)

numbers = []

for a in range(limit1+1, limit2+1):
    for b in range(2, a):
        if a % b == 0:
            break
    else:
        numbers.append(a)
print(len(numbers))

# Введите натуральное число: 3
# 143

