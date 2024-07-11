# Определите количество натуральных значений n   из отрезка [1;300]
# , при которых значение F (n )   превышает   10 ** 5
from functools import lru_cache
lru_cache(None)
def f(n):
    if int(n) != n or n < 0: # добавить такую проверку
        return  -99999999
    if n < 3:
        return  2 * n * n  + 2
    if n > 2 and n % 5 == 0:
        return 2 * f(n-2) + f(n/2) + n
    if n > 2 and n % 5 != 0:
        return n * n + f(n-2) + 1 + f(n/3)
ans = 0
for i in range(1, 301):
    if f(i) > 10 ** 5:
        ans += 1
print(ans)#  ответ 0