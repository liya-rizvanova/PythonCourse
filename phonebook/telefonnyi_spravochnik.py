'''
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в двух файлах,
разных форматов записи.
1. Программа должна выводить данные
2. Программа должна сохранять данные
3. Использование функций. Ваша программа не должна быть линейной.

Дополнить телефонный справочник возможностью добавления/удаления данных.
'''
from logger import *

def interface():
    print("Welcome! I'm phone directory bot! \n 1 - create data \n 2 - show data \n 3 - change data \n 4 - delete data")
    command = int(input('Select an action: '))

    while command != 1 and command != 2 and command != 3 and command != 4:   # если пользователь ввел некорректное число
        print('Действие не выбрано!')
        command = int(input('Выберите действие: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        change_data()
    elif command == 4:
        delete_data()

interface()