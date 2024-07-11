# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
# Определите максимальную длину цепочки вида XYZXYZXYZ...
# (составленной из фрагментов XYZ, последний фрагмент может быть неполным).
# Для выполнения этого задания следует написать программу.
f=open('fail').readline()
f=f.replace('XYZ','Q')
c=0
mx=0
for i in range(len(f)-2):
    if f[i]+f[i+1]+f[i+2] =='QXY':
        c+=5
        mx = max(mx, c)
    elif f[i]+f[i+1]=='QX':
        c+=4
        mx = max(mx, c)
    elif f[i]=="Q":
        c+=3
        mx=max(mx, c)
    else:
        c=0
print(mx)
