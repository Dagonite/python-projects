"""
Game where a user gets to shoot arrows at a target. The arrows are offset by
wind so this needs to be taken into account before each shot. After shooting all
arrows a score and a grade are given.
"""

import random

from graphics import Circle, GraphWin, Line, Point, Polygon, Rectangle, Text

from Pract05.pract05 import distance_between_points, draw_circle


# constants
WSD = 0.25  # wind start deviation
WD = 0.1  # wind deviation after an arrow is shot
WTH = 0.08  # wind threshold (determines wind direction threshold for the wind direction message)
ARROWS = 8  # number of arrows to shoot
GRADES = {
    9 * ARROWS: "amazing at this game",
    8 * ARROWS: "pretty good at this game",
    6 * ARROWS: "average at this game",
    4 * ARROWS: "below average at this game",
    2 * ARROWS: "bad at this game",
    0: "terrible at this game",
}


def archery_game():
    """Program entry point."""
    win, wind_text, zone_text, score_text, score = draw_gui()
    score = shoot_arrows(win, wind_text, zone_text, score_text, score)
    give_grade(wind_text, score_text, score)

    # wait for user to click on the screen
    cursor = win.getMouse()
    cursor_x, cursor_y = cursor.getX(), cursor.getY()
    win.close()

    # if the user clicked on the target, reload the window
    if distance_between_points(Point(cursor_x, cursor_y), Point(0.5, 0.5)) <= 0.3:
        archery_game()


def draw_gui():
    """Create the graphics window and draw the target."""
    # create the window
    win = GraphWin("Archery game", 500, 500)
    win.setBackground("cyan")
    win.setCoords(0, 0, 1, 1)
    centre = Point(0.5, 0.5)

    # draw the grass
    ground_rect = Rectangle(Point(-0.01, -0.01), Point(1.01, 0.5)).draw(win)
    ground_rect.setFill("green")

    # draw the target legs
    left_target_stand = Polygon(Point(0.02, -0.01), Point(0.45, 0.5), Point(0.55, 0.5), Point(0.12, -0.01)).draw(win)
    left_target_stand.setFill("brown")
    left_target_stand.setWidth(2)

    right_target_stand = Polygon(Point(0.98, -0.01), Point(0.55, 0.5), Point(0.45, 0.5), Point(0.88, -0.01)).draw(win)
    right_target_stand.setFill("brown")
    right_target_stand.setWidth(2)

    # draw the target
    draw_circle(win, centre, 0.3, "blue")
    draw_circle(win, centre, 0.2, "red")
    draw_circle(win, centre, 0.1, "yellow")

    # draw the text displaying the score
    score = 0
    score_text = Text(Point(0.5, 0.04), f"Score: {score}").draw(win)
    score_text.setSize(18)
    score_text.setStyle("bold")

    # draw the text displaying where an arrow has landed
    zone_text = Text(Point(0.5, 0.09), "").draw(win)
    zone_text.setSize(12)
    zone_text.setStyle("bold")

    # draw the text describing wind conditions
    wind_text = Text(Point(0.5, 0.97), "Wind: ").draw(win)
    wind_text.setSize(12)
    wind_text.setStyle("bold")

    return win, wind_text, zone_text, score_text, score


def shoot_arrows(win, wind_text, zone_text, score_text, score):
    """Prompt user to shoot arrows at the target by left-clicking."""
    h_wind, v_wind = random.uniform(-WSD, WSD), random.uniform(-WSD, WSD)

    for _ in range(ARROWS):
        # determine wind direction
        wind = ""
        if v_wind > WTH:
            wind += "north"
        elif v_wind < -WTH:
            wind += "south"
        if h_wind > WTH:
            wind += "east"
        elif h_wind < -WTH:
            wind += "west"
        if wind == "":
            wind = "Calm"

        # display wind direction
        wind_text.setText(f"Wind: {wind.title()}")

        # wait for left-click
        cursor_pos = win.getMouse()
        arrow_x = cursor_pos.getX() + h_wind  # add horizontal wind to x value
        arrow_y = cursor_pos.getY() + v_wind  # add vertical wind to y value

        # add wind deviation for next arrow shot
        h_wind += random.uniform(-WD, WD)
        v_wind += random.uniform(-WD, WD)

        # get the distance from the target centre of where the arrow will land
        arrow_zone = distance_between_points(Point(arrow_x, arrow_y), Point(0.5, 0.5))

        # determine what zone the arrow will land in
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

        score_text.setText(f"Score: {score}")

    return score


def give_grade(wind_text, score_text, score):
    """Display what score and grade the user has received."""
    for grade, desc in GRADES.items():
        if score >= grade:
            grade_text = desc
            break

    wind_text.setText(f"You scored {score}, meaning you're {grade_text}")

    score_text.setSize(10)
    score_text.setText("Click on the target to play again\nClick anywhere else to quit")


def draw_arrow(win, arrow_x, arrow_y):
    """Draw an arrow onto the given graphics window."""
    arrow_shaft = Circle(Point(arrow_x, arrow_y), 0.008).draw(win)
    arrow_shaft.setFill("brown")

    for x in (1, -1):
        fletching = Line(Point(arrow_x + 0.02, arrow_y + 0.02 * x), Point(arrow_x - 0.02, arrow_y - 0.02 * x)).draw(win)
        fletching.setWidth(2)
        fletching.setFill("gray")


if __name__ == "__main__":
    archery_game()
