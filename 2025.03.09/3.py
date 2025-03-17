number = int(input('Введите количество минут: '))

interval_hour = number // 60
interval_min = number % 60

print(f'{number} мин. - это {interval_hour} час. {interval_min} мин.')

# Введите количество минут: 500
# 500 мин. - это 8 час. 20 мин.