# сумма всех делителей числа кроме самого числа и 1 кратна 13
# 350300, первые 6 таких чисел
n = 350300
cnt = 0
while cnt != 6:
    d = set()
    for i in range(2, n):
        if n % i == 0:
            d.add(i)
    if sum(d) % 13 == 0:
        print((n, sum(d) // 13))
        cnt += 1
    n += 1
