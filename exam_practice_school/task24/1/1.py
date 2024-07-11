# Текстовый файл состоит из символов Z, Y, X, O и P.
# Определите максимальное количество идущих подряд символов,
# среди которых не более 4 пар вида гласная + согласная в прилагаемом файле
s = open("24-5__33ojv.txt").readline()

s = s.replace('Y', 'O').replace('Z','P').replace('X', 'P')
s = s.replace('OP','O P').split()
m = 0
for i in range(len(s)-4):
    s1 = s[i] + s[i+1] + s[i+2] + s[i+3] + s[i+4]
    if len(s1) > m:
        m = len(s1)
print(m)
