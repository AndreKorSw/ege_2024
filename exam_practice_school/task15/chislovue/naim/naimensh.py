# d = list(range(17, 59))
# c = list(range(29, 81))
# a = []
# for x in range(1, 100):
#     if (((x in d)) <= (((not(x in c)) and (not(x in a))) <= (not(x in d)))) == False:
#         a.append(x)
# print(a)

# важно: просматривать полностью ответ чтобы отрезок не рвался например [9,10, 11, 14, 15, 16]
# особнно если есть эквивалентность ~ == <->

p1, p2, q1, q2, r1, r2 = 10, 40, 5, 15, 35, 50
P = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
R = [i / 10 for i in range(r1 * 10, r2 * 10 + 1)]
Q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]
A = set()
def f(x, a):
    return ((x in A) or (x in P) or ((x in Q) <= (x in R)))
for x in [i / 10 for i in range(10, 600)]:
    if not f(x, A):
        A.add(x)
print(sorted(A))