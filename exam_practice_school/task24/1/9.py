# символов латинского алфавита. Определите максимальное количество идущих подряд символов,
# среди которых любые три символа из набора A, B, C, D, E, F в различных комбинациях (с учётом повторений) не образуют тройку.
f = open()
s = f.readline()
s = s.replace("B’", "’A’").replace("’C’", '’A’').replace("’D’", "A’").replace("’E", "A").replace("’F", '’A’')
while "’AAA’" in s:
    s = s.replace("’AAA’", "’AA AA’")
s = s.split()
print(max(map(len, s)))