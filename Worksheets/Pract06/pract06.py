# Practical Worksheet 6: If Statements and For Loops

from graphics import *
import random
from pract05 import distance_between_points


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


# is_leap_year(2000)
# >>> True

# is_leap_year(2004)
# >>> True

# is_leap_year(2096)
# >>> True

# is_leap_year(2100)
# >>> False


def days_in_month1(month, year):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 31


def days_in_month2(month, year):
    num_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2 and is_leap_year(year):
        return 29
    else:
        return num_days[month - 1]


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


def body_mass_index_table():
    print(" cm")
    for cm in range(200, 149, -5):
        print(cm, end=" ")
        for kg in range(50, 101, 5):
            bmi = 10000 * kg / cm ** 2
            print("{0:6.1f}".format(bmi), end="")
        print()
    print()
    print(end="   ")
    for kg in range(50, 101, 5):
        print("{0:>6}".format(kg), end="")
    print("   kg")


'''1. A fast-food company charges £1.50 for delivery to your home, except for 
large orders of £10 or more where delivery is free. Write a function 
fast_food_order_price that asks the user for the basic price of an order and 
prints a “The total price of your order is . . . ” message containing the 
total price including any delivery charges. '''
def fast_food_order_price():
    price = eval(input("Enter the price of the food order: "))
    if price < 10:
        price += 1.50
    print("The total price of your order is £{0:0.2f}.".format(price))


'''2. Write a what_to_do_today function that asks the user to enter today’s 
temperature, and then prints a message suggesting what to do. For 
temperatures of above 25 degrees, a swim in the sea should be suggested; for 
temperatures between 10 and 25 degrees (inclusive), shopping in Gunwharf 
Quays is a good idea, and for temperatures of below 10 degrees it’s best to 
watch a film at home. '''
def what_to_do_today():
    temperature = eval(input("Enter the temperature: "))
    if temperature > 25:
        print("Go swim in the sea.")
    elif temperature >= 10 and temperature <= 25:
        print("Go shopping in Gunwharf Quays.")
    else:
        print("Watch a film at home.")


'''3. Write a function display_square_roots that has two parameters, 
start and end, and displays the square roots of numbers between these two 
values, shown to three decimal places. For example, the call 
display_square_roots(2, 4) should result in the following output: The square 
root of 2 is 1.414 The square root of 3 is 1.732 The square root of 4 is 
2.000 '''
def display_square_roots(start, end):
    for i in range(start, end + 1):
        print("The square root of {0} is {1:0.3f}".format(i, i ** .5))


'''4. A school teacher marks her pupils’ coursework out of 20, but needs to 
translate these marks to a grade of A, B, C or F (where marks of 16 or above 
get an A, marks between 12 and 15 result in a B, marks between 8 and 11 give 
a C, and marks below 8 get an F). Write a calculate_grade function that takes 
a mark as a parameter and returns the corresponding grade as a single-letter 
string. If the parameter value is too big or too small, the function should 
return a mark of X. '''
def calculate_grade(mark):
    if mark > 20 or mark < 0:
        return "X"
    elif mark >= 16:
        return "A"
    elif mark >= 12:
        return "B"
    elif mark >= 8:
        return "C"
    else:
        return "F"


'''5. Write a function peas_in_a_pod that asks the user for a number, 
and then draws that number of “peas” (green circles of radius 50) in a “pod” 
(graphics window of exactly the right size). E.g., if the user enters 5, 
a graphics window of size 500 × 100 should appear. '''
def peas_in_a_pod():
    peas = eval(input("Enter a number of peas: "))
    win = GraphWin("Peas in a pod", peas * 100, 100)
    for pea in range(peas):
        circle = Circle(Point(50 + pea * 100, 50 ), 50)
        circle.setFill("green")
        circle.draw(win)


'''6. A train company prices tickets based on journey distance: tickets cost 
£3 plus 15p for each kilometre (e.g. a ticket for a 100 kilometre journey 
costs £18). However, senior citizens (people who are 60 or over) and children 
(15 or under) get a 40% discount. Write a ticket_price function that takes 
the journey distance and passenger age as parameters (both integers), 
and returns the price of the ticket in pounds (i.e. a float). '''
def ticket_price(distance, age):
    ticket = 3 + distance * .15
    if age >= 60 or age <= 15:
        ticket *= .40
    return format(ticket, ".2f")


'''7. Write a numbered_square function that has a parameter n and displays a 
“numbered” square of size n; e.g, a call numbered_square(4) should result in 
the output: 4 5 6 7 3 4 5 6 2 3 4 5 1 2 3 4 (Notice that the top-left figure 
should should always be n.) '''
def numbered_square(n):
    for y in list(range(n, 0, -1)):
        for x in range(n):
            print(x + y, end = " ")
        print()


