for i in range(174457, 174505 + 1):
    dividers = []
    for j in range(2, i//2 + 1):
        if i % j == 0:
            dividers.append([i//j, j])
    if len(dividers) == 2:
        print(dividers)