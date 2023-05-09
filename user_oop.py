'''  Создайте базовый класс User, у которого есть:

метод __init__, принимающий имя пользователя и его роль. Их необходимо сохранить в атрибуты экземпляра name и role соответственно
Затем создайте класс Access , у которого есть:

приватный атрибут класса __access_list , в котором хранится список ['admin', 'developer']
 
приватный статик-метод __check_access , который принимает название роли и возвращает True, если роль находится в списке __access_list , иначе - False
 
публичный статик-метод get_access , который должен принимать экземпляр класса User и проверять есть ли доступ у данного пользователя к ресурсу при помощи метода __check_access  . Если у пользователя достаточно прав, выведите на экран сообщение
«User <name>: success», если прав недостаточно - «AccessDenied»
Если передается тип данных, отличный от экземпляр класса User, необходимо вывести сообщение:
«AccessTypeError» '''


class User:

    def __init__(self, name, role) -> None:
        self.name = name
        self.role = role


class Access:
    __access_list = ['admin', 'developer']

    @staticmethod
    def __check_access(role):
        return role in Access.__access_list

    @staticmethod
    def get_access(inst):
        if not isinstance(inst, User):
            print('AccessTypeError')
        elif Access.__check_access(inst.role):
            print(f'User {inst.name}: success')
        else:
            print('AccessDenied')


user1 = User('batya99', 'admin')
Access.get_access(user1)  # печатает "User batya99: success"

zaya = User('milaya_zaya999', 'user')
Access.get_access(zaya) # печатает AccessDenied

Access.get_access(5) # печатает AccessTypeError
