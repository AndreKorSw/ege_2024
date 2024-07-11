from itertools import product
c = 0
alph = "012345678"
words = product(alph, repeat = 5)
for w in words:
    w = "".join(w)
    if w[0] != "0" and w.count("5") == 1:
        w = w.replace("1", "*")
        w = w.replace("2", "*")
        w = w.replace("3", "*")
        w = w.replace("4", "*")
        if not("*5" in w or "5*" in w):
            c +=1
print(c)