'''
32. Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума).

Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
'''


list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

for i in range(len(list_1)):
  if min_number <= list_1[i] <= max_number:
    print(i)   # 1 2 3 6 7 9 10 11 13 14 16 19 (каждое значение выводится на новой строчке)




# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_value = 6
# max_value = 10

# for i in range(len(list_1)):
#     if min_value <= list_1[i] <= max_value:
#         print(i, end=' ')



list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
list_2 = []
max = 10
min = 6
for i in range(len(list_1)):
    if list_1[i] >= min and list_1[i] <= max:
        list_2.append(i)
print(list_2)



# def find_indices_in_range(arr, min_value, max_value):
#     # Находим индексы элементов, принадлежащих заданному диапазону
#     indices = [index for index, value in enumerate(arr) if min_value <= value <= max_value]
#     return indices

# # Ввод списка чисел
# numbers = list(map(int, input("Введите элементы списка через пробел: ").split()))

# # Ввод минимального и максимального значений
# min_value = int(input("Введите минимальное значение: "))
# max_value = int(input("Введите максимальное значение: "))

# # Поиск и вывод индексов в заданном диапазоне
# result = find_indices_in_range(numbers, min_value, max_value)
# print(result)
