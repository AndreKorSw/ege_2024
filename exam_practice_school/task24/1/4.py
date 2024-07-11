s = open("5__2pp6z.txt").readline()
c = 1
mx = 0
for i in range(1, len(s)):
    if s[i] == s[i -1] == "L":
        c +=1
    else:
        mx = max(c, mx)
        c = 1
print(mx)
s = open("5__2pp6z.txt").readline()
c = 0
mx = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1] == "L":
        c +=1
    else:
        mx = max(c, mx)
        c = 0
print(mx+ 1)
