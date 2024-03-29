'''
8. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками (то есть разломить
шоколадку на два прямоугольника).

3 2 4 -> yes
3 2 1 -> no
'''


# Получаем данные от пользователя
a = int(input("Введите ширину шоколадки (a): "))
b = int(input("Введите высоту шоколадки (b): "))
c = int(input("Введите количество долек (c): "))

# Проверяем, можно ли отломить c долек
if c <= a * b and (c % a == 0 or c % b == 0):
    print("yes")
else:
    print("no")


'''
Теперь код учитывает, что количество долек не должно превышать общее количество
долек в шоколадке (a * b), и проверяет, можно ли отломить указанное количество
долек с учетом их распределения по ширине (a) или высоте (b).
'''

'''
# Получаем данные от пользователя
a = int(input("Введите ширину шоколадки (a): "))
b = int(input("Введите высоту шоколадки (b): "))
c = int(input("Введите количество долек (c): "))

# Проверяем, можно ли отломить c долек
if c >= a or c >= b:
    print("yes")
else:
    print("no")
'''

'''
Этот код запрашивает у пользователя размеры шоколадки (a и b) и количество долек (c).
Затем он проверяет, можно ли отломить указанное количество долек от шоколадки и
выводит "yes" или "no" в зависимости от результата.
'''