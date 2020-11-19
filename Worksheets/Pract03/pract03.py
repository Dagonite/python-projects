# Practical Worksheet 3: Graphical Programming

from graphics import GraphWin, Line, Point, Circle, Rectangle, Text, Entry
import math


def coordinate_transformations():
    win = GraphWin("Coordinate transformations", 330, 160)
    win.setCoords(0, 0, 1, 1)

    line = Line(Point(0, .25), Point(1, .25))
    line.draw(win)


'''1. The draw_stick_figure function is incomplete. Finish it by giving the
figure arms and legs. '''


def draw_stick_figure():
    win = GraphWin("Stick figure")

    head = Circle(Point(100, 60), 20)
    head.draw(win)

    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)

    leftArm = Line(Point(100, 90), Point(60, 120))
    leftArm.draw(win)

    rightArm = Line(Point(100, 90), Point(140, 120))
    rightArm.draw(win)

    leftLeg = Line(Point(100, 120), Point(70, 180))
    leftLeg.draw(win)

    rightLeg = Line(Point(100, 120), Point(130, 180))
    rightLeg.draw(win)


'''2. Write a draw_circle function which asks the user for the radius of a
circle and then draws the circle in the centre of a graphics window. '''


def draw_circle():
    win = GraphWin("Circle")
    win.setCoords(0, 0, 1, 1)
    centre = Point(.5, .5)

    radius = eval(input("Enter the radius: ")) / 100
    print(radius)
    circle = Circle(centre, radius)
    circle.draw(win)


'''3. Write a draw_archery_target function which draws a coloured target
consisting of concentric circles of yellow (innermost), red and blue. The
sizes of the circles should be in correct proportion i.e. the red circle
should have a radius twice that of the yellow circle, and the blue circle
should have a radius three times that of the yellow circle. (Hint: objects
drawn later will appear on top of objects drawn earlier.) '''


def draw_archery_target():
    win = GraphWin("Target")
    win.setCoords(0, 0, 1, 1)
    centre = Point(.5, .5)

    yellow_circle = Circle(centre, .1)
    yellow_circle.setFill("yellow")

    red_circle = Circle(centre, yellow_circle.getRadius() * 2)
    red_circle.setFill("red")

    blue_circle = Circle(centre, yellow_circle.getRadius() * 3)
    blue_circle.setFill("blue")

    blue_circle.draw(win)
    red_circle.draw(win)
    yellow_circle.draw(win)


'''4. Write a draw_rectangle function which asks the user for the height and
width of a rectangle and draws it in the centre of a graphics window of size
200 × 200 (i.e. with an equal space to the left and right of the rectangle,
and also above and below the rectangle). Assume that the user enters values
less than 200. (Hint: you need to work out the coordinates of the top-left
and bottom-right points from the rectangle dimensions and the dimensions of
the window — think about how much space there should be to the left of,
and above, the rectangle.) '''


def draw_rectangle():
    win = GraphWin("Rectangle")
    height = eval(input("What is the height: "))
    width = eval(input("What is the width: "))
    rectangle = Rectangle(Point(100 - width / 2, 100 - height / 2),
                          Point(100 + width / 2, 100 + height / 2))
    rectangle.draw(win)


'''5. Write a blue_circle function that allows the user to draw a blue circle
of radius 50 by clicking the location of its centre on the window. '''


def blue_circle():
    win = GraphWin("Blue Circle")
    message = Text(Point(100, 100), "Click anywhere to place a blue circle")
    message.setSize(8)
    message.draw(win)
    centre = win.getMouse()
    circle = Circle(centre, 50)
    circle.setFill("blue")
    circle.draw(win)
    message.setText("")


'''6. The function draw_line allows the user to draw a line by choosing two
points of his/her choice. Write a function ten_lines that allows the user to
draw 10 such lines. (Hint: combine the code from drawLine with a loop that
uses range(10).) '''


def ten_lines():
    win = GraphWin("Line drawer")
    for i in range(10):
        draw_line(win)


def draw_line(win):
    message = Text(Point(100, 100), "Click on first point")
    message.draw(win)
    p1 = win.getMouse()
    message.setText("Click on second point")
    p2 = win.getMouse()
    line = Line(p1, p2)
    line.draw(win)
    message.setText("")


'''7. Write a ten_strings function which allows the user to plot 10 strings
of their choice at locations of a graphics window chosen by clicking on the
mouse (the strings should be entered one-by-one by the user within a text
entry box at the top of the graphics window, clicking the mouse after
entering each one). '''


def ten_strings():
    win = GraphWin("Ten strings", 400, 300)
    message = Text(Point(200, 15), "Enter what you want then click where you "
                                   "want")
    message.draw(win)
    input_box = Entry(Point(200, 50), 10)
    input_box.draw(win)

    for i in range(10):
        position = win.getMouse()

        if input_box.getText() == "":
            new_message = Text(position, "[EMPTY MESSAGE]")

        else:
            new_message = Text(position, input_box.getText())

        new_message.draw(win)
        input_box.setText("")

    message.setText("You have used up all of your messages")


