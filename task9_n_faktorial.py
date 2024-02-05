'''
9. По данному целому неотрицательному n вычислите значение n!.
N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N)
0! = 1 Решить задачу используя цикл while

Input:  5
Output: 120 
'''

n = int(input("Введите число: "))

i = 1
res = 1

while i <= n:
    res = res * i # res *= i
    i += 1
    
print(f"Факториал числа {n} равен {res}")


'''
number = int(input("Введите число: "))

i = 1
res = 1

while i <= number:
    res *= i
    i += 1

print(f"{number}! равен {res}")
'''

'''
number = int(input("Введите число: "))
fact = number
res = 1

while number > 1:
    res *= number
    number -= 1

print(f"{fact}! равен {res}")
'''