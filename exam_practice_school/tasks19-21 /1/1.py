from functools import lru_cache

heaps = 50
heap = 39
@lru_cache(None)
def gameres(x, s):
    if s + x >= heaps:
        return 0
    nextcodes = [gameres(x+2, s), gameres(x*3, s), gameres(x, s+2), gameres(x, s*3)]
    negative = [i for i in nextcodes if i <= 0]
    if negative:
        res = -max(negative) + 1
    else:
        res = -max(nextcodes)
    return res

for i in range(1, heaps):
    if gameres(1, heap) == -1:
        print("19-----", i)
for i in range(1, heaps):
    if gameres(1, heap) == 2:
        print("20-----", i)
for i in range(1, heaps):
    if gameres(1, heap) == -2:
        print("21-----", i)