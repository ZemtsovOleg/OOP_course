''' Создайте класс Student, у которого есть:

конструктор __init__, который принимает 3 аргумента и создает приватные атрибуты __name, __age, __branch;
 
приватный метод __display_details , который выводит на экран информацию о студенте в следующем виде:
Имя: <name>
Возраст: <age>
Направление: <branch>
метод access_private_method, который вызывает приватный метод __display_details.
Пример использования кода:

obj = Student("Adam Smith", 25, "Information Technology")
obj.access_private_method()

#Output
Имя: Adam Smith
Возраст: 25
Направление: Information Technology '''


class Student:

    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print(
            f'Имя: {self.__name}\nВозраст: {self.__age}\nНаправление: {self.__branch}')

    def access_private_method(self):
        self.__display_details()


obj = Student("Adam Smith", 25, "Information Technology")
obj.access_private_method()
