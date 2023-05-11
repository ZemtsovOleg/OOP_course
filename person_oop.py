''' Создайте класс Person, у которого есть:

конструктор __init__, принимающий 3 аргумента: name, surname, gender. Атрибут gender может принимать только 2 значения: "male" и "female", по умолчанию "male". Если в атрибут gender передается любое другое значение, печатать сообщение: "Не знаю, что вы имели ввиду? Пусть это будет мальчик!" и проставить атрибут gender значением "male"
 
переопределить метод __str__ следующим образом: 
если объект - мужчина (атрибут gender = "male"), возвращать строку "Гражданин <Фамилия> <Имя>"
если объект - женщина (атрибут gender = "female"), возвращать строку "Гражданка <Фамилия> <Имя>" '''


# Напишите определение класса Person

class Person:

    def __init__(self, name: str, surname: str, gender: str = 'male') -> None:
        self.name = name
        self.surname = surname
        if gender in ('male', 'female'):
            self.gender = gender
        else:
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
            self.gender = 'male'
            

    def __str__(self) -> str:
        return f"{('Гражданин', 'Гражданка')[self.gender == 'female']} {self.surname} {self.name}"


# Ниже код для проверки методов класса Person
p1 = Person('Chuck', 'Norris')
assert p1.name == 'Chuck'
assert p1.surname == 'Norris'
assert p1.gender == 'male'
assert isinstance(p1, Person)
assert str(p1) == 'Гражданин Norris Chuck'

# нужно распечатать предупреждение из условия
p2 = Person('Оби-Ван', 'Кеноби', True)
assert str(p2) == 'Гражданин Кеноби Оби-Ван'
assert p2.__dict__ == {'name': 'Оби-Ван',
                       'surname': 'Кеноби', 'gender': 'male'}
assert isinstance(p2, Person)

p3 = Person('Mila', 'Kunis', 'female')
assert isinstance(p3, Person)
assert str(p3) == 'Гражданка Kunis Mila'

print(p1)
print(p2)
print(p3)