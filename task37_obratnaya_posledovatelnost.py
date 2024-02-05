'''
37. Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

Input:  2 -> 3 4
Output: 4 3
'''


# elements = int(input("Введите количество элементов: "))
# numbers = input("Введите числа через пробел: ").split()

# reversed_numbers = reversed(numbers)
# print(f"Обратная последовательность чисел: {' '.join(reversed_numbers)}")



# elements = int(input("Введите количество элементов: "))
# numbers = input("Введите числа через пробел: ").split()

# new_string = reversed(numbers)
# print(" ".join(new_string))



# def reverse_sequence(count):
#     if count > 0:
#         num = int(input("Введите число: "))
#         reverse_sequence(count - 1)
#         print(num, end=' ')

# # Пример использования
# elements = int(input("Введите количество элементов: "))
# reverse_sequence(elements)



# def reverse_sequence(numbers):
#     if not numbers:
#         return
#     else:
#         current_number = int(numbers.pop())
#         reverse_sequence(numbers)
#         print(current_number, end=' ')

# # Пример использования
# input_numbers = input("Введите числа через пробел: ").split()
# reverse_sequence(list(reversed(input_numbers)))



def f(n):
    if n == 0:
        return ''   # условие выхода из рекурсии
    k = int(input())
    return f(n - 1) + f'{k}'

n = int(input())
print(f(n))