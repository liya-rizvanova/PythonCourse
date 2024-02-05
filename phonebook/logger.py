from data_create import *

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()

    var = int(input(f'Select format to save data: \n\n'
                    f'Version 1: \n'
                    f'{name}\n{surname}\n{phone}\n{address}\n\n'
                    f'Version 2: \n'
                    f'{name};{surname};{phone};{address}\n\n'
                    f'Select format: '))

    while var != 1 and var != 2:
        print('Wrong entrance!')
        var = int(input("Select format: "))

    entry_id = None
    if var == 1:
        file_path = 'C:/Users/Администратор/Desktop/PythonCourse/phonebook/data_first_variant.csv'
        entry_id = get_next_entry_id(file_path, 5)
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(f'{entry_id}\n{name}\n{surname}\n{phone}\n{address}\n')
            
    elif var == 2:
        file_path = 'C:/Users/Администратор/Desktop/PythonCourse/phonebook/data_second_variant.csv'
        entry_id = get_next_entry_id(file_path, 1)
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(f'{entry_id};{name};{surname};{phone};{address}\n')

    if entry_id is not None:
        print(f"Data added successfully with entry ID: {entry_id}")

def get_next_entry_id(file_path, lines_per_entry):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:            
            data = f.readlines()
        
        existing_entry_ids = set(int(data[i].strip().split(';')[0]) for i in range(0, len(data), lines_per_entry))
        max_entry_id = max(existing_entry_ids, default=0)
        
        next_entry_id = max_entry_id + 1

        return next_entry_id
    except FileNotFoundError:        
        return 1


