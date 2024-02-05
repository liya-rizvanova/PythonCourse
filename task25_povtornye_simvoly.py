'''
25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

Input:  a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

Для решения данной задачи используйте функцию .split()
'''


# stroka = input().split()
# res = {}

# for i in stroka:
#     if i in res:
#         print(f'{i}_{res[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     res[i] = res.get(i, 0) + 1



line = "a a a b c a a d c d d".split()
print(line)
res = {}

# for letter in line:   # letter - циклическая переменная
#     if letter not in res:   # поиск по ключам
#         print(letter, end=' ')
#         res[letter] = 0   # res - словарь [letter] - ключ(которому передаются циклические переменные) = 0 - значение
#     else:
#         res[letter] += 1
#         print(f"{letter}_{res[letter]}", end=' ')

#2
# for letter in line:
#     if letter not in res:
#         print(letter, end=' ')        
#     else:
#         print(f"{letter}_{res[letter]}", end=' ')
#     res[letter] = res.get(letter, 0) + 1

#3
new_line = ''

for letter in line:
    if letter not in res:
        new_line += f"{letter} "
    else:
        new_line += f"{letter}_{res[letter]} "
    res[letter] = res.get(letter, 0) + 1

print(new_line)