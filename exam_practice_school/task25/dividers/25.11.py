# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку
# [110203;110245], числа,
# имеющие ровно четыре различных чётных натуральных делителя
for i in range(110203, 110245):
    c = 0
    deliteli = []
    for j in range(2, int(i**0.5)+1, 2):
        if i % j == 0:
            deliteli.append(j)
            if len(deliteli) > 4:
                break
            deliteli.append(i//j)
            c += 1
    if len(deliteli)==4:
        print(i, sorted(deliteli))


