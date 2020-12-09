"""5. Create a class called ”Book” for a bookshop. The book will need to contain the
title, author, number of pages, ISBN number, price, and the number of copies available.
The number of copies can be assumed to be 0 upon creation of the object. Therefore,
the parameters for the constructor should be title, author, number of pages, ISBN,
and price __init__(self, title, author, no_pages, isbn, price). The class will require
a number of methods to allow the bookshop to:

change the price change_price(self, new_price);
sell a copy of the book sell_copy(self);
restock the book restock(self, new_copies);
and print all the information about the book retrieve_book_information(self).
"""


class Book:
    def __init__(self, title, author, no_pages, isbn, price):
        self.title = title
        self.author = author
        self.no_pages = no_pages
        self.isbn = isbn
        self.price = price
        self.copies = 0

    def change_price(self, new_price):
        self.price = new_price

    def sell_copy(self):
        self.copies -= 1

    def restock(self, new_copies):
        self.copies += new_copies

    def retrieve_book_information(self):
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Pages: {self.no_pages}\n"
            f"ISBN: {self.isbn}\n"
            f"Price: {self.price:.2f}\n"
            f"Copies: {self.copies}"
        )


book1 = Book("Nineteen Eighty-Four", "George Orwell", 328, 9780141393049, 7.99)
book1.change_price(6.99)
book1.restock(30)
book1.sell_copy()
print(book1.retrieve_book_information())
