'''
Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое 
значение некоторой характеристики, и возвращает True, если это так. Если значение характеристики для 
разных объектов отличается – то False. Для пустого набора объектов, функция должна возвращать True. 
Аргумент characteristic – это функция, которая принимает объект и вычисляет его характеристику.
====================================               ====================================
1. Ввод:                                           2. Ввод:
values = [0, 2, 10, 6]                             values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):               if same_by(lambda x: x % 2, values):
    print('same')                                      print('same')
else:                                              else:
    print('different')                                 print('different')
------------------------------------               ------------------------------------
Вывод: same                                        Вывод: differen
'''
def same_by(characteristic, object):
    result = True
    list_1 = [characteristic(x) for x in object]
    for i in range(len(list_1) - 1):   # проверяем действительно ли все элементы одинаковы
        if list_1[i] != list_1[i + 1]:
            result = False
    return result

# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')