'''
28. Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

2 2 -> 4
'''


# def sum_num(a, b):
#     if a == 0:
#         return b
#     elif b == 0:
#         return a
#     else:
#         # Рекурсивно уменьшаем одно из чисел на 1, а другое увеличиваем на 1
#         return sum_num(a - 1, b + 1)

# # Ввод данных
# a = int(input("Enter A: "))
# b = int(input("Enter B: "))

# result = sum_num(a, b)
# print(result)


'''
def sum_recursive(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        # Рекурсивно уменьшаем одно из чисел на 1, а другое увеличиваем на 1
        return sum_recursive(a - 1, b + 1)

# Пример использования
result = sum_recursive(5, 3)
print(result)
'''

'''
Эта функция использует базовые случаи, когда одно из чисел равно 0, иначе рекурсивно вызывает саму себя,
уменьшая одно число на 1 и увеличивая другое на 1.
'''


def sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum(a + 1, b - 1)

a = 3
b = 5
print(sum(a, b))