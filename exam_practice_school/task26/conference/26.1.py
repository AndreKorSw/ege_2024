# Входной файл содержит сведения о заявках на проведение занятий в конференц-зале. В каждой заявке указаны время начала и время окончания мероприятия (в минутах от начала суток). Если время начала одного мероприятия меньше времени окончания другого, то провести можно только одно из них. Если время окончания одного мероприятия совпадает с временем начала другого, то провести можно оба. Определите максимальное количество мероприятий, которое можно провести в конференц-зале и самое позднее время окончания последнего мероприятия.
#
# Задание 26
#
# Входные данные
#
# В первой строке входного файла находится натуральное число N (N < 1000)  — количество заявок на проведение мероприятий.
#
# Следующие N строк содержат пары чисел, обозначающих время начала и время окончания мероприятий. Каждое из чисел натуральное, не превосходящее 1440.
#
# Запишите в ответе два числа: максимальное  — количество мероприятий, которое можно провести в конференц-зале и самое позднее время окончания последнего мероприятия (в минутах от начала суток).
#
# Типовой пример организации данных во входном файле
#
# 5

# https://alex-math.ru/gia/show/zadaniye-26-informatika-dyemo-2024/

# f = open('26 (4).txt')
# n = int(f.readline())
# conferences = []
# for i in f:
#     start, end = map(int, i.split())
#     conferences.append([start,end])
#
# conferences.sort(key=lambda x: (x[1], x[0]))
# print(conferences)

f = open('26_2024.txt')
applications_quantity = int(f.readline())  # количество заявок, в программе нигде не используется. пусть будет
applications = []  # список кортежей (начало заявки, конец заявки)
applications_begin = set()  # множество времён начал заявок

while s := f.readline():  # заполняем массив заявок и множество начал заявок
    s_app = s.split()
    applications.append((int(s_app[0]), int(s_app[1])))
    applications_begin.add(int(s_app[0]))

max_events = 0  # здесь будет максимальное кол-во мероприятий
max_break = 0  # здесь будет максимальный перерыв между двумя последними событиями

for curr_begin in applications_begin:  # итерируемся по всевозможным началам мероприятий
    min_end = min([e[1] for e in filter(lambda v: v[0] == curr_begin,
                                        applications)])  # находим событие, заканчивающееся раньше всего
    min_end_prev = 0  # здесь будем запоминать время окончания предыдущего события
    avail_app = [e for e in filter(lambda v: v[0] >= min_end,
                                   applications)]  # оставляем только те события, которые начинаются не раньше времени окончания последнего мероприятия
    events = 1  # количество мероприятий
    while avail_app:  # пока всё еще имеются мероприятия, которые можно провести
        min_end_prev = min_end  # время окончания предыдущего события
        min_end = min([e[1] for e in avail_app])  # находим время окончания следующего события
        events += 1
        avail_app = [e for e in filter(lambda v: v[0] >= min_end, avail_app)]  # отфильтровываемся

    if events >= max_events:
        last_begin_event = max([e[0] for e in filter(lambda v: v[0] >= min_end_prev,
                                                     applications)])  # максимальное время начала последнего события
        last_break = last_begin_event - min_end_prev  # максимальный перерыв между предпоследним и последним мероприятием
        if events == max_events:
            max_break = max(max_break, last_break)
        else:
            max_events = events
            max_break = last_break

print(max_events, max_break)