'''
12. Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих
чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

4 4 -> 2 2
5 6 -> 2 3
'''


# # Вводим сумму и произведение чисел
# S = int(input("Введите сумму чисел: "))
# P = int(input("Введите произведение чисел: "))

# # Ищем подходящие пары чисел
# found = False
# for X in range(1, 1001):
#     Y = S - X  # Выражаем Y через S и X
#     if X * Y == P:
#         found = True
#         break

# # Выводим результат
# if found:
#     print("Найденные числа: X =", X, ", Y =", Y)
# else:
#     print("Не удалось найти подходящие числа.")



# s = int(input("Введите сумму чисел: "))
# p = int(input("Введите произведение чисел: "))

# solutions = []
# for i in range(1, 1001):
#     for j in range(1, 1001):
#         if s == i + j and p == i * j:
#             solutions.append((min(i, j), max(i, j)))
# solutions = list(set(solutions))

# for solution in solutions:
#     print(solution[0], solution[1])

# #1
# s = 12
# p = 27

# for num_1 in range(1, s//2):
#     num_2 = s - num_1
#     if p == num_1 * num_2:
#         break

# print(num_1, num_2)

# #2
# s = 12
# p = 27

# for num_1 in range(1, int(p**0.5) + 1):
#     num_2 = p / num_1
#     if s == num_1 + num_2:
#         break

# print(num_1, int(num_2))
    
#3
s = 12
p = 27

a = 0
for x in range(s):
    y = s - x
    if x + y == s and x * y == p:
        a += 1
        print(x, y)   # 3  9
        break