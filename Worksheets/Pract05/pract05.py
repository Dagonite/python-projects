# Practical Worksheet 5: Using functions
# Folders for Pract05 and Pract06 merged so that I can import pract05.py into
# pract06.py easily.

import math
from graphics import *


def product(x, y):
    return x * y


def product_tests():
    print(product(2, 3) + product(5, 9))
    print(product(product(4, 2), 4))
    print(product(product(4, 2), product(5, 9)))
    print(product("hello", 5))


'''
1.
The pract05.py file contains a function area_of_circle which has a parameter
representing a circle’s radius, and returns the area of the circle. Write a similar
function called circumference_of_circle that has a radius parameter and returns
the circumference of the circle.
'''
def area_of_circle(radius):
    return math.pi * radius ** 2


def circumference_of_circle(radius):
    return 2 * math.pi * radius

'''
2.
Write a function circle_info which asks the user to input the radius of a circle,
and then outputs a message that includes both the area and the circumference of
the circle (displayed to three decimal places); e.g. if the user enters a radius
of 5, then the output message might be:
    -> The area is 78.540 and the circumference is 31.416
Your function should call both the area_of_circle and the circumference_of_circle
functions to do the calculations.
'''
def circle_info():
    radius = eval(input("Enter the radius of the circle: "))
    area = area_of_circle(radius)
    circumference = circumference_of_circle(radius)
    print("The area is {0:0.3f} and the circumference is {1:0.3f}".format(area, circumference))

'''
3.
The draw_circle function in pract05.py draws a circle on a graphics window with
a given centre point, radius and colour. Complete the supplied draw_brown_eye_in_centre
function so that it calls draw_circle three times in order to draw a brown “eye”
in the centre of a graphics window. The radii of the white, brown and black circles
should be 60, 30 and 15 respectively
'''
def draw_circle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


def draw_brown_eye_in_centre():
    win = GraphWin()
    centre = Point(100, 100)
    radius = 60
    colours = ["white", "brown", "black"]
    for i in range(3):
        if i == 2:
            draw_circle(win, centre, radius / 4, colours[i])
        else:
            draw_circle(win, centre, radius / (i + 1), colours[i])


'''
4.
Write a function draw_block_of_stars which has two parameters width and height,
and outputs a rectangle of asterisks of the appropriate dimensions. For example,
the function call draw_block_of_stars(5, 3) should result in the following output:

    *****
    *****
    *****
'''
def draw_block_of_stars(width, height):
    for y in range(height):
        print("*" * width)


'''
Now, write a function drawLetterE that displays a large capital letter E; for example:

    **********
    **********
    **
    **
    ********
    ********
    **
    **
    **********
    **********

Your function should work by calling the draw_block_of_stars function an appropriate
number of times.
'''
def draw_letter_E():
    draw_block_of_stars(10, 2)
    draw_block_of_stars(2, 2)
    draw_block_of_stars(8, 2)
    draw_block_of_stars(2, 2)
    draw_block_of_stars(10, 2)


'''
5.
Add code to the supplied draw_brown_eye function so that, by calling draw_circle
three times, it draws a single brown eye, where the graphics window, centre point
and radius of the eye are all given as parameters to your function. Now, by using
your completed draw_brown_eye function, write a draw_pair_of_brown_eyes function
(without parameters) that draws a pair of eyes on a graphics window.
'''
def draw_brown_eye(win, centre, radius):
    draw_circle(win, centre, radius, "white")
    draw_circle(win, centre, radius / 2, "brown")
    draw_circle(win, centre, radius / 4, "black")


def draw_pair_of_brown_eyes():
    win = GraphWin("Brown eyes", 300, 200)
    draw_brown_eye(win, Point(90, 100), 60)
    draw_brown_eye(win, Point(210, 100), 60)


'''
6.
Write a function distance_between_points that has two parameters p1 and p2, each of
type Point, and returns the distance between them. This function should use the
formula for Pythagoras’ Theorem, as in practical worksheet P02. For example, the
function call:

    distance_between_points(Point(1, 2), Point(4, 6))

should result in the value 5.0 being returned. (Hint: you’ll need to use the getX
and getY methods to get the x and y coordinates of points p1 and p2.)
'''
def distance_between_points(p1, p2):
    p1X = p1.getX()
    p1Y = p1.getY()

    p2X = p2.getX()
    p2Y = p2.getY()

    distance = math.sqrt((p2X - p1X) ** 2 + (p2Y - p1Y) ** 2)
    return distance


'''
7.
It should be clear that it is impossible to output letters such as A or O using only
the draw_block_of_stars function. To allow for more complex letters such as these,
write a new function draw_blocks that outputs up to four rectangles next to each
other (consisting of spaces, then asterisks, then spaces and finally asterisks,
all of the same height). The widths of the four rectangles and their common height
should be parameters. E.g., a call: draw_blocks(0, 5, 4, 3, 2) will result in the
output:

    *****    ***
    *****    ***

(with no space before the first asterisks due to the 0 argument). Now, write a function
draw_letter_A that uses draw_blocks in order to display a large capital A in asterisks,
such as:

    ********
    ********
   **      **
   **      **
   **********
   **********
   **      **
   **      **
   **      **
'''
def draw_blocks(space1, width1, space2, width2, height):
    for y in range(height):
        print(" " * space1, end="")
        print("*" * width1, end="")
        print(" " * space2, end="")
        print("*" * width2)


