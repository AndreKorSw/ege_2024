for i in range(128, 256):
    s = bin(i)[2:]
    new_s = ''
    for j in s:
        if j == '0':
            new_s += '1'
        if j == '1':
            new_s += '0'
    new_s = int(new_s, 2)
    if i - new_s == 105:
        print(i)