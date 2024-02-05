'''
33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''


n = int(input())

list1 = list()
for i in range(n):
    x = int(input())
    list1.append(x)

max_n = max(list1)
min_n = min(list1)

for i in range(len(list1)):
    if list1[i] == max_n:
        list1[i] = min_n

print(list1)



# import random

# def replace_max_with_min(grades, grades_list, max_grade, current_index=0):
#     if current_index < grades:
#         if grades_list[current_index] == max_grade:
#             grades_list[current_index] = min(grades_list)
#         replace_max_with_min(grades, grades_list, max_grade, current_index + 1)

# grades = int(input('Введите количество оценок: '))
# grades_list = []

# # Генерация случайных оценок и вывод их на экран
# for i in range(grades):
#     grade = random.randint(1, 5)
#     grades_list.append(grade)
#     print(grade, end=' ')

# # Нахождение максимальной оценки
# max_grade = max(grades_list)

# # Замена максимальных оценок на минимальные с использованием рекурсии
# replace_max_with_min(grades, grades_list, max_grade)

# print()
# print(*grades_list)


'''
Эта рекурсивная функция replace_max_with_min проходит по списку оценок и заменяет максимальные оценки на минимальные.
Однако, следует отметить, что использование циклов более простое и эффективное решение для данной задачи.
'''


import random

grades = int(input('Введите количество оценок: '))
grades_list = []

# Генерация случайных оценок и вывод их на экран
for i in range(grades):
    grade = random.randint(1, 5)
    grades_list.append(grade)
    print(grade, end=' ')

# Нахождение максимальной оценки
max_grade = max(grades_list)

# Замена максимальных оценок на минимальные
for i in range(grades):
    if grades_list[i] == max_grade:
        grades_list[i] = min(grades_list)

print()
print(*grades_list)


'''
import random

grades = int(input('Введите количество оценок: '))
grades_list = []

# Генерация случайных оценок и вывод их на экран
for i in range(grades):
    grade = random.randint(1, 5)
    grades_list.append(grade)
    print(grade, end=' ')

# Нахождение минимальной и максимальной оценок
min_grade = min(grades_list)
max_grade = max(grades_list)

# Замена минимальных оценок на максимальные и наоборот
for i in range(grades):
    if grades_list[i] == min_grade:
        grades_list[i] = max_grade
    elif grades_list[i] == max_grade:
        grades_list[i] = min_grade

print()
print(*grades_list)
'''