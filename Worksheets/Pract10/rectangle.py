'''
2.
Create a class called ”Rectangle”. The object should be created with a height
and width which are passed as parameters to the constructor __init__(self,
height, width). The user will require three things to be calculated: the area
calculate_area(self); the perimeter calculate_perimeter(self); and the
diagonal length between opposing corners calculate_diagonal_length(self).
Additionally, you will need to create a method which will print all the
information relating to the rectangle retrieve_information(self).
'''


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return self.width * 2 + self.height * 2

    def calculate_diagonal_length(self):
        return ((self.height ** 2) + (self.width ** 2)) ** 0.5

    def retrieve_information(self):
        return (f"Height: {self.height:.2f}\n"
                f"Width: {self.width:.2f}\n"
                f"Area: {self.calculate_area():.2f}\n"
                f"Perimeter: {self.calculate_perimeter():.2f}\n"
                f"Diagonal length: {self.calculate_diagonal_length():.2f}"
                )


rect1 = Rectangle(5, 8)
print("Rectangle 1:")
print(rect1.retrieve_information())
print()
rect2 = Rectangle(3, 11)
print("Rectangle 2:")
print(rect2.retrieve_information())
