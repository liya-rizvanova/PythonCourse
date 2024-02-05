'''
45. Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все пары
дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке,
разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

Ввод:             Вывод:
300               220 284
'''


k = int(input())
list1 = list()   # здесь хранятся кортежи, т.е. 1ый элемент - само число, а 2ой - сумма его делителей

for i in range(k):
    summa = 0
    for j in range(1, i//2 + 1):
        if i % j == 0:
            summa += j
    list1.append(tuple([i, summa]))

for i in range(len(list1)):
    for j in range(i, len(list1)):
        if i != j and list1[i][0] == list1[j][1] and list1[i][1] == list1[j][0]: 
            print(*list1[i])   # * означает распаковку кортежа, т.е. если без * (220, 284), то со * 220 284



# def sum_of_divisors(n):
#     # Функция для вычисления суммы делителей числа n
#     return sum(i for i in range(1, n) if n % i == 0)

# def find_friendly_pairs(k):
#     # Поиск и вывод пар дружественных чисел
#     for num1 in range(1, k):
#         # Для каждого числа num1 от 1 до k (не включительно)
#         sum1 = sum_of_divisors(num1)

#         # Проверка, является ли сумма делителей num1 другим дружественным числом
#         if sum1 < k and num1 < sum1 and sum_of_divisors(sum1) == num1:
#             print(f"{num1} {sum1}")

# # Ввод значения k
# k = int(input("Введите значение k: "))

# # Поиск и вывод пар дружественных чисел
# find_friendly_pairs(k)