"""Program which draws a grid on a graphics window using a specified size. A person is drawn in the centre of the grid 
and they will move in random directions until they leave the grid."""

import time
from random import random

import matplotlib.pyplot as plt
import numpy as np
from graphics import Circle, GraphWin, Line, Point, Rectangle, Text


def main(squares=None):
    if squares is None:
        squares = get_input()
    elif squares % 2 == 0:
        squares += 1
        squares = min(19, squares)

    squares_with_border = squares + 1
    win, person, square_texts = draw_grid(squares_with_border)
    total_steps = simulate_steps(win, person, squares, square_texts)
    win.close()
    return total_steps, squares


def get_input():
    while True:
        try:
            squares = int(
                input("\nEnter the grid size (must be an odd number more than 2 and less than 20): > ").strip()
            )
            if squares % 2 == 0:
                raise ValueError("please enter an odd number")
            elif squares < 3:
                raise ValueError("please enter a number greater than 2")
            elif squares > 19:
                raise ValueError("please enter a number less than 20")
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

    print(f"\nIt took {total_steps} steps to leave a grid of size {squares}\n")

    return total_steps


def draw_step(win, person, x, y):
    person.move(x, y)
    time.sleep(0.1)


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
                # [walks, steps, average, high, low]
                stats[stat_key] = [1, int(row[0]), int(row[0]), int(row[0]), int(row[0])]
            else:
                stats[stat_key][0] += 1  # walks
                stats[stat_key][1] += int(row[0])  # steps
                stats[stat_key][3] = max(stats[stat_key][3], int(row[0]))  # high
                stats[stat_key][4] = min(stats[stat_key][4], int(row[0]))  # low

    print(("{}" + "{:>10}" * 5).format("Size", "Walks", "Steps", "Avg", "High", "Low"))
    for size, stat_value in stats.items():
        walks, steps, max_steps, min_steps = stat_value[0], stat_value[1], stat_value[3], stat_value[4]
        ronded_avg = round(steps / walks, 1)
        stats[size][2] = ronded_avg  # avg
        print(("{:>4}" + "{:>10}" * 5).format(size, walks, steps, ronded_avg, max_steps, min_steps))

    return stats


def display_results(stats):
    x = stats.keys()

    # high and low steps
    plt.title("Highest and Lowest Number of Steps it has Taken to Leave a Grid of a Certain Size")
    plt.xlabel("Grid Size")
    plt.ylabel("# of steps")

    y = [y[3] for y in stats.values()]
    plt.plot(x, y, label="Highest steps", marker="o")

    y = [y[4] for y in stats.values()]
    plt.plot(x, y, label="Lowest steps", marker="o")

    plt.legend()
    display_graph("high-low.png")

    # avg steps
    plt.title("Average Number of Steps it takes Leave a Grid of a Certain Size")
    plt.ylabel("Average # of steps")
    plt.xlabel("Grid Size")

    y = [y[2] for y in stats.values()]
    plt.bar(x, y)

    display_graph("average.png")


def display_graph(out_file):
    plt.grid(True)
    plt.tight_layout()
    plt.show(block=False)
    plt.waitforbuttonpress()
    plt.savefig(out_file)
    plt.close()


if __name__ == "__main__":
    total_steps, squares = main()
    write_to_csv(total_steps, squares)
    stats = process_csv()
    display_results(stats)
