f = open("107_9 (2).csv")
g =[list(map(int, i.split(","))) for i in f]
c =0
for i in g:
    i = sorted(i)
    if (min(i) + max(i))**2 > i[1]**2 + i[2]**2 + i[3]**2:
        c +=1
print(c)