''' У нас уже имеется с предыдущего урока класс Registration. Давайте добавим в него следующее: 

в метод  __init__ добавляется еще один аргумент: пароль. Как в примере с логином, вы должны будете сохранить переданный пароль через password через сеттер  password (см пункт 3 в этом задании). Примерный код метода __init__ 
def __init__(self, логин, пароль):
    self.login = логин # передаем в сеттер login значение логин 
    self.password = пароль # передаем в сеттер password значение пароль 
Должны сработать свойства сеттер login из предыдущего задания  и сеттер password из пункта 3 для проверки валидности переданных значений

Свойство геттер password, которое возвращает значение self.__password;
Свойство сеттер password, принимает значение нового пароля. Его необходимо перед сохранением проверить на следующее:
новое значение пароля должно быть строкой(не список, словарь и т.д. ) в противном случае вызываем исключение TypeError("Пароль должен быть строкой")
 
Длина нового пароля должна быть от 5 до 11 символов, в противном случае вызывать исключение ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
 
Новый пароль должен содержать хотя бы одну цифру. Для этого создаем staticmethod is_include_digit , который проходит по всем элементам строки и проверяет наличие цифр. В случае отсутствия цифрового символа вызываем исключение: ValueError('Пароль должен содержать хотя бы одну цифру')
 
Строка password должна содержать элементы верхнего и нижнего регистра. Создаем staticmethod is_include_all_register, который с помощью цикла проверяет элемента строчки на регистр. В случае ошибки вызываем: ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
 
Строка password помимо цифр должна содержать только латинские символы. Для этого создайте staticmethod is_include_only_latin , который проверяет каждый элемент нового значения на принадлежность к латинскому алфавиту(проверка должна быть как в верхнем, так и нижнем регистре). В случае, если встретится нелатинский символ, вызвать ошибку ValueError('Пароль должен содержать только латинский алфавит'). Подсказка: из модуля string можно импортировать переменную ascii_letters, она хранит в себе все латинские символы в верхнем и нижнем регистре
 
Пароль не должен совпадать ни с одним из легких паролей, хранящихся в файле easy_passwords.txt. Сохраните данный файл к себе в папку с вашей программой и не меняйте название. С помощью staticmethod создаем метод check_password_dictionary и проверяем наличие нашего пароля в данном файле. Если значение совпадет со значением из файла, то в сеттер вызываем исключение: ValueError('Ваш пароль содержится в списке самых легких') '''

# Напишите определение класса Registration

import string
with open('easy_passwords.txt', encoding='utf-8') as f:
    easy_passwords = f.read().split()

class Registration:

    def __init__(self, login, password) -> None:
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        if not isinstance(login, str):
            raise TypeError
        if not login.count('@') == 1:
            raise ValueError
        if not login[login.index('@'):].find('.') > 0:
            raise ValueError
        else:
            self.__login = login

    @property
    def password(self):
        return self.__password

    @staticmethod
    def is_include_digit(password):
        return any(map(str.isdigit, password))

    @staticmethod
    def is_include_all_register(password):
        return any((password.islower(), password.isupper()))

    @staticmethod
    def is_include_only_latin(password):
        return all(l in string.ascii_letters for l in password)

    @staticmethod
    def check_password_dictionary(password):
        return password in easy_passwords

    @password.setter
    def password(self, password):
        if not isinstance(password, str):
            TypeError("Пароль должен быть строкой")
        if 5 > len(password) > 13:
            ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if self.is_include_digit(password):
            ValueError('Пароль должен содержать хотя бы одну цифру')
        if self.is_include_all_register(password):
            ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if self.is_include_only_latin(password):
            ValueError('Пароль должен содержать только латинский алфавит')
        if self.check_password_dictionary(password):
            ValueError('Ваш пароль содержится в списке самых легких')
        else:
            self.__password = password


# Ниже код для проверки класса Registration
try:
    s2 = Registration("fga", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError(
        "Registration('fga', 'asd12') как можно записать такой логин?")

try:
    s2 = Registration("fg@a", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError(
        "Registration('fg@a', 'asd12') как можно записать такой логин?")

s2 = Registration("translate@gmail.com", "as1SNdf")
try:
    s2.login = "asdsa12asd."
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12asd как можно записать такой логин?")

try:
    s2.login = "asdsa12@asd"
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12@asd как можно записать такой логин?")

assert Registration.check_password_dictionary(
    'QwerTy123'), 'проверка на пароль в слове не работает'

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError(
        "QwerTy123 хранится в словаре паролей, как его можно было сохранить?")


# try:
#     s2.password = "KissasSAd1f"
# except ValueError as e:
#     pass
# else:
#     raise ValueError(
#         "KissasSAd1f хранится в словаре паролей, как его можно было сохранить?")

# try:
#     s2.password = "124244242"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("124244242 пароль НЕОЧЕНЬ, как его можно было сохранить?")

# try:
#     s2.password = "RYIWUhjkdbfjfgdsffds"
# except ValueError as e:
#     pass
# else:
#     raise ValueError(
#         "RYIWUhjkdbfjfgdsffds пароль НЕОЧЕНЬ, как его можно было сохранить?")

# try:
#     s2.password = "CaT"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("CaT пароль НЕОЧЕНЬ, как его можно было сохранить?")

# try:
#     s2.password = "monkey"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("monkey пароль НЕОЧЕНЬ, как его можно было сохранить?")

# try:
#     s2.password = "QwerTy123"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("QwerTy123 пароль есть в слове, нельзя его использовать")

# try:
#     s2.password = "HelloQEWq"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("HelloQEWq пароль НЕОЧЕНЬ, как его можно было сохранить?")

# try:
#     s2.password = [4, 32]
# except TypeError as e:
#     pass
# else:
#     raise TypeError("Пароль должен быть строкой")

# try:
#     s2.password = 123456
# except TypeError as e:
#     pass
# else:
#     raise TypeError("Пароль должен быть строкой")

print('U r hacked Pentagon')
