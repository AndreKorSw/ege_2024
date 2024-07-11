
count = 0
for x in range(1, 14):
    for y in range(1, 14):
        if -x / 3 ** 0.5 + 14 > y > x / 3 ** 0.5:
            count += 1
print(count)