string = input('Введите текст: ')

acceptable_numbers = {'1', '0'}

if string[:2] == '0b':
    number = set(string.replace(string[:2], ""))
elif string[:1] == 'b':
    number = set(string.replace(string[:1], ""))
else: 
    number = set(string)

if number == acceptable_numbers:
    print('да')
else:
    print('нет')
        
# Введите текст: b0111010000110
# да
# Введите текст: 111112
# нет
