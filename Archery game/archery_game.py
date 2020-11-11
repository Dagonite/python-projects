# archery_game.py

from graphics import *
import math
import random


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

        arrow_zone = distance_between_points(Point(arrow_x, arrow_y), Point(.5, .5))

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
    wind_text.setText("You scored {0}, meaning you're {1}".format(score, grade_text))

    score_text.setSize(10)
    score_text.setText("Click anywhere on the target to play again\nClick anywhere else to quit")
    choice = win.getMouse()
    choice_x = choice.getX()
    choice_y = choice.getY()

    if distance_between_points(Point(choice_x, choice_y), Point(.5, .5)) <= .3:
        win.close()
        archery_game()
    else:
        win.close()


def draw_circle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


def distance_between_points(p1, p2):
    p1X = p1.getX()
    p1Y = p1.getY()

    p2X = p2.getX()
    p2Y = p2.getY()

    distance = math.sqrt((p2X - p1X) ** 2 + (p2Y - p1Y) ** 2)
    return distance


def draw_arrow(win, arrow_x, arrow_y):
    arrow_shaft = Circle(Point(arrow_x, arrow_y), .008)
    arrow_shaft.setFill("brown")
    arrow_shaft.draw(win)

    fletching = Line(Point(arrow_x + .02, arrow_y + .02), Point(arrow_x - .02, arrow_y - .02))
    fletching.setWidth(2)
    fletching.setFill("gray")
    fletching.draw(win)

    fletching = Line(Point(arrow_x + .02, arrow_y - .02), Point(arrow_x - .02, arrow_y + .02))
    fletching.setWidth(2)
    fletching.setFill("gray")
    fletching.draw(win)


archery_game()
