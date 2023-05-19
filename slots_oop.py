''' Создайте класс с именем Person , экземпляры которого имеют следующие атрибуты:

first_name хранит имя человека в виде строки;
 
last_name строка, хранит фамилию человека в виде строки;
 
age хранит возраст человека в виде целого числа.
Переопределите также метод __str__ так, чтобы он возвращал строку

{Имя} {Фамилия} is {Возраст} years old
Используйте атрибут __slots__ для указания атрибутов, чтобы каждый экземпляр класса использовал только память, необходимую для хранения перечисленных атрибутов.  '''


class Person:

    __slots__ = ('first_name', 'last_name', 'age')

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} is {self.age} years old'


# Код ниже не удаляйте, он нужен для проверок
arshavin = Person("Andrew", "Arshavin", 35)
assert arshavin.first_name == 'Andrew'
assert arshavin.last_name == 'Arshavin'
assert arshavin.age == 35
print(arshavin)

mg = Person("Max", "Galkin", 44)
assert mg.first_name == 'Max'
assert mg.last_name == 'Galkin'
assert mg.age == 44
print(mg)

try:
    arshavin.city = 'SPB'
except AttributeError:
    print('Нельзя создавать новые атрибуты')
