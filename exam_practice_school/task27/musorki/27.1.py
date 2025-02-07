# В городе М расположена кольцевая автодорога длиной в километров с движением в обе стороны. На каждом километре автодороги расположены пункты приема мусора определенной вместимости. В пределах кольцевой дороги в одном из пунктов сборки мусора собираются поставить мусороперерабатывающий завод таким образом, чтобы стоимость доставки мусора была минимальной. Стоимость доставки мусора вычисляется, как вместимость пункта сбора умноженная на расстояние от пункта сбора мусора до мусороперерабатывающего завода. Если мусороперерабатывающий завод находится рядом с пунктом сбора расстояние считается нулевым. Контейнеры нумеруются с 1 до М. Рядом с каким пунктом сбора мусора нужно поставить мусороперерабатывающий завод?
#
# Описание входных данных
#
# Первое число - количество контейнеров для мусора. Последующие и чисел количество килограмм мусора, которое производится на точке. Описание выходных данных
#
# Одно число номер контейнер для мусора рядом с которым стоит расположить перерабатывающий завод.

#для файла а
f = open('')
n = int(f.readline())
a = [int(s) for s in f]
res = []
for i in range(n):
    stoimost = 0
    for j in range(n):
        stoimost += a[j] * min(abs(j - i), n - abs(j - i))#так как дорого кольцевая и мы представляем в виде циферблата чтобы посчитать правильно
    res.append([stoimost, i])
print(min(res))
