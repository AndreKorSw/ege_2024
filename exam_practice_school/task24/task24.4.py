with open('24.txt') as f:
    f=f.readline()
mx=0
c=0
for i in range(len(f)-1):
    if f[i] == "X" and f[i + 1] == "Z" and f[i + 2] == "Z" and f[i + 3] == "Y":
        if mx<c:
            mx=c
        c+=3
    else:
        c+=1

    mx=max(c,mx)
print(mx)
