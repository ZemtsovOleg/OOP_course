'''   Создайте базовый класс  Person, у которого есть:

конструктор __init__, который должен принимать на вход имя и номер паспорта и записывать их в атрибуты name, passport
 
метод display, который печатает на экран сообщение «<имя>: <паспорт>»;
Затем создайте подкласс Employee , унаследованный от Person. В нем должен быть реализован:

метод  __init__, который принимает именно в таком порядке четыре значения: имя, паспорт, зарплату и отдел. Их нужно сохранить в атрибуты  name, passport, salary,department. При этом создание атрибутов name, passportнеобходимо делегировать базовому классу Person
a = Employee('Raul', 886012, 200000, "QA")   
 
a.display() # печатает "Raul: 886012" '''


# Напишите определение классов Person и Employee

class Person:

    def __init__(self, name: str, passport: int) -> None:
        self.name = name
        self.passport = passport

    def display(self):
        print(f'{self.name}: {self.passport}')

class Employee(Person):

    def __init__(self, name: str, passport: int, salary: int, department: str) -> None:
        super().__init__(name, passport)
        self.salary = salary
        self.department = department


# Ниже располагается код для проверки

assert issubclass(Employee, Person)

emp = Person("just human", 123456)
emp.display()
assert emp.__dict__ == {'name': 'just human', 'passport': 123456}

emp2 = Employee("Geek2", 534432, 321321, 'Roga & Koputa')
emp2.display()
assert emp2.__dict__ == {'salary': 321321, 'department': 'Roga & Koputa',
                         'name': 'Geek2', 'passport': 534432}