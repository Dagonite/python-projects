"""
Program which draws a grid on a graphics window using a specified size. A person
is drawn at the centre of the grid and they will move in random directions until
they leave the grid.
"""

import csv
import time
from random import random

from graphics import Circle, GraphWin, Line, Point, Rectangle, Text


def main(squares=None):
    if squares is None or squares % 2 == 0:
        squares = get_input()

    squares_with_border = squares + 1
    win, person, square_texts = draw_grid(squares_with_border)
    total_steps = simulate_steps(person, squares, square_texts)
    win.close()
    write_to_csv(total_steps, squares)
    process_csv()


def get_input():
    while True:
        try:
            squares = int(input("\nEnter the grid size (must be an odd number more than 2 and less than 20): > ").strip())
            if squares % 2 == 0:
                raise ValueError("please enter an odd number")
            if squares < 3:
                raise ValueError("please enter a number greater than 2")
            if squares > 19:
                raise ValueError("please enter a number less than 20")
            break
        except ValueError as error:
            print(error)

    return squares


def draw_grid(size):
    squares = size - 1
    win = GraphWin("Graphical traced walk", 50 * size, 50 * size)
    win.setCoords(0, size, size, 0)

    border_rectangle = Rectangle(Point(0.5, 0.5), Point(size - 0.5, size - 0.5)).draw(win)
    border_rectangle.setFill("gray")
    border_rectangle.setWidth(2)

    centre_square = Rectangle(
        Point(size / 2 - 0.5, size / 2 - 0.5),
        Point(size / 2 + 0.5, size / 2 + 0.5),
    ).draw(win)
    centre_square.setFill("cyan")
    centre_square.setOutline("")

    person = Circle(Point(size / 2, size / 2), 0.25).draw(win)
    person.setFill("red")

    square_texts = [[""] * squares for _ in range(squares)]

    for i in range(squares):
        for j in range(squares):
            # Grid lines
            Line(Point(1.5 + j, 0.5), Point(1.5 + j, size - 0.5)).draw(win)
            Line(Point(0.5, 1.5 + j), Point(size - 0.5, 1.5 + j)).draw(win)

            # Text within each square
            square_text = Text(Point(1 + j, 1 + i), "").draw(win)
            square_texts[i][j] = square_text

    return win, person, square_texts


def simulate_steps(person, squares, square_texts):
    total_steps = 0
    grid = [[0] * squares for _ in range(squares)]
    current_col = current_row = int(squares / 2)
    time.sleep(1)

    while True:
        random_step = random()
        total_steps += 1
        if random_step < 0.25:
            current_row -= 1  # Go up
            draw_step(person, 0, -1)
        elif random_step >= 0.25 and random_step < 0.5:
            current_col += 1  # Go right
            draw_step(person, 1, 0)
        elif random_step >= 0.5 and random_step < 0.75:
            current_row += 1  # Go down
            draw_step(person, 0, 1)
        else:
            current_col -= 1  # Go left
            draw_step(person, -1, 0)

        # Break if person leaves the grid
        if current_row == -1 or current_row == squares or current_col == -1 or current_col == squares:
            break

        grid[current_row][current_col] += 1
        square_texts[current_row][current_col].setText(grid[current_row][current_col])

    print(f"\nIt took {total_steps} steps to leave a grid of size {squares}\n")

    return total_steps


def draw_step(person, x, y):
    person.move(x, y)
    time.sleep(0.1)


def write_to_csv(*data, path="traced_walks.csv"):
    with open(path, "a", newline="", encoding="utf_8") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(data)


def process_csv(path="traced_walks.csv"):
    with open(path, encoding="utf_8") as csvfile:
        reader = csv.reader(csvfile)
        data = [*reader]

    stats = {}
    for steps, size in data:
        steps = int(steps)
        if size not in stats:
            # [walks, steps, high, low]
            stats[size] = [1] + [steps] * 3
        else:
            stats[size][0] += 1  # Walks
            stats[size][1] += steps  # Steps
            stats[size][2] = max(stats[size][2], steps)  # High
            stats[size][3] = min(stats[size][3], steps)  # Low

    print(("{}" + "{:>10}" * 5).format("Size", "Walks", "Steps", "Avg", "High", "Low"))
    for size, (walks, steps, max_steps, min_steps) in stats.items():
        ronded_avg = round(steps / walks, 1)
        print(("{:>4}" + "{:>10}" * 5).format(size, walks, steps, ronded_avg, max_steps, min_steps))


if __name__ == "__main__":
    main()
