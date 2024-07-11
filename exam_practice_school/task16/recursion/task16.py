import sys
sys.setrecursionlimit()
def f(n):
    if n == 1:
        return 0
    if n > 1:
        return f(n - 1) + n
def g(x):
    if x == 1:
        return 1
    if x > 1:
        return g(x - 1) * x
print(f(5)+g(5))