'''8. Write a ten_coloured_rectangles function to allow the user to draw 10
coloured rectangles on the screen. The user should choose the coordinates of
the top-left and bottom-right corners by clicking on the window. The colour
of each rectangle should be chosen by the user by entering a colour in a text
entry box at the top of the window. (The colour of each rectangle is given by
the string that is in this box when the user clicks its bottom-right point.)
The entry box should initially contain the string “blue”. (Assume that the
user never enters an invalid colour into the entry box.) '''


def ten_coloured_rectangles():
    win = GraphWin("Ten Rectangles", 400, 700)
    message = Text(Point(200, 15), "Enter what colour you want then click "
                                   "where you want")
    message.draw(win)
    input_box = Entry(Point(200, 50), 10)
    input_box.setText("blue")
    input_box.draw(win)
    hint = Text(Point(200, 80), "Click the top left point")
    hint.draw(win)

    for i in range(10):
        hint.setText("Click the top left point")
        p1 = win.getMouse()
        hint.setText("Click the bottom left point")
        p2 = win.getMouse()

        if input_box.getText() == "":
            rectangle = Rectangle(p1, p2)
            rectangle.setFill("blue")

        else:
            rectangle = Rectangle(p1, p2)
            rectangle.setFill(input_box.getText())

        rectangle.draw(win)
        input_box.setText("")
        hint.setText("")

    message.setText("You have used up all of your messages")


'''9. [harder] Write a five_click_stick_figure function that allows the user
to draw a (symmetric) stick figure in a graphics window using five clicks of
the mouse to determine the positions of its features. Each feature should be
drawn as the user clicks the points. (Hint: the radius of the head is the
distance between points 1 and 2 — see the previous worksheet.) Note that only
the y-coordinate of point (3) should be used — its x coordinate should be
copied from point (1). '''


def five_click_stick_figure():
    win = GraphWin("Five Click Stick Figure", 800, 600)
    message = Text(Point(400, 15), "Click to create your stick figure")
    message.draw(win)

    head_centre = win.getMouse()
    head_centreX, head_centreY = head_centre.getX(), head_centre.getY()
    head_perim = win.getMouse()
    head_perimX, head_perimY = head_perim.getX(), head_perim.getY()
    head_radius = math.sqrt((head_perimX - head_centreX) ** 2 +
                            (head_perimY - head_centreY) ** 2)
    head = Circle(head_centre, head_radius)
    head.draw(win)

    torso = win.getMouse()
    torso_line = Line(Point(head_centreX, head_centreY + head_radius),
                      Point(head_centreX, torso.getY()))
    torso_line.draw(win)

    arm_reach = win.getMouse()
    arm_length = head_centreX - arm_reach.getX()
    arms_line = Line(Point(arm_reach.getX(), arm_reach.getY()),
                     Point(head_centreX + arm_length, arm_reach.getY()))
    arms_line.draw(win)

    leg_reach = win.getMouse()
    left_leg_line = Line(Point(head_centreX, torso.getY()),
                         Point(leg_reach.getX(), leg_reach.getY()))
    left_leg_line.draw(win)

    leg_distance = head_centreX - leg_reach.getX()
    right_leg_line = Line(Point(head_centreX, torso.getY()),
                          Point(head_centreX + leg_distance, leg_reach.getY()))
    right_leg_line.draw(win)


'''10. [harder] Write a plot_rainfall function, which plots a histogram for
daily rainfall figures over a 7 day period. The rainfall figures should be
entered one-by-one into a text entry box within the window. The bars of the
histogram should be numbered along the bottom (note: instructions very vague on
this one). '''


def plot_rainfall():
    win = GraphWin("Plot Rainfall", 550, 300)
    message = Text(Point(275, 15), "Enter rainfall in mm over the last 7 days")
    message.draw(win)
    input_box = Entry(Point(275, 50), 10)
    input_box.draw(win)

    line1 = Line(Point(50, 70), Point(50, 260))
    line2 = Line(Point(50, 260), Point(470, 260))
    line1.draw(win)
    line2.draw(win)

    for i in range(7):
        text = Text(Point(70 + i * 60, 270), "Day " + str(i + 1))
        text.draw(win)

    for i in range(6):
        text = Text(Point(30, 255 - i * 36), i * 40)
        text.draw(win)

    for i in range(7):
        win.getMouse()
        box_message = int(input_box.getText())

        rectangle = Rectangle(Point(50 + i * 60, 260 - box_message),
                              Point(110 + i * 60, 260))
        rectangle.draw(win)

    message.setText("You're all finished")
