''' Создайте класс Registration, который пока будет проверять только введенный логин. Под логином мы будем подразумевать почту пользователя, поэтому необходимо будет сделать некоторые проверки.

В классе Registration необходимо реализовать:

метод __init__ принимающий один аргумент логин пользователя. Метод __init__ должен сохранить переданный логин через сеттер (см пункт 3). То есть когда отработает данный код 
def __init__(self, логин):
    self.login = логин # передаем в сеттер login значение логин 
должно сработать свойство сеттер login из пункта 3 для проверки валидности переданного значения

Cвойство геттер login, которое возвращает значение self.__login;
 
Свойство сеттер login, принимает значение нового логина. Новое значение мы должны проверить на следующее:
строковое значение, если поступают другие типы данных необходимо вызвать исключение при помощи строки raise TypeError
 
логин, так как является почтой, должен содержать один символ собаки «@». В случае, если в логине отсутствует символ «@», вызываем исключение при помощи строки raise ValueError
 
логин должен содержать символ точки «.» после символа «@».В случае, если после @ нету точки, вызываем исключение при помощи строки raise ValueError
Если значение проходит проверку новое значение логина сохраняется в атрибут self.__login
'''

# Напишите определение класса Registration


class Registration:

    def __init__(self, login) -> None:
        self.login = login

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


# Ниже код для проверки класса Registration


try:
    result = Registration("fga")
except ValueError as error:
    print("Логин fga должен содержать один символ '@'")

try:
    result = Registration(1234)
except TypeError as error:
    print("Пароль должен быть строкой")

try:
    result = Registration("f@ga@")
except ValueError as error:
    print("Логин f@ga@ должен содержать только один символ '@'")

try:
    result = Registration("fg@a")
except ValueError as error:
    print("В логине fg@a должен быть символ '.' после символа '@'")

try:
    result = Registration("fg.@a")
except ValueError as error:
    print("В логине fg.@a должна быть '.' после символа '@'")

result = Registration("translate@gmail.com")
assert result.login == "translate@gmail.com"
assert result._Registration__login == "translate@gmail.com"

try:
    result.login = "asdsa12asd."
except ValueError as error:
    print("Логин asdsa12asd. должен содержать один символ '@'")

try:
    result.login = "asdsa12@asd"
except ValueError as error:
    print("asdsa12@asd должен быть символ '.' после символа '@'")

result.login = "alligator13@how.do"
assert result.login == "alligator13@how.do"
assert result._Registration__login == "alligator13@how.do"
