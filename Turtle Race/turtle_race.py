# turtle_race.py

from random import sample, randrange, randint, triangular
from turtle import Turtle, Screen

# name: [color, headstart, min_forward, max_forward, deviation]
TURTLE_STATS = {
    "Lugo": ["red", 60, 11, 14, 9],
    "Pyson": ["green", 100, 9, 16, 16],
    "Steady": ["blue", 50, 13, 13, 0],
    "Lars": ["orange", 10, 12, 16, 14],
    "Dagon": ["gray", 0, 9, 21, 11],
    "Kelp": ["yellow", 10, 8, 28, 23],
    "Dizzy": ["purple", 70, 4, 36, 28],
    "Selwyn": ["pink", 20, 5, 24, 14],
    "Knight": ["brown", 40, 10, 17, 4],
    "Shade": ["black", 0, 1, 45, 18],
}

WIDTH, HEIGHT = randrange(600, 1400, 100), 500


def main():
    turtle_names, track_lines_count, v_spacing = select_turtles()
    pen, START_LINE = draw_screen(track_lines_count, v_spacing)

    # draw_track_limits(pen, track_lines_count, START_LINE, v_spacing)
    racing_turtles = create_turtles(pen, turtle_names, v_spacing, START_LINE)
    completed, dnf = start_race(racing_turtles, v_spacing)
    print_finishing_order(completed, dnf)


def select_turtles():
    TURTLE_COUNT = 6  # number of turtles in the race
    turtle_names = sample(TURTLE_STATS.keys(), TURTLE_COUNT)  # list of randomly selected turtles

    track_lines_count = len(turtle_names) + 1  # number of track dividers
    v_spacing = HEIGHT // track_lines_count  # the spacing between the turtles and the track dividers

    return turtle_names, track_lines_count, v_spacing


def draw_screen(track_lines_count, v_spacing):
    # create window
    win = Screen()
    win.setup(WIDTH, HEIGHT + 100)
    win.title("Turtle Race")

    # color background green
    win.bgcolor("forestgreen")

    # draw orange track
    pen = Turtle()
    pen.color("chocolate")
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    pen.goto(-WIDTH // 2, HEIGHT // 2 - 25)
    pen.pendown()
    pen.begin_fill()
    for _ in range(2):
        pen.forward(WIDTH)
        pen.right(90)
        pen.forward(HEIGHT - 45)
        pen.right(90)
    pen.end_fill()

    # coords for the centre of the start line
    START_LINE = (-WIDTH // 2, -HEIGHT // 2)

    # draw white track lines
    pen.color("white")
    for i in range(track_lines_count):
        pen.penup()
        pen.goto(START_LINE[0], START_LINE[1] + i * v_spacing + v_spacing // 2)
        pen.pendown()
        pen.forward(WIDTH)

    return pen, START_LINE


def create_turtles(pen, turtle_names, v_spacing, START_LINE):

    # list of turtle() objects
    racing_turtles = []

    # loop over the chosen turtles and place them on the start line
    for i, turtle_name in enumerate(turtle_names, start=1):
        # place turtle
        turtle_color, headstart, *_ = TURTLE_STATS[turtle_name]
        turtle = Turtle("turtle")
        turtle.name = turtle_name
        turtle.color(turtle_color)
        turtle.penup()
        curr_pos = START_LINE[1] + i * v_spacing
        turtle.goto(START_LINE[0] + 25 + headstart, curr_pos)
        turtle.start_pos = curr_pos
        turtle.pendown()
        racing_turtles.append(turtle)

        # write turtle's name
        pen.color(turtle_color)
        pen.penup()
        pen.goto(START_LINE[0] + 10, curr_pos + 10)
        pen.down()
        pen.shapesize(outline=8)
        pen.write(turtle_name, font=("Arial", 14, "bold"))

    return racing_turtles


def start_race(racing_turtles, v_spacing):
    completed = []  # turtles that have finished the race
    dnf = []  # turtles that did not finish

    while racing_turtles:
        for turtle in racing_turtles:
            # unpack turtle stats
            *_, min_forward, max_forward, deviation = TURTLE_STATS[turtle.name]

            # choose random direction for the turtle to stray in
            curr_deviation = randint(-deviation, deviation)

            # choose random amount for the turtle to move by
            distance = triangular(min_forward, max_forward, min_forward + max_forward // max(4, min_forward))

            # deviate turtle's direction
            turtle.right(curr_deviation)

            # move the turtle forward
            turtle.forward(distance)

            # make turtle face forward again
            turtle.right(-curr_deviation)

            # find turtle's current position
            x, y = turtle.pos()

            if x >= WIDTH // 2 - 30:
                completed.append(turtle)
                racing_turtles.remove(turtle)
            elif y < turtle.start_pos - v_spacing // 2 or y > turtle.start_pos + v_spacing // 2:
                dnf.append(turtle)
                racing_turtles.remove(turtle)

    dnf.reverse()

    return completed, dnf


def print_finishing_order(completed, dnf):
    for i, turtle in enumerate(completed, start=1):
        print(i, turtle.name)
    for turtle in dnf:
        print("DNF", turtle.name)


if __name__ == "__main__":
    main()
    input("\nPress enter to continue > ")
