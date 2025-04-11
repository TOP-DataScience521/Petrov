cities = [
    {
        'Барнаул': 2,
        'Ижевск': 4,
        'Иркутск': 5,
        'Казань': 4,
        'Новокузнецк': 5,
        'Пермь': 1,
        'Уфа': 5,
        'Хабаровск': 5,
        'Ярославль': 5
    },
    {
        'Барнаул': 2,
        'Воронеж': 3,
        'Иркутск': 6,
        'Казань': 1,
        'Оренбург': 6,
        'Тюмень': 5
    },
    {
        'Казань': 2,
        'Краснодар': 6,
        'Красноярск': 7,
        'Новосибирск': 1,
        'Пермь': 5,
        'Уфа': 3
    },
    {
        'Владивосток': 5,
        'Екатеринбург': 2,
        'Краснодар': 1,
        'Москва': 4,
        'Новосибирск': 6,
        'Самара': 4,
        'Тольятти': 7,
        'Тюмень': 5,
        'Ярославль': 5
    }
]

cities_dictionary = {}

for i in cities:
    for key, value in i.items():
        if key in cities_dictionary:
            cities_dictionary[key].update({value})
        else: 
            cities_dictionary[key] = {value}
            
for key, value in cities_dictionary.items():
    print(repr(key), repr(value), sep = ': ')

# 'Барнаул': {2}
# 'Ижевск': {4}
# 'Иркутск': {5, 6}
# 'Казань': {1, 2, 4}
# 'Новокузнецк': {5}
# 'Пермь': {1, 5}
# 'Уфа': {3, 5}
# 'Хабаровск': {5}
# 'Ярославль': {5}
# 'Воронеж': {3}
# 'Оренбург': {6}
# 'Тюмень': {5}
# 'Краснодар': {1, 6}
# 'Красноярск': {7}
# 'Новосибирск': {1, 6}
# 'Владивосток': {5}
# 'Екатеринбург': {2}
# 'Москва': {4}
# 'Самара': {4}
# 'Тольятти': {7}
    



