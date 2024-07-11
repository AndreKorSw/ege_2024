from collections import Counter
with open('fail') as f:
    f=f.readline()
t=''
for i in range(len(f)-2):
    if f[i] == f[i+1]:
        t+=f[i+2]
print(Counter(t).most_common())