def central_tendency(number1: float, number2: float, *numbers: float) -> dict[str, float]:
    numbers_all = sorted([number1, number2, *numbers])
    count_numbers = len(numbers_all)
    
    medium = count_numbers // 2
    if len(numbers_all) % 2 == 0:
        median = (numbers_all[medium] + numbers_all[medium - 1]) / 2
    else:
        median = float(numbers_all[medium])
        
    arithmetic = sum(numbers_all) / count_numbers
    
    product_num = 1
    for i in numbers_all:
        product_num *= i
        
    geometric = product_num ** (1 / count_numbers)
    harmonic = count_numbers / sum(1/i for i in numbers_all)
    
    indicators = ['median', 'arithmetic', 'geometric', 'harmonic']
    result = (median, arithmetic, geometric, harmonic)

    return dict(zip(indicators, result))
    
# >>> central_tendency(4,3,2,1,100)
# {'median': 3.0, 'arithmetic': 22.0, 'geometric': 4.742881219558624, 'harmonic': 2.388535031847134}
    
# >>> sample = [10, 8, 5, 9]
# >>> central_tendency(*sample)
# {'median': 8.5, 'arithmetic': 8.0, 'geometric': 7.745966692414834, 'harmonic': 7.461139896373057}    