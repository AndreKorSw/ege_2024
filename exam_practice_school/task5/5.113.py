for i in range(10000, 100000):
    s1=str(i)[0]
    s2=str(i)[1]
    s3=str(i)[2]
    s4=str(i)[3]
    s5=str(i)[4]
    res1=int(s5)+int(s3)+int(s1)
    res2=int(s2)+int(s4)
    if res1>=res2:
        res=int(str(res2)+str(res1))
    else:
        res=int(str(res1)+str(res2))
    if res==621:
        print(i)
        break