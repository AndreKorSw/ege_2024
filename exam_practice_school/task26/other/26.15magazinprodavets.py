# Продавец предоставляет покупателю, делающему большую закупку, скидку по следующим правилам:
#
# — на каждый второй товар стоимостью больше 50 рублей предоставляется скидка 25%;
#
# — общая стоимость покупки со скидкой округляется вверх до целого числа рублей;
#
# — порядок товаров в списке определяет продавец и делает это так, чтобы общая сумма скидки была наименьшей.
#
# По известной стоимости каждого товара в покупке необходимо определить общую стоимость покупки с учётом скидки и стоимость самого дорогого товара, на который будет предоставлена скидка.
#
# Входные данные.
#
# Задание 26
#
# Первая строка входного файла содержит число N  — общее количество купленных товаров. Каждая из следующих N строк содержит одно целое число  — стоимость товара в рублях.
#
# В ответе запишите два целых числа: сначала общую стоимость покупки с учётом скидки, затем стоимость самого дорогого товара, на который будет предоставлена скидка.
#
# Пример входного файла:
#


# Заметим, что числа, меньшие 51 можно сразу суммировать, поскольку на них скидка не распространяется. Поэтому, построчно считывая числа из файла, числа, меньшие 51, будем сразу накапливать в переменной sum, а остальные числа будем записывать в массив. Далее, отсортировав массив по возрастанию, будем прибавлять к переменной sum стоимость товара с учётом скидки, если данный элемент массива имеет индекс, меньший, чем количество чисел, поделённое пополам, и без учёта скидки в остальных случаях.
# # 6
# from math import ceil
f = open("inf_22_10_20_26.txt")
colvo_kup_tovarov = int(f.readline())
price_for_tovar = sorted([int(i) for i in f])
price_with_sale =[]
final_price = 0
max_price = 0
for i in range(colvo_kup_tovarov):
    if price_for_tovar[i] <= 50:
        final_price += price_for_tovar[i]
    else:
        price_with_sale.append(price_for_tovar[i])
for i in range(len(price_with_sale)):
    if i < len(price_with_sale) // 2:
        final_price += price_with_sale[i] * 0.75
        max_price = round(price_with_sale[i])
    else:
        final_price += price_with_sale[i]
print(ceil(final_price), max_price)

