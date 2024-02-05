'''
Лекция 2
'''

# Списки
'''
Список - это упорядоченный конечный набор элементов - это тот же самый массив, 
в котором можно хранить элементы любых типов данных.
'''
list_1 = []   # cоздание пустого списка
list_2 = list()   # cоздание пустого списка
list_1 = [7, 9, 11, 13, 15, 17]
print(list_1)   # без * -> [7, 9, 11, 13, 15, 17]
list_2 = [7, 9, 11, 13, 15, 17]
print(*list_2)   # распаковываем массив при поможи * -> 7 9 11 13 15 17

# вывести первый элемент списка
list_1 = [7, 9, 11, 13, 15, 17]
print(list_1[0])   # 7

# если хотим вывести последний элемент списка
list_1 = [7, 9, 11, 13, 15, 17]
print(list_1[-1])   # 17 # -1 означает то, что индексация идет с конца

# len(имя_списка) - узнать количество элементов в списке
list_1 = [7, 9, 11, 13, 15, 17]
print(len(list_1))   # 6

# # Заполнение списка во время работы программы:
# list_1 = list()   # создание пустого списка
# for i in range(5):   # цикл выполнится 5 раз
#     n = int(input())   # пользователь вводит целое число
#     list_1.append(n)   # сохранение элемента в конец списка
# # 1-я итерация цикла(повторение 1): n = 12, list_1 = [12]
# # 2-я итерация цикла(повторение 2): n = 7, list_1 = [12, 7]
# # 3-я итерация цикла(повторение 3): n = -1, list_1 = [12, 7, -1]
# # 4-я итерация цикла(повторение 4): n = 21, list_1 = [12, 7, -1, 21]
# # 5-я итерация цикла(повторение 5): n = 0, list_1 = [12, 7, -1, 21, 0]
# print(list_1) # [12, 7, -1, 21, 0]

# Взаимодействие цикла for со списком:
list_1 = [12, 7, -1, 21, 0]
for i in list_1:
    print(i)   # вывод каждого элемента списка

list_1 = [12, 7, -1, 21, 0]
for i in range(len(list_1)):
    print(list_1[i])   # вывод каждого элемента списка

list_1 = []
print(list_1)
for i in range(5):
    list_1.append(i)
    print(list_1)   # [] # [0] # [0, 1] # [0, 1, 2] # [0, 1, 2, 3] # [0, 1, 2, 3, 4]

# Удаление последнего элемента списка.
# Метод pop() удаляет последний элемент из списка:
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop())   # 0
print(list_1)   # [12, 7, -1, 21]
print(list_1.pop())   # 21
print(list_1)   # [12, 7, -1]
print(list_1.pop())   # -1
print(list_1)   # [12, 7]

# Удаление конкретного элемента из списка.
# Надо указать значение индекса в качестве аргумента функции pop:
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(0))   # 12
print(list_1)   # [7, -1, 21, 0]

# Добавление элемента на нужную позицию.
# Функция insert — указание индекса (позиции) и значения.
list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(2, 11))   # (2, 11) где 2 - позиция, на которую нужно вставить 11 - элемент, который необходимо вставить на указанную позицию
print(list_1)   # [12, 7, 11, -1, 21, 0]

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # последний элемент не выводится при срезе, т.к. i начинается с 0
print(list_1[0])   # 1
print(list_1[1])   # 2
print(list_1[len(list_1)-1])   # 10
print(list_1[-1])   # 10
print(list_1[-5])   # 6
print(list_1[:])   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2])   # [1, 2]
print(list_1[len(list_1)-2:])   #[9, 10]
print(list_1[2:9])   # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18])   # []
print(list_1[0:len(list_1):6])   # [1, 7]
print(list_1[::6])   # [1, 7]

'''
Кортеж — это неизменяемый список.
В случае защиты каких-либо данных от изменений (намеренных или случайных). Кортеж занимает меньше места в
памяти и работают быстрее, по сравнению со списками. Нпр. пароли, либо название хоста.
'''
# () - кортеж(tuple), [] - список(list)

t = ()   # создание пустого кортежа
print(type(t))   # class <'tuple'>

t = (1) 
print(type(t))   # class <'int'>

t = (1,)   # чтобы преобразовать int в tuple, необходимо поставить после числа ,
print(type(t))   # class <'tuple'>

t = (28, 9, 1990)
print(type(t))   # class <'tuple'>

v = [1, 8, 9]   
print(v)   # [1, 8, 9]
print(type(v))   # class <'list'>
v = tuple(v)
print(v)   # (1, 8, 9)
print(type(v))   # class <'tuple'>

# разъединить кортеж на 3 переменные
a, b, c = v
print(a, b, c)   # 1 8 9

colors = ['red', 'green', 'blue']
print(colors)   # ['red', 'green', 'blue']
t = tuple(colors)
print(t)   # ('red', 'green', 'blue')

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))   # r:red g:green b:blue

t = (1, 7, 10)
for i in t:
    print(i)   # 1 7 10

t = (1, 7, 10)
for i in range(len(t)):
    print(t[i])   # 1 7 10

