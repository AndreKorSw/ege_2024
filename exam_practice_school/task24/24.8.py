with open('248.txt') as f:
    f=f.readline()
f=f.replace('LDR', 'Q')
mx=0
c=0
for i in range(len(f)-2):
    if f[i]+f[i+1]+f[i+2]=='QLD':
        c+=5
        mx=max(mx, c)
    elif  f[i]+f[i+1]=='QL':
        c+=4
        mx = max(mx, c)
    elif f[i] =='Q':
        c+=3
        mx = max(mx, c)
    else:
        c=0
print(mx)