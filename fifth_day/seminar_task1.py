"""Задание №1
✔ Пользователь вводит строку из четырёх
или более целых чисел, разделённых символом “/”.
Сформируйте словарь, где:
✔второе и третье число являются ключами.
✔первое число является значением для первого ключа.
✔четвертое и все возможные последующие числа
 хранятся в кортеже как значения второго ключа.
"""

def create_dict(str_):
    first_value, first_key, second_key, *second_value = str_
    return {first_key:first_value, second_key:second_value}
# str_ = "1/23/4/5/6/7".split("/")

str_ = input("ВВедите числ через слэш: ")
str_ = str_.split("/")
print(create_dict(str_))