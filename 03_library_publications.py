class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self._author = author
        self._year = year
        
    def get_info(self):
        return f'"{self.title}" ({self._author}, {self._year})'


class Book(Publication):
    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn
        
    def get_info(self):
        return f'"{self.title}" ({self._author}, {self._year}), ISBN: {self.isbn}'
    

class Magazine(Publication):
    def __init__(self, title, editor, year, issue_number):
        super().__init__(title, editor, year)
        self.editor = editor
        self.issue_number = issue_number
        
    def get_info(self):
        return f'"{self.title}" (Ред. {self.editor}, {self._year}), Выпуск №{self.issue_number}'


if __name__ == '__main__':
    # Пример использования
    my_book = Book("1984", "Джордж Оруэлл", 1949, "978-5-17-118893-0")
    my_magazine = Magazine("Мир фантастики", "А. Иванов", 2023, 12)
    
    print(my_book.get_info())
    print(my_magazine.get_info())