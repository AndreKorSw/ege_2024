# Назовём нетривиальным делителем натурального числа его делитель, не равный единице и самому числу.
# Найдите все натуральные числа, принадлежащие отрезку [123456789, 223456789] и имеющие ровно три нетривиальных делителя.
# Для каждого найденного числа запишите в ответе его наибольший нетривиальный делитель. Ответы расположите в порядке возрастания.
for i in range(123456789, 223456789):
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



#нетривиальный делитель не равный единице и самому числу. Все натур числа от 4234679, 10157812 имеющ ровно 5 таких делителя. В ответ само чилсо и наибольший делительь

# !!!оптимизация 1основанная на паре делителей. Если число полный квадрат то делителей нечетное кол-во, иначе четное -> будем проверять только числа которые являются полными квадратами

