# Текстовый файл содержит строку из заглавных
# латинских букв и точек, всего не более 106   символов.
# Определите максимальное количество идущих подряд символов, среди которых не более четырех точек и количество букв первой половины латинского алфавита превышает
# количество букв второй половины латинского алфавита.
s = open('24_M3.txt').readline().split('.')
alph = sorted('QWERTYUIOPASDFGHJKLZXCVBNM')
first_chapter = "".join(alph[:13])
second_chapter = "".join(alph[13:])
mx = 0
for i in range(1,len(s)-2):
    substr = '.'.join(s[i:i+5])
    count_first = sum([substr.count(x) for x in first_chapter])
    count_second = sum([substr.count(x) for x in second_chapter])
    if count_first > count_second:
        mx = max(mx,len(substr))
print(mx)