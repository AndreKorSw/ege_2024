# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку
# [120115;120200],
# число, имеющее максимальное количество различных натуральных делителей,
# если таких чисел несколько  найдите максимальное из них.
# Выведите на экран количество делителей такого числа и само число.
max_del = 0
for i in range(120115,120200):
    cnt_del = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt_del += 1
        if max_del < cnt_del:
            max_del = cnt_del
            val = i
print(val, max_del)



