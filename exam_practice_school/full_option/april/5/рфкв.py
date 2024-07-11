def tri(n):
    x = ""
    while n != 0:
        x = str(n % 3) + x #  вопрос куда дописывать  остаток или +=
        n //= 3
    return x
mn = 1000000
for n in range(1, 1000):
    x = tri(n)
    if n % 3 == 0:
        x += x[-2:]
    else:
        x += tri(n % 3 *5)
    if int(x, 3) > 133:
        print(int(x, 3))
        mn = min(mn, int(x, 3))
print(mn)