def print_data():
    print("Show data from the 1st file: \n")
    with open('C:/Users/Администратор/Desktop/PythonCourse/phonebook/data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []

        for i in range(0, len(data_first), 5):
            entry_id = data_first[i].strip()
            
            if not entry_id.isdigit():
                entry_id = None

            entry_data = ''.join(data_first[i + 1:i + 5])
            data_first_list.append((entry_id, entry_data))

        for entry_id, entry in data_first_list:
            if entry_id is not None:
                print(f"\n{entry_id}:\n{entry}")

    print("\nShow data from the 2nd file: \n")
    with open('C:/Users/Администратор/Desktop/PythonCourse/phonebook/data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        data_second_list = []

        for i in range(0, len(data_second), 1):
            entry_id, *entry_data = data_second[i].strip().split(';')
            
            if not entry_id.isdigit():
                entry_id = None

            entry_data = ';'.join(entry_data)
            data_second_list.append((entry_id, entry_data))

        for entry_id, entry in data_second_list:
            if entry_id is not None:
                print(f"{entry_id}: {entry}\n")
    

def change_data():
    entry_id_to_change = input("Enter the entry ID of the record you want to change: ")
    file_choice = input("Enter 1 to change in data_first_variant.csv or 2 to change in data_second_variant.csv: ")

    if file_choice == '1':
        file_path = 'C:/Users/Администратор/Desktop/PythonCourse/phonebook/data_first_variant.csv'
        if update_entry_in_file1(file_path, entry_id_to_change):
            print("Entry updated successfully!")
        else:
            print(f"No entry found with the specified entry ID in {file_path}.")
    elif file_choice == '2':
        file_path = 'C:/Users/Администратор/Desktop/PythonCourse/phonebook/data_second_variant.csv'
        if update_entry_in_file2(file_path, entry_id_to_change):
            print("Entry updated successfully!")
        else:
            print(f"No entry found with the specified entry ID in {file_path}.")
    else:
        print("Invalid file choice.")


def update_entry_in_file1(file_path1, entry_id_to_change):    
    with open(file_path1, 'r', encoding='utf-8') as f:
        data = f.readlines()
    
    found_index = None
    for i in range(0, len(data), 5):
        entry_id = data[i].strip()
        
        if entry_id == entry_id_to_change:
            found_index = i
            break

    if found_index is not None:        
        print("Found entry to change:")
        print(data[found_index])
        
        new_name = input('Enter new name: ')
        new_surname = input('Enter new surname: ')
        new_phone = input('Enter new phone number: ')
        new_address = input('Enter new address: ')
        
        data[found_index + 1] = f'{new_name}\n'
        data[found_index + 2] = f'{new_surname}\n'
        data[found_index + 3] = f'{new_phone}\n'
        data[found_index + 4] = f'{new_address}\n'
        
        with open(file_path1, 'w', encoding='utf-8') as f:
            f.writelines(data)

        return True
    else:
        return False

def update_entry_in_file2(file_path2, entry_id_to_change):    
    with open(file_path2, 'r', encoding='utf-8') as f:
        data = f.readlines()
    
    found_index = None
    for i in range(0, len(data), 1):
        entry_id = data[i].strip().split(';')[0]
        
        if entry_id == entry_id_to_change:
            found_index = i
            break

    if found_index is not None:        
        print("Found entry to change:")
        print(data[found_index])
        
        new_name = input('Enter new name: ')
        new_surname = input('Enter new surname: ')
        new_phone = input('Enter new phone number: ')
        new_address = input('Enter new address: ')
        
        if ';' in data[found_index]:
            data[found_index:found_index + 1] = [f'{entry_id_to_change};{new_name};{new_surname};{new_phone};{new_address}\n']
        else:
            data[found_index] = f'{entry_id_to_change};{new_name};{new_surname};{new_phone};{new_address}\n'
        
        with open(file_path2, 'w', encoding='utf-8') as f:
            f.writelines(data)

        return True
    else:
        return False


def delete_data():
    file_choice = input("Enter 1 to delete from data_first_variant.csv or 2 to delete from data_second_variant.csv: ")
    entry_id_to_delete = input("Enter the entry ID of the record you want to delete: ")

    if file_choice == '1':
        file_path1 = 'C:/Users/Администратор/Desktop/PythonCourse/phonebook/data_first_variant.csv'
        delete_entry_in_file1(file_path1, entry_id_to_delete)
        print("Entry deleted successfully!")
    elif file_choice == '2':
        file_path2 = 'C:/Users/Администратор/Desktop/PythonCourse/phonebook/data_second_variant.csv'
        delete_entry_in_file2(file_path2, entry_id_to_delete)
        print("Entry deleted successfully!")
    else:
        print("Invalid file choice.")

def delete_entry_in_file1(file_path1, entry_id_to_delete):    
    with open(file_path1, 'r', encoding='utf-8') as f:
        data = f.readlines()
    
    found_index = None
    for i in range(0, len(data), 5):
        entry_id = data[i].strip()
        
        if entry_id == entry_id_to_delete:
            found_index = i
            break

    if found_index is not None:        
        del data[found_index:found_index + 5]
        
        with open(file_path1, 'w', encoding='utf-8') as f:
            f.writelines(data)        
    else:
        print(f"No entry found with the specified entry ID in {file_path1}.")


def delete_entry_in_file2(file_path2, entry_id_to_delete):    
    with open(file_path2, 'r', encoding='utf-8') as f:
        data = f.readlines()
    
    found_index = None
    for i in range(0, len(data), 1):
        entry_id = data[i].strip().split(';')[0]
        
        if entry_id == entry_id_to_delete:
            found_index = i
            break

    if found_index is not None:        
        entry_lines = data[found_index:found_index + 1]
        del data[found_index:found_index + len(entry_lines)]
        
        with open(file_path2, 'w', encoding='utf-8') as f:
            f.writelines(data)
    else:
        print(f"No entry found with the specified entry ID in {file_path2}.")













# def input_data():
#     name = name_data()
#     surname = surname_data()
#     phone = phone_data()
#     address = address_data()
#     var = int(input(f'Select format to save data: \n\n'
#     f'Version 1: \n'
#     f'{name}\n{surname}\n{phone}\n{address}\n\n'
#     f'Version 2: \n'
#     f'{name};{surname};{phone};{address}\n\n'
#     f'Select format: '))
    
#     while var !=1 and var!= 2:
#         print('Wrong entrance!')
#         var = int(input("Select format: "))

#     if var == 1:
#         with open('C:/Users/Администратор/Desktop/PythonCourse/phonebook/data_first_variant.csv', 'a', encoding='utf-8') as f:   # где a - append
#             f.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
#     elif var == 2:
#         with open('C:/Users/Администратор/Desktop/PythonCourse/phonebook/data_second_variant.csv', 'a', encoding='utf-8') as f:
#             f.write(f'{name};{surname};{phone};{address}\n\n')
        

# def print_data():
#     print("Show data from the 1st file: \n")
#     #with open('data_first_variant.csv', 'r', encoding='utf-8') as f:   # где r - read
#     with open(r'C:/Users/Администратор/Desktop/PythonCourse/phonebook/data_first_variant.csv', 'r', encoding='utf-8') as f:
#         data_first = f.readlines()
#         data_first_list = []
#         j = 0
#         for i in range(len(data_first)):
#             if data_first[i] == '\n' or i == len(data_first) - 1:
#                 data_first_list.append(''.join(data_first[j:i + 1]))
#                 j = i
#         print(''.join(data_first_list))
                
#     print("Show data from the 2nd file: \n")
#     #with open('data_second_variant.csv', 'r', encoding='utf-8') as f:   # где r - read
#     with open(r'C:/Users/Администратор/Desktop/PythonCourse/phonebook/data_second_variant.csv', 'r', encoding='utf-8') as f:
#         data_second = f.readlines()
#         print(*data_second)

# def change_data():
#     phone_to_change = input("Enter the phone number of the entry you want to change: ")

#     # Открываем файл для чтения
#     with open('C:/Users/Администратор/Desktop/PythonCourse/phonebook/data_first_variant.csv', 'r', encoding='utf-8') as f:
#         data_first = f.readlines()

#     # Ищем запись с указанным номером телефона
#     found_index = None
#     for i, entry in enumerate(data_first):
#         if phone_to_change in entry:
#             found_index = i
#             break

#     if found_index is not None:
#         # Найдено совпадение, предоставляем пользователю возможность изменить данные
#         print("Found entry to change:")
#         print(data_first[found_index])

#         # Получаем новые данные
#         new_name = name_data()
#         new_surname = surname_data()
#         new_phone = phone_data()
#         new_address = address_data()

#         # Меняем данные в списке
#         data_first[found_index] = f'{new_name}\n{new_surname}\n{new_phone}\n{new_address}\n\n'

#         # Открываем файл для записи
#         with open('C:/Users/Администратор/Desktop/PythonCourse/phonebook/data_first_variant.csv', 'w', encoding='utf-8') as f:
#             f.writelines(data_first)

#         print("Entry updated successfully!")
#     else:
#         print("No entry found with the specified phone number.")

# def delete_data():
#     data_to_delete = input("Enter the phone number of the entry you want to delete: ")

#     # Открываем файл для чтения
#     with open('C:/Users/Администратор/Desktop/PythonCourse/phonebook/data_first_variant.csv', 'r', encoding='utf-8') as f:
#         data_first = f.readlines()

#     # Ищем запись с указанным номером телефона
#     found_index = None
#     for i, entry in enumerate(data_first):
#         if data_to_delete in entry:
#             found_index = i
#             break

#     if found_index is not None:
#         # Найдено совпадение, удаляем запись из списка
#         del data_first[found_index]

#         # Открываем файл для записи
#         with open('C:/Users/Администратор/Desktop/PythonCourse/phonebook/data_first_variant.csv', 'w', encoding='utf-8') as f:
#             f.writelines(data_first)

#         print("Entry deleted successfully!")
#     else:
#         print("No entry found with the specified phone number.")

    