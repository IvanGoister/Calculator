
equation = input('Введіть рівняння: ')
equation = equation.replace(' ', '')
len_equation=len(equation)
# Отримувати рівняння як стороку +
# Видалити зайві пробіли +
# Визначити позиції з знаками операції +
# Розділити числа по окремим змінним
# Пріоритети виконання операцій
print(equation)
print(len(equation))
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

for i in range(0, len_equation):
    if equation[i] in symbols:
        symbols_loc.append(i)
    else:
        pass


def symbols_location():
    for i in range(0, len_equation):
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

#   1+2*34+5/6+789

def create_numbers():
    last_i = symbols_loc[0]
    numbers.append(int(equation[0:last_i]))
    for i in symbols_loc:
        if i == symbols_loc[0]:
            last_i = i + 1
            pass
        else:
            numb=equation[last_i:i]
            numbers.append(int(numb))
            last_i=i+1
    if symbols_loc[-1] < len(equation):
        tt=symbols_loc[-1]+1
        th=equation[tt:]
        numbers.append(int(th))
    else:
        pass
    return numbers
create_numbers()

print('symbols_loc ',  symbols_loc)
print('loc_plus ',  loc_plus)
print('loc_minus ', loc_minus)
print('loc_multi ', loc_multi)
print('loc_divide ', loc_divide)
print('loc_open ', loc_open)
print('loc_close ', loc_close)
print('numbers ', numbers)
