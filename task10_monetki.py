'''
10. На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное
число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.

5 -> 1 0 1 1 0
2
'''

'''
def min_flips(coins):
    # Первая сторона (решка)
    flips_heads = sum(1 for c in coins if c == 1)
    
    # Вторая сторона (герб)
    flips_tails = sum(1 for c in coins if c == 0)
    
    # Возвращаем минимальное количество переворотов
    return min(flips_heads, flips_tails)

# Пример использования
n = 5
coins = [1, 0, 1, 1, 0]
result = min_flips(coins)
print(result)
'''

'''
# Вводим количество монет
n = int(input("Введите количество монет: "))

# Вводим последовательность монет (0 - герб, 1 - решка)
coins = list(map(int, input("Введите последовательность монет (0 и 1 через пробел): ").split()))

# Первая сторона (решка)
flips_heads = sum(1 for c in coins if c == 1)

# Вторая сторона (герб)
flips_tails = sum(1 for c in coins if c == 0)

# Выводим минимальное количество переворотов
result = min(flips_heads, flips_tails)
print("Минимальное количество переворотов:", result)
'''


n = int(input("Введите количество монет: "))
coins = list(map(int, input("Введите последовательность монет (0 и 1 через пробел): ").split()))

count_zero = 0
count_one = 0

for coin in coins:
    if coin == 0:
        count_zero += 1
    else:
        count_one += 1

if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)

