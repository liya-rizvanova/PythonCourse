'''
13. 1) Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю
историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями
статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют
период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
Напишите программу, помогающую синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается
N целых чисел. 
Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

2) Пользователь вводит число N (1 ≤ N ≤ 10). Далее построчно N чисел от -50 до 50. Нужно вывести наибольшее количество
идущих подряд положительных чисел.

Input:  6 -> -20 30 -40 50 10 -10
Output: 2
'''
# 1

import random

days = int(input('Введите количество дней: '))
max_count = 0 # максимальное количество + температур
counter = 0
for _ in range(days):
    t = random.randint(-50, 50)
    print(t, end = ' ')
    if t > 0:
        counter += 1
        if counter > max_count:
            max_count = counter
    else:
        counter = 0
print()
print(f'{max_count = }')

#2
'''
import random

days = int(input('Введите количество дней: '))
max_count = 0 # максимальное количество + температур
counter = 0
for _ in range(days):
    t = random.randint(-50, 50)
    print(t, end = ' ')
    if t > 0:
        counter += 1
    else:
        if counter > max_count:
            max_count = counter
        counter = 0
if counter > max_count:
    max_count = counter
print()
print(f'{max_count = }')
'''

'''
n = int(input())
print()
k = 0   # здесь хранится инфо сколько на данный момент длится оттепель
max = 0   # здесь хранится инфо о максимальном количестве дней оттепели (самая длинная оттепель)

for i in range(n):   # n - сколько раз мы будем повторять цикл
    x = int(input())   # при каждой итерации вводим температуру х
    if x > 0:
        k += 1   # если температура х > 0, то k увеличиваем на 1 те. текущая оттепель стала на 1 день больше
    else:
        if max < k:   # если макс оттепель < чем текущая оттепель, то делаем переприсваивание, то
            max = k
        k = 0   # обнуляем вне цикла
#if max < k:  # если в конце не стоит отрицательная температура, делпем доп. проверку 9 -> 7 11 -2 31 -5 9 5 7 4 итог 4
#   max = k   # если убрать эту проверку итог 2
print()
print(max)
'''

'''
temperatures = input().split()
temperatures = list(map(int, temperatures))

k = 0   # здесь хранится информация, сколько на данный момент длится оттепель
max_days = 0   # здесь хранится информация о максимальном количестве дней оттепели (самая длинная оттепель)

for temp in temperatures:
    x = int(temp)
    if x > 0:
        k += 1   # если температура x > 0, то k увеличиваем на 1, т.е. текущая оттепель стала на 1 день больше
    else:
        if max_days < k:   # если максимальная оттепель < текущей оттепели, то делаем переприсваивание
            max_days = k
        k = 0   # обнуляем текущую оттепель только когда температура меньше или равна 0

# После завершения цикла нужно еще раз проверить, не является ли последняя оттепель самой длинной
if max_days < k:
    max_days = k

print(max_days)
'''