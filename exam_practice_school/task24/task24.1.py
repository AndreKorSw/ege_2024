with open('fail') as f:
    f=f.readline()
mx=0
c=1
for i in range(len(f)-1):
    if f[i] != f[i+1]:
        c+=1
        mx=max(mx, c)

    else:
        c=1
print(mx)