# 16
# fn = 2 n < 3
# fn = 2n + 5 + f(n-2) n >=3
f = [0] * 3500
for n in range(1, 3500):
    if  n < 3:
        f[n] = 3
    else:
        f[n] = 2 * n + 5 + f[n-2]
print(f[3027] - f[3023])
# fn = 1; n == 1
# fn = 2 * fn-1 + n + 1; n > 1
f[0] * 50
f[1] = 1
for n in range(2, 50):
    f[n] = 2*f[n-1] + n + 3
print(f[19])
# f(n) = 1 n <2
# f(n) = f(n/3) + 1  n >=2 n %3 ==0
# f(n) = f(n-2) + 5 n >=2 n %3 !=0
# найти кол во значений n на отрезке [1 100001] для которых f(n) == 55
f = [0] * 100001
for n in range(1, 100001):
    if n < 2:
        f[n] = 1
    elif n % 3 == 0:
        f[n] = f[n // 3] + 1
    else:
        f[n] = f[n-2] + 5
print(f.count(55))