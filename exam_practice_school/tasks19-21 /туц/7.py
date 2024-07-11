from functools import lru_cache
heaps = 65
@lru_cache(maxsize=None)
def game_result(x, s):
    if x + s >= heaps:
        return 0
    next_codes = [game_result(x+1, s),game_result(x, s+1), game_result(x*3, s), game_result(x, s*3)]
    negative = [i for i in next_codes if i <= 0]
    if negative:
        res = -max(negative) + 1
    else:
        res = -max(next_codes)
    return res
heap = 6
for i in range(1, heaps):
    if game_result(heap, i) == -1:
        print("19 ---", i)
for i in range(1, heaps):
    if game_result(heap, i) == 2:
        print("20 ---берем последний ответ", i)
for i in range(1, heaps):
    if game_result(heap, i) == -2:
        print("21 --- берем минимальный", i)


def f(a, b, m):
    if a + b >= heaps: return m % 2 == 0
    if m == 0: return 0
    h = [f(a+1, b, m-1), f(a, b+1, m-1), f(a*3, b, m - 1), f(a, b * 3, m - 1)]
    return any(h) if (m-1) % 2 == 0 else all(h)

print("19)", [s for s in range(1, heaps-heap) if f(heap, s, 2)])
print("19)", [s for s in range(1, heaps-heap) if not f(heap, s, 1) and f(heap, s, 3)])
print("19)", [s for s in range(1, heaps-heap) if not f(heap, s, 2) and f(heap, s, 4)])