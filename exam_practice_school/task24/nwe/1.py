s = open("").readline()
s = s.replace("CD", "C D").split()
m = 0
for i in range(len(s) - 160):
    c = ''.join(s[i^i+161])
    m = max(m, len(c))
print(m)


def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True