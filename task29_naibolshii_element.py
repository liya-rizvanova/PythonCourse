'''
29. Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить значение наибольшего элемента
последовательности, которая завершается первым встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не  такими смышлеными. Никто из ребят не смог до 
конца сделать это задание. Они решили так: у кого  будет меньше ошибок в коде, тот и выиграл спор.
За помощью товарищи обратились к Вам, студентам.
Программные коды:

Ваня: (2 ошибки)                  Петя: (3 ошибки)
n = int(input())                  n = int(input())  
max_number = 1000                 max_number = -1
while n != 0:                     while n < 0:
 n = int(input())                  n = int(input())
 if max_number > n:                if max_number < n:
  max_number = n                    n = max_number
print(max_number)                 print(n)

'''

n = int(input())
max_number = n   # or max_number = -1
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)


'''
Задача №29 1) Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. Однако 2  друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам

2) Задача – «На вход программе подаются натуральные числа,как только пользователь введёт 0 ввод прекращается. Вывести наибольший элемент получившейся последовательности». 
Есть два кода с ошибками, нужно определить  где ошибок меньше.

Примечание: Программные коды на следующих слайдах
'''

# Ваня:

n = int(input())
max_number = n # mist1 max_number = 1000
while n != 0:
   n = int(input())
   if max_number < n: # mist2 if max_number > n:
       max_number = n
print(max_number)

# Петя:

# mist1 n = int(input()) 
max_number = -1
while n != 0: # mist2 while n < 0:
   n = int(input())
   if max_number < n:
       max_number = n # mist3 n = max_number
print(max_number) # mist4 print(n)
 
 

