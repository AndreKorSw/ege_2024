# 174457, 174505 числа у кот
# два различн натур делителя не считая единицы
# и самого числа
for i in range(174457, 174505+1):
    d = set()
    for j in range(2, i):
        if i % j == 0:
            d.add(j)
    if len(d) == 2:
        print(d)
