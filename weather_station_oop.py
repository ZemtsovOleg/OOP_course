class Person:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

bob = Person()
bob.name = 'Bob'

print(bob.name)

ivan = Person()
ivan.name = 'Ivan'

print('Bob name =', bob.name)