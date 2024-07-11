c=0
for n in range(300, 401):
    a=[]
    for i in str(n):
        a.append(i)
    r=sorted(a)
    mx=int(str(r[2])+str(r[1]))
    mn=int(str(r[0])+str(r[1]))

    if mx-mn==20:
        c+=1
print(c)



