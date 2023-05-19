import json
import functools
import sys
import os


def counter(func):
    count = 0

    def iner():
        nonlocal count
        count += 1
        print(count)
        return func()
    return iner


@counter
def test():
    return 'ok'


test()


@functools.cache
def rec(n):
    if not n:
        return 1
    return rec(n-1) * n


print(rec(5))
print()


class Cat:
    pass


print(Cat.__dict__)
print()
print(dir(Cat))

print()
print(dir())
print()
print(__file__)
print()
print(globals())


class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            value = self.current
            self.current += 1
            return value
        else:
            self.current = 0
            raise StopIteration


# Создаем объект итератора
my_iterator = MyIterator(5)

# Итерация по объекту итератора
for item in my_iterator:
    print(item)


class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.prev = 0
        self.current = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            value = self.current
            self.prev, self.current = self.current, self.prev + self.current
            self.count += 1
            return value
        else:
            self.prev = 0
            self.current = 1
            self.count = 0
            raise StopIteration


# Создаем объект итератора
fib_iterator = FibonacciIterator(10)

# Итерация по объекту итератора
for number in fib_iterator:
    print(number)

print('ok')

for number in fib_iterator:
    print(number)

print(issubclass(bool, object))

print(issubclass(bool, int))

print(type(bool))

print(type(type))

print(issubclass(bool, type))


class Person:

    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self} can walk")

    def __str__(self):
        return f"{type(self).__name__} {self.name}"


class Doctor(Person):
    pass


p = Person("Adam")
d = Doctor("Alex")
print(p)  # --> Person Adam
print(d)  # --> Doctor Alex
d.walk()  # --> Doctor Alex can walk


class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person1("John", 30)
a = json.dumps(person.__dict__)
print(type(json))
print(isinstance(a, str))
print(a)


class Phone:
    __slots__ = ['brand', 'model', '__dict__']


phone1 = Phone()
phone1.brand = 'Apple'
phone1.model = 'iPhone 14'

print(phone1.brand)
print(phone1.model)
phone1.price = 1000
print(phone1.price)

print(phone1.__dict__)


class Point:

    __slots__ = 'x', 'y'

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


s = Point(3, 4)
print(s.__sizeof__())
d = PointSlots(3, 4)
print(d.__sizeof__())

print(type(s.__slots__))


print(phone1.__slots__)


class Cat:
    shared_attr = {
        'breed': 'pers',
        'color': 'black'
    }
    age = 1

    def __init__(self, name, city):
        self.__dict__ = Cat.shared_attr
        self.name = name
        self._city = city


cat1 = Cat('Ivan', 'London')
cat2 = Cat('Vika', ' London')
cat1.weight = 5  # Добавляем параметр в ЭК
print('cat1:', cat1.__dict__)
print('cat2:', cat2.__dict__)

print(Cat.shared_attr)
print(Cat.__dict__)
print(cat1.__dict__)
print(cat1.shared_attr)
print(cat1.color)
print(cat1._city)
