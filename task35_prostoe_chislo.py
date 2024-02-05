'''
35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

Input:  5
Output: yes 
'''

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# # Пример использования
# number = int(input("Введите число: "))
# result = "yes" if is_prime(number) else "no"
# print(result)



def prime(n):
    flag = True
    i = 2
    while i < n and flag:
        if n % i == 0:
            flag = False

        i += 1
    if flag:
        return 'yes'
    else:
        return 'no'
        
n = int(input())
print(prime(n))
