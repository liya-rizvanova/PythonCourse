'''
41. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.
Сначала вводится число N — количество элементов в массиве, далее записаны N чисел — элементы массива.
Массив состоит из целых чисел (каждое число вводится с новой строки).
Ввод:                                 Ввод:
5                                     5
1 2 3 4 5                             1 5 1 5 1
Вывод:                                Вывод:
0                                     2
'''


n = int(input())
list1 = list()
for i in range(n):
    x = int(input())
    list1.append(x)

count = 0
for i in range(1, n - 1):
    if list1[i-1] < list1[i] > list1[i + 1]:   # if list1[i-1] < list1[i] and list1[i] > list1[i + 1]:
        count += 1

print(f"\n{count}")

# def count_special_elements(arr):
#     count = 0
#     n = len(arr)

#     for i in range(1, n - 1):
#         if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
#             count += 1

#     return count

# # Ввод массива
# n = int(input("Введите количество элементов в массиве: "))
# arr = [int(input()) for _ in range(n)]

# # Подсчет и вывод результата
# result = count_special_elements(arr)
# print(result)
