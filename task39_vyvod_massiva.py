'''
39. Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива

Ввод: (каждое число вводится с новой строки)                  Вывод:
7                                                             3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1
'''


n = int(input())
list1 = list()
for i in range(n):
    x = int(input())
    list1.append(x)

m = int(input())
list2 = list()
for i in range(m):
    x = int(input())
    list2.append(x)

count = 0
for i in range(n):
    for j in range(m):
        if list1[i] == list2[j]:
            count +=1
        if count == 0:
            print(list1[i])
        count = 0



# def find_unique_elements(arr1, arr2):
#     unique_elements = []
#     for element in arr1:
#         if element not in arr2:
#             unique_elements.append(element)
#     return unique_elements

# # Ввод массива arr1
# n = int(input("Введите количество элементов в первом массиве: "))
# arr1 = [int(input()) for _ in range(n)]

# # Ввод массива arr2
# m = int(input("Введите количество элементов во втором массиве: "))
# arr2 = [int(input()) for _ in range(m)]

# # Поиск уникальных элементов и вывод результата
# result = find_unique_elements(arr1, arr2)
# print(" ".join(map(str, result)))