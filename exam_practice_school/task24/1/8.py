s = open("15__1tiyo.txt").readline().replace("A", "X").replace("E", "X").replace("C", "Y").replace("B", "Y").replace("D", "Y").replace("F", "Y")
c = 0
mx = 0
for i in range(0, len(s) - 2, 2):
    if (s[i] == "X" and s[i+1] == "Y") or (s[i] == "Y" and s[i-1] == "X"):
        c+=1
    else:
        mx = max(c, mx)
        c = 0
print(mx)