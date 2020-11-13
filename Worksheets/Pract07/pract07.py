from graphics import *
from pract05 import draw_brown_eye, distance_between_points
from pract06 import calculate_grade
import time


def mult(a, b):
    total = 0
    for i in range(a):
        total += b
    return total


def add_up_numbers1():
    total = 0
    more_numbers = "y"
    while more_numbers == "y":
        number = eval(input("Enter a number "))
        total += number
        more_numbers = input("Any more numbers? ")
    print("The total is", total)


def add_up_numbers2():
    total = 0
    number = eval(input("Number (0 to stop): "))
    while number != 0:
        total = total + number
        number = eval(input("Number (0 to stop): "))
    print("The total is", total)


def add_up_numbers3():
    total = 0
    n_str = input("Number (return to stop): ")
    while n_str != "":
       number = eval(n_str)
       total += number
       n_str = input("Number (return to stop): ")
    print("The total is", total)


# (note the need for "len(string) == 0" to appear twice).
def get_string1():
    string = ""
    while len(string) == 0:
        string = input("Enter a non-empty string: ")
        if len(string) == 0:
            print("You didn't enter anything!")
    return string


# The same validation example, this time using the
# loop-and-a-half pattern.
def get_string2():
    while True:
        string = input("Enter a non-empty string: ")
        if len(string) > 0:
            break
        print("You didn't enter anything!")
    return string


'''
1.
Write a get_name function that reads a person’s name from the user. Assume that
a valid name is any string of alphabetic characters only, such as “Jenny”. If the
user enters an invalid name, the function should continue to ask the user for a
name until she/he enters a valid one. Once a valid name has been entered, this
should be returned. (Hint: use the isalpha method discussed above.)
'''
def get_name():
    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            break
        print("The name must contain only alphabetic characters!")
    return name


'''
2.
The file pract07.py includes an incomplete traffic_lights function that draws a
set of traffic lights, with all lights off (i.e. black). Fill in the body of the
while loop at the bottom of this function so that it will continuously cycle through
the standard red → red/amber → green → amber → red sequence, simulating a real set
of traffic lights. Use “yellow” for amber, and add realistic delays between light
changes using the sleep function from the time module. E.g.,

    import time
    time.sleep(5)
'''
# will cycle twice and then close
def traffic_lights():
    win = GraphWin("Traffic light")
    red = Circle(Point(100, 50), 20)
    red.setFill("red")
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)
    start = time.time()
    while True:
        time.sleep(5)
        amber.setFill("yellow")
        time.sleep(2)
        red.setFill("black")
        amber.setFill("black")
        green.setFill("green")
        time.sleep(5)
        amber.setFill("yellow")
        green.setFill("black")
        time.sleep(2)
        amber.setFill("black")
        red.setFill("red")
        if time.time() - start > 20:
            win.close()
            break


'''
3.
In pract06, you wrote a calculate_grade function that returned a grade for a pupil’s
coursework based on a mark. Write a function grade_coursework that asks the user
for a mark and, using a call to calculate_grade, displays a “The pupil achieved a
grade of ...” message including the grade achieved. The function should only display
a grade for valid marks (i.e. between 0 and 20) – if the user enters an invalid
mark, they should be re-prompted until they enter a valid one.
'''
def grade_coursework():
    mark = ""
    while not mark.isdigit():
        mark = input("Enter your mark: ")
    grade = calculate_grade(eval(mark))
    print("The pupil acheived a grade of", grade)


'''
4.
Write an order_price function that works out the price of an order of goods. The
function should repeatedly ask the user for (i) the unit price of a product in the
order, (ii) the quantity of that product in the order, and (iii) whether there are
any more products in the order. When the user has completed entering prices &
quantities, the function should output a message containing the total order price
to 2 decimal places.
'''
def order_price():
    total = 0
    quantity = 0
    while True:
        unit_price = eval(input("Enter the unit price of a product (0 to stop): "))

        while unit_price > 0:
            quantity = round(eval(input("Enter the quantity of the product (0 to stop): ")))

            if quantity > 0:
                break
            elif quantity == 0:
                unit_price = 0
                break

        if unit_price == 0:
            break

        total += unit_price * quantity

    if total > 0:
        print("The order price is £{:.2f}".format(total))


'''
4.
Write a clickable_eye function which draws a brown eye of radius 100 (note: I've
set my own coords so this will be different) within a graphics window of sufficient
size. The function should then respond to each user click on the eye by displaying
(underneath the eye) the name of the part of the eye clicked on (i.e. one of “pupil”,
“iris”, “sclera” (or “white”)). The user should be able to finish (i.e. close the
window) by clicking on any point outside the eye. (Hint: use your draw_brown_eye
and distance_between_points functions from pract05.py.)
'''
def clickable_eye():
    win = GraphWin("Clickable eye", 800, 800)
    win.setCoords(0, 0, 1, 1)
    centre = Point(.5, .5)
    radius = .35
    draw_brown_eye(win, centre, radius)

    zone_text = Text(Point(.5, .07), "")
    zone_text.setSize(18)
    zone_text.setStyle('bold')
    zone_text.draw(win)

    while True:
        choice = win.getMouse()
        choice_x = choice.getX()
        choice_y = choice.getY()
        choice_zone = distance_between_points(Point(choice_x, choice_y),
                                              Point(.5, .5))

        if choice_zone > radius:
            win.close()
            break
        elif choice_zone >= radius / 2 and choice_zone <= radius:
            zone_text.setText("Sclera")
        elif choice_zone >= radius / 4 and choice_zone <= radius / 2:
            zone_text.setText("Iris")
        else:
            zone_text.setText("Pupil")


'''
5.
The pract07.py file contains functions fahrenheit_to_celsius and celsius_to_fahrenheit
for converting between temperature units. Using calls to these two functions, write
a temperature_converter function that provides a text-based interface which allows
the user to (repeatedly) convert temperature values until he/she wishes to stop.
The user should be asked which way the conversion should be performed separately
for each conversion.
'''
# For exercise 6
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius):
    return 9 / 5 * celsius + 32
