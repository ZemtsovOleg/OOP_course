''' Давайте определим магические методы __str__ и __repr__ для класса GroceryItem, представляющего продуктовый товар:

Создайте класс GroceryItem, который имеет следующие методы:

метод __init__, который устанавливает значения атрибутов name, price и quantity: название товара, его цену и количество
 
магический метод __str__, который возвращает строковое представление товара в следующем виде:
Name: {name}
Price: {price}
Quantity: {quantity}
 

магический метод __repr__, который возвращает однозначное строковое представление объекта
GroceryItem({name}, {price}, {quantity}) '''

# Напишите определение класса GroceryItem       

class GroceryItem:

    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f'Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}'
    
    def __repr__(self) -> str:
        return f'GroceryItem({self.name}, {self.price}, {self.quantity})'

# Ниже код для проверки методов класса GroceryItem
banana = GroceryItem('Banana', 10, 5)
assert banana.__str__() == """Name: Banana
Price: 10
Quantity: 5"""
assert repr(banana) == 'GroceryItem(Banana, 10, 5)'
print(banana)
print(f"{banana!r}")

dragon_fruit = GroceryItem('Dragon fruit', 5, 350)
assert dragon_fruit.__str__() == """Name: Dragon fruit
Price: 5
Quantity: 350"""
assert repr(dragon_fruit) == 'GroceryItem(Dragon fruit, 5, 350)'
print(dragon_fruit)
print(f"{dragon_fruit!r}")