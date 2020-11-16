# Practical Worksheet 7: Using Booleans and While Loops

from graphics import *
from pract05 import draw_brown_eye, distance_between_points, draw_circle
from pract06 import calculate_grade
import time
import random


def add_digits():
    number = input("Enter a number: ")
    x = 0
    for y in number:
        x = x + int(y)
    print(x)


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
5.
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
6.
The pract07.py file contains functions fahrenheit_to_celsius and celsius_to_fahrenheit
for converting between temperature units. Using calls to these two functions, write
a temperature_converter function that provides a text-based interface which allows
the user to (repeatedly) convert temperature values until he/she wishes to stop.
The user should be asked which way the conversion should be performed separately
for each conversion.
'''
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_fahrenheit(celsius):
    return 9 / 5 * celsius + 32


def temperature_converter():
    while True:
        conv_type = input("\nEnter 'ftc' for Fahrenheit-to-Celcius, 'ctf' for "
                            "Celsius-to-Fahrenheit, or 'q' to quit: ").lower()
        if conv_type == "ftc" or conv_type == "ctf":
            while True:
                temperature = input("Enter the temperature in degrees (whole number): ")
                if temperature.isdigit():
                    if conv_type == "ftc":
                        result = round(fahrenheit_to_celsius(int(temperature)))
                        txt = "{0}°F is equivalent to {1}°C"
                    elif conv_type == "ctf":
                        result = round(celsius_to_fahrenheit(int(temperature)))
                        txt = "{0}°C is equivalent to {1}°F"
                    print(txt.format(temperature, result))
                    break
                else:
                    print("Error: Invalid answer")
        elif conv_type == "q":
            break
        else:
            print("Error: Invalid answer")
            continue


'''
7.
Write a guess_the_number function. The function should generate a random number
between 1 and 100 (using randint from the random module) and then allow the user
to guess the number. After each incorrect guess, it should display “Too high” or
“Too low” as appropriate. If the user guesses the number within seven guesses, it
should display a “You win!” message saying how many guesses it took. After seven
incorrect guesses, the function should display a “You lose! – the number was
. . . ” message.
'''
def guess_the_number():
    random_n = random.randint(1, 100)
    for i in range(1, 8):
        while True:
            guess = input("Guess the number: ")
            if guess.isdigit():
                guess = int(guess)
                if guess == 0 or guess > 100:
                    print("Error: Value out of range\n")
                else:
                    break
            else:
                print("Error: Invalid value\n")

        if guess == random_n:
            if i == 1:
                print("You win! It took you only 1 guess")
            else:
                print(f"You win! It took you {i} guesses")
            break
        if guess > random_n:
            print("Too high\n")
        if guess < random_n:
            print("Too low\n")
        if i == 7:
            print(f"You lose, the random number was {random_n}")


'''
8.
Write a table_tennis_scorer function that allows the user to keep track of the
points of two players in a game of table tennis. In table tennis, the first player
to reach 11 points wins the game; however, a game must be won by at least a two
point margin. The points for the players should be displayed on two halves of a
graphics window, and the user clicks anywhere on the appropriate side to increment
a player’s score. As soon as one player has won, a “wins” message should appear
on that side.
'''
def table_tennis_scorer():
    win = GraphWin("Table tennis scorer", 500, 500)
    win.setCoords(0, 0, 1, 1)

    left_score = 0
    right_score = 0

    divider = Line(Point(.5, 0), Point(.5, 1))
    divider.draw(win)

    left_score_text = Text(Point(.25, .6), 0)
    left_score_text.setSize(35)
    left_score_text.draw(win)

    right_score_text = Text(Point(.75, .6), 0)
    right_score_text.setSize(35)
    right_score_text.draw(win)

    while not((left_score >= 11 or right_score >= 11) and
              (left_score >= (right_score + 2) or right_score >= (left_score + 2))):
        cursor = win.getMouse()
        if cursor.getX() <= .5:
            left_score += 1
            left_score_text.setText(left_score)
        else:
            right_score += 1
            right_score_text.setText(right_score)

    if left_score > right_score:
        winner_text_centre = Point(.25, .5)
    else:
        winner_text_centre = Point(.75, .5)

    winner_text = Text(winner_text_centre, "Winner")
    winner_text.setSize(20)
    winner_text.draw(win)

    cursor = win.getMouse()
    win.close()


'''
9. [harder]
Write a function clickable_box_of_eyes that takes two parameters columns and rows,
and displays a rows × columns grid of blue eyes (all of radius 50) within a box
(rectangle). There should be a border of size 50 between the box and the edge of
the window. For each click of the mouse inside the box, the function should behave
as follows: if the click is on an eye, the row and column of that eye should be
displayed in the space below the box, for example as shown below given the click
denoted by the dot (note that row and column numbers should begin at 1):

