'''  Создайте базовый класс Vehicle, у которого есть:

метод __init__, принимающий название транспортного средства, пробег и вместимость. Их необходимо сохранить в атрибуты экземпляра name, mileage и  capacity соответственно
 
метод fare , который возвращает стоимость проезда из расчета  capacity * 100:
 
метод display , который печатает строку следующего вида:
Total <name> fare is: <метод fare>
 

Затем создайте подкласс Bus , унаследованный от Vehicle. В нем необходимо:

переопределить метод __init__. Он должен принимать два значения: название транспортного средства и пробег. Необходимо делегировать создание атрибутов name, mileage и  capacityбазовому классу, в качестве аргумента передайте capacity  значение 50
 
переопределить метод fare . Он должен получить стоимость проезда у родительского класса и увеличить ее на 10%. 
 

После создайте подкласс Taxi , унаследованный от Vehicle. В нем необходимо:

переопределить метод __init__. Он должен принимать два значения: название транспортного средства и пробег. Необходимо делегировать создание атрибутов name, mileage и  capacityбазовому классу, в качестве аргумента передайте capacity  значение 4
 
переопределить метод fare . Он должен получить стоимость проезда у родительского класса и увеличить ее на 35%.  '''


# Напишите определение классов Vehicle Bus и Taxi

class Vehicle:

    def __init__(self, name: str, mileage: int, capacity: int) -> None:
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self) -> int:
        return self.capacity * 100

    def display(self):
        print(f'Total {self.name} fare is: {self.fare()}')


class Bus(Vehicle):

    def __init__(self, name: str, mileage: int, capacity: int = 50) -> None:
        super().__init__(name, mileage, capacity)

    def fare(self):
        return super().fare() * 1.10


class Taxi(Vehicle):

    def __init__(self, name: str, mileage: int, capacity: int = 4) -> None:
        super().__init__(name, mileage, capacity)

    def fare(self):
        return super().fare() * 1.35


# Ниже располагается код для проверки


sc = Vehicle('Scooter', 100, 2)
sc.display()

merc = Bus("Mercedes", 120000)
merc.display()

polo = Taxi("Volkswagen Polo", 15000)
polo.display()

t = Taxi('x', 111)
assert t.__dict__ == {'name': 'x', 'mileage': 111, 'capacity': 4}
t.display()
b = Bus('t', 123)
assert b.__dict__ == {'name': 't', 'mileage': 123, 'capacity': 50}
b.display()
