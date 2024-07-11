# f = open("27_A_17566.txt")
# a = [int(i) for i in f]
# n = 10000
# mn = 1000000 #мин сумма
# ml = 0 # максимальная длинна минимальной суммы
# for i in range(1, n):
#     s = 0 # сумма
#     for j in range(i+1, n):
#         s+=a[j]
#         if s % 2  != 0 and s < mn or (s == mn and ml < j - i):
#             ml = j - i
#             mn = s
