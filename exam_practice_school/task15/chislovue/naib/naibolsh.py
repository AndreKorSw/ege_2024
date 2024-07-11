# P = [i for i in range(5,31)]
# Q = [i for i in range(14,24)]
# A = [i for i in range(5,31)]
# for x in range(5,31):
#     if (((x in P) == (x in Q)) <= (not(x in A))) == True:
#         A.remove(x)
# print(max(A) - min(A))


# важно: просматривать полностью ответ чтобы отрезок не рвался например [9,10, 11, 14, 15, 16]
# особнно если есть эквивалентность ~ == <->
p1, p2, q1, q2 = 2, 10, 6, 14
p = [i / 10 for i in range(p1 *10, p2* 10)]
q = [i / 10 for i in range(q1 *10, q2* 10)]
a = set([i / 10 for i in range(10, 201)])
def f(x, a):
    return (((x in a) <= (x in p)) or (x in q))
for x in [i/10 for i in range(10, 201)]:
    if not f(x,a):
        a.remove(x)
print(a)