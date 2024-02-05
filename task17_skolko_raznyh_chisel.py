'''
17. Дан список чисел. Определите, сколько в нем встречается различных чисел.

Input:  [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
'''

list1 = [1, 1, 2, 3, 5, 5]

print(len(set(list1)))

'''
Тип множество не допускает использование различных элементов.
Список преобазуется в множество при помощи функции set(). # 1, 2, 3, 5
Для того, чтобы посчитать количество элементов в отфильтрованном списке используется функция len() # 4
'''

from random import randint

size = int(input("Enter size: "))

# list1 = []

# for _ in range(size):
#     num = randint(1, 10)
#     list1.append(num)

list1 = [randint(1, 10) for _ in range(size)]
print(list1)

print(len(set(list1)))

# 2
res_list = []

for num in list1:
    if num not in res_list:
        res_list.append(num)

# [res_list.append(num) for num in list1 if num not in res_list]
# res_list = [num if num not in res_list else 0 for num in list1]
print(res_list)