# Назовём нетривиальным делителем натурального числа его делитель,
# не равный единице и самому числу.
#  Найдите все натуральные числа, принадлежащие отрезку
#  [289123456;389123456] и имеющие ровно три нетривиальных делителя.
#  Для каждого найденного числа запишите в ответе его наибольший
#  нетривиальный делитель. Ответы расположите в порядке возрастания.
for i in range(289123456, 389123456+1):
    dividers = set()
    if (i ** 0.5) == int(i ** 0.5):  # !!! оптимизация 1
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                dividers.add(j)
                dividers.add(i // j)
            if len(dividers) > 3:
                break
    if len(dividers) == 3:
        print(i, max(dividers))
