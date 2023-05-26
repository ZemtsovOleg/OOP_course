''' Ваша задача создать класс Customer, который содержит:

метод __init__, принимающий на вход имя пользователя и необязательный аргумент баланс его счета(по умолчанию 0). Эти значения необходимо сохранить в атрибуты name и balance ;
 
статический метод check_type , принимающий на вход одно значение. Если оно не является числом (не принадлежит классу int или float) необходимо вызывать исключение TypeError('Банк работает только с числами'). Это все, метод check_type должен только вызывать исключение в случае неправильного типа, возвращать она ничего не должна
 
метод withdraw  , принимающий на вход значение для списания. Необходимо сперва проверить переданное значение на тип при помощи метода check_type  . Если исключений не возникло, необходимо проверить что у покупателя достаточно средств на балансе. Если денег хватает, то необходимо уменьшить баланс. Если средств не хватает , нужно вызвать исключение ValueError('Сумма списания превышает баланс')
 
метод deposit  , принимающий на вход значение для зачисления на баланс. При помощи метода check_type  проверьте, что передано число. Если исключений не возникло, увеличьте значение баланса покупателя на указанную сумму '''

# Напишите определение класса Customer


class Customer:

    def __init__(self, name: str, balance: int | float = 0) -> None:
        self.name = name
        self.balance = balance

    @staticmethod
    def check_type(value: int | float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError('Банк работает только с числами')

    def withdraw(self, value: int | float) -> None:
        self.check_type(value)
        if value > self.balance:
            raise ValueError('Сумма списания превышает баланс')
        self.balance -= value

    def deposit(self, value: int | float) -> None:
        self.check_type(value)
        self.balance += value


# Ниже код для проверки класса Customer


assert Customer.check_type(
    2) is None, 'Метод check_type не должен ничего возращать'
assert Customer.check_type(
    2.5) is None, 'Метод check_type не должен ничего возращать'

for i in ['hello', [1, 2, 3], dict(), set()]:
    try:
        Customer.check_type(i)
    except TypeError as error:
        print(error)
    else:
        raise TypeError(
            f'Метод check_type должен вызывать ошибку если передать {i}')

bob = Customer('Bob Odenkirk')
assert bob.balance == 0
assert bob.name == 'Bob Odenkirk'
try:
    bob.deposit('hello')
except TypeError as error:
    print(error)
else:
    raise ValueError("Нельзя вносить на счет баланса строку")

try:
    bob.deposit([])
except TypeError as error:
    print(error)
else:
    raise ValueError("Нельзя вносить на счет баланса список")

bob.deposit(200)
assert bob.balance == 200

try:
    bob.withdraw(300)
except ValueError as e:
    print(e)
else:
    raise ValueError("Проверьте списание при превышении лимита")

bob.withdraw(150)
assert bob.balance == 50

terk = Customer('Terk', 1000)
assert terk.name == 'Terk'
assert terk.balance == 1000
terk.withdraw(999)
assert terk.balance == 1, 'Не списались деньги, проверяйте списание'
terk.withdraw(1)
assert terk.balance == 0, 'Не списались деньги, проверяйте списание'

try:
    terk.withdraw(1)
except ValueError as e:
    print(e)
else:
    raise ValueError("Проверьте списание при превышении лимита")
assert terk.balance == 0
