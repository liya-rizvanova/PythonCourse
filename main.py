print(5)

# Напишем программу, которая находит все делители числа, введенного пользователем.

# Получаем данные от пользователя
user_number = int(input("Введите число: "))

# Инициализируем список для хранения делителей
divisors = []

# Ищем делители
for i in range(1, user_number + 1):
    if user_number % i == 0:
        divisors.append(i)

# Выводим результат
print(f"Делители числа {user_number}: {divisors}")
