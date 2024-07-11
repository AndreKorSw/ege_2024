with open('24.5.txt') as f:
    f=f.readline()
c=0
mx=0
for i in range(len(f)-1):
    if f[i]=='Z':
        c+=1
        mx=max(c, mx)
    else:
        c=0
print(mx)