# ''' Создайте класс Employee, который имеет следующие методы:

# метод __init__, который устанавливает значения атрибутов name, __position, __hours_worked и __hourly_rate.

# приватный метод calculate_salary, который считает зарплату сотрудника, умножая отработанные часы на часовую оплату. Метод должен вернуть посчитанную зарплату.

#  защищенный метод _set_position, который принимает название должности и изменяет пользователю значение атрибута __position.

#  публичный метод get_position, который возвращает атрибут __position.

# публичный метод get_salary, который возвращает результат вызова приватного метода calculate_salary.

# публичный метод get_employee_details, который возвращает информацию о работнике в виде следующий строки

# "Name: {name}, Position: {position}, Salary: {salary}"

# Здесь значение salary должно рассчитываться при помощи приватного метода calculate_salary. '''

# # Напишите определение класса Employee


# class Employee:

#     def __init__(self, name, position, hours_worked, hourly_rate) -> None:
#         self.name = name
#         self.__position = position
#         self.__hours_worked = hours_worked
#         self.__hourly_rate = hourly_rate

#     def __calculate_salary(self):
#         return self.__hours_worked * self.__hourly_rate

#     def _set_position(self, position):
#         self.__position = position

#     def get_position(self):
#         return self.__position

#     def get_salary(self):
#         return self.__calculate_salary()

#     def get_employee_details(self):
#         return (f"Name: {self.name}, Position: {self.__position}, Salary: {self.__calculate_salary()}")


# # Ниже код для проверки методов класса Employee
# employee = Employee("Джеки Чан", 'manager', 20, 40)
# assert employee.name == 'Джеки Чан'
# assert employee._Employee__hours_worked == 20
# assert employee._Employee__hourly_rate == 40
# assert employee._Employee__position == 'manager'
# assert employee.get_position() == 'manager'
# assert employee.get_salary() == 800
# assert employee._Employee__calculate_salary() == 800
# assert employee.get_employee_details(
# ) == 'Name: Джеки Чан, Position: manager, Salary: 800'
# employee._set_position('Director')
# assert employee.get_employee_details(
# ) == 'Name: Джеки Чан, Position: Director, Salary: 800'

# employee_2 = Employee("Пирс Броснан", 'actor', 35, 30)
# assert employee_2._Employee__calculate_salary() == 1050
# assert employee_2.get_employee_details(
# ) == 'Name: Пирс Броснан, Position: actor, Salary: 1050'

# print('Good')


''' Создайте класс Employee, который имеет следующие методы:

метод __init__, который устанавливает значения приватных атрибутов __name  и __salary: имя работника и его зарплату
 
приватный геттер метод для атрибута __name
 
приватный геттер метод для атрибута __salary
 
приватный сеттер метод для атрибута __salary: он должен позволять сохранять в атрибут __salary только положительные числа. В остальных случаях не сохраняем переданное значение в сеттер и печатаем на экран сообщение "ErrorValue:<value>".
 
свойство title, у которого есть только геттер из пункта 2.
 
свойство reward, у которого геттером будет метод из пункта 3, а сеттером — метод из пункта 4. '''

# Напишите определение класса Employee

class Employee:

    def __init__(self, name, salary) -> None:
        self.__name = name
        self.__salary = salary

    def __get_name(self):
        return self.__name

    def __get_salary(self):
        return self.__salary

    def __set_salary(self, salary):
        if isinstance(salary, (int, float)) and salary > 0:
            self.__salary = salary
        else:
            print(f'ErrorValue:{salary}')

    title = property(fget=__get_name)
    reward = property(fget=__get_salary, fset=__set_salary)


# Ниже код для проверки методов класса Employee
employee = Employee("John Doe", 50000)
assert employee.title == "John Doe"
assert employee._Employee__name == "John Doe"
assert isinstance(employee, Employee)
assert isinstance(type(employee).title,
                  property), 'Вы не создали property title'
assert isinstance(type(employee).reward,
                  property), 'Вы не создали property reward'

assert employee.reward == 50000
employee.reward = -100  # ErrorValue:-100

employee.reward = 1.5
assert employee.reward == 1.5

employee.reward = 70000
assert employee.reward == 70000
employee.reward = 'hello'  # Печатает ErrorValue:hello
employee.reward = '777'  # Печатает ErrorValue:777
employee.reward = [1, 2]  # Печатает ErrorValue:[1, 2]
assert employee.reward == 70000
employee._Employee__set_salary(55000)
assert employee._Employee__get_salary() == 55000