If the user clicks within the box but not on an eye, the displayed message should
be “Between eyes”. The window should close when the user clicks outside the box.
'''
def clickable_box_of_eyes(cols, rows):
    b_and_cols = cols + 1   # columns plus border
    b_and_rows = rows + 1   # rows plus border
    win = GraphWin("Clickable box of eyes", 100 * b_and_cols, 100 * b_and_rows)
    win.setCoords(0, b_and_rows, b_and_cols, 0)

    for i in range(1, b_and_rows):
        for j in range(1, b_and_cols):
            draw_blue_eye(win, Point(j, i), .5)

    container = Rectangle(Point(.5, .5),
                          Point(b_and_cols - .5, b_and_rows -.5))
    container.draw(win)

    message = Text(Point(b_and_cols / 2, b_and_rows - .25), "")
    message.setSize(20)
    message.draw(win)

    while True:
        cursor = win.getMouse()
        col = int(cursor.getX() + .5)
        row = int(cursor.getY() + .5)

        if col == 0 or row == 0 or col == b_and_cols or row == b_and_rows:
            win.close()
            break
        elif distance_between_points(cursor, Point(col, row)) > .5:
            message.setText("Between eye")
        else:
            message.setText(f"Eye at row {row}, column {col}")


def draw_blue_eye(win, centre, radius):
    draw_circle(win, centre, radius, "white")
    draw_circle(win, centre, radius / 2, color_rgb(135,207,255))
    draw_circle(win, centre, radius / 4, "black")


'''
10. [harder]
Write a find_the_circle function to play a simple game. This should start by
displaying a graphics window, and creating (but not displaying) a circle of radius
30 at a random position (use the randint function from the random module). The user
should then have 10 attempts at locating the circle (by clicking on the graphics
window). Each time (except the first) the user misses the circle, a “getting closer”
or “getting further away” message should be displayed (depending on the position
of the current and previous clicks). If the user manages to find the circle (by
clicking within its circumference), then the circle should be displayed and the
user given some points: 10 points for finding it with the first click, down to 1
point for finding it with the 10th click. The game then restarts. However, each
time the game restarts the circle should be given a new random position and its
radius reduced by 10%. The game ends when the user fails to find the circle within
10 clicks. The total number of points scored should then be displayed (note: game
is too hard with radius 30 circle so I've uped it to 60).
'''
def find_the_circle():
    win = GraphWin("Find the circle", 300, 440)
    score, radius, loss = 0, 60, False

    divider = Rectangle(Point(-1, 300),
                        Point(300, 360))
    divider.setFill("gray")
    divider.draw(win)

    warning_text = Text(Point(150, 330), "Click in the space\nabove this grey rectangle")
    warning_text.setSize(12)
    warning_text.setStyle("bold")
    warning_text.draw(win)

    status_text = Text(Point(150, 385), "")
    status_text.setSize(12)
    status_text.setStyle("bold")
    status_text.draw(win)

    score_text = Text(Point(150, 415), "Score: 0")
    score_text.setSize(12)
    score_text.setStyle("bold")
    score_text.draw(win)

    points_text = Text(Point(150, 25), "")
    points_text.setSize(14)
    points_text.setStyle("bold")
    points_text.draw(win)

    while True:
        centre_x, centre_y = random.randint(0, 300), random.randint(0, 300)
        centre = Point(centre_x, centre_y)

        hidden_circle = Circle(centre, radius)
        hidden_circle.setFill("red")

        status_text.setText("Find the circle!")

        distances = []

        for i in range(1, 11):
            while True:
                cursor = win.getMouse()
                cursor_y = cursor.getY()
                if cursor_y <= 300:
                    break

            distance = distance_between_points(centre, cursor)
            distances.append(distance)

            if distance <= radius:
                hidden_circle.draw(win)
                divider.undraw()
                divider.draw(win)
                points_text.undraw()
                points_text.draw(win)
                if i == 1:
                    points_text.setText("You get 10 points!")
                    status_text.setText("Click 1: you got it first try")
                else:
                    status_text.setText(f"Click {i}: you got it")
                    if i == 10:
                        points_text.setText(f"You get 1 point!")
                    else:
                        points_text.setText(f"You get {11-i} points!")
                radius *= .9
                score += 11 - i
                time.sleep(4)
                hidden_circle.undraw()
                status_text.setText("")
                points_text.setText("")
                score_text.setText(("Score:", score))
                break
            elif i == 1:
                status_text.setText("Click 1: missed")
            elif distances[i-1] > distances[i-2]:
                status_text.setText(f"Click {i}: further away")
            elif distances[i-1] == distances[i-2]:
                status_text.setText(f"Click {i}: same distance")
            else:
                status_text.setText(f"Click {i}: closer")

            if i == 10:
                loss = True
                break

        if loss:
            score_text.setText("Game over")
            hidden_circle.draw(win)
            divider.undraw()
            divider.draw(win)
            points_text.undraw()
            points_text.draw(win)
            break

    points_text.setText(f"Your score is {score}")
    time.sleep(4)
    win.close()
