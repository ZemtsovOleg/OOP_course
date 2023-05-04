''' Создайте класс Library, который имеет следующие методы:

метод __init__, который принимает список названий книг и сохраняет его в приватном атрибуте __books.
 
приватный метод check_availability, который принимает название книги и возвращает True, если книга присутствует в библиотеке, в противном случае возвращается False.
 
публичный метод search_book, который ищет книгу в библиотеке при помощи приватного метода check_availability. Возвращает True, если нашел,  иначе False.
 
публичный метод return_book, который принимает название книги, которую нужно вернуть в библиотеку (добавить в конец атрибута __books), ничего возвращать не нужно.
 
защищенный метод checkout_book, который принимает на вход название книги. Если книга имеется в наличии, ее необходимо выдать читателю и удалить из списка книг. Метод в таком случае должен вернуть True , как знак того, что операция выдачи книги прошла успешно. Если книга отсутствовала, необходимо вернуть False. '''


# Напишите определение класса Library       

class Library:

    def __init__(self, books) -> None:
        self.__books = books

    def __check_availability(self, book):
        return book in self.__books
    
    def search_book(self, book):
        return self.__check_availability(book)

    def return_book(self, book):
        self.__books.append(book)

    def _checkout_book(self, book):
        if book in self.__books:
            self.__books.remove(book)
            return True
        return False

    
    

# Ниже код для проверки методов класса Library
library = Library(["War and Peace", "Moby-Dick", "Pride and Prejudice"])

assert library._Library__books == ["War and Peace", "Moby-Dick", "Pride and Prejudice"]
assert library.search_book("Moby-Dick") == True
assert library.search_book("Jane Air") == False

assert library._Library__check_availability("War and Peace") == True
assert library._checkout_book("Moby-Dick") == True
assert library._Library__books == ["War and Peace", "Pride and Prejudice"]

assert library.search_book("Moby-Dick") == False
assert library.return_book("Moby-Dick") is None
assert library._Library__books == ["War and Peace", "Pride and Prejudice", "Moby-Dick"]
assert library.search_book("Moby-Dick") == True
print('Good')