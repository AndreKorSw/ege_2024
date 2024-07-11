# Системный администратор раз в неделю создаёт архив пользовательских файлов. Однако объём диска, куда он помещает архив, может быть меньше, чем суммарный объём архивируемых файлов. Известно, какой объём занимает файл каждого пользователя.
#
# По заданной информации об объёме файлов пользователей и свободном объёме на архивном диске определите максимальное число пользователей, чьи файлы можно сохранить в архиве, а также максимальный размер имеющегося файла, который может быть сохранён в архиве, при условии, что сохранены файлы максимально возможного числа пользователей.
#
# Входные данные.
#
# Задание 26
#
# В первой строке входного файла находятся два числа: S  — размер свободного места на диске (натуральное число, не превышающее 10 000) и N  — количество пользователей (натуральное число, не превышающее 4000). В следующих N строках находятся значения объёмов файлов каждого пользователя (все числа натуральные, не превышающие 100), каждое в отдельной строке.
#
# Запишите в ответе два числа: сначала наибольшее число пользователей, чьи файлы могут быть помещены в архив, затем максимальный размер имеющегося файла, который может быть сохранён в архиве, при условии, что сохранены файлы максимально возможного числа пользователей.
f = open("26.2.txt")
disk_capacity, num_users = map(int, f.readline().split())
files = sorted(map(int, f))
max_num_users = 0
max_file = 0
cur_capacity = 0
for file in files:
    if cur_capacity + file <= disk_capacity:
        cur_capacity += file
        max_file = max(max_file, file)
        max_num_users += 1
    else:
        print(max_num_users, disk_capacity - cur_capacity + max_file)
        break