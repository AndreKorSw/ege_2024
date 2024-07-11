for i in range(100, 1000):
    s1=str(i)[0]
    s2 = str(i)[1]
    s3 = str(i)[2]
    res1=int(s1)*int(s2)
    res2=int(s2)*int(s3)
    if res1>=res2:
        res=int(str(res2)+str(res1))
    else:
        res = int(str(res1) + str(res2))
    if res==621:
        print(i)
        break