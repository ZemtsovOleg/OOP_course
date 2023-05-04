'''
Оба метода используют шаблон проектирования Singleton, который позволяет создать только один экземпляр класса. Отличия между методами заключаются в том, как сохраняется состояние объекта.

В методе Person.__init__, для сохранения состояния объекта используется классовый словарь _shared_state. При создании нового экземпляра класса Person, его словарь __dict__ перенаправляется на классовый словарь _shared_state, который содержит данные предыдущих экземпляров класса. Это означает, что все экземпляры класса Person совместно используют один и тот же словарь _shared_state.

В методе Cat.__init__, для сохранения состояния объекта используется атрибут класса __shared_attr. При создании нового экземпляра класса Cat, его словарь __dict__ перенаправляется на атрибут класса __shared_attr, который также содержит данные предыдущих экземпляров класса. Однако, в отличие от метода Person.__init__, Cat.__shared_attr объявлен как атрибут класса, а не как классовый словарь. Это означает, что он может быть наследован подклассами и изменен, что может привести к ошибкам в работе программы.

Таким образом, в целом метод Person.__init__ более надежен и безопасен для использования, так как не подвержен ошибкам при наследовании.
'''


class Person:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Cat:
    __shared_attr = {}

    def __init__(self):
        self.__dict__ = Cat.__shared_attr


bob = Person()
bob.name = 'Bob'

print(bob.name)

ivan = Person()
ivan.name = 'Ivan'

print('Bob name =', bob.name)
print(bob.__dict__)


oliver = Cat()
oliver.name = 'Oliver'

print(oliver.name)

leo = Cat()
leo.name = 'Leo'

print('Leo name =', leo.name)
print(leo.__dict__)



class CustomLabel:

    def __init__(self, text: str, **kwargs) -> None:
        self.text = text
        self.config(**kwargs)

    def config(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    # или можно так
    def config(self, **kwargs):
        self.__dict__.update(**kwargs)
