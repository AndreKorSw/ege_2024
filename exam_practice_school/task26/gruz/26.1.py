# на грузовом судне перевозят контейнеры разной массы и одинак габаритов
f = open('')
capacity, n = map(int, f.readline().split())
containers = sorted([int(s) for s in f])# все коробки
on_board_containers = []# коробки которые будем хранить на судне
for i in range(len(containers)):
    if sum(on_board_containers) + containers[i] <= capacity:#если влезают то добавляем на судно
        on_board_containers.append(containers[i])

    elif sum(on_board_containers[:-1]) + containers[i] <= capacity:# если не влезает то смотрим без последнего влезает или нет 
        del on_board_containers[-1]
        on_board_containers.append(containers[i])

print(len(on_board_containers), max(on_board_containers))