'''8. The pract06.py file contains an incomplete draw_coloured_eye function 
for which the graphics window, centre point, radius and eye colour (a string) 
are given as parameters. Complete the draw_coloured_eye function so that it 
draws an eye like those from last week, but for any given colour. Write 
another function eye_picker that asks the user for the coordinates of the 
centre of an eye, its radius and colour. If the user inputs a valid eye 
colour (blue, grey, green or brown), then an appropriately coloured eye 
should be displayed in a graphics window. Otherwise, just a “not a valid eye 
colour” message should be output. (Note: remember to avoid repetitive code.) '''
def draw_circle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


def draw_coloured_eye(win, centre, radius, colour):
    draw_circle(win, centre, radius, "white")
    draw_circle(win, centre, radius / 2, colour)
    draw_circle(win, centre, radius / 4, "black")


def eye_picker():
    centre_coord = eval(input("Enter the coordinate for the centre of the eye "
                              "(as a tuple): "))
    x_coord, y_coord = centre_coord
    centre = Point(x_coord, y_coord)

    radius = eval(input("Enter the radius of the eye: "))

    colours = ["grey", "green", "blue", "green"]
    colour = ""
    while colour not in colours:
        print("The available colours are: ", end="")
        print(*colours, sep=", ")
        colour = input("Enter the colour of the eye: ").lower()

    win = GraphWin("Coloured eye")
    draw_coloured_eye(win, centre, radius, colour)


'''9. This exercise and the following one help to prepare you for the Python 
assignment. The table below shows 10 different “patch designs”. Each patch 
design features a regular arrangement of lines, circles, rectangles and/or 
text, and has dimensions of 100×100 pixels. 

Write a function draw_patch_window (without parameters) which displays, 
in a graphics window of size 100×100 pixels, the patch design which is 
labelled with the final digit of your student number. The patch design should 
be displayed in red, as in the table. It’s important that your program draws 
the patch design accurately, but don’t worry if one pixel is chopped off at 
the edge of the window. Note that you don’t need to draw a border around the 
patch design. '''
def draw_patch_window():
    win = GraphWin("Patch design", 100, 100)
    for distance in (20, 40, 60, 80, 100):
        line = Line(Point(0, distance), Point(distance, 0))
        line.setFill("red")
        line.setWidth(2)
        line.draw(win)

        line = Line(Point(100 - distance, 0), Point(100, distance))
        line.setFill("red")
        line.setWidth(2)
        line.draw(win)

    for distance in (20, 40, 60, 80):
        line = Line(Point(distance, 100), Point(100, distance))
        line.setFill("red")
        line.setWidth(2)
        line.draw(win)

        line = Line(Point(0, distance), Point(100 - distance, 100))
        line.setFill("red")
        line.setWidth(2)
        line.draw(win)


'''10. Write a function draw_patch which draws the same patch design, 
but which takes four parameters: the window in which to draw the patch, 
the x and y coordinates of where the top-left corner of the patch should be, 
and the colour of the patch. '''
def draw_patch(win, x, y, colour):
    for distance in (20, 40, 60, 80, 100):
        line = Line(Point(x, distance + y), Point(x + distance, y))
        line.setFill(colour)
        line.setWidth(2)
        line.draw(win)

        line = Line(Point(x + 100 - distance, y), Point(x + 100, y + distance))
        line.setFill(colour)
        line.setWidth(2)
        line.draw(win)

    for distance in (20, 40, 60, 80):
        line = Line(Point(x + distance, y + 100), Point(x + 100, y + distance))
        line.setFill(colour)
        line.setWidth(2)
        line.draw(win)

        line = Line(Point(x, y + distance), Point(x + 100 - distance, y + 100))
        line.setFill(colour)
        line.setWidth(2)
        line.draw(win)


'''Write another function draw_patchwork (without parameters) which uses 
draw_patch to draw a blue “patchwork” three patches wide and two patches high 
in a graphics window of size 300 × 200 pixels. '''
def draw_patchwork():
    win = GraphWin("Patchwork", 300, 200)
    colour = "blue"
    for y in range(2):
        for x in range(3):
            draw_patch(win, x * 100, y * 100, colour)


'''11. Write an eyes_all_around function that allows the user to plot exactly 
30 eyes on a graphics window of dimensions 500 by 500 by clicking on chosen 
centre points. All eyes should be of radius 30, but they should be of 
different colours: specifically, the colours should repeatedly cycle through 
the sequence “blue”, “grey”, “green” and “brown”. Your function should call 
draw_coloured_eye to draw each eye. '''
def eyes_all_around():
    win = GraphWin("Eyes all around", 500, 500)
    colours = ["blue", "grey", "green", "brown"]
    for eye in range(30):
        eye_colour = eye % 4
        centre = win.getMouse()
        draw_coloured_eye(win, centre, 30, colours[eye_colour])
    win.close()


