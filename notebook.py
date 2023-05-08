''' Создайте класс Notebook, у которого есть:

конструктор __init__, принимающий список записей, в нем могут находиться любые значения. Необходимо сохранить его в защищенном атрибуте ._notes
свойство notes_list, которое распечатает содержимое атрибута ._notes в виде упорядоченного списка (см. пример ниже)
note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list
После этого на экране вы должны увидеть:

1.Buy Potato
2.Buy Carrot
3.Wash car 

'''


class Notebook:

    def __init__(self, notes) -> None:
        self._notes = notes

    @property
    def notes_list(self):
        for i, k in enumerate(self._notes, 1):
            print(i, k, sep='.')


note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list
