''' Нам необходимо создать класс Building. Мы должны научиться создавать здание определенной этажности и уметь бронировать за компанией определенный этаж в здании. Важно, что в нашем классе за одним этажом может быть закреплена только одна компания

Для этого в классе Building должно быть реализованы

метод __init__, который принимает количество этажей в здании
метод __setitem__, который закрепляет за определенным этажом компанию. Если этаж был занят другой компанией, нужно заменить название другой компанией
метод __getitem__, который возвращает название компании с этого этажа. В случае, если этаж пустует, следует вернуть None
метод __delitem__, который высвобождает этаж
В этом задании вы сами решаете какие атрибуты создавать внутри класса, главное реализовать магические методы из списка выше '''


class Building:

    def __init__(self, house: int) -> None:
        self.house = [None] * house

    def __setitem__(self, item: int, value: str) -> None:
        self.house[item] = value

    def __getitem__(self, item: int) -> str:
        return self.house[item]

    def __delitem__(self, item: int) -> None:
        self.house[item] = None


iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])