'''12. [harder] Write an archery_game function. This function should draw a 
target (like that from pract03) using the supplied draw_circle function. Your 
function should then allow the user to click on the graphics window five 
times, representing the firing of five arrows – each click representing the 
point on the target that is aimed at. 

Fluctuating atmospheric conditions should be considered – your solution
should generate two random values representing the amount an arrow will move
horizontally and vertically from the aimed position during its flight, and these
values should be adjusted a little (again randomly) after each arrow.

Generating random numbers is easily accomplished using the randint function from
the random module. This function takes two arguments and returns a random number
between these two values. For example, try:

    import random
    for i in range(10):
        print(random.randint(1, 5))

Each time the user clicks, the function should (i) display a small black 
circle representing where the arrow hits, and (ii) record the number of 
points scored. The points awarded for each arrow (click) are as follows: 10 
for the yellow area, 5 for red and 2 for blue. After the final arrow, 
the function should display the total score on the graphics window. (Hint: 
calculate distances by first importing your pract05.py file and using the 
distance_between_points function. '''
def archery_game():
    win = GraphWin("Archery game", 500, 500)
    win.setBackground("cyan")
    win.setCoords(0, 0, 1, 1)
    centre = Point(.5, .5)

    ground_rect = Rectangle(Point(-.01, -.01), Point(1.01, .5))
    ground_rect.setFill("green")
    ground_rect.draw(win)

    left_target_stand = Polygon(Point(.02, -.01), Point(.45, .5),
                                Point(.55, .5), Point(.12, -.01))
    left_target_stand.setFill("brown")
    left_target_stand.setWidth(2)
    left_target_stand.draw(win)

    right_target_stand = Polygon(Point(.98, -.01), Point(.55, .5),
                                 Point(.45, .5), Point(.88, -.01))
    right_target_stand.setFill("brown")
    right_target_stand.setWidth(2)
    right_target_stand.draw(win)

    draw_circle(win, centre, .3, "blue")
    draw_circle(win, centre, .2, "red")
    draw_circle(win, centre, .1, "yellow")

    grades = ["amazing at this game", "pretty good at this", "average at this",
    "below average at this", "awful at this"]

    score = 0
    score_text = Text(Point(.5, .04), "Score: {0}".format(score))
    score_text.setSize(18)
    score_text.setStyle('bold')
    score_text.draw(win)

    zone_text = Text(Point(.5, .09), "")
    zone_text.setSize(12)
    zone_text.setStyle('bold')
    zone_text.draw(win)

    wind_text = Text(Point(.5, .97), ("Wind: "))
    wind_text.setSize(12)
    wind_text.setStyle('bold')
    wind_text.draw(win)

    wsd = .25   # wind start deviation
    wd = .1    # wind deviation per arrow

    h_wind, v_wind = random.uniform(-wsd, wsd), random.uniform(-wsd, wsd)

    for arrow in range(5):
        wth = .08    # wind threshold
        wind = ""

        if v_wind > wth:
            wind += "north"
        elif v_wind < -wth:
            wind += "south"

        if h_wind > wth:
            wind += "east"
        elif h_wind < -wth:
            wind += "west"

        if wind == "":
            wind = "Calm"

        wind_text.setText("Wind: {0}".format(wind.title()))

        cursor_pos = win.getMouse()
        arrow_x = cursor_pos.getX() + h_wind
        arrow_y = cursor_pos.getY() + v_wind

        h_wind += random.uniform(-wd, wd)
        v_wind += random.uniform(-wd, wd)

        arrow_zone = distance_between_points(Point(arrow_x, arrow_y),
                                             Point(.5, .5))

        if arrow_zone <= .3:
            draw_arrow(win, arrow_x, arrow_y)
            if arrow_zone < .1:
                zone_text.setText("YELLOW ZONE (10 POINTS!)")
                score += 10
            elif arrow_zone >= .1 and arrow_zone < .2:
                zone_text.setText("RED ZONE (5 POINTS!)")
                score += 5
            else:
                zone_text.setText("BLUE ZONE (2 POINTS!)")
                score += 2
        else:
            zone_text.setText("TARGET MISSED (0 POINTS!)")

        score_text.setText("Score: {0}".format(score))

    if score > 44:
        grade = 0
    elif score > 34:
        grade = 1
    elif score > 24:
        grade = 2
    elif score > 19:
        grade = 3
    else:
        grade = 4

    grade_text = grades[grade]
    wind_text.setText("You scored {0}, meaning you're "
                      "{1}".format(score, grade_text))

    score_text.setSize(10)
    score_text.setText("Click anywhere on the target to play again\nClick "
                       "anywhere else to quit")
    choice = win.getMouse()
    choice_x = choice.getX()
    choice_y = choice.getY()

    if distance_between_points(Point(choice_x, choice_y), Point(.5, .5)) <= .3:
        win.close()
        archery_game()
    else:
        win.close()


def draw_arrow(win, arrow_x, arrow_y):
    arrow_shaft = Circle(Point(arrow_x, arrow_y), .008)
    arrow_shaft.setFill("brown")
    arrow_shaft.draw(win)

    fletching = Line(Point(arrow_x + .02, arrow_y + .02),
                     Point(arrow_x - .02, arrow_y - .02))
    fletching.setWidth(2)
    fletching.setFill("gray")
    fletching.draw(win)

    fletching = Line(Point(arrow_x + .02, arrow_y - .02),
                     Point(arrow_x - .02, arrow_y + .02))
    fletching.setWidth(2)
    fletching.setFill("gray")
    fletching.draw(win)
