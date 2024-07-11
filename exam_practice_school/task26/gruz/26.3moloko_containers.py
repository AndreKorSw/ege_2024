# Молокозавод произвел крупную поставку молочных продуктов, которые требуется отправить на продажу с помощью грузового поезда. Все продукты были распределены4 по контейнерам, количество и масса каждого известны. У поезда имеется ограничение по массе продуктов, которое он может увести за раз, оно также известно.
#
# По заданной информации о массе контейнеров и общей массе, которую поезд может увести за один раз, определите наибольшее количество контейнеров, которое он сможет увести
#
# Также определите количество контейнеров, которые заведомо не сможет увести поезд, при условии, что количество погруженных контейнеров наибольшее.
#
# Входные данные.
#
# В первой строке входного файла находятся два числа: М - максимальная масса, которая может быть погружена на поезд (натуральное число, не превышающее 10000 ) и количество контейнеров (натуральное число, не превышающее 1000). В следующих и строках находятся массы всех имеющихся контейнеров (все числа натуральные, не превышающие 200), каждое в отдельной строке.
#
# Запишите в ответе два числа через пробел: наибольшее количество контейнеров, которое поезд смож увести за раз, затем число контейнеров, которые заведомо не сможет увести поезд, при условии, что количество погруженных контейнеров наибольшее.

f = open("")
m = 10000
n = 900
a = sorted([int(i) for i in f])
cur_capacity = []
cnt_over = 0
for i in range(len(a)):
    if a[i] + cur_capacity <= m:
        cur_capacity.append(a[i])
    elif sum(cur_capacity)[:-1] + a[i] > m:
        cnt_over += 1
print(len(cur_capacity), cnt_over)