#23  прибавить 1 умножить на два. исходное число 1 конечное 35, должно содержать 10 и не содержать 17
def f(x, y):
    if x > y or x == 17:
        return 0
    elif x == y:
        return 1
    else:
        return f(x+1, y) + f(x*2, y)

print(f(1,10) * f(10,35))