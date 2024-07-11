f = open("27_A_17538.txt")
n = 311
s = [int(i) for i in f]
mxa = 0
for l in range(n):
    for m in range(l+1, n):
        for r in range(m + 2, n):
            mxa = max(mxa, (sum(s[m+1:r+1]) - sum(s[l:m+1])))
print(mxa)