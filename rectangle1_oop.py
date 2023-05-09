''' Создайте класс Rectangle, у которого есть:

конструктор __init__, принимающий 2 аргумента: длину и ширину. 
свойство area, которое возвращает площадь прямоугольника;

r1 = Rectangle(3, 5)
r2 = Rectangle(6, 1)

print(r1.area) # 15
print(r2.area) # 6 '''

# Напишите определение класса Rectangle       

class Rectangle:

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.length * self.width
        return self.__area

# Ниже код для проверки методов класса Rectangle

r1 = Rectangle(5, 10)
assert isinstance(r1, Rectangle)
assert r1.area == 50
assert isinstance(type(r1).area, property), 'Вы не создали property area'

r2 = Rectangle(15, 3)
assert isinstance(r2, Rectangle)
assert r2.area == 45
assert isinstance(type(r2).area, property), 'Вы не создали property area'

r3 = Rectangle(43, 232)
assert r3.area == 9976        
print('Good')