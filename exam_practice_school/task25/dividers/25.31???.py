# Найдите все натуральные числа, принадлежащие отрезку [101000000,102000000],
# у которых ровно три различных чётных делителя (при этом количество нечётных делителей может быть любым).
# В ответе перечислите найденные числа в порядке возрастания.



#

def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True
for i in range(101000000, 102000000 + 1, 2):
    if (i // 2) ** 0.5 == int((i // 2) ** 0.5):
        if isprime((i // 2) ** 0.5):
            print(i)