def draw_letter_A():
    draw_blocks(1, 8, 0, 0, 2)
    draw_blocks(0, 2, 6, 2, 2)
    draw_blocks(0, 10, 0, 0, 2)
    draw_blocks(0, 2, 6, 2, 3)


'''
    ********
    **      **
    **       **
    **      **
    ********
    **      **
    **       **
    **       **
    **********
'''
def draw_letter_B():
    draw_blocks(0, 9, 0, 0, 1)
    draw_blocks(0, 2, 6, 2, 1)
    draw_blocks(0, 2, 7, 2, 1)
    draw_blocks(0, 2, 6, 2, 1)
    draw_blocks(0, 8, 0, 0, 1)
    draw_blocks(0, 2, 6, 2, 1)
    draw_blocks(0, 2, 7, 2, 1)
    draw_blocks(0, 2, 7, 2, 1)
    draw_blocks(0, 10, 0, 0, 1)


'''
       ******
     **********
    **        **
    **
    **
    **
    **        **
     **********
       ******
'''
def draw_letter_C():
    draw_blocks(3, 6, 0, 0, 1)
    draw_blocks(1, 10, 0, 0, 1)
    draw_blocks(0, 2, 8, 2, 1)
    draw_blocks(0, 2, 0, 0, 1)
    draw_blocks(0, 2, 0, 0, 1)
    draw_blocks(0, 2, 0, 0, 1)
    draw_blocks(0, 2, 8, 2, 1)
    draw_blocks(1, 10, 0, 0, 1)
    draw_blocks(3, 6, 0, 0, 1)



'''
8.
Write a draw_four_pairs_of_brown_eyes function (which doesn’t have parameters) that
opens a graphics window and allows the user to draw four pairs of eyes. Each pair is
drawn by clicking the mouse twice: the first click gives the centre of the left-most eye,
and the second gives any point on the outer circumference of this eye. (Hint: This
function should call the distance_between_points function from exercise 6 to obtain
the radius of each eye, as well as the draw_brown_eye function from exercise 5 to draw
the eyes.)
'''
def draw_four_pairs_of_brown_eyes():
    win = GraphWin("Four pairs of brown eyes", 1200, 800)
    for eye_pair in range(4):
        p1 = win.getMouse()
        p2 = win.getMouse()
        radius = distance_between_points(p1, p2)
        draw_brown_eye(win, p1, radius)
        draw_brown_eye(win, (Point(p1.getX() + radius * 2, p1.getY())), radius)


'''
9. [harder]
Write a display_text_with_spaces function which will display a given string at a
given point-size at a given position on a given graphics window (i.e. it should
have four parameters). The string should be displayed with spaces between each
character (for example, hello would be displayed as h e l l o). Now, using this
function, write another function construct_vision_chart that constructs an optician’s
vision chart. Your function should first open a graphics window. It should then
ask the user for six strings, displaying them on the graphics window as they are
entered. The strings should be displayed in upper case, and from the top of the
window to the bottom with descending point sizes of 30, 25, 20, 15, 10 and 5.
(Make sure that the lines are well-spaced out — you might need to experiment a
little with spacing.)
'''
def display_text_with_spaces(win, line, size, y):
    upper_line = line.upper()
    spaced_line = upper_line.replace("", " ")[1:-1]
    message = Text(Point(250, y), spaced_line)
    message.setFace("courier")  # setFace seems to not work a lot of the time
    message.setSize(size)
    message.draw(win)

def construct_vision_chart():
    win = GraphWin("Vision chart", 500, 400)
    message = Text(Point(0, 0), "")

    for i in range(6):
        line = input("Give me a string: ")
        size = 30 - 5 * i
        y = 60 * (i + 1)
        display_text_with_spaces(win, line, size, y)


'''
10. [harder]
Write a draw_stick_figure_family function. This function should display a group of
four or five stick figures (representing a family) in a graphics window. All the
stick figures should be the same shape (e.g. that of exercise 1, pract03),
but they should be of different sizes and positions. Begin by copying your
draw_stick_figure function from pract03.py, and changing it so that it has three
parameters, representing a graphics window, the position of the figure (a Point)
and its size (an int). (What the position and size mean exactly is up to you.)
Your draw_stick_figure_family function should contain just four or five calls to the
modified version of draw_stick_figure.
'''
def draw_stick_figure(win, position, size):
    posX = position.getX()
    posY = position.getY()

    head = Circle(position, size)
    head.draw(win)

    body = Line(Point(posX, posY + size),
                Point(posX, posY + size * 3))
    body.draw(win)

    arms = Line(Point(posX - size, posY + size * 2),
                Point(posX + size, posY + size * 2))
    arms.draw(win)

    left_leg = Line(Point(posX, posY + size * 3),
                    Point(posX - size, posY + size * 5))
    left_leg.draw(win)

    right_leg = Line(Point(posX, posY + size * 3),
                     Point(posX + size, posY + size * 5))
    right_leg.draw(win)

def draw_stick_figure_family():
    win = GraphWin("Stick Figure Family", 250, 200)
    draw_stick_figure(win, Point(50, 50), 25)
    draw_stick_figure(win, Point(100, 50), 20)
    draw_stick_figure(win, Point(150, 50), 18)
    draw_stick_figure(win, Point(200, 50), 15)
