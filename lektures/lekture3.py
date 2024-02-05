'''
💡 Функция — это фрагмент программы, используемый многократно

def function_name(x):
    # body line 1
    # ...
    # body line n
    # optional return
'''
# Задание: Необходимо создать функцию sumNumbers(n), которая будет считать сумму всех элементов от 1 до n.

def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1): # т.к. нужны все значения из промежутка [1, n], вызываем функцию range, от 1 до n + 1, т.к. range не включает последний элемент
        summa += i
    print(summa)

sumNumbers(5)   # 15 - вызывая функцию передаем в нее столько значений, сколько переменнх указано при создании

# чтобы функция возвращала какое-либо значение используем return
def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa

print(sumNumbers(5))

# еще один вариант записи
def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa

a = sumNumbers(5)
print(a)

# вариант присваивания значений переменнойб передаваемой функции
def sumNumbers(n, y = "Hello"):   # y - присваиваем значение по умолчанию
    print(y)
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa

print(sumNumbers(5))  # Hello 15

def sumNumbers(n, y = "Hello"):   # y - присваиваем значение по умолчанию
    print(y)
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa

print(sumNumbers(5, "Hi"))   # Hi 15 - в независимости от того, что есть значение по умолчанию

# запрашиваем число от пользователя
def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa
n = int(input())   # 7
print(sumNumbers(n))   # 28

# если мы не знаем какое количество переменных будем передавать
def sum_str(*args):   # * указывает на то, что мы хотим передать неограниченное количество аргументов
    res = ''
    for i in args:
        res += i
    return res

print(sum_str('w', 'o', 'r', 'l', 'd'))   # world
print(sum_str('w', 'o', 'r', 'l', 'd', '!', '!', '!'))   # world!!!
print(sum_str(0, 0, 1))   # TypeError: can only concatenate str (not "int") to str

# Чтобы избежать ошибки, можyj преобразовать каждый аргумент в строку с помощью str():
def sum_str(*args):
    res = ''
    for i in args:
        res += str(i)
    return res

print(sum_str(0, 0, 1))   # 001

'''
Модульность
Чтобы начать взаимодействовать с функцией в файле function_file.py необходимо добавить эту возможность 
к себе в программный код. Сначала мы обращаемся к файлу(без расширения). 
C помощью import мы можем вызвать эту функцию в другом скрипте и дальше использовать её в новом файле. 
Можно сократить название функции в рабочем файле с помощью команды:
Alias (псевдоним) — альтернативное имя, которое даётся функции при еt импорте из файла.
'''
import function_file

print(function_file.max1(5,9))

# либо
from function_file import max1

print(max1(5,9))

# если не знаем имя фунции, можем импортировать все функции при помощи *
from function_file import *   # * импортирует все функции из файла

print(max1(5,9))

# на время работы с программой можем изменить имя модуля
import function_file as f1

print(f1.max1(5,9))

# пример работы с другой функцией
import function_file

print(function_file.other(1))   # Целое
print(function_file.other(2.3))   # 23
print(function_file.other(28))   # None

'''
В Python можно перемножать строку на число.
В данной функции есть два аргумента: symbol (символ или число) и count (число, на которое умножается первый аргумент).
Если введены оба аргумента, функция работает без ошибок. Если только символ — функция выдает ошибку.
'''
def new_string(symbol, count):
    return symbol * count
print(new_string('!', 5))   # !!!!!
print(new_string('!'))   # TypeError missing 1 required positional argument: 'count'

'''
Можно указать значение переменной count по умолчанию. Например, если значение явно не указано 
(нет второго аргумента), по умолчанию значение переменной count равно трем.
'''
def new_string(symbol, count=3):
    return symbol * count
print(new_string('!', 5))   # !!!!!
print(new_string('!'))   # !!!
print(new_string(4))   # 12

'''
● Можно указать любое количество значений аргумента функции.
● Перед аргументом надо поставить *.
В примере ниже функция работает со строкой, поэтому при введении чисел программа выдаёт ошибку:
'''
def concatenatio(*params):
    res = ""
    for item in params:
        res += item
    return res
print(concatenatio('a', 's', 'd', 'w'))   # asdw
print(concatenatio('a', '1'))   # a1
# print(concatenatio(1, 2, 3, 4))   # TypeError: ...

'''
Рекурсия
Внутри функции fib(n), сначала задается базис, если число n равно 1 или 2, это означает, что первое число и
второе число последовательности равны 1, поэтому возвращаем 1. Как мы ранее проговорили:
'''
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)
list_1 = []
for i in range(1, 10):
    list_1.append(fib(i - 2))
print(list_1)   # [1, 1, 2, 3, 5, 8, 13, 21, 34]

'''
Два друга решили поиграть в игру: один загадывает число от 1 до 100, 
другой должен отгадать.
'''
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 3]))
'''
● 1-е повторение рекурсии:
○ array = [10, 5, 2, 3]
○ pivot = 10
○ less = [5, 2, 3]
○ greater = []
○ return quicksort([5, 2, 3]) + [10] + quicksort([])
● 2-е повторение рекурсии:
○ array = [5, 2, 3]
○ pivot = 5
○ less = [2, 3]
○ greater = []
○ return quicksort([2, 3]) + [5] + quicksort([]) # Важно! Не забывайте, что
здесь помимо вызова рекурсии добавляется список [10]
● 3-е повторение рекурсии:
○ array = [2, 3]
○ return [2, 3] # Сработал базовый случай рекурсии
На этом работа рекурсии завершилась и итоговый список будет выглядеть таким образом: 
[2, 3] + [5] + [10] = [2, 3, 5, 10]
'''

# Сортировка слиянием
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
nums = [38, 27, 43, 3, 9, 82, 10]
merge_sort(nums)
print(nums)
