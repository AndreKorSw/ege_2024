s = open("27-6a__1vjmj.txt").readlines()[1:]
# Дано число N, затем N натуральных чисел. Требуется найти количество пар чисел, сумма которых кратна 34.
#
# Входные данные: Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество чисел N (1 ≤ N ≤ 10000).
# Каждая из следующих N строк содержит одно натуральное число, не превышающее 1000.
#
# В ответе укажите два числа через пробел: сначала значение для файла А, затем для файла B.

s = open("27-6a__1vjmj.txt").readlines()[1:]
cnt = 0
for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
        if (int(s[i])+int(s[j])) % 34 == 0:
            cnt += 1
print(cnt)


# with open() as f:
#     n = int(f.readline())
#     count = 0
#     D = 34# 1-Делитель ,который мы должны проверить = 17,2 делитель = 2.Общий делитель = 17*2 = 34
#     k = [0]*D#массив,в котором каждый элемент- это количество чисел с определенном остатком от D
#     for i in range(n):
#         x = int(f.readline())
#         for d in range(D):# проходимся по нашим остаткам
#             if (x+d) % 34 == 0:
#                 count += k[d]#прибавляем к счетчику значение в списке k под индексом остатка
#         k[x % D] += 1# увеличиваем определенное значение в списке,в зависимости от того,чему равен остаток x от D
# print(count)