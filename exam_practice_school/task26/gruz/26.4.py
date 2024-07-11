f = open("26 (2).txt")

capacity, quantity = map(int, f.readline().split())
containers = sorted([int(i) for i in f])
cur_containers = []
for i in range(len(containers)):
    if sum(cur_containers) + containers[i] <= capacity:
        cur_containers.append(containers[i])
    elif sum(cur_containers[:-1]) + containers[i] < capacity:
        cur_containers = cur_containers[:-1]
        cur_containers.append(containers[i])
print(max(cur_containers), len(cur_containers))