# В заявке указаны время сдачи багажа и время освобождения ячейки (в минутах от начала суток). Багаж одного пассажира размещается в одной свободной ячейке с минимальным номером. Ячейки пронумерованы начиная с единицы. Размещение багажа в ячейке или её освобождение происходит в течение 1 мин. Багаж можно поместить в только что освобождённую ячейку начиная со следующей минуты.
#
# Если в момент сдачи багажа свободных ячеек нет, то пассажир уходит. Определите, сколько пассажиров сможет сдать свой багаж в течение 24 ч и какой номер будет иметь ячейка, которую займут последней. Если таких ячеек несколько, укажите минимальный номер ячейки.
#
# Входные данные
#
# В первой строке входного файла находится натуральное число K, не превышающее 1000,  — количество ячеек в камере хранения.
#
# Во второй строке  — натуральное число N (N ≤ 1000), обозначающее количество пассажиров. Каждая из следующих N строк содержит два натуральных числа, каждое из которых не превышает 1440: указанное в заявке время размещения багажа в ячейке и время освобождения ячейки (в минутах от начала суток).
#
# Запишите в ответе два числа: количество пассажиров, которые смогут воспользоваться камерой хранения, и номер последней занятой ячейки.

f = open('1_26.txt')
k = int(f.readline())
n = int(f.readline())
bagazhi = []
slots = [0]*k
for s in f:
    start, end = map(int, s.split())
    bagazhi.append([start, end])
bagazhi.sort()
last_slot = 0
cnt = 0
for i in range(len(bagazhi)):
    for j in range(len(slots)):#пытаемся положить багаж в каждую из ячеек
        if slots[j] == 0:
            slots[j] = bagazhi[i][1]
            cnt += 1
            last_slot = j + 1
            break
        elif slots[j] + 1 <= bagazhi[i][0]: # если занята то смотримпо времени освобождения
            slots[j] = bagazhi[i][1]
            cnt += 1
            last_slot = j + 1
            break

print(cnt, last_slot)