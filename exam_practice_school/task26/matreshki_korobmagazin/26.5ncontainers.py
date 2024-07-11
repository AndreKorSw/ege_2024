# На складе хранятся кубические контейнеры двух цветов различного размера.
#
# Чтобы сократить занимаемое при хранении место, контейнеры вкладывают друг в друга. Чтобы вложенные контейнеры было лучше видно, их цвета при вложении обязательно должны чередоваться, то есть нельзя вкладывать контейнер в контейнер такого же цвета. Один контейнер можно вложить в другой, если размер стороны внешнего контейнера превышает размер стороны внутреннего на 7 и более условных единиц. Группу вложенных друг в друга контейнеров называют блоком. Количество контейнеров в блоке может быть любым. Каждый блок, независимо от количества и размера входящих в него контейнеров, а также каждый одиночный контейнер, не входящий в блоки, занимает при хранении одну складскую ячейку.
#
# Зная размеры и цвета всех контейнеров, определите максимально возможное количество контейнеров в одном блоке и минимальное количество ячеек для хранения всех контейнеров.



f = open("26.5.txt")
a = [i for i in f]
diff = 7
containers = []
for i in range(len(a)):
    size, color = int(a[i].split()[0]), a[i].split()[1]

    containers.append([size, color])
containers.sort(reverse=True)
#
kuda_kladem =[containers[0]]
bloks = []
for i in range(1, len(containers)):
    bloks = []
    if kuda_kladem[-1][0] - containers[i][0] >= diff and kuda_kladem[-1][1] != containers[i][1]:
        kuda_kladem.append(containers[i])
    bloks.append(kuda_kladem)

print(len(bloks[0]), len(bloks))
#
#
# box=[]
# cklad =[]
# for i in f:
#     size, color = i.split()
#     box.append([int(size),color])
# box.sort(reverse=True)
# while len(box)>0:
#     block = [box.pop(0)]
#     for j in range (len(box)):
#         if block[-1][0]-box[j][0] >= 7 and box[j][1] != block[-1][1]:
#             block.append(box[j])
#             box[j]=''
#     box = [x for x in box if x!='']
#     cklad.append(block)
# print(max(len(x) for x in cklad), len(cklad))