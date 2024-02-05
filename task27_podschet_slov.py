'''
27. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.

Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells

Output: 13
'''


# stroka = input().split()

# set_1 = set()

# for i in stroka:
#     set_1.add(i.lower())

# print(len(set_1))



# def count_unique_words(text):
#     words = text.split()
#     unique_words = set(words)
#     return len(unique_words)

# # Пример использования
# user_text = input("Введите текст: ")
# result = count_unique_words(user_text)
# print(f"Количество различных слов: {result}")



# def count_unique_words(text):
#     words = text.split()
#     unique_words = set()
#     for word in words:
#         # Убираем лишние символы вокруг слова (знаки препинания и т. д.)
#         clean_word = ''.join(c for c in word if c.isalnum())
#         if clean_word:
#             unique_words.add(clean_word.lower())
#     return len(unique_words)

# # Пример использования
# user_text = """She sells sea shells on the sea shore
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore
# I'm sure that the shells are sea shore shells"""
# result = count_unique_words(user_text)



text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure "\
"So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".lower()
words = text.split()
print(words)
uniq_words = set(words)
print(uniq_words)
result = len(uniq_words)
print(result)