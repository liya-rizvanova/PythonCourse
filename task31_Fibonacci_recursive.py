'''
31. Последовательностью Фибоначчи называется последовательность чисел
a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи

Input: 7
Output: 21

Ряд чисел Фибоначчи:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, …
'''


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Введите номер числа Фибоначчи: '))
result = fibonacci(n + 1)  # Оставляем передачу n, так как индексы начинаются с 0
print(f"Число Фибоначчи под номером {n}: {result}")



# def f(n):
#     if n == 0 or n == 1:
#         return 1
#     return f(n - 1) + f(n - 2)

# n = int(input())

# print(f(n - 2))


'''
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Пример использования
N = int(input("Введите N: "))
result = fibonacci(N)
print(f"Число Фибоначчи под номером {N}: {result}")
'''