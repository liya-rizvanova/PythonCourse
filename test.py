'''
31. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 13

Задание необходимо решать через рекурсию
'''

# def fibonacci(n):
#     if n ==0:
#         return 0
#     else:
#         if n == 1 or n == 2:
#             return 1
#         return fibonacci(n - 1) + fibonacci(n - 2)

# n = int(input("Enter fibonacci number: "))
# print(fibonacci(n + 1))



# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# n = int(input("Enter fibonacci number: "))
# print(fibonacci(n + 1))



# def fibonacci(n):
#     if n == 0 or n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# n = int(input("Enter fibonacci number: "))
# print(fibonacci(n))

# Засекаем время работы кода
# import time

# def fibonacci(n):
#     if n == 0 or n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
# start = time.time()
# n = int(input("Enter fibonacci number: "))
# print(fibonacci(n))
# end = time.time()
# delta = end - start 
# print(f'Код работал {delta} сек.')

'''
33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4

Output: 1 3 3 3 1
'''
# from random import randint
# #1
# size = int(input("Input size of list: "))
# list_1 = [randint(1, 5)]
# min_num = list_1[0]
# max_num = list_1[0]
# i_max_nums = [0]

# for i in range(size-1):
#     num = randint(1, 5)
#     list_1.append(num)
#     if num < min_num:
#         min_num = num
#     if num > max_num:
#         max_num = num
#         i_max_nums = [i + 1]
#     elif num == max_num:
#         i_max_nums.append(i + 1)

# for i in i_max_nums:
#     list_1[i] = min_num

# #2
# list_1 = [randint(1, 5) for _ in range(size) ]
# print(list_1)

# min_num = min(list_1)
# max_num = max(list_1)
# #2.1
# for i in range(len(list_1)):
#     if list_1[i] == max_num:
#         list_1[i] = min_num
# #2.2
# while max_num in list_1:
#     i_max_num = list_1.index(max_num)
#     list_1[i_max_num] = min_num

# print(list_1)

'''
35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)

Input: 5

Output: yes
'''
# def simple(num):
#     for div in range(2, num):
#         if num % div == 0:
#             return 'no'
#     return 'yes'

# n = int(input('Введите число:'))
# print(simple(n))



# def simple(num):
#     if num != 2 and num % 2 == 0:
#         return 'no'
#     for div in range(3, int(num ** 0.5) + 1, 2):
#         if num % div == 0:
#             return 'no'
#     return 'yes'

# n = int(input('Введите число:'))
# print(simple(n))

# # 36

# # 2   18
# # 3   12
# # 4   9
# # 6   6


# def simple(num):
#     if num not in (2,3,5,7) and num % 2 == 0 and num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
#         return 'no'
#     for div in range(3, int(num ** 0.5) + 1, 2):
#         if num % div == 0:
#             return 'no'
#     return 'yes'

# n = int(input('Введите число:'))
# print(simple(n))

'''
37. Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

Input:    2 -> 3 4
Output: 4 3
'''
# def reverse_nums(n):
#     if n == 0:
#         return ""
#     num = input("Введите число последовательности: ")
#     return reverse_nums(n-1) + " " + num

# size = int(input("Введите натуральное число: "))
# print(reverse_nums(size).strip())

'''
Задача №39.  1) Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит  число N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива

2) (пользовательский ввод можно заменить на рандомный ввод)
Пользователь вводит  размер первого массива – N
и элементы первого массива. 
затем размер второго массива M  
и элементы второго массива
Нужно вывести те элементы первого массива, которых нет во втором массиве, при этом порядок последовательности сохранить исходный
Ввод: 			Вывод:
7			3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1
'''
# from random import randint

# size_1 = int(input("Enter array size: "))
# # list_1 = list()
# # for _ in range(size_1):
# #     list_1.append(randint(1, 10))

# list_1 = [randint(1, 10) for _ in range(size_1)]
# print(list_1)

# size_2 = int(input("Enter array size: "))
# # list_2 = list()
# # for _ in range(size_2):
# #     list_2.append(randint(1, 10))

# list_2 = [randint(1, 10) for _ in range(size_2)]
# print(list_2)

# for num in list_1:
#     if num not in list_2:
#         print(num, end = ' ')

'''
41.  1) Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве выведет количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве  Далее записаны N чисел — элементы массива. Массив состоит из целых чисел. 
2) (пользовательский ввод можно заменить на рандомный)
Пользователь вводит  размер массива – N
и элементы массива (целые числа). 
нужно из этого массива вывести количество элементов, у которых ближайшие соседние элементы меньше самого элемента.

Ввод: 			Ввод:
5			5
1 2 3 4 5			1 5 1 5 1

Вывод:			Вывод:
0			2
'''
# size = int(input('Enter N: '))

# list_1 = [randint(1, 10) for _ in range(size)]

# print(list_1)

