#9
f = open("09 (3).csv")
g = [list(map(int, i.split(","))) for i in f]
c = 0
for i in g:
    if (i.count(min(i)) == 1) and ((max(i)) > ((sum(i)-max(i))/5)*3) and len(set(i)) != len(i):
        c += 1
print(c)