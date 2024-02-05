'''
15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза.
Все числа натуральные и не превышают 3000.
Пользователь вводит одно число N. Далее идут N чисел, записанных на новой строчке каждое.
Вывести максимальное и минимальное (циклы)

Input:  5 -> 5 1 6 5 9
Output: 1 9
'''

n = int(input())

max = -1
min = 3001

for i in range(n):
    x = int(input())
    if x > max:
        max = x
    if x < min:
        min = x

print(max, min)



# from random import randint

# watermealon = int(input("Enter watermealon amount: "))

# min_weight = float("inf") # бесконечность
# max_weight = -float("inf") # - бесконечность

# for _ in range(watermealon):
#     weight = randint(1, 10)
#     print(weight, end = ' ')
#     if weight > max_weight:
#         max_weight = weight
#     if weight < min_weight:
#         min_weight = weight
# print()
# print(min_weight, max_weight)

#2

# from random import randint

# watermealon = int(input("Enter watermealon amount: "))
# weight = randint(1, 10)
# print(weight, end = ' ')
# min_weight = weight
# max_weight = weight

# for _ in range(watermealon - 1):
#     weight = randint(1, 10)
#     print(weight, end = ' ')
#     max_weight = max(weight, max_weight)
#     min_weight = min(weight, min_weight)
    
# print()
# print(min_weight, max_weight)