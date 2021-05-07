# graphical_traced_walk.py
"""Program which asks the user to pick a grid size and then draws a grid on a graphics window. A person is drawn in the 
centre and they will move in random directions until they leave the grid."""

import time
from random import random

from graphics import Circle, GraphWin, Line, Point, Rectangle, Text


def main(squares=0):
    if squares % 2 == 0:
        squares = get_inputs()

    squares_with_border = squares + 1
    win, person, square_texts = draw_grid(squares_with_border)
    total_steps = simulate_steps(win, person, squares, square_texts)
    write_to_csv(total_steps, squares)
    win.close()


def get_inputs():
    while True:
        try:
            squares = int(input("\nEnter the grid size (must be an odd number and more than 2): > ").strip())
            if squares % 2 == 0:
                raise ValueError("please enter an odd number")
            elif squares < 3:
                raise ValueError("please enter a number larger than 2")
            break
        except ValueError as error:
            print(error)

    return squares


def draw_grid(squares_with_border):
    squares = squares_with_border - 1
    win = GraphWin("Graphical traced walk", 50 * squares_with_border, 50 * squares_with_border)
    win.setCoords(0, squares_with_border, squares_with_border, 0)

    border_rectangle = Rectangle(Point(0.5, 0.5), Point(squares_with_border - 0.5, squares_with_border - 0.5)).draw(win)
    border_rectangle.setFill("gray")
    border_rectangle.setWidth(2)

    centre_square = Rectangle(
        Point(squares_with_border / 2 - 0.5, squares_with_border / 2 - 0.5),
        Point(squares_with_border / 2 + 0.5, squares_with_border / 2 + 0.5),
    ).draw(win)
    centre_square.setFill("cyan")
    centre_square.setOutline("")

    person = Circle(Point(squares_with_border / 2, squares_with_border / 2), 0.25).draw(win)
    person.setFill("red")

    square_texts = [[""] * squares for _ in range(squares)]

    for i in range(squares):
        for j in range(squares):
            # grid lines
            Line(Point(1.5 + j, 0.5), Point(1.5 + j, squares_with_border - 0.5)).draw(win)
            Line(Point(0.5, 1.5 + j), Point(squares_with_border - 0.5, 1.5 + j)).draw(win)

            # text within each square
            square_text = Text(Point(1 + j, 1 + i), "").draw(win)
            square_texts[i][j] = square_text

    return win, person, square_texts


def simulate_steps(win, person, squares, square_texts):
    total_steps = 0
    grid = [[0] * squares for _ in range(squares)]
    current_col = current_row = int(squares / 2)
    time.sleep(1)

    while True:
        random_step = random()
        total_steps += 1
        if random_step < 0.25:
            current_row -= 1  # go up
            draw_step(win, person, 0, -1)
        elif random_step >= 0.25 and random_step < 0.5:
            current_col += 1  # go right
            draw_step(win, person, 1, 0)
        elif random_step >= 0.5 and random_step < 0.75:
            current_row += 1  # go down
            draw_step(win, person, 0, 1)
        else:
            current_col -= 1  # go left
            draw_step(win, person, -1, 0)

        # break if person leaves the grid
        if current_row == -1 or current_row == squares or current_col == -1 or current_col == squares:
            break

        grid[current_row][current_col] += 1
        square_texts[current_row][current_col].setText(grid[current_row][current_col])

    print(f"\nIt took {total_steps} steps to leave a grid of size {squares}")

    return total_steps


def draw_step(win, person, x, y):
    person.move(x, y)
    time.sleep(0.25)


def write_to_csv(*data, path="traced_walks.csv"):
    import csv

    with open(path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(data)


def process_csv(path="traced_walks.csv"):
    import csv

    stats = {}

    with open(path) as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            stat_key = row[1]
            if stat_key not in stats:
                stats[stat_key] = [0, 0]
            stats[stat_key][0] += int(row[0])
            stats[stat_key][1] += 1

    for stat_key, stat_value in stats.items():
        print(f"On average it has taken {stat_value[0]/stat_value[1]} steps to leave a grid of size {stat_key}")


if __name__ == "__main__":
    process_csv()
