'''
11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

Input: 5
Output: 6

Ряд чисел Фибоначчи:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, …
'''


a = int(input('Введите число Фибоначчи: '))

n1 = 0
n2 = 1
r = 1
count = 3

while r < a:
    n1 = n2
    n2 = r
    r = n1 + n2
    count += 1

if a != r:
    count = -1
print(count)


'''
a = int(input('Введите число Фибоначчи: '))

n1 = 1
n2 = 2
count = 4

while n2 < a:
    n2, n1 = n1 + n2, n2
    count += 1

if a != n2:
    count = -1
print(count)
'''

'''
n = int(input())

n0 = 0
n1 = 0
n2 = 1
i = 2

while n0 < n:
    n0 = n1 + n2
    n1 = n2
    n2 = n0
    i += 1
    if n0 > n:
        i = -1
print(i)
'''

'''
A = int(input())

n0, n1, n2 = 0, 0, 1
i = 2

while n2 < A:
    n0, n1, n2 = n1, n2, n1 + n2
    i += 1

if n2 == A:
    print(i)
else:
    print(-1)
'''

'''
A = int(input())

n0, n1, n2 = 0, 0, 1
i = 2

for i in range(2, A + 1):
    n0, n1, n2 = n1, n2, n1 + n2
    i += 1
    if n2 == A:
        print(i)
        break
else:
    print(-1)
'''

'''
В этой версии кода используется цикл for вместо while, а также добавлено условие for-else,
которое выполняется, если цикл завершается естественным образом (без прерывания).
'''