"""Watch turtles race it out."""

import csv
from random import randint
from time import perf_counter
from turtle import Screen, Turtle

import matplotlib.pyplot as plt

TURTLES = {
    "Blood": "red",
    "Citrus": "orange",
    "Lemon": "yellow",
    "Verdant": "green",
    "Sky": "blue",
    "Lapis": "indigo",
    "Amethyst": "violet",
}

WIDTH, HEIGHT = 1000, 500


def main():
    win, v_spacing, pen = draw_screen(len(TURTLES))
    turtle_objs = place_turtles(v_spacing)
    winner, duration = race(turtle_objs, pen)
    win.exitonclick()
    write_to_csv(winner.name, duration)
    process_csv()


def draw_screen(TURTLE_COUNT):
    # create window
    win = Screen()
    win.setup(WIDTH, HEIGHT)
    win.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    win.title("Turtle Race")

    # color background
    win.bgcolor("chocolate")

    # draw white track lines
    pen = Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.color("white")
    WHITE_LINES = TURTLE_COUNT + 1
    v_spacing = HEIGHT // WHITE_LINES
    for i in range(WHITE_LINES):
        pen.penup()
        pen.goto(0, i * v_spacing + v_spacing // 2)
        pen.pendown()
        pen.forward(WIDTH)

    # draw finish line
    white_square = Turtle("square")
    white_square.color("white")
    white_square.penup()
    white_square.speed(0)

    black_square = Turtle("square")
    black_square.color("black")
    black_square.penup()
    black_square.speed(0)

    FIRST_ROW_X = WIDTH - WIDTH // 20
    SECOND_ROW_X = FIRST_ROW_X + 21.5
    BASE_Y = HEIGHT - HEIGHT // 50
    OFFSET_Y = HEIGHT - HEIGHT // 50 - 21.5

    for i in range(HEIGHT // 40):
        # first column of white squares
        stamp_square(white_square, FIRST_ROW_X, BASE_Y - 43 * i)

        # second column of black squares
        stamp_square(black_square, SECOND_ROW_X, BASE_Y - 43 * i)

        # first column of black squares
        stamp_square(black_square, FIRST_ROW_X, OFFSET_Y - 43 * i)

        # second column of white squares
        stamp_square(white_square, SECOND_ROW_X, OFFSET_Y - 43 * i)

    return win, v_spacing, pen


def stamp_square(square, x, y):
    square.goto(x, y)
    square.stamp()


def place_turtles(v_spacing):
    # create objects for each turtle
    turtle_objs = []
    for i, turtle_name in enumerate(TURTLES, start=1):
        turtle = Turtle("turtle")
        turtle.color_str = TURTLES[turtle_name]
        turtle.name = turtle_name
        turtle.color(turtle.color_str)
        turtle.penup()
        curr_y = i * v_spacing
        turtle.goto(25, curr_y)
        turtle.pendown()
        turtle_objs.append(turtle)

    return turtle_objs


def race(turtle_objs, pen):
    # simulate race
    start = perf_counter()
    racing = True
    while racing:
        for turtle in turtle_objs:
            distance = randint(1, 20)
            turtle.forward(distance)
            x, _ = turtle.pos()

            if x >= WIDTH - WIDTH // 25:
                WINNER = turtle
                racing = False

    end = perf_counter()

    # draw black rectangle backdrop for winner's name
    pen.penup()
    pen.goto(-10, HEIGHT // 2 + 60)
    pen.color("black")
    pen.begin_fill()
    pen.forward(WIDTH + 10)
    pen.right(90)
    pen.forward(70)
    pen.right(90)
    pen.forward(WIDTH + 10)
    pen.right(90)
    pen.forward(70)
    pen.end_fill()

    # write winner's name
    pen.penup()
    pen.goto(WIDTH // 2, HEIGHT // 2)
    pen.down()
    pen.color(WINNER.color_str)
    pen.write(f"The winner is {WINNER.name}", align="center", font=("Deja Vu Sans Mono", 30, "normal"))

    return WINNER, end - start


def write_to_csv(*data, path="races.csv"):
    with open(path, "a", newline="", encoding="utf_8") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(data)


def process_csv(path="races.csv"):
    with open(path, encoding="utf_8") as csvfile:
        reader = csv.reader(csvfile)
        data = [(turtle, float(duration)) for turtle, duration in reader]

    # populate dict with data
    stats = {}
    for turtle, duration in data:
        if turtle not in stats:
            stats[turtle] = [duration]
        else:
            stats[turtle].append(duration)

    create_graphs(stats)


def create_graphs(stats):
    # text size constants
    MEDIUM_SIZE = 14
    BIGGER_SIZE = 20

    # set style
    plt.style.use("seaborn")

    # create subplots
    _, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # create scatter graph
    for turtle in stats:
        ax1.scatter(stats[turtle], [" "] * len(stats[turtle]), label=turtle, marker="x", c=TURTLES[turtle], s=80)

    # scatter graph design changes
    ax1.invert_xaxis()
    ax1.set_title("Winning Time for Each Race", fontsize=BIGGER_SIZE)
    ax1.set_xlabel("Time (s)", fontsize=MEDIUM_SIZE)
    ax1.legend()

    # create pie chart
    _, texts, autotexts = ax2.pie(
        [len(stats[turtle]) for turtle in stats],
        labels=stats.keys(),
        autopct="%1.1f%%",
        radius=1.2,
        colors=[TURTLES[turtle] for turtle in stats],
        center=(0, 40),
        textprops={"fontsize": MEDIUM_SIZE, "weight": "bold"},
        wedgeprops={"linewidth": 1.5, "edgecolor": "black"},
    )

    # make pie % values white unless turtle is Lemon
    for text, autotext in zip(texts, autotexts):
        if text.get_text() != "Lemon":
            autotext.set_color("white")

    # pie chart design changes
    no_of_races = len(sum(stats.values(), []))
    ax2.set_title(f"Win Distribution of {no_of_races} races", fontsize=BIGGER_SIZE, y=1.08)

    # export as image
    plt.savefig("stats_graphs.png", bbox_inches="tight")


if __name__ == "__main__":
    main()
