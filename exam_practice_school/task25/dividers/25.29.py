# Пусть M(N)— пятый по величине делитель натурального числа N без учёта самого числа и единицы.
# Если у числа N меньше 5 различных делителей, не считая единицы и самого числа, считаем, что M(N)=0.
n = 460000000+1
cnt = 0
while cnt != 5:
    dividers = []
    for i in range(2, (n//2) + 1):
        if n % i == 0:
            dividers.append(n//i)
        if len(dividers) == 5:
            print(dividers)
            val = dividers[4]
            if val > 0:
                print(val)
                cnt+=1
                break
    n+=1



# count = 0
# i = 460000001
# while count < 5:
#     halfI = i // 2
#     countDel = 0
#     for j in range(2, halfI + 1):
#         if i % j == 0:
#             countDel += 1
#             if countDel == 5:
#                 print(i // j)
#                 count += 1
#                 break
#     i += 1