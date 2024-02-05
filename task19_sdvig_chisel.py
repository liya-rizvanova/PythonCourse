'''
19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K – положительное число.

Input:  [1, 2, 3, 4, 5] K = 3
Output: [4, 5, 1, 2, 3]
'''


list = [5, 4, 6, 7, -10]
k = int(input())
k = k % len(list)

list_res = []

for i in range(k):
    list_res.append(list[len(list) - 1 - i])
print(list_res)

for i in range(len(list) - k ):
    list_res.append(list[i])
print(list_res)



numbers = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3

# for i in range(k):
#     last_num = numbers.pop()
#     numbers.insert(0, last_num)
# print(f'{numbers=}')

print(f'{numbers[-k:] + numbers[:-k] = }')