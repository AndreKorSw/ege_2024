from itertools import product

def f(x, y, A):
    return ((x in A) <= (x*x <= 81)) and ((y * y <= 36) <= (y in A))
A = set(range(-100, 100))
for x, y in product(range(-100, 100), repeat = 2):
    if not f(x, y, A):
        A.remove(x)
print(sorted(A))

# def f(x,y,a):
#     return((x in a)<= (x*x <=81)) and ((y*y <=36) <= (y in a))
# a=[ i for i in range(-100,100)]
# for x in range(-100,100):
#           for y in  range(-100,100):
#                     if not f(x,y,a):
#                         a.remove(x)
# print(sorted(a))