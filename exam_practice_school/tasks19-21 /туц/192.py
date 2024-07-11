from functools import lru_cache
heaps = 227
@lru_cache(maxsize=None)
def game_result(x, s):
    if x + s >= heaps:
        return 0
    next_codes = [game_result(x+1, s),game_result(x, s+1), game_result(x*2, s), game_result(x, s*2)]
    negative = [i for i in next_codes if i <= 0]
    if negative:
        res = -max(negative) + 1
    else:
        res = -max(next_codes)
    return res
heap = 17
for i in range(1, heaps):
    if game_result(heap, i) == -1:
        print("19 ---", i)
for i in range(1, heaps):
    if game_result(heap, i) == 2:
        print("20 ---берем последний ответ", i)
for i in range(1, heaps):
    if game_result(heap, i) == -2:
        print("21 --- берем минимальный", i)