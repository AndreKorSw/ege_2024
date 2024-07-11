
from itertools import permutations
y = [list(map(int,i.split(","))) for i in open('107_9.txt.csv')]
q = 0
for u in y:
    if all(n[0]+n[1]>n[2] for n in permutations(u,3)):
        q += 1
print(q)