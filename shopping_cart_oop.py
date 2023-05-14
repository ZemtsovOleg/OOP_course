''' В этой задаче мы создадим аналог корзины покупок и для этого нам понадобиться реализовать класс ShoppingCart. В нем 

должно содержаться следующее:

метод __init__. , который создает в экземпляре атрибут items. Изначально должен быть пустым словарем, в нем будут содержаться покупки;
 
метод __getitem__ , который возвращает по названию товара его текущее количество или 0, если товар отсутствует в корзине 
 
метод __setitem__ , который проставляет по названию товара его количество в корзине. Если товар отсутствовал, его необходимо добавить, если присутствовал - нужно проставить ему новое количество
 
метод __delitem__ , который удаляет товар из корзины
 
метод add_item, который добавляет товар к текущим. Это значит, что если товар уже присутствовал в корзине, то необходимо увеличить его количество. Если товар отсутствовал, нужно его добавить. Данный метод принимает обязательно название товара и необязательно его количество (по умолчанию количество равно 1).
 
 метод remove_item, который удаляет некоторое количество товара из корзины. Если хотят удалить из корзины столько же товара, чем там имеется или больше, необходимо удалить его из корзины.  В остальных случаях уменьшаем количество товара на переденное количество. Данный метод принимает обязательно название товара и необязательно его количество (по умолчанию количество равно 1). Предусмотрите ситуацию, когда удаляемый товар отсутствует в корзине '''

# Напишите определение класса ShoppingCart


class ShoppingCart:

    def __init__(self) -> None:
        self.items = {}

    def __getitem__(self, item: str) -> int:
        return self.items.get(item, 0)

    def __setitem__(self, item: str, value: int) -> None:
        self.items[item] = value

    def __delitem__(self, item: str) -> None:
        self.items.pop(item)

    def add_item(self, item: str, value: int = 1) -> None:
        self.items[item] = self.items.get(item, 0) + value

    def remove_item(self, item: str, value: int = 1) -> None:
        if self.items.get(item, 0) > value:
            self.items[item] = self.items.get(item, 0) - value
        else:
            self.items.pop(item, None)


# Ниже код для проверки методов класса ShoppingCart
# Create a new shopping cart
cart = ShoppingCart()

# Add some items to the cart
cart.add_item('Apple', 3)
cart.add_item('Banana', 2)
cart.add_item('Orange')

assert cart['Banana'] == 2
assert cart['Orange'] == 1
assert cart['Kivi'] == 0

cart.add_item('Orange', 9)
assert cart['Orange'] == 10

print("Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")

cart['Apple'] = 5
cart['Banana'] = 7
cart['Kivi'] = 11
assert cart['Apple'] == 5
assert cart['Banana'] == 7
assert cart['Kivi'] == 11

print("Updated Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")

# Remove an item from the cart
cart.remove_item('Banana')
assert cart['Banana'] == 6

cart.remove_item('Apple', 4)
assert cart['Apple'] == 1

cart.remove_item('Apple', 2)
assert cart['Apple'] == 0
assert 'Apple' not in cart.items

cart.remove_item('Potato')

del cart['Banana']
assert cart['Banana'] == 0
assert 'Banana' not in cart.items

print("Updated Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")
