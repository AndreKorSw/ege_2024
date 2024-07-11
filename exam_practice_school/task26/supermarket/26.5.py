f = open()
n = int(f.readline())
items = [int(i) for i in f]
items.sort()
print(sum(items) - sum(items[:n//6])*0.5)
items.sort(reverse=True)
sale = 0
for i in range(n):
    if (i + 1) % 6 == 0:
        sale += items[i] * 0.5

print(sum(items) - sale)