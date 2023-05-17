''' Давайте представим, что в 2020 году в Москве проводили опрос и выявили, к какому классу люди себя относят. По результатам опроса все люди разделились на сладкоежек, вегетарианцев и любителей мяса. Давайте напишем программу, которая поможет нам подвести итоги опроса. Для создания программы нужно:

1. Создать родительский класс Initialization, который состоит из:

 метода инициализации, в который поступают аргументы: capacity - целое число, food - список из строковых названий еды. Если в значение capacity  передается не целое число, вывести надпись ‘Количество людей должно быть целым числом’ и не создавать для таких экземпляров атрибуты capacity и food.
2. Создать дочерний класс Vegetarian от класса Initialization, который состоит из: 

метода инициализации, принимающего аргументы capacity, food. Нужно создать одноименные атрибуты через вызов родительского метода __init__.
 
метода __str__, который возвращает строку формата "<capacity> людей предпочитают не есть мясо! Они предпочитают <food>"
3. Создать дочерний класс MeatEater от класса Initialization, который состоит из: 

метода инициализации, принимающего аргументы capacity, food. Нужно создать одноименные атрибуты через вызов родительского метода __init__.
 
метода __str__, который возвращает строку формата "<capacity> мясоедов в Москве! Помимо мяса они едят еще и <food>"
4. Создать дочерний класс SweetTooth от класса Initialization, который состоит из: 

метода инициализации, принимающего аргументы capacity, food. Нужно создать одноименные атрибуты через вызов родительского метода __init__.
 
магического метода __str__, который возвращает строку формата ‘Сладкоежек в Москве <capacity>. Их самая любимая еда: <food>’; 
 
магического  метода __eq__, который будет позволять сравнивать экземпляры класса SweetTooth  с числами и другими нашими классами. Если сравнение происходит с целым числом и атрибут capacity с ним совпадает, то необходимо вернуть True, в противном случае - False. Если же сравнение идет с другим нашим классом(Vegetarian или MeatEater) и значения атрибутов capacity равны, то возвращается True, в противном случае - False. А если же сравнивается с другим типом данных, верните ‘Невозможно сравнить количество сладкоежек с <значение>’;
 
магического  метода __lt__. Если сравнение происходит с целым числом и количество сладкоежек (атрибут capacity) меньше, необходимо вернуть True, в противном случае - False. Если сравнение происходит с экземпляром одного из наших классов Vegetarian или MeatEater и сладкоежек меньше, то верните True, в противном случае верните False. В случае если сравнение идет с остальными типами данных, верните ‘Невозможно сравнить количество сладкоежек с <значение>’
 
магического  метода __gt__. Если сравнение происходит с целым числом и количество сладкоежек больше, необходимо вернуть значение True, в противном же случае - False. Если сравнение происходит с другим нашим классом Vegetarian или MeatEater и сладкоежек больше, то верните True, в противном случае - False. В случае если сравнение идет с остальными типами данных, верните ‘Невозможно сравнить количество сладкоежек с <значение>’ '''


# Напишите определение классов Initialization Vegetarian MeatEater и SweetTooth


import functools


@functools.total_ordering
class Initialization:

    def __init__(self, capacity: int, food: list) -> None:
        if isinstance(capacity, int):
            self.capacity = capacity
            self.food = food
        else:
            print('Количество людей должно быть целым числом')

    def __eq__(self, other: object) -> bool | str:
        if isinstance(other, (Initialization)):
            return self.capacity == other.capacity
        if isinstance(other, int):
            return self.capacity == other
        return f'Невозможно сравнить количество сладкоежек с {other}'

    def __lt__(self, other: object) -> bool | str:
        if isinstance(other, (Initialization)):
            return self.capacity < other.capacity
        if isinstance(other, int):
            return self.capacity < other
        return f'Невозможно сравнить количество сладкоежек с {other}'


class Vegetarian(Initialization):

    def __str__(self) -> str:
        return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'


class MeatEater(Initialization):

    def __str__(self) -> str:
        return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'


class SweetTooth(Initialization):

    def __str__(self) -> str:
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'


# Ниже располагается код для проверки
p1 = Initialization('Chuck', [])
assert isinstance(p1, Initialization)
assert not hasattr(
    p1, 'capacity'), 'Не нужно создавать атрибут "capacity", если передается не целое число'
assert not hasattr(
    p1, 'food'), 'Не нужно создавать атрибут "food", если передается не целое число'

c1 = Vegetarian(100, [1, 2, 3])
print(c1)
assert isinstance(c1, Vegetarian)
assert c1.capacity == 100
assert c1.food == [1, 2, 3]

b1 = MeatEater(1000, ['Arkasha'])
print(b1)
assert isinstance(b1, MeatEater)
assert b1.capacity == 1000
assert b1.food == ['Arkasha']

pla = SweetTooth(444, [2150, 777])
print(pla)
assert isinstance(pla, SweetTooth)
assert pla.capacity == 444
assert pla.food == [2150, 777]
assert pla > 100
assert not pla < 80
assert not pla == 90
assert pla > c1
assert not pla < c1
assert not pla == c1
assert not pla > b1
assert pla < b1
assert not pla == b1

v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
# 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
print(v_first)
# Количество людей должно быть целым числом
v_second = Vegetarian([23], ['nothing'])

m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
# 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
print(m_first)
s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
# Сладкоежек в Москве 30000. Их самая любимя еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
print(s_first)
# Сладкоежек больше, чем людей с другим вкусовым предпочтением
print(s_first > v_first)
# Количество сладкоежек из опрошенных людей совпадает с 30000
print(30000 == s_first)
print(s_first == 25000)  # Количество людей не совпадает
print(100000 < s_first)  # Количество сладкоежек в Москве не больше, чем 100000
print(100 < s_first)  # Количество сладкоежек больше, чем 100
