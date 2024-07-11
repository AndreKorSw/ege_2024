with open('24.7.txt') as f:
    f=f.readline()
c=1
mx=0
for i in range(len(f)-1):
    if f[i]!=f[i+1]:
        c+=1
        mx=max(c, mx)
    else:
        c=1
print(mx)