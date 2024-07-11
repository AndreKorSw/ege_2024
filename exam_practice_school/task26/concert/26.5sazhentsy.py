# САЖЕНЦЫ!!!

# найти ряд с наибольшим номером в котором есть два соседних места,так что слева и справа места занят
# в ответ максимальный номер ряда и минимальный номер места
f = open("")
n = int(f.readline())
places = []
for s in f:
    row, place = map(int, s.split())
    places.append([row, place])
diff_between_places = 14
places = sorted(places)
for i in range(1, len(places)):
    if (places[i][0] == places[i - 1][0]) and ((places[i][1] - places[i-1][1]) == diff_between_places):
        print(places[i-1], places[i])
