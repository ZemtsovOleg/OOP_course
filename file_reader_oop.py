''' Ниже в коде представлена реализация класса FileReader, который должен при итерирации считывать построчно содержимое файла

Ваша задача дописать метод __next__, чтобы он возвращал по порядку строки из файла, пока содержимое файла не закончится. Строку нужно очистить слева и справа от символов пробелов и переносов на новую строку '''

class FileReader:
    def __init__(self, filename: str) -> None:
        self.index = -1
        with open(filename, encoding='utf-8') as f:
            self.file = f.readlines()

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.file):
            # self.index = -1
            raise StopIteration
        return self.file[self.index].strip()


s = FileReader('lorem.txt')

for line in s:
    print(line)

print(s.index)