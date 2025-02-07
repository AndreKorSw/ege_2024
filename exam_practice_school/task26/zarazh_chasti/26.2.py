# При проведении эксперимента заряженные частицы попадают на чувствительный экран, представляющий из себя матрицу размером 10 000 на 10 000 точек. При попадании каждой частицы на экран в протоколе фиксируются координаты попадания: номер ряда (целое число от 1 до 10 000) и номер позиции в ряду (целое число от 1 до 10 000).
#
# Точка экрана, в которую попала хотя бы одна частица, считается светлой, точка, в которую ни одна частица не попала,  — тёмной.
#
# При анализе результатов эксперимента рассматривают группы светлых точек, расположенных в одном ряду подряд, то есть без тёмных точек между ними.
#
# Вам необходимо по заданному протоколу определить максимальную длину такой группы и номер ряда, в котором эта группа встречается. Если таких рядов несколько, укажите минимально возможный номер.
#
# Входные данные.
#
# Задание 26
#
# Первая строка входного файла содержит целое число N  — общее количество частиц, попавших на экран. Каждая из следующих N строк содержит 2 целых числа: номер ряда и номер позиции в ряду.
#
# В ответе запишите два целых числа: сначала максимальную длину непрерывной группы светлых точек, затем  — номер ряда, в котором эта группа встречается.



f = open("26 (8).txt")
n = int(f.readline())
chasti = []
for i in f:
    row, place = map(int, i.split())
    chasti.append([row, place])
chasti.sort()
print(len(chasti))