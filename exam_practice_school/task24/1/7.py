s = open("2__1vf5w.txt").readline()
d = 0
mxd = 0
mxa = 0
a = 0
for i in range(len(s) - 1):
    if s[i].isdigit() and s[i + 1].isdigit():
        d+=1
    else:
        mxd =  max(mxd, d)
        d = 0
    if s[i].isalpha() and s[i + 1].isalpha():
        a += 1
    else:
        mxa = max(mxa, a)
        a = 0

print(max(mxa, mxd)+1)

