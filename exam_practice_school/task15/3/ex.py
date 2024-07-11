#разное
for a in range(100, 0, -1):
    count = 0
    for x in range(1, 100):
        if (120 % a == 0) and ((x % 36 == 0) <= ((x % a != 0) <= (120 % x != 0))):
            count+=1
    if count == 99:
        print(a)
        break