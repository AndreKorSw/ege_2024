
f=open('24.6.txt')
s=f.read()
maxi=0
c=0
i=0
while i < len(s)-2:
    if s[i] in "AO" and s[i+1] in 'AO' and s[i+2] in 'CDF':
        c+=1
        maxi=max(maxi,c)
        i+=2
    else:
        c=0
        i+=1
print(maxi)