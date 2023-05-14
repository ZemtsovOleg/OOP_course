''' Создайте класс  Order, который имеет следующие методы:

метод __init__, который устанавливает значения атрибутов cart и customer: список покупок и имя покупателя
 
магический метод __add__, который описывает добавления товара в список покупок. Результатом такого сложения должен быть новый заказ, в котором все покупки берутся из старого заказа и в конец добавляется новый товар. Покупатель в заказе остается прежним
 
магический метод __radd__, который описывает добавления товара в список покупок при правостороннем сложении. Результатом такого сложения должен быть новый заказ, в котором все покупки берутся из старого заказа и в начало списка покупок добавляется новый товар. Покупатель в заказе остается прежним
 магический метод __sub__, который описывает исключение товара из списка покупок. Результатом вычитания должен быть новый заказ
 

магический метод __rsub__, который описывает исключение товара из списка покупок при правостороннем вычитании. Результатом должен быть таким же как и при __sub__ '''

# Напишите определение класса Order


class Order:

    def __init__(self, cart, customer) -> None:
        self.cart = cart
        self.customer = customer

    def __add__(self, other: str):
        return Order(self.cart + [other], self.customer)

    def __radd__(self, other: str):
        return Order([other] + self.cart, self.customer)

    def __sub__(self, other: str):
        if other in self.cart:
            self.cart.remove(other)
        return Order(self.cart, self.customer)

    def __rsub__(self, other: str):
        return self.__sub__(other)     


# Ниже код для проверки методов класса Order

order = Order(['banana', 'apple'], 'Гена Букин')

order_2 = order + 'orange'
assert order.cart == ['banana', 'apple']
assert order.customer == 'Гена Букин'
assert order_2.cart == ['banana', 'apple', 'orange']

order = 'mango' + order
assert order.cart == ['mango', 'banana', 'apple']
order = 'ice cream' + order
assert order.cart == ['ice cream', 'mango', 'banana', 'apple']

order = order - 'banana'
assert order.cart == ['ice cream', 'mango', 'apple']

order3 = order - 'banana'
assert order3.cart == ['ice cream', 'mango', 'apple']

order = order - 'mango'
assert order.cart == ['ice cream', 'apple']
order = 'lime' - order
assert order.cart == ['ice cream', 'apple']
print('Good')
