# Practical Worksheet 6: if statements and for loops

from graphics import *
import random


# list(range(1, 10, 2))
# >>> [1, 3, 5, 7, 9]

# list(range(4, 22, 3))
# >>> [4, 7, 10, 13, 16, 19]

# list(range(10, 0, -1))
# >>> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def is_leap_year_tests():
    print(is_leap_year(2000))
    print(is_leap_year(2004))
    print(is_leap_year(2009))
    print(is_leap_year(2100))


def days_in_month(month, year):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 31


def nested_loops():
    for i in range(3):
        print("Outer loop with i =", i)
        for j in range(4):
            print("Inner loop with i =", i, "and j =", j)
        print()


def triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


'''
1.
A fast-food company charges £1.50 for delivery to your home, except for large orders
of £10 or more where delivery is free. Write a function fast_food_order_price that
asks the user for the basic price of an order and prints a “The total price of your
order is . . . ” message containing the total price including any delivery charges.
'''
def fast_food_order_price():
    price = eval(input("Enter the price of the food order: "))
    if price < 10:
        price += 1.50
    print("The total price of your order is £{0:0.2f}.".format(price))


'''
2.
Write a what_to_do_today function that asks the user to enter today’s temperature,
and then prints a message suggesting what to do. For temperatures of above 25 degrees,
a swim in the sea should be suggested; for temperatures between 10 and 25 degrees
(inclusive), shopping in Gunwharf Quays is a good idea, and for temperatures of
below 10 degrees it’s best to watch a film at home.
'''
def what_to_do_today():
    temperature = eval(input("Enter the temperature: "))
    if temperature > 25:
        print("Go swim in the sea.")
    elif temperature >= 10 and temperature <= 25:
        print("Go shopping in Gunwharf Quays.")
    else:
        print("Watch a film at home.")


'''
3.
Write a function display_square_roots that has two parameters, start and end, and
displays the square roots of numbers between these two values, shown to three decimal
places. For example, the call display_square_roots(2, 4) should result in the following
output:
    The square root of 2 is 1.414
    The square root of 3 is 1.732
    The square root of 4 is 2.000
'''
def display_square_roots(start, end):
    for i in range(start, end + 1):
        print("The square root of {0} is {1:0.3f}".format(i, i ** .5))


'''
4.
A school teacher marks her pupils’ coursework out of 20, but needs to translate
these marks to a grade of A, B, C or F (where marks of 16 or above get an A, marks
between 12 and 15 result in a B, marks between 8 and 11 give a C, and marks below
8 get an F). Write a calculate_grade function that takes a mark as a parameter and
returns the corresponding grade as a single-letter string. If the parameter value
is too big or too small, the function should return a mark of X.
'''
def calculate_grade(mark):
    if mark > 20 or mark < 0:
        return("X")
    elif mark >= 16:
        return("A")
    elif mark >= 12:
        return("B")
    elif mark >= 8:
        return("C")
    else:
        return("F")


'''
5.
Write a function peas_in_a_pod that asks the user for a number, and then draws that
number of “peas” (green circles of radius 50) in a “pod” (graphics window of exactly
the right size). E.g., if the user enters 5, a graphics window of size 500 × 100
should appear.
'''
def peas_in_a_pod():
    peas = eval(input("Enter a number of peas: "))
    win = GraphWin("Peas in a pod", peas * 100, 100)
    for pea in range(peas):
        circle = Circle(Point(50 + pea * 100, 50 ), 50)
        circle.setFill("green")
        circle.draw(win)


'''
6.
A train company prices tickets based on journey distance: tickets cost £3 plus 15p
for each kilometre (e.g. a ticket for a 100 kilometre journey costs £18). However,
senior citizens (people who are 60 or over) and children (15 or under) get a 40%
discount. Write a ticket_price function that takes the journey distance and passenger
age as parameters (both integers), and returns the price of the ticket in pounds
(i.e. a float).
'''
def ticket_price(distance, age):
    ticket = 3 + distance * .15
    if age >= 60 or age <= 15:
        ticket *= .40
    return format(ticket, ".2f")


'''
7.
Write a numbered_square function that has a parameter n and displays a “numbered”
square of size n; e.g, a call numbered_square(4) should result in the output:
    4 5 6 7
    3 4 5 6
    2 3 4 5
    1 2 3 4
(Notice that the top-left figure should should always be n.)
'''
def numbered_square(n):
    for y in list(range(n, 0, -1)):
        for x in range(n):
            print(x + y, end = " ")
        print()


'''
8.
The pract06.py file contains an incomplete draw_coloured_eye function for which
the graphics window, centre point, radius and eye colour (a string) are given as
parameters. Complete the draw_coloured_eye function so that it draws an eye like
those from last week, but for any given colour. Write another function eye_picker 
that asks the user for the coordinates of the centre of an eye, its radius and
colour. If the user inputs a valid eye colour (blue, grey, green or brown), then
an appropriately coloured eye should be displayed in a graphics window. Otherwise,
just a “not a valid eye colour” message should be output. (Note: remember to avoid
repetitive code.)
'''
