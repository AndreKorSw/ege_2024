def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(700000, 700100):
    d = div(i)
    if d:
        m = str(min(d) + max(d))
        if m[-1] == "4":
            print(i, m)