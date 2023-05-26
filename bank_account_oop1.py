''' Создайте класс BankAccount, который представляет банковский счет, у которого есть:

метод __init__, принимающий баланс(атрибут balance)
 
метод deposit для пополнения баланса. Если пользователь пытается внести отрицательную сумму на счет, должно возникать исключение NegativeDepositError("Нельзя пополнить счет отрицательным значением"):
 
метод withdraw для вывода денег. Если пользователь пытается снять больше денег, чем есть на счете, должно возникать исключение InsufficientFundsError("Недостаточно средств для снятия")
Исключения NegativeDepositError и InsufficientFundsError вам также необходимо создать '''

# Напишите определение класса BankAccount и исключений
# NegativeDepositError и InsufficientFundsError


class NegativeDepositError(Exception):
    def __str__(self) -> str:
        return "Нельзя пополнить счет отрицательным значением"


class InsufficientFundsError(Exception):
    def __str__(self) -> str:
        return "Недостаточно средств для снятия"


class BankAccount:

    def __init__(self, balance: int) -> None:
        self.balance = balance

    def deposit(self, value: isinstance) -> None:
        if value < 1:
            raise NegativeDepositError
        self.balance += value

    def withdraw(self, value: int):
        if value > self.balance:
            raise InsufficientFundsError
        self.balance -= value


# Ниже код для проверки

try:
    raise InsufficientFundsError("Недостаточно средств")
except Exception as e:
    if not isinstance(e, InsufficientFundsError):
        raise ValueError('Реализуйте исключение InsufficientFundsError')

try:
    raise NegativeDepositError("Внесено отрицательное значение")
except Exception as e:
    if not isinstance(e, NegativeDepositError):
        raise ValueError('Реализуйте исключение NegativeDepositError')

account = BankAccount(100)
assert account.balance == 100

account.deposit(50)
assert account.balance == 150

account.withdraw(75)
assert account.balance == 75

try:
    account.withdraw(100)
except InsufficientFundsError as e:
    print(e)  # "Недостаточно средств"

assert account.balance == 75

try:
    account.deposit(-50)
except NegativeDepositError as e:
    print(e)  # "Внесено отрицательное значение"
