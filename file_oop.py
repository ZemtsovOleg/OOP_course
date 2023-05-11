''' Создайте класс  File, у которого есть:

метод __init__, который должен принимать на вход имя файла и записывать его в атрибут name. Также необходимо создать атрибуты in_trash , is_deleted  и записать в них значение False
 
метод  restore_from_trash, который печатает фразу «Файл {name} восстановлен из корзины» и проставляет атрибут in_trash в значение False
 
метод  remove, который печатает фразу «Файл {name} был удален» и проставляет атрибут is_deleted  в значение True
 
метод read, который
печатает фразу «ErrorReadFileDeleted({name})», если атрибут is_deleted истин, и выходит из метода
печатает фразу «ErrorReadFileTrashed({name})», если атрибут in_trash истин, и выходит из метода
печатает фразу «Прочитали все содержимое файла {self.name}» если файл не удален и не в корзине
метод write, который принимает значение content для записи и 
печатает фразу «ErrorWriteFileDeleted({name})», если атрибут is_deleted истин, и выходит из метода
печатает фразу «ErrorWriteFileTrashed({name})», если атрибут in_trash истин, и выходит из метода
печатает фразу «Записали значение {content} в файл {self.name}», если файл не удален и не в корзине 

С предыдущего урока у вас должен быть создан класс  File, у которого имеется:

метод __init__
метод  restore_from_trash
метод  remove
метод read
метод write
Далее создайте класс  Trash у которого есть:

атрибут класса  content изначально равный пустому списку
 
статик-метод  add, который принимает файл и сохраняет его в корзину: для этого нужно добавить его в атрибут content и проставить файлу атрибут in_trash значение True. Если в метод add передается не экземпляр класса File, необходимо вывести сообщение «В корзину добавлять можно только файл»
 
статик-метод  clear, который запускает процесс очистки файлов в корзине. Необходимо для всех файлов, хранящийся в атрибуте content , в порядке их добавления в корзину вызвать метод файла remove. Атрибут content  после очистки должен стать пустым списком. Сама процедура очистки должна начинаться фразой «Очищаем корзину» и заканчиваться фразой «Корзина пуста»
 
статик-метод  restore, который запускает процесс восстановления файлов из корзины. Необходимо для всех файлов, хранящийся в атрибуте content , в порядке их добавления в корзину вызвать метод файла restore_from_trash. Атрибут content  после очистки должен стать пустым списком. Сама процедура восстановления должна начинаться фразой «Восстанавливаем файлы из корзины» и заканчиваться фразой «Корзина пуста»'''

# Напишите определение классов File и Trash     

class File:

    def __init__(self, name) -> None:
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        print(f'Файл {self.name} восстановлен из корзины')
        self.in_trash = False

    def remove(self):
        print(f'Файл {self.name} был удален')
        self.is_deleted = True

    def read(self):
        if self.is_deleted:
            print(f'ErrorReadFileDeleted({self.name})')
        elif self.in_trash:
            print(f'ErrorReadFileTrashed({self.name})')
        else:
            print(f'Прочитали все содержимое файла {self.name}')
    
    def write(self, content):
        if self.is_deleted:
            print(f'ErrorWriteFileDeleted({self.name})')
        elif self.in_trash:
            print(f'ErrorWriteFileTrashed({self.name})')
        else:
            print(f'Записали значение {content} в файл {self.name}')

class Trash:
    content = []

    @staticmethod
    def add(file):
        if isinstance(file, File):
            Trash.content.append(file)
            file.in_trash = True
        else:
            print('В корзину добавлять можно только файл')

    @staticmethod
    def clear():
        print('Очищаем корзину')
        for file in Trash.content:
            file.remove()
        Trash.content.clear()
        print('Корзина пуста')
    
    @staticmethod
    def restore():
        print('Восстанавливаем файлы из корзины')
        for file in Trash.content:
            file.restore_from_trash()
        Trash.content.clear()
        print('Корзина пуста')


# Ниже код для проверки класса File и Trash    

f1 = File('puppies.jpg')
f2 = File('cat.jpg')
f3 = File('xxx.doc')
passwords = File('pass.txt')

for file in [f1, f2, f3, passwords]:
    assert file.is_deleted is False
    assert file.in_trash is False

f3.read()
f3.remove()
assert f3.is_deleted is True
f3.read()
f3.write('hello')

assert Trash.content == []

Trash.add(f2)
Trash.add(passwords)
Trash.add(f3)

f1.read()
Trash.add(f1)
f1.read()

for file in [f1, f2, f3, passwords]:
    assert file.in_trash is True

for f in [f2, passwords, f3, f1]:
    assert f in Trash.content

Trash.restore()
assert Trash.content == [], 'После восстановления корзина должна была очиститься'

Trash.add(passwords)
Trash.add(f2)
Trash.add('hello')
Trash.add(f1)

for f in [passwords, f2, f1]:
    assert f in Trash.content


Trash.clear()

for file in [passwords, f2, f1]:
    assert file.is_deleted is True

assert Trash.content == [], 'После удаления файлов корзина должна была очиститься'

f1.read()