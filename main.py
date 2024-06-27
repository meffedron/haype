# Функция для проверки, являются ли строки анаграммами
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Запрос ввода от пользователя
user_str1 = input("Введите первую строку: ")
user_str2 = input("Введите вторую строку: ")

# Вызов функции и вывод результата
if are_anagrams(user_str1, user_str2):
    print("Строки являются анаграммами.")
else:
    print("Строки не являются анаграммами.")