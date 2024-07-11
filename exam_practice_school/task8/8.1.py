from itertools import product
alph = 'ABCDXYZ'
words = product(alph, repeat = 4)
cnt = 0
for w in words:
    word = "".join(w)
    if (word[0] == "X" or word[0] == "Y" or word[0] == "Z") and (word[1:].count("X") == 0 and word[1:].count("Y")== 0 and word[1:].count("Z")== 0):
        cnt += 1
print(cnt)
