


f = open("26.txt")

max_boxes = 0
min_len_side_box = 0
colvo_korobok = int(f.readline())
boxes = sorted([int(i) for i in f], reverse= True)
diff = 3
podarok = [boxes[0]]

for i in range(1, colvo_korobok):
    if podarok[-1] - boxes[i] >= diff:
        podarok.append(boxes[i])
print(len(podarok), min(podarok))