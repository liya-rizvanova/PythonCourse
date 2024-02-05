'''
3. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.

Input:  20 21 22(ввод чисел НЕ в одну строку)
Output: 32
'''

a = int(input())
b = int(input())
c = int(input())

s1 = ((a + 1)//2)
s2 = ((b + 1)//2)
s3 = ((c + 1)//2)

print(s1 + s2 + s3)


'''
# class_1 = int(input("Enter number of students in 1st class: "))
# class_2 = int(input("Enter number of students in 2nd class: "))
# class_3 = int(input("Enter number of students in 3nd class: "))

# tables_1 = ((class_1 + 1)//2)
# tables_2 = ((class_2 + 1)//2)
# tables_3 = ((class_3 + 1)//2)

# print(tables_1 + tables_2 + tables_3)
'''

'''
import math

def calculate_desks(class1, class2, class3):
    # Суммируем количество учащихся и делим на 2
    total_students = class1 + class2 + class3
    desks_required = math.ceil(total_students / 2)
    return desks_required

# Пример использования
class1_students = 20
class2_students = 21
class3_students = 22

result = calculate_desks(class1_students, class2_students, class3_students)
print(result)
'''

'''
Для решения этой задачи, нам нужно определить количество парт,
которое потребуется для трех новых математических классов.
Условие гласит, что за каждой партой может сидеть два учащихся.

Просто сложим количество учащихся в каждом классе и разделим на два,
так как за каждой партой сидят два учащихся. Мы также округлим результат
вверх, так как не можем купить часть парты.

В этом коде мы используем функцию calculate_desks, которая принимает
количество учащихся в каждом из трех классов и возвращает минимальное
количество парт, которое нужно приобрести.
Функция math.ceil используется для округления результата вверх.
'''

'''
import math

def calculate_desks(class1, class2, class3):
    # Суммируем количество учащихся и делим на 2
    total_students = class1 + class2 + class3
    desks_required = math.ceil(total_students / 2)
    return desks_required

# Получаем данные от пользователя
class1_students = int(input("Введите количество учащихся в первом классе: "))
class2_students = int(input("Введите количество учащихся во втором классе: "))
class3_students = int(input("Введите количество учащихся в третьем классе: "))

result = calculate_desks(class1_students, class2_students, class3_students)
print(f"Минимальное количество парт: {result}")
'''

'''
Этот код использует функцию input для запроса данных у пользователя.
int используется для преобразования введенных значений в целые числа.
Затем программа вычисляет минимальное количество
парт с использованием введенных данных и выводит результат.
'''