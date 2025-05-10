def strong_password(password):
    password_numbers = 0
    numbers = list("1234567890")
    special_symbol = list("/!?()[]{}.,;:""''«»–—_…")

    for i in list(password):
        if i in numbers:
            password_numbers +=1
            
    for j in list(password):
        if j in special_symbol:
            check_special_symbol = True
            break
        else:
            check_special_symbol = False
        
    if password_numbers < 2:
        return False
    else:
        if check_special_symbol == False:
            return False
        else:
            if len(password)<8:
                return False
            else:
                if password == password.upper() or password == password.lower():
                    return False
                else:
                    return True
                    
# >>> strong_password('aP3:kD_l3')
# True
# >>> strong_password('qwerty111')
# False