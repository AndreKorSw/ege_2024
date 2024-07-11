f = open("09 (1).csv")
g = [list(map(int, i.split(","))) for i in f]
c = 0
for i in g:
    if len(set(i)) == 5:
        if (max(i) + min(i)) * 3 <= 2*(sum(i) - (max(i) + min(i))):
            c += 1
print(c)