for n in range(10000, 100000):
    s=str(n)
    s1=int(s[0])+int(s[2])+int(s[4])
    s2=int(s[1])+int(s[3])
    if s1<=s2:
        f=str(s1)+str(s2)
    else:
        f=str(s2)+str(s1)
    if f=="723":
        print(n)
        break
