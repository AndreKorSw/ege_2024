# Напишите программу, которая ищет среди целых чисел, принадлежащих
# числовому отрезку [95632;95700], числа, имеющие ровно шесть различных
# чётных натуральных делителей
for i in range(95632, 95700+1):
    dividers = []
    for j in range(2, i + 1, 2):
        if i % j == 0:
            dividers.append(j)
        if len(dividers) > 6:
            break
    if len(dividers) == 6:
        print(sorted(dividers))