# count = 0

# for i in range(1, (size-1)):
#     if list_1[i - 1] < list_1[i] > list_1[i + 1]:
#         count += 1
# print(count)


'''Задача №43.  Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. Все числа списка находятся на разных строках.

2) (пользовательский ввод можно заменить на рандомный)
Пользователь вводит  размер массива – N
и элементы массива (целые числа). 
нужно посчитать сколько повторений у каждого числа
посчитанные числа можно посчитать повторно в паре с другими числами

Ввод:			Вывод:
1 2 3 2 3 2 2 2 			11'''

# from random import randint

# size_1 = int(input("Enter array size: "))

# list_1 = [randint(1, 3) for _ in range(size_1)]
# print(list_1)

# count = 0
# for i in range(size_1 - 1):
#     for j in range(i + 1, size_1):
#         if list_1[i] == list_1[j]:
#             count += 1
# print(count)


'''
45. Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
(пользовательский ввод можно заменить на рандомный)
Пользователь вводит натуральное число – k
В диапазоне от 0 до k нужно вывести все пары чисел N и M, в которых сумма делителей N равняется M, а сумма делителей M равняется N (число само на себя делить нельзя)
Пары необходимо выводить по одной паре в строке, разделяя числа пробелами. Каждая пара выводится только один раз, без повторов.

Пример: Возьмём 2 числа 220 и 284. Найдём их делители
Делители 220 – (1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110)
1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284
Делители 284 – (1, 2, 4, 71, 142 )
1 + 2 + 4 + 71 + 142 = 220
Ввод: Вывод:
300 220 284
'''

# import math

# def div_sum(number):
#     sum_div = 1
#     sqrt_num = number ** 0.5
#     if sqrt_num == int(sqrt_num):
#         sum_div += int(sqrt_num)
#     for div in range(2, int(sqrt_num)):
#         if number % div == 0:
#             sum_div += div + (number // div)
#     return sum_div


# k = int(input('Введите число k: '))

# for num_1 in range(2, k):
#     num_2 = div_sum(num_1)
#     if div_sum(num_2) == num_1 and num_1 < num_2:
#         print(num_1, num_2)



'''
47.  1) У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать): 

transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))

Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

2) Есть код:

transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transformed_values = list(map(transformation, values))
if values == transformed_values:
         print(‘ok’)
else:
         print(‘fail’)

- В переменную transformation нужно прописать такую функцию, что бы в переменной transformed_values получилась копия списка values
'''

# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#          print('ok')
# else:
#          print('fail')


'''
49.  1) Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую  площадь. Гарантируется, что самая далекая планета ровно одна

2) - Дан список размеров(длина, ширина) эллипсов 
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
Напишите функцию find_farthest_orbit(list_of_orbits), которая находит площадь самого большого эллипса и возвращает кортеж с его размерами.
Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b – длины и ширина осей эллипса
-   Площадь кругов учитывать не нужно, т.е если у эллипса a == b, то это круг.
При решении задачи используйте списочные выражения.
Гарантируется, что самый большой эллипс всего один.
'''

# def find_farthest_orbit(list_of_orbits):
#     max_area = 0
#     ab_max_area = ()
#     for a, b in list_of_orbits:
#         if a != b:
#             area = a * b
#             if area > max_area:
#                 max_area = area
#                 ab_max_area = a, b
#     return ab_max_area


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))

# #2
# def find_farthest_orbit(list_of_orbits):

#     # 1
#     # list_of_ellipse = [a, b for a, b in list_of_orbits if a != b]
#     # list_of_areas = [a * b for a, b in list_of_ellipse]
#     # 2
#     list_of_ellipse = list(filter(lambda a_b: a_b[0] != a_b[1], list_of_orbits))
#     list_of_areas = list(map(lambda a_b: a_b[0] * a_b[1], list_of_ellipse))
#     max_area = max(list_of_areas)
#     i_max_area = list_of_areas.index(max_area)
#     return list_of_ellipse[i_max_area]
    
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))


'''51. Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
Ввод:							Вывод:
values = [0, 2, 10, 6]		same
if same_by(lambda x: x % 2 == 0, values):
	print(‘same’)
else:
	print(‘different’)'''

def same_by(characteristic, objects):
	values_2 = list(filter(characteristic, objects))
	return objects == values_2

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2 == 0, values):
	print('same')
else:
	print('different')
	
#2
def same_by(characteristic, objects):
	return len(set(map(characteristic, objects))) < 2

values = [1, 3, 15, 7]
if same_by(lambda x: x % 2 == 0, values):
	print('same')
else:
	print('different')
	
#3
def same_by(characteristic, objects):
    new_list = list(map(characteristic, objects))
    return any(new_list) == all(new_list)

values = [1, 3, 15, 7]
if same_by(lambda x: x % 2 == 0, values):
    print('same')
else:
    print('different')