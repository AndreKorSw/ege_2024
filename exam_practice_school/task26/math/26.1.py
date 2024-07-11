# В текстовом файле записан набор натуральных чисел, не превышающих 109.
# Гарантируется, что все числа различны. Необходимо определить, сколько в наборе таких пар чисел, что числа в паре имеют разную чётность,
# а их сумма тоже присутствует в файле, и чему равна наибольшая из сумм таких пар.

f = open("26.1.txt")
n = int(f.readline())
print(n)
all_nums = [int(i) for i in f]
cnt = 0
max_sum = 0
for i in range(1, n-1):
    for j in range(i+1, n):
        if ((all_nums[i] + all_nums[j]) % 2 == 1) and (all_nums[i]+all_nums[j] in all_nums):
            cnt +=1
            max_sum = max(max_sum, all_nums[i]+all_nums[j])
print(cnt, max_sum)