# Так как кортеж неизменяемый, то не даст нам изменить [0] в отличие от списка
t = (1, 9, 4, 5)
t[0] = 3
print(t)   # t[0] = 3 ^^^ TypeError: 'tuple' object does not support item assignment

t = [1, 9, 4, 5]
t[0] = 3
print(t)   # [3, 9, 4, 5]

t = tuple(['red', 'green', 'blue'])
print(t[0])   # red
print(t[2])   # blue
t[0] = 'black'   # TypeError: 'tuple' object does not support item assignment
for e in t:
    print(e)   # red green blue
  
t = ['red', 'green', 'blue']
print(t[0])   # red
print(t[2])   # blue
t[0] = 'black' 
for e in t:
    print(e)   # black green blue

'''
Словари
💡 Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
В списках в качестве ключа используется индекс элемента. 
В словаре для определения элемента используется значение ключа (строка, число).
'''
# {} - словарь(dictionary) либо a = dict() либо {key: value,}

dictionary = {}
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary)   # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left'])   # ←
print(dictionary['up'])   # ↑
dictionary['left'] = '⇐'
print(dictionary['left'])   # ⇐
print(dictionary['type'])   # KeyError: 'type'- если обращаемся к несуществующему ключу
del dictionary['left']   # удаление элемента # {'up': '↑', 'down': '↓', 'right': '→'}

for item in dictionary:   # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))   # up: ↑ # down: ↓ # right: →
    # print(item)   # up down right

for (k, v) in dictionary.items():   # k - ключ v - значение
    print(k, v)   # up: ↑ # down: ↓ # right: →

print(dictionary.items())   # dict_items([('up', '↑'), ('left', '←'), ('down', '↓'), ('right', '→')])

d = dict()
d['q'] = 'qwerty'
print(d)   # {'q': 'qwerty'} - в нашем словаре есть ключ 'q', по которому если обратимся, то получим 'qwerty'

d['w'] = 'werty'
print(d)   # {'q': 'qwerty', 'w': 'werty'}

print(d['q'])   # qwerty - при обращении по ключу получаем вложенное значение

# можем добавлять значения в словарь
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
dictionary[898] = 11111
print(dictionary)   # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→', 898: 11111}

'''
Множества - используются для получения уникальных значений.
💡 Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
Одно множество может содержать значения любых типов. Если у Вас есть два множества, можно 
совершать над ними любые стандартные операции, нпр., объединение, пересечение и разность.
'''
# {} отличается от словаря тем, что в словаре указывается ключ : и значение, а здесь просто перечисление через ,
colors = {'red', 'green', 'blue'}
print(colors)   # {'red', 'green', 'blue'}
colors.add('red')
print(colors)   # {'red', 'green', 'blue'}
colors.add('gray')
print(colors)   # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors)   # {'green', 'blue','gray'}
colors.remove('red')   # KeyError: 'red' - в случае если мы пытаемся удалить ранее удаленный элемент
colors.discard('red')   # ok - .discard() проверяет есть ли это значение и если есть удаляет его, если нетб то просто пропускает эту строку кода
print(colors)   # {'green', 'blue','gray'}
colors.clear()   # { } - .clear() удаляет все значения из списка
print(colors)   # set()

q = set()   # создает множества

# Операции со множествами в Python
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()   # c = {1, 2, 3, 5, 8}
u = a.union(b)   # u = {1, 2, 3, 5, 8, 13, 21} - создает список уникальных значений из множеств a и b
i = a.intersection(b)   # i = {8, 2, 5} - выбирает пересекающиеся элементы обоих множеств a и b
dl = a.difference(b)   # dl = {1, 3} - из множества a вычитаем все значения, содержащиеся в множестве b
dr = b.difference(a)   # dr = {13, 21} - из множества b вычитаем все значения, содержащиеся в множестве a
q=a.union(b).difference(a.intersection(b))   # {1, 21, 3, 13} - a.intersection(b) первое действие, а далее a.union(b).difference()

# Неизменяемое или замороженное множество(frozenset) — множество, с которым не будут работать методы удаления и добавления.
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})

'''
List Comprehension «генератора списка». 
List comprehension — это упрощенный подход к созданию списка, который задействует цикл for, 
а также инструкции if-else для определения того, что в итоге окажется в финальном списке.

1. Простая ситуация — список:
list_1 = [exp for item in iterable]
1. Выборка по заданному условию:
list_1 = [exp for item in iterable (if conditional)]
'''
# Задача: Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
# Решение:
# 1. Создать список чисел от 1 до 100
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1)   # [1, 2, 3,..., 100]

# Эту же функцию можно записать так:
list_1 = [i for i in range(1, 101)]   # [1, 2, 3,..., 100]

# 2. Добавить условие (только чётные числа)
list_1 = [i for i in range(1, 101) if i % 2 == 0]   # [2, 4, 6,..., 100]

# Допустим, вы решили создать пары каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]   # [(2, 2), (4, 4),...,(100, 100)]

# Также можно умножать, делить, прибавлять, вычитать. Нпр., умножить значение на 2.
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1)   # [0, 4, 8, 12, 16]

