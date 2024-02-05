'''
14. Требуется вывести все целые степени двойки (т.е. числа вида 2k ), не превосходящие числа N.

10 -> 1 2 4 8
16 -> 1 2 4 8 16
'''

'''
# Вводим число N
N = int(input("Введите число N: "))

# Используем цикл для вывода целых степеней двойки
power_of_two = 1
while power_of_two <= N:
    print(power_of_two, end=" ")
    power_of_two *= 2
'''

'''
# Вводим число N
N = int(input("Введите число N: "))

# Используем цикл для вывода целых степеней двойки
power_of_two = 1
while power_of_two <= N:
    print(power_of_two)
    power_of_two *= 2
'''


n = int(input())

i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1



n = int(input())

k = 1
while k <= n:
    print(k)
    k *= 2