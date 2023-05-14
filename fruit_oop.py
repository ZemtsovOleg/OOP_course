''' Создайте класс  Fruit, который имеет:

метод __init__, который устанавливает значения атрибутов name и price: название и цена фрукта
 
методы сравнения. Здесь вы сами решаете какие магические методы реализовывать, главное чтобы фрукты могли сравниваться с числами и другими фруктами по цене. Смотрите тесты ниже в коде '''

# Напишите определение класса Fruit

import functools
''' Примечание Хотя этот декоратор позволяет легко создавать полностью упорядоченные типы с хорошим поведением, он достигается за счет более медленного выполнения и более сложных трассировок стека для производных методов сравнения. Если бенчмаркинг производительности показывает, что это является узким местом для данного приложения, вместо этого реализация всех шести расширенных методов сравнения, вероятно, обеспечит легкое повышение скорости. '''


@functools.total_ordering
class Fruit:

    def __init__(self, name: str, price: int | float) -> None:
        self.name = name
        self.price = price

    # @staticmethod
    # def check_value(value):
    #     if type(value) == int or isinstance(value, float):
    #         return value
    #     elif isinstance(value, Fruit):
    #         return value.price

    def __eq__(self, other) -> bool:
        if isinstance(other, Fruit):
            return self.price == other.price
        if isinstance(other, (int, float)):
            return self.price == other

        # return self.price == (other.price if isinstance(other, Fruit) else other)

    def __lt__(self, other) -> bool:
        if isinstance(other, Fruit):
            return self.price < other.price
        if isinstance(other, (int, float)):
            return self.price < other

        # return self.price < (other.price if isinstance(other, Fruit) else other)


# Ниже код для проверки методов класса Fruit

apple = Fruit("Apple", 0.5)
orange = Fruit("Orange", 1)
banana = Fruit("Banana", 1.6)
lime = Fruit("Lime", 1.0)

assert (banana > 1.2) is True
assert (banana >= 1.2) is True
assert (banana == 1.2) is False
assert (banana != 1.2) is True
assert (banana < 1.2) is False
assert (banana <= 1.2) is False

assert (apple > orange) is False
assert (apple >= orange) is False
assert (apple == orange) is False
assert (apple != orange) is True
assert (apple < orange) is True
assert (apple <= orange) is True

assert (orange == lime) is True
assert (orange != lime) is False
assert (orange > lime) is False
assert (orange < lime) is False
assert (orange <= lime) is True
assert (orange >= lime) is True
print('Good')
