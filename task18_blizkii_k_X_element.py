'''
18. Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.

5
A = 1 2 3 4 5
X = 6 -> 5
'''

'''
list = list(map(int, input("Введите последовательность чисел: ").split()))
n = int(input("Какое число ищем? "))

closest_element = list[0]
min_difference = abs(n - list[0])

# Используем цикл для поиска ближайшего элемента
for num in list:
    difference = abs(n - num)
    if difference < min_difference:
        min_difference = difference
        closest_element = num

print(closest_element)
'''


# list_1 = [1, 2, 3, 4, 5]
# k = 6

# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)


'''
# Вводим количество элементов в массиве
N = int(input("Введите количество элементов в массиве: "))

# Вводим массив чисел
A = [int(input()) for _ in range(N)]

# Вводим число X, для которого ищем ближайший элемент
X = int(input("Введите число X: "))

# Инициализируем переменные для хранения ближайшего элемента и минимальной разницы
closest_element = A[0]
min_difference = abs(X - A[0])

# Используем цикл для поиска ближайшего элемента
for num in A:
    difference = abs(X - num)
    if difference < min_difference:
        min_difference = difference
        closest_element = num

# Выводим результат
print("Ближайший элемент:", closest_element)
'''

import math

list_1 = [1, 2, 4, 4, 5]
k = 3

difference = abs(list_1[0] - k)  # модуль числа
nearest = list_1[0]
for i in range(1, len(list_1)):
    curr_duff = abs(list_1[i] - k)
    if curr_duff < difference:
        nearest = list_1[i]
        difference = curr_duff
print(nearest)