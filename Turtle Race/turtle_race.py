# turtle_race.py

from turtle import Turtle, Screen
from random import randint
from time import sleep

TURTLES = {
    "Verdant": "green",
    "Lapis": "blue",
    "Selwyn": "purple",
    "Knight": "yellow",
    "Shade": "black",
}

WIDTH, HEIGHT = 1000, 500


def main():
    v_spacing, pen = draw_screen(len(TURTLES))
    turtle_objs = place_turtles(v_spacing)
    WINNER, moves = race(turtle_objs, pen)
    write_to_csv(WINNER.name, moves)
    sleep(5)


def draw_screen(RACERS_COUNT):
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
    WHITE_LINES = RACERS_COUNT + 1
    v_spacing = HEIGHT // WHITE_LINES
    for i in range(WHITE_LINES):
        pen.penup()
        pen.goto(0, i * v_spacing + v_spacing // 2)
        pen.pendown()
        pen.forward(WIDTH)

    return v_spacing, pen


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
    moves = 0
    racing = True
    while racing:
        for turtle in turtle_objs:
            distance = randint(1, 20)
            turtle.forward(distance)
            x, _ = turtle.pos()

            if x >= WIDTH - WIDTH // 25:
                WINNER = turtle
                racing = False
        moves += 1

    # write winner's name
    pen.color(WINNER.color_str)
    pen.penup()
    pen.goto(WIDTH // 2, HEIGHT // 2)
    pen.down()
    pen.write("The winner is " + WINNER.name, align="center", font=("Roman", 30, "bold"))

    return WINNER, moves


def write_to_csv(*data, path="races.csv"):
    import csv

    with open(path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(data)


def process_csv(path="races.csv"):
    from collections import Counter
    from operator import itemgetter
    import csv

    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        moves = []
        for row in reader:
            moves.append((row[0], int(row[1])))

    stats = {}
    longest_win = moves[0]
    shortest_win = moves[0]
    total_moves = 0
    for move in moves:
        if move[1] > longest_win[1]:
            longest_win = move
        if move[1] < shortest_win[1]:
            shortest_win = move
        if move[0] not in stats:
            stats[move[0]] = 1
        else:
            stats[move[0]] += 1
        total_moves += move[1]

    stats = dict(sorted(stats.items(), key=itemgetter(1), reverse=True))

    for stat in stats.items():
        print(stat[0], "has", stat[1], "win(s)")

    print(longest_win[0], "has the longest win with", longest_win[1], "moves")
    print(shortest_win[0], "has the shorted win with", shortest_win[1], "moves")
    print(f"On average a turtle wins in {total_moves // len(moves)} moves")


if __name__ == "__main__":
    main()
    process_csv()