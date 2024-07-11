# Текстовый файл состоит из символов,
# обозначающих заглавные буквы латинского алфавита и цифры от 1 до 9 включительно.
# Определите количество подстрок, начинающихся с цифры, большей 0, за которой следуют буквы,
# причём количество букв равно цифре, с которой начинается подстрока.
s = open().readline()
digits = "0123456789"
count = 0
words = []
for i in range(len(s)):
    try:
        if s[i] in digits and int(s[i]) > 0:
            if all(s[j] not in digits for j in range(i + 1, i + int(s[i]) + 1)):
                count += 1
                words += [s[i:i + int(s[i]) + 1]]
    except IndexError:
        pass
print(len(words))
