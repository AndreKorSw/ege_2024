# На вход программы подаётся: в первой строке — количество входных чисел
# N (N  ≤ 106)  . В последующих N строках - последовательность из N целых чисел.
# Известно, что каждое число положительное и не превышает 700 000 000. Найти среди них такие три числа, что их сумма максимальна,
# и хотя бы два из них имеют разные остатки от деления на 17. Ответом является такая максимальная сумма.
# Гарантируется, что такая тройка чисел есть. Пример организации исходных данных во входном файле:
f = open("27B__1vpyj.txt").readlines()[1:]
mx = 0
for i in range(1, len(f)-1):
    for j in range(i+1, len(f)):
        for v in range(j+1, len(f) - 1):
            if (int(f[i]) % 17 != int(f[j]) % 17) or (int(f[i]) % 17 != int(f[v]) % 17) or (int(f[j]) % 17 != int(f[v]) % 17):
                sm = int(f[i]) + int(f[j]) + int(f[v])
                mx = max(sm, mx)
print(mx)