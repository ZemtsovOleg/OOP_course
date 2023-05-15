''' Создайте класс Countdown, который должен принимать начальное значение и вести обратный отсчет до нуля, возвращая каждое значение в последовательности каждый раз, когда вызывается __next__. Когда обратный отсчет достигает нуля, итератор должен вызвать исключение StopIteration. Для этого вам понадобиться реализовать:

метод __init__. Он должен принимать одно положительное число - начало отсчета
 
методы __iter__ и __next__ для итерирования по значениям класса Countdown.  '''


# Напишите определение класса Countdown

class Countdown:

    def __init__(self, n: int) -> None:
        self.n = n + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n:
            self.n -= 1
            return self.n
        raise StopIteration


# Ниже код для проверки методов класса Countdown

count = Countdown(2)

assert hasattr(count, '__next__') is True
assert hasattr(count, '__iter__') is True

iterator = iter(count)
assert next(iterator) == 2
assert next(iterator) == 1
assert next(iterator) == 0
try:
    print(next(iterator))
    raise ValueError('Не реализовали StopIteration')
except StopIteration:
    pass

print('Элементы итератора Countdown(7)')
for i in Countdown(7):
    print(i)

print('-' * 10)
print('Элементы итератора Countdown(10)')
for i in Countdown(10):
    print(i)
