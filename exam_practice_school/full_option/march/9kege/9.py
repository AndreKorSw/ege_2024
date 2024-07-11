# print("x y z w u")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((x <= (z == w)) or not(y <= w)):
#                         print(x, y, z, w)

# for n in range(1, 1000):
#     x = bin(n)[2:]
#     # print(x, x[:-1], x[:2])
#     if x[-1] == "0":
#         x = x[:-1] + x[:2]
#     else:
#         continue
#     x = x[::-1]
#
#     if int(x, 2) == 123:
#         print(n)

def find_initial_number(target):
    n = 1
    while True:
        binary_n = bin(n)[2:]  # получаем двоичное представление числа N без "0b" в начале
        if '0' not in binary_n:
            print("Алгоритм аварийно завершился. Нуля нет в двоичной записи числа", n)
            return
        reversed_binary_n = binary_n[::-1]
        index_of_zero = reversed_binary_n.find('0')
        if index_of_zero == -1:
            print("Алгоритм аварийно завершился. Нуля нет в обратной двоичной записи числа", n)
            return
        else:
            new_binary_n = reversed_binary_n[:index_of_zero][::-1] + reversed_binary_n[:2]
            if int(new_binary_n, 2) == target:
                return n
        n += 1

result = find_initial_number(123)
print(result)