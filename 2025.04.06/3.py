def countable_nouns(number: int, words: tuple[str, str, str]):
    numerical_series_1 = [1]
    numerical_series_2 = [2]
    numerical_series_3 = [0]
    
    if int(numerical_series_1[0]) == number:
        return words[0]
    elif int(numerical_series_2[0]) == number:
        return words[1]       
    elif int(numerical_series_3[0]) == number:
        return words[2]  
    else:
        numerical_series_1.append(21)
        if int(numerical_series_1[-1]) <= number:
            while int(numerical_series_1[-1]) < number:
                numerical_series_1.append(numerical_series_1[-1] + 10)
                
        numerical_series_2.append(3)       
        if int(numerical_series_2[-1]) <= number:
            while int(numerical_series_2[-1]) < number:
                if len(numerical_series_2) % 3 == 0:
                    numerical_series_2.append(numerical_series_2[-3]+20)
                else:
                    numerical_series_2.append(numerical_series_2[-1]+1)
                    
        numerical_series_3.append(5)
        if int(numerical_series_3[-1]) <= number:
            while int(numerical_series_3[-1]) < number:
                if number >= 20 and number % 10 < 5:
                    return words[1]
                elif number >= 20:
                    numerical_series_3 = list(range(5, 21))
                    number_start = 25
                    while number_start <= number:
                        for i in range(number_start, number_start + 6):
                            if i <= number:
                                numerical_series_3.append(i)
                        number_start = number_start + 10                
                elif numerical_series_3[-1] <= 20:
                    numerical_series_3.append(numerical_series_3[-1]+1)
                    
    if int(numerical_series_1[-1]) == number:
        return words[0]
    elif int(numerical_series_2[-1]) == number:
        return words[1]      
    elif int(numerical_series_3[-1]) == number:
        return words[2]
                
# >>> countable_nouns(676, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'                
                
                

                
                




