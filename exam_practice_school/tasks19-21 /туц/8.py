
#одна куча
from functools import lru_cache
heap = 58
@lru_cache(maxsize=None)
def game_result(s):
    if s >= heap:
        return 0
    next_codes = [game_result(s+1),game_result(s+4), game_result(s*2)]
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
# #
# heap = 58
# def f(s, m):
#     if s >= heap: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s+1, m - 1), f(s+4, m - 1), f(s*2, m - 1)]
#     return any(h) if (m-1) % 2 == 0 else all(h)
#
# print("19)", [s for s in range(1, heap) if f(s, 2)])
# print("20)", [s for s in range(1, heap) if not f(s, 1) and f(s, 3)])
# print("21)", [s for s in range(1, heap) if not f(s, 2) and f(s, 4)])