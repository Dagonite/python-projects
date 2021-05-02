# archery_game.py
"""Game where a user has to shoot arrows at a target. The arrows are offset by wind so the user has to take this into 
account before each shot. After firing all arrows, the user gets a score and a grade."""

import random

from graphics import Circle, GraphWin, Line, Point, Polygon, Rectangle, Text

from pract05 import distance_between_points
from pract06 import draw_circle


def archery_game():
    win = GraphWin("Archery game", 500, 500)
    win.setBackground("cyan")
    win.setCoords(0, 0, 1, 1)
    centre = Point(0.5, 0.5)

    ground_rect = Rectangle(Point(-0.01, -0.01), Point(1.01, 0.5)).draw(win)
    ground_rect.setFill("green")

    left_target_stand = Polygon(Point(0.02, -0.01), Point(0.45, 0.5), Point(0.55, 0.5), Point(0.12, -0.01)).draw(win)
    left_target_stand.setFill("brown")
    left_target_stand.setWidth(2)

    right_target_stand = Polygon(Point(0.98, -0.01), Point(0.55, 0.5), Point(0.45, 0.5), Point(0.88, -0.01)).draw(win)
    right_target_stand.setFill("brown")
    right_target_stand.setWidth(2)

    draw_circle(win, centre, 0.3, "blue")
    draw_circle(win, centre, 0.2, "red")
    draw_circle(win, centre, 0.1, "yellow")

    grades = [
        "amazing at this game",
        "pretty good at this game",
        "average at this game",
        "below average at this game",
        "awful at this game",
    ]

    score = 0
    score_text = Text(Point(0.5, 0.04), "Score: {}".format(score)).draw(win)
    score_text.setSize(18)
    score_text.setStyle("bold")

    zone_text = Text(Point(0.5, 0.09), "").draw(win)
    zone_text.setSize(12)
    zone_text.setStyle("bold")

    wind_text = Text(Point(0.5, 0.97), ("Wind: ")).draw(win)
    wind_text.setSize(12)
    wind_text.setStyle("bold")

    wsd = 0.25  # wind start deviation
    wd = 0.1  # wind deviation per arrow
    wth = 0.08  # wind threshold
    arrows = 5  # number of arrows to shoot

    h_wind, v_wind = random.uniform(-wsd, wsd), random.uniform(-wsd, wsd)

    for _ in range(arrows):
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

        wind_text.setText("Wind: {}".format(wind.title()))

        cursor_pos = win.getMouse()
        arrow_x = cursor_pos.getX() + h_wind
        arrow_y = cursor_pos.getY() + v_wind

        h_wind += random.uniform(-wd, wd)
        v_wind += random.uniform(-wd, wd)

        arrow_zone = distance_between_points(Point(arrow_x, arrow_y), Point(0.5, 0.5))

        if arrow_zone <= 0.3:
            draw_arrow(win, arrow_x, arrow_y)
            if arrow_zone < 0.1:
                zone_text.setText("YELLOW ZONE (10 POINTS!)")
                score += 10
            elif arrow_zone >= 0.1 and arrow_zone < 0.2:
                zone_text.setText("RED ZONE (5 POINTS!)")
                score += 5
            else:
                zone_text.setText("BLUE ZONE (2 POINTS!)")
                score += 2
        else:
            zone_text.setText("TARGET MISSED (0 POINTS!)")

        score_text.setText("Score: {}".format(score))

    if score > 220 / arrows:
        grade = 0
    elif score > 170 / arrows:
        grade = 1
    elif score > 120 / arrows:
        grade = 2
    elif score > 95 / arrows:
        grade = 3
    else:
        grade = 4

    grade_text = grades[grade]
    wind_text.setText("You scored {}, meaning you're {}".format(score, grade_text))

    score_text.setSize(10)
    score_text.setText("Click on the target to play again\nClick anywhere else to quit")

    choice = win.getMouse()
    choice_x, choice_y = choice.getX(), choice.getY()

    win.close()

    if distance_between_points(Point(choice_x, choice_y), Point(0.5, 0.5)) <= 0.3:
        archery_game()


def draw_arrow(win, arrow_x, arrow_y):
    arrow_shaft = Circle(Point(arrow_x, arrow_y), 0.008).draw(win)
    arrow_shaft.setFill("brown")

    for x in (1, -1):
        fletching = Line(Point(arrow_x + 0.02, arrow_y + 0.02 * x), Point(arrow_x - 0.02, arrow_y - 0.02 * x)).draw(win)
        fletching.setWidth(2)
        fletching.setFill("gray")


if __name__ == "__main__":
    archery_game()
