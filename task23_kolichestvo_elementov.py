'''
23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента с предыдущим номером).

Input:  [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)

Примечание: Пользователь может вводить значения списка или список задан изначально.
'''

list = [0, -1, 5, 2, 3]

count = 0 # сода записываются все элементы, которые больше предыдущего

for i in range(1, len(list)): # проверяем элементы от 1го элемента, до конца списка
    if list[i] > list[i-1]:
        count += 1
print(count)



list_1 = [0, -1, 5, 2, 3]

count = 0

for i in range(1, len(list_1)):
    if list_1[i] > list_1[i - 1]:
        count += 1

print(count)
print(sum([1 for i in range(1, len(list_1)) if list_1[i] > list_1[i - 1]]))

#2
numbers = [0, -1, 5, 2, 3]
count = 0

# for i in range(len(numbers) - 1):
#     if numbers[i] > numbers[i + 1]:
#         count += 1
# print(count)

# print([1 for i in range(len(numbers) - 1) if numbers[i] > numbers[i + 1]])
print(len([print(f'{numbers[i]} > {numbers[i + 1]}') for i in range(len(numbers) - 1) if numbers[i] > numbers[i + 1]]))