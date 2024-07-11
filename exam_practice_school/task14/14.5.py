alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(5, 36):
    for x in alphabet[:p]:
        for y in alphabet[:p]:
            if int(f'12', p) * int(f'34', p) == int(f'{x}{y}', p) ** 2:
                print(int(f'{y}{x}', p))