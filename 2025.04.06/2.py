def taxi_cost(meters, minutes = 0) -> int | None:
    if meters < 0 or minutes < 0:
        return None
    elif meters == 0:
        result = 80 + 80 + (minutes // 1) * 3
        return result
    else:
        result = 80 + (meters // 150) * 6 + (minutes // 1) * 3
        return result
        
# >>> taxi_cost(1000, 2)
# 122
# >>> taxi_cost(0)
# 160
# >>> print(taxi_cost(-3))
# None
# >>> print(type(taxi_cost(3)))
# <class 'int'>
