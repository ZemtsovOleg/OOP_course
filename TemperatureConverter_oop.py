''' Создайте класс TemperatureConverter, который имеет следующие методы:

 статический метод celsius_to_fahrenheit, который принимает температуру в градусах Цельсия и переводит ее в градусы по Фаренгейту, используя следующую формулу: 


статический метод fahrenheit_to_celsius, который принимает температуру в градусах по Фаренгейту и переводит ее в градусы по Цельсия, используя следующую формулу: 


Во всех этих формулах буква С обозначает градусы по цельсию, а буква F - градусы по Фаренгейту '''

# Напишите определение класса TemperatureConverter


class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * (9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * (5 / 9)


# Ниже код для проверки методов класса TemperatureConverter
assert TemperatureConverter.celsius_to_fahrenheit(0) == 32.0
assert TemperatureConverter.celsius_to_fahrenheit(10) == 50.0
assert TemperatureConverter.celsius_to_fahrenheit(15) == 59.0
assert TemperatureConverter.celsius_to_fahrenheit(20) == 68.0
assert TemperatureConverter.celsius_to_fahrenheit(25) == 77.0
assert TemperatureConverter.celsius_to_fahrenheit(30) == 86.0

assert TemperatureConverter.fahrenheit_to_celsius(86) == 30.0
assert TemperatureConverter.fahrenheit_to_celsius(77) == 25.0
assert TemperatureConverter.fahrenheit_to_celsius(68) == 20.0
assert TemperatureConverter.fahrenheit_to_celsius(59) == 15.0
assert TemperatureConverter.fahrenheit_to_celsius(50) == 10.0
assert TemperatureConverter.fahrenheit_to_celsius(32) == 0
print('Good')
