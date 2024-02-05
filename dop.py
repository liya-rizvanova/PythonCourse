import os
os.system('cls||clear')

# a = 'Python'
# b = 'Hello world!'
# z = 'Привет, меня зовут Вася!'
# age = 25

# print(a, b, z, age)
# print(a, b, z, age, sep=' ', end='\n')
# print(a, b, z, age, sep=z)

# print(a, end=a)
# print(b, end=a)
# print(z, end=a)
# print(age, end='~~~')
# print(age)

# 12:33
# s = 'Python'

# print(*s) # -> print('P', 'y', 't', 'h', 'o', 'n')
# print()
# print(*s, sep='\n')

# выведет:

# P y t h o n

# P
# y
# t
# h
# o
# n


# a = 'Python'
# age = 25
# name = "John"

# print(f'Привет, меня зовут {name}, мне {age} лет.')
# print('Привет, меня зовут {}, мне {} лет. Я учу {}'.format(name, age, a))
# print('Привет, меня зовут {b}, мне {z} лет. Я учу {a}'.format(a=name, b=age, z=a))
# print('Hi, %s.' % name)

# x = 12
# y = 23
# z = 4

# print(f'Результат выражения {x*y**z}')
# print(f'Результат выражения {x*y**z=}')
# print(f'Результат выражения {x}*{y}**{z}={x*y**z}')


# range(start=0, stop, step=1)#

# range(5) -> range(start=0, stop=5, step=1) -> 0,1,2,3,4
# range(2, 10) -> range(start=2, stop=10, step=1) -> 2,3,4,5,6,7,8,9
# range(3, 15, 2) -> range(start=3, stop=15, step=2) -> 3,5,7,9,11,13

# 0  1   2   3    4
# text = '2  3   4   5   7'
#        -5 -4  -3  -2   -1
       
# print(text[2]) -> 4
# print(text[-2]) -> 5
# print(text[1:4]) -> 345
# print(text[:3]) -> 234
# print(text[3:]) -> 57
# print(text[:]) -> 23457
# print(text[::2]) -> 247


# text = '23457'
# print(text[2]) #-> 4
# print(text[-2]) #-> 5
# print(text[1:4]) #-> 345
# print(text[:3]) #-> 234
# print(text[3:]) #-> 57
# print(text[:]) #-> 23457
# print(text[::2]) #-> 247
# print(text[::-2]) #-> 742
# text_2 = '234571235365676758'
# print(text_2[3: 9: 2])
# print(text_2[7: 1: -2])
# print(text_2[::-1]) #-> 857676563532175432


# new_text = 'Hello, world!'

# for symbol in new_text:
#     print(symbol)
    
# print(*range(len(new_text)))  

# for i in range(len(new_text)):
#     print(new_text[i:])

# print(new_text[-2:])
# print(int('1234562кг'[:-2]))

# for num in range(50):
#     if num % 2 == 0:
#         continue
#     if num % 3 == 0:
#         print(num, end=' ')
#     if num == 33:
#         break
# else:
#     print('Я всё, закончил!') # выводится только по прохождении всего цикла



# text = 'sdffghdfghwergsdfgh'
# my_list = [123,345,567,534]
# num = 1235346

# my_set = {1234,456,678}
# my_set.add(text)
# my_set.add(my_list)
# print(my_set)

# my_set.update(text)
# my_set.update(my_list)
# my_set.update(num)
# print(my_set)



# num = 45
# text = 'hello'
# my_list = [1,2,3,4,5, [11,22,33, [777,888,999]]]
# print(my_list)

# my_list_2 = my_list
# print(my_list_2)
# print()
# my_list_2[2] = 999
# print(my_list)
# print(my_list_2)
# print()

# my_list_3 = my_list.copy()
# print(my_list_3)
# print()
# my_list_3[3] = 0
# print(my_list)
# print(my_list_3)
# print()

# my_list_4 = my_list[:] # list(my_list)
# print(my_list_4)
# print()
# my_list_4[-1][1] = '~~~~'
# print(my_list)
# print(my_list_4)
# print()

# my_list_5 = copy.deepcopy(my_list)
# print(my_list_5)
# print()
# my_list_5[-1][-1][1] = 'XXX'
# print(my_list)
# print(my_list_5)




# import copy

# my_tuple = (1,2,3,4,5, [11,22,33, [777,888,999]])
# print(my_tuple)

# my_tuple_2 = my_tuple[:]
# print(my_tuple_2)
# print()
# my_tuple_2[-1][1] = '~~~~'
# print(my_tuple)
# print(my_tuple_2)
# print()

