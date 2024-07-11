def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
for x in range(800000, 800100):
    d = div(x)
    for i in d:
        if i % 10 == 9 and i != 9 and i != x:
            print(x, min([s for s in d if s % 10 == 9 and  s != 9 and s != x]))