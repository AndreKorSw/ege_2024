f = open("26 (8).txt")
n = int(f.readline())
chastici = []

for s in f:
    row, number = map(int, s.split())
    chastici.append([row, number])

chastici.sort()
cur_len = 1
for i in range(len(chastici)):
    if chastici[i][0] == chastici[i+1][0] and chastici[i+1][1] - chastici[i][1] <= 1:
        if chastici[i+1][1] - chastici[i][1] == 1:
            cur_len += 1
            print(cur_len, chastici[i][0])
    else:
        cur_len = 1
        break
