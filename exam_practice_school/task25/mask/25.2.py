#25
#   * - любая последовательность цифр любой длинны, включая символ *
# найти все чила соответ маске 123*нч56, кот делятся без остатка на 206
for i in range(2060, 10**8+1, 206):
    s = str(i)
    if (s[:3] == '123') and (s[-2:] == '56') and (int(s[-4]) % 2 != 0) and (int(s[-3]) % 2 == 0):
        print(i, i // 206)