# чтобы ни одна буква не оставась на прежнем месте
from itertools import *
a = "ГЛУБИНА"
words = permutations(a)
c = 0
for i in words:
    w = "".join(i)
    t = [j != a.find(w[j]) for j in range(len(a))]
    if all(t):
        c+=1
print(c)