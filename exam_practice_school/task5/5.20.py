for i in range(1000, 10000): # чтобы найти наибольшее нужно развернуть цикл
     s = str(i)
     k1 = int(s[0]) + int(s[1])
     k2 = int(s[1]) + int(s[2])
     k3 = int(s[2]) + int(s[3])
     first = str(k1 + k2 + k3 - max(k1, k2, k3) - min(k1, k2, k3)) #серединное значение
     second = str(max(k1, k2, k3))
     res = first + second
     if res == "1517":
         print(i)
