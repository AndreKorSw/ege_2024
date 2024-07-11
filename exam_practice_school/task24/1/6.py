# В текстовом файле 4.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F.
# Определите максимальное количество идущих подряд символов, среди которых нет подстроки CEDA./
s = open("4__2pp6x.txt").readline().replace("CEDA", "CED EDA").split(" ")
print(len(sorted(s, key = lambda x: -len(x))[0]))