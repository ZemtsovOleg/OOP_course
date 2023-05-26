''' Напишите функцию sum_numbers, которая принимает один аргумент numbers. Это должен быть список, состоящий из целых и вещественных чисел. Функция sum_numbers должна возвращать сумму всех элементов списка, но прежде чем находить сумму необходимо выполнить следующие проверки:

Аргумент numbers должен быть именно списком, если передан другой тип, необходимо выкинуть исключение TypeError('Аргумент numbers должен быть списком')
 
numbers не должен быть пустым, иначе возбуждаем исключение ValueError("Пустой список")
 
внутри numbers должны быть только типы int и float, иначе возбуждаем исключение TypeError('Неправильный тип элемента') '''

# Напишите определение функциии sum_numbers


def sum_numbers(numbers: list[int, float]) -> int | float:
    if not isinstance(numbers, list):
        raise TypeError('Аргумент numbers должен быть списком')
    if not numbers:
        raise ValueError("Пустой список")
    try:
        return sum(numbers)
    except TypeError:
        raise TypeError('Неправильный тип элемента')


# Ниже код для проверки функциии sum_numbers
for value in (True, (1, 2, 3), {1: 'hello'}, {1, 2, 3}):
    try:
        result = sum_numbers(value)
    except TypeError as error:
        print(error)

try:
    result = sum_numbers([])
except ValueError as error:
    print(error)

try:
    sum_numbers([1, 'hello', 2, 3])
except TypeError as error:
    print(error)

try:
    sum_numbers([1, 2, 3, 4, 5, [1, 2, 3]])
except TypeError as error:
    print(error)

try:
    sum_numbers([1, 2, 3, 4, 5, {1, 2, 3}])
except TypeError as error:
    print(error)

try:
    sum_numbers([1, 2, 3, 4, 5, (1, 2, 3)])
except TypeError as error:
    print(error)

assert sum_numbers([1, 2, 3, 4, 5]) == 15
assert sum_numbers([1, 2, 3, 4, 5.0]) == 15.0
