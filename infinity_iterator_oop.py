''' Создайте класс InfinityIterator, который реализует бесконечный итератор, который будет при каждой новой итерации или вызовы функции next будет возвращать число, увеличенное на 10 от предыдущего значения. Начинать нужно с нуля. '''


class InfinityIterator:

    def __init__(self) -> None:
        self.n = -10

    def __iter__(self):
        return self

    def __next__(self):
        self.n += 10
        return self.n


a = iter(InfinityIterator())

print(next(a))
print(next(a))
print(next(a))
