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