# my_tuple_3 = copy.deepcopy(my_tuple)
# print(my_tuple_3)
# print()
# my_tuple_3[-1][-1][1] = 'XXX'
# print(my_tuple)
# print(my_tuple_3)



# my_dict = {'Иванов':1, 'Петров': 2, 'Сидоров':3, 'Николаев':4}
# # print(f'{my_dict=}')
# # print(f'{my_dict["Петров"]=}')
# # print()
# print(my_dict)
# print(my_dict["Петров"])
# print()
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print()
# # print(f'{len(my_dict.keys())=}')
# # print(f'{sum(my_dict.values())=}')
# # print(f'{my_dict.items()=}')
# # print()
# # print(f'{list(my_dict.keys())[3]=}')
# # print(f'{list(my_dict.values())=}')
# # print(f'{list(my_dict.items())=}')
# # print()

# # for key in my_dict:
# # print(key, end='\t')
# # print('\n')

# # for key in my_dict.keys():
# # print(key, end='\t')
# # print('\n')

# # for value in my_dict.values():
# # print(value, end='\t')
# # print('\n')

# # for item in my_dict.items():
# # print(item, end='\t')
# # print('\n')

# for key, value in my_dict.items():
# print(key, value,sep='-', end='\t')
# print('\n')

# # q,w,*e = (111,222)
# # print(q)
# # print(w)
# # print(e)

# # my_list = [(1,2,3), (11,22,33), (111,222,333)]
# # for q,w,*e in my_list:
# # print(q, w, e, sep='-')

# for key, value in my_dict.items():
# print(key,value, sep=': ', end='\t')
# print('\n')



# my_dict = {'Иванов':1, 'Петров': 2, 'Сидоров':3, 'Николаев':4}

# text = 'hello world!'
# text = text[6:] + ' ' + text[: 5]

# # my_dict['Алексеев'] = my_dict['Петров']
# # del my_dict['Петров']

# my_dict['Алексеев'] = my_dict.pop('Петров')



# my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]

# res_list = filter(lambda x: x % 2 == 0, my_list)
# print(res_list)
# print(list(res_list))

# res_list=[]
# f = lambda x: x % 2 == 0
# for el in my_list:
#     if f(el):
#         res_list.append(el)
# print(res_list)



# my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]

# res_list = filter(lambda x: x % 2 == 0, my_list)
# print(res_list)
# print(list(res_list))

# res_list=[]
# f = lambda x: x % 2 == 0
# for el in my_list:
#     if f(el):
#         res_list.append(el)
# print(res_list)

# f = lambda x: x % 2 == 0
# res_list = [el for el in my_list if f(el)]
# print(res_list)


# my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]

# # res_list = map(lambda x: x ** 2 , my_list)
# # print(res_list)
# # print(list(res_list))

# #1
# res_list = list(map(lambda x: x % 2 == 0, my_list))
# print(res_list)
# #2
# res_list=[]
# f = lambda x: x % 2 == 0
# for el in my_list:
#     res_list.append(f(el))
# print(res_list)
# #3
# f = lambda x: x % 2 == 0
# res_list = [f(el) for el in my_list]
# print(res_list)


# var2 = '10 8 3 5 7 9' 
# var3 = '10 3 8 4 5' 

# str_1 = list(map(int,var2.split()))
# str_2 = list(map(int,var3.split()))
# list_1 = set(str_1)
# list_2 = set(str_2)
# list_3 = list_1.intersection(list_2)
# #list_3.sort()
# print(*sorted(list_3))


a = 5
print(a:= 10)

print(a)

while a:= a - 1:
    print(a)


print(all([True, True, True, True]))
print(all([True, False, True, True]))
print(all([False, False, False, False]))
print()
print(any([True, True, True, True]))
print(any([True, False, True, True]))
print(any([False, False, False, False]))
print()
print(all([1, 2, 3, 4]))
print(all([1, 0, 3, 4]))
print(all([0, 0, 0, 0]))
print()
print(any([1, 2, 3, 4]))
print(any([1, 0, 3, 4]))
print(any([0, 0, 0, 0]))
print()
print(all(['dfg', 'sdf', 'sdf', 'cvb']))
print(all(['dfg', '', 'sdf', 'cvb']))
print(all(['', '', '', '']))
print()
print(any(['dfg', 'sdf', 'sdf', 'cvb']))
print(any(['dfg', '', 'sdf', 'cvb']))
print(any(['', '', '', '']))
print()
print(all([[''], ('',), {''}, ['']]))
print(all([[''], [], [''], ['']]))
print(all([{}, {}, {}, []]))
print()
print(any([[''], ('',), {''}, ['']]))
print(any([[''], [], [''], ['']]))
print(any([{}, {}, {}, []]))
print()


