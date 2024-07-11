#Сколько существует программ, которые преобразуют исходное число 1
# в число 11 и при этом не содержат
# двух команд умножения подряд?
def f(x, y, flag):
    if x> y:
        return 0
    if x == y:
        return 1
    elif flag:
        return f(x+1, y, True) + f(x+2, y, True) + f(x*2, y, False)
    else:
        return f(x+1, y, True) + f(x+2, y, True)
print((f(1, 11, True)))

