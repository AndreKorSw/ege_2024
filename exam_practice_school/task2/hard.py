print("x y z w --- F")
# смотрим чтобы не было одинаковых столбиков когда вписываем нули и единицы, максимально все исключаем
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = int(((w <= x) == (z <= y)) and ((not(y)) or w))
                print(x, y, z, w, "___", f)
