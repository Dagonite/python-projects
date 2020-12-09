"""10. You have been asked by the library to create a borrower class. The first name,
last name, borrower number, and maximum number of books they can loan should be set
when the object is created. The library would like the object to hold the following
information:

• first name
• last name
• borrower number
• maximum number of books which can be loaned
• the number of books currently on loan (assume this to be 0 initially)
• the outstanding fine accrued by the borrower (assume this to be 0 initially)

The library need to be able to increase the maximum number of books the person can
loan, loan books to the person, return books, associate a fine with the borrower,
record that the borrower has paid some of their fine, and print the information held
about the borrower."""


class Borrower:
    borrower_number = 0
    max_no_of_loans = 5

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Borrower.borrower_number += 1
        self.borrower_number = Borrower.borrower_number
        self.max_no_of_loans = Borrower.max_no_of_loans
        self.books_on_loan = 0
        self.outstanding_fine = 0.00

    def increase_max_book_loan(self, value):
        self.max_no_of_loans += value
        print("Max number of loans increased for this borrower")

    def loan_book(self):
        if self.books_on_loan >= self.max_no_of_loans:
            print("Borrower already at max number of loans")
        else:
            self.books_on_loan += 1
            print("Book successfully loaned")

    def return_book(self):
        if self.books_on_loan > 0:
            self.books_on_loan -= 1
            print("Book successfully returned")
        else:
            print("Borrower has no books to return")

    def add_fine(self, fine):
        self.outstanding_fine += fine
        print(f"Fine increased by £{fine:.2f}")

    def reduce_fine(self, value):
        if value <= self.outstanding_fine:
            self.outstanding_fine -= value
            print(f"Fine reduced by £{value:.2f}")
        else:
            print("Value is higher than borrower's current fine")

    def retrieve_borrower_information(self):
        return (
            f"\nName: {self.first_name} {self.last_name}\n"
            f"Borrrower number: {self.borrower_number}\n"
            f"Max number of loans: {self.max_no_of_loans}\n"
            f"Number of books on loan: {self.books_on_loan}\n"
            f"Outstanding fine: £{self.outstanding_fine:.2f}"
        )


borrower1 = Borrower("John", "Doe")
for _ in range(6):
    borrower1.loan_book()
borrower1.increase_max_book_loan(1)
borrower1.loan_book()
borrower1.loan_book()
borrower1.return_book()
borrower1.return_book()
borrower1.add_fine(6.99)
borrower1.add_fine(4.99)
borrower1.reduce_fine(11.00)

print()

borrower2 = Borrower("Mary", "Sue")
borrower2.increase_max_book_loan(5)
for _ in range(8):
    borrower2.loan_book()
borrower2.return_book()
borrower2.return_book()
borrower2.add_fine(4.00)
borrower2.reduce_fine(5.00)
borrower2.reduce_fine(4.00)

print(borrower1.retrieve_borrower_information())
print(borrower2.retrieve_borrower_information())
