#14  Для найденных значений x и y вычислите частное от деления значения арифметического выражения на 56
# и укажите его в ответе в десятичной системе счисления.
result_search = []
for x in '0123456789ABCDE':
    for y in '0123456789ABCDE':
        t = int('90' + x + '4' + y, 15) + int('91' + x + y + '2', 16)
        if t % 56 == 0:
            result_search.append(t)
if result_search:
    print(min(result_search) // 56)