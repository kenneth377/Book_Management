import uuid

class Book:
    booklist = []

    def __init__(self, title, author, genre, price=0, quantity=0) -> None:
        self.id = str(uuid.uuid4())
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__price = price
        self.__quantity = quantity

        Book.booklist.append(self)

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self,value):
        self.__title = value

    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self,value):
        self.__author = value

    @property
    def genre(self):
        return self.__genre
    
    @genre.setter
    def genre(self,value):
        self.__genre = value

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,value):
        self.__price = value


    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self,value):
        self.__quantity = value

    def update(self, key, val):
        setattr(self, key, val)

    def remove(self):
        Book.booklist.remove(self)

    @classmethod
    def search(cls, strin):
        for book in cls.booklist:
            for key,value in book.__dict__.items():
                if strin in str(value):
                    print(book.__dict__)

                