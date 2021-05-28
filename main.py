
equation = input('Введіть рівняння: ')
equation = equation.replace(' ', '')
# Отримувати рівняння як стороку +
# Видалити зайві пробіли +
# Визначити позиції з знаками операції +
# Розділити числа по окремим змінним
# Пріоритети виконання операцій

#~~~~~~~~~~~~~~

# Логіка визначення виразу в дужках

symbols = [ '+', '-', '*', '/', '(', ')']
symbols_loc = []
loc_plus = []
loc_minus = []
loc_multi = []
loc_divide = []
loc_open = []
loc_close = []
numbers = []

for i in range len(equation):
    if equation[i] in symbols:
        symbols_loc.append(i)
    else:
        pass

def create_numbers():
    ttt=0
    for i in symbols_loc:
        numb=equation[ttt:i]
        numbers.append(numb)
        ttt=ttt+i
    return numbers
create_numbers()



def symbols_location():
    for i in range len(equation):
        if equation[i] == "(":
           loc_open.append(i)
        elif equation[i] == ")":
            loc_close.append(i)
        elif equation[i] == "+":
            loc_plus.append(i)
        elif equation[i] == "-":
            loc_minus.append(i)
        elif equation[i] == "*":
            loc_multi.append(i)
        elif equation[i] == "/":
            loc_divide.append(i)
        else:
            pass
    return loc_open, loc_close, loc_plus, loc_minus, loc_multi, loc_divide
symbols_location()
