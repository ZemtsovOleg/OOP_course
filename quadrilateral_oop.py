''' Сейчас вам нужно создать класс Quadrilateral(четырехугольник), в котором есть:

метод __init__. Он должен сохранять в экземпляр класса два атрибута: width и height. При этом в сам метод __init__ может передаваться один аргумент(тогда в width и height присваивать это одно одинаковое значение, тем самым делать квадрат), либо два аргумента( первый идет в атрибут width, второй - в height)
 
метод __str__ , который работает следующим образом: 
если width и height одинаковые, возвращать строку «Квадрат размером <width>х<height>»
в противном случае, возвращать строку «Прямоугольник размером <width>х<height>»
переопределить метод __bool__ так, чтобы он возвращал True, если объект является квадратом, и False в противном случае '''


# Напишите определение класса Quadrilateral

class Quadrilateral:
    def __init__(self, width: int, height: int = None) -> None:
        self.width = width
        self.height = height or width

    def __str__(self) -> str:
        return f"{('Прямоугольник', 'Квадрат')[bool(self)]} размером {self.width}х{self.height}"

    def __bool__(self) -> bool:
        return self.width == self.height


# Ниже код для проверки методов класса Quadrilateral

q1 = Quadrilateral(10)
print(q1)
assert q1.height == 10
assert q1.width == 10
assert bool(q1) is True
assert q1.__str__() == "Квадрат размером 10х10"
assert isinstance(q1, Quadrilateral)

q2 = Quadrilateral(3, 5)
print(q2)
assert q2.__str__() == "Прямоугольник размером 3х5"
assert bool(q2) is not True
assert isinstance(q2, Quadrilateral)

q3 = Quadrilateral(4, 7)
print(q3)
assert bool(q3) is False
assert q3.__str__() == "Прямоугольник размером 4х7"
assert isinstance(q3, Quadrilateral)
