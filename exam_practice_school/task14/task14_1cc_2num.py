#14
alphabet = "0123456789abcdefghjklmnopqrstuv"
for x in alphabet:
    f = int(f'123{x}ab', 31) + int(f'3ce{x}321', 31)
    if f % 17 == 0:
        print(f // 17)


