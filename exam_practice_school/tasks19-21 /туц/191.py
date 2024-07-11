#одна куча
from functools import lru_cache
heap = 39
@lru_cache(maxsize=None)
def game_result(s):
    if s >= heap:
        return 0
    next_codes = [game_result(s+1),game_result(s+3), game_result(s*2)]
    negative = [i for i in next_codes if i <= 0]
    if negative:
        res = -max(negative) + 1
    else:
        res = -max(next_codes)
    return res

for i in range(1, heap):
    if game_result(i) == -1:# любой ход одна куча
        print("19 ---", i)
for i in range(1, heap):
    if game_result(i) == 2:
        print("20 ---", i) #берем минимальные
for i in range(1, heap):
    if game_result(i) == -2:
        print("21 ---", i)