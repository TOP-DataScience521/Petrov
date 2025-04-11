scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

word = list((input('Введите слово: ').upper()).replace('Ё', 'Е'))
result = 0

for i in word:
    for a, b in scores_letters.items():
        if i in b:
            result += a

print(result)

# Введите слово: ёлка
# 6
# Введите слово: синхрофазотрон
# 29
