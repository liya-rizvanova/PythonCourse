'''
4. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем
Петя и Сережа вместе?

6  -> 1 4 1
24 -> 4 16 4
60 -> 10 40 10
'''


n = int(input("Введите общее количество журавликов (S): "))

n1 = n // 6
n2 = n // 6
n3 = (n // 6) * 4

print(n1, n3, n2)


'''
n = int(input("Введите общее количество журавликов (S): "))

x = n // 6

petya = x
katya = 4 * x
sereja = x

print(f"{petya} {katya} {sereja}")
'''

'''
# Получаем данные от пользователя
total_cranes = int(input("Введите общее количество журавликов (S): "))

# Вычисляем количество журавликов, которое сделали Петя и Сережа (x)
x = total_cranes // 6

# Вычисляем количество журавликов, которое сделал каждый ребенок
petya_cranes = x
katya_cranes = 4 * x
sereja_cranes = x

# Выводим результат
print(f"{petya_cranes} {katya_cranes} {sereja_cranes}")
'''

'''
# Получаем данные от пользователя
total_cranes = int(input("Введите общее количество журавликов (S): "))

# Вычисляем количество журавликов, которое сделали Петя и Сережа (x)
x = total_cranes // 6

# Вычисляем количество журавликов, которое сделала Катя
katya_cranes = 4 * x

# Выводим результат
print(f"Петя и Сережа сделали по {x} журавликов каждый.")
print(f"Катя сделала {katya_cranes} журавликов.")
'''

'''
# Получаем данные от пользователя
total_cranes = int(input("Введите общее количество журавликов (S): "))

# Вычисляем количество журавликов, которое сделали Петя и Сережа (x)
x = total_cranes // 6

# Вычисляем количество журавликов, которое сделал каждый ребенок
petya_cranes = x
katya_cranes = 4 * x
sereja_cranes = x

# Выводим результат
print(f"Петя сделал {petya_cranes} журавликов.")
print(f"Катя сделала {katya_cranes} журавликов.")
print(f"Сережа сделал {sereja_cranes} журавликов.")
'''

'''
Пользователь вводит общее количество журавликов (total_cranes), и затем
программа вычисляет количество журавликов, которое сделали Петя и Сережа
(x) и количество журавликов, которое сделала Катя (katya_cranes).
'''