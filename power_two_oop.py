''' Создайте класс PowerTwo, который возвращает следующую степень двойки, начиная с нулевой степени (20=1). Внутри класса реализуйте:

метод __init__. Он должен принимать одно положительное число - степень двойки, до которой нужно итеририроваться включительно (см пример ниже)
 
методы __iter__ и __next__ для итерирования по степеням двойки '''

# Напишите определение класса PowerTwo


class PowerTwo:

    def __init__(self, n: int) -> None:
        self.n = n
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.index:
            self.index += 1
            return 2 ** self.index
        raise StopIteration


# Ниже код для проверки методов класса PowerTwo

numbers = PowerTwo(2)

assert hasattr(numbers, '__next__') is True
assert hasattr(numbers, '__iter__') is True

iterator = iter(numbers)
print('Элементы итератора PowerTwo(2)')
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
    raise ValueError('Не реализовали StopIteration')
except StopIteration:
    pass

print('-' * 15)
print('Элементы итератора PowerTwo(20)')
for i in PowerTwo(20):
    print(i)
