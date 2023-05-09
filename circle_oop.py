class Circle:

    def __init__(self, radius):
        if not Circle.is_positive(radius):
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter: int):
        return cls(diameter / 2)

    @staticmethod
    def is_positive(n: int) -> bool:
        return n > 0

    @staticmethod
    def area(radius) -> float:
        return 3.14 * radius ** 2


# код ниже не нужно удалять, в нем находятся проверки
circle_1 = Circle.from_diameter(10)
assert isinstance(circle_1, Circle)
assert circle_1.radius == 5.0
print(f"circle_1.radius={circle_1.radius}")
assert Circle.is_positive(10)
assert not Circle.is_positive(-5)
assert Circle.area(1) == 3.14
assert Circle.area(2) == 12.56

print(Circle.__dict__)
print(circle_1.__dict__)
print(Circle.area(1))