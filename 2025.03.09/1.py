from datetime import datetime


user_name = input('Пожалуйста, введите ваше имя: ')
user_surname = input('Пожалуйста, введите вашу фамилию: ')
user_birth = int(input('Пожалуйста, введите год вашего рождения: '))

year_now = datetime.now().year
user_age = year_now - user_birth

print(user_surname, ' ', user_name, ', ', user_age, sep="")


# Пожалуйста, введите ваше имя: Андрей
# Пожалуйста, введите вашу фамилию: Петров
# Пожалуйста, введите год вашего рождения: 1997
# Петров Андрей, 28


# ИТОГ: 2/2


# КОММЕНТАРИЙ: PEP 8 — сборник рекомендаций по стилистическому оформлению Python кода — их стоит использовать для большего удобства чтения своего и чужого кода: https://peps.python.org/pep-0008/

