'''
30. Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
'''


a1 = 2
d = 3
n = 4

for i in range(n):
  print(a1 + i * d)



# def generate_arithmetic_progression(a1, d, n):
#     # Генерация массива элементов арифметической прогрессии
#     progression = [a1 + (i - 1) * d for i in range(1, n + 1)]
#     return progression

# # Ввод значений с клавиатуры
# a1 = int(input("Введите первый элемент прогрессии: "))
# d = int(input("Введите разность прогрессии: "))
# n = int(input("Введите количество элементов: "))

# # Генерация и вывод массива в одну строку
# result = generate_arithmetic_progression(a1, d, n)
# print(*result)



# def generate_arithmetic_progression(a1, d, n):
#     # Генерация массива элементов арифметической прогрессии
#     progression = [a1 + (i - 1) * d for i in range(1, n + 1)]
#     return progression

# # Ввод значений с клавиатуры
# a1 = int(input("Введите первый элемент прогрессии: "))
# d = int(input("Введите разность прогрессии: "))
# n = int(input("Введите количество элементов: "))

# # Генерация и вывод каждой цифры результата на новой строке
# result = generate_arithmetic_progression(a1, d, n)
# for number in result:
#     print(number)
