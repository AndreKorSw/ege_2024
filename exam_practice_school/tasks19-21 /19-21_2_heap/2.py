from functools import lru_cache

heaps = 0
heap = 0

@lru_cache(maxsize=None)
def game_Result(x, s):
    if x + s >= heaps:
        return 0
    nextcodes = [game_Result(x+1, s), game_Result(x, s+1), game_Result(x*2, s), game_Result(x, s*2)]
    negative = [i for i in nextcodes in i <= 0]
    if negative:
        res = -max(negative)+1
    else:
        res = -max(nextcodes)
    return res

for i in range(1, heaps):
    if game_Result(heap, i) == -1:
        print("19", i)
for i in range(1, heaps):
    if game_Result(heap, i) == 2:
        print("20", i)
for i in range(1, heaps):
    if game_Result(heap, i) == -2:
        print("21", i)