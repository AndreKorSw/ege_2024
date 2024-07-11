
#23 Сколько существует программ, которые преобразуют исходное число 1в число 20,
# и при этом траектория вычислений содержит ровно одно из чисел 9 и 10?
def f(x, y):
    if x > y or x == 10:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 2, y)
def f1(x, y):
    if x > y or x == 9:
        return 0
    if x == y:
        return 1
    else:
        return f1(x + 1, y) + f1(x * 2, y)
print(f(1, 9) * f(9, 20) + f1(1, 10) * f1(10, 20))