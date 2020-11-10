# patchwork_sampler.py

# Requires John Zelle's simple object oriented graphics library to work.
# The patchwork patterns are specific to my student number.
# Stop console to exit the sampler once done.

from graphics import *
import numpy as np


def main():
    win, size, colours = get_inputs()
    colour_tracker = create_patchwork(win, size, colours)
    cycle_colours(win, size, colours, colour_tracker)


def get_inputs():
    """
    Gets user inputs to determine the size and colours of the patchwork.
    :return win: the graphics window used to display the patchwork
    :return size: the size of the patchwork grid
    :return colours: list of colours being used
    """
    sizes = [5, 7, 9]
    size = 0
    print("The three sizes are 5, 7, and 9")

    while size not in sizes:
        size = eval(input("Enter a size: "))

    print("The patchwork will be a", str(size) + "x" + str(size), "grid")

    available_colours = ["red", "green", "blue", "orange", "brown", "pink"]
    colours = []

    for i in range(3):
        while True:
            print("The available colours are: ", end="")
            print(*available_colours, sep=", ")
            colour = input("Enter an above colour: ").lower()
            if colour in colours:
                print("You have already chosen", colour)
            elif colour in available_colours:
                colours.append(colour)
                available_colours.remove(colour)
                break

    print("You have chosen...", end=" ")
    for i in range(3):
        if i == 2:
            print("and", colours[i])
        else:
            print(colours[i], end=", ")

    win = GraphWin("Patchwork sampler", 100 * size, 100 * size)
    win.setBackground("white")

    return win, size, colours


def create_patchwork(win, size, colours):
    """
    Generates the three different patch types onto the graphics window.
    :param win: the graphics window used to display the patchwork
    :param size: the size of the patchwork grid
    :param colours: list of colours being used
    :return colour_tracker: 2d array of each tiles' current colour
    """
    colour_tracker = [0] * size ** 2

    first_patch(win, size, colours[0])  # first patch always starts as colours[0] so don't need to return anything
    colour_tracker = second_patch(win, size, colours[1], colour_tracker)
    colour_tracker = third_patch(win, size, colours[2], colour_tracker)
    return colour_tracker


def first_patch(win, size, colour):
    """
    Creates the first patch which forms a tile outline for the patchwork.
    :param win: the graphics window used to display the patchwork
    :param size: the size of the patchwork grid
    :param colour: the colour being used
    :return: None
    """
    for width in range(size):
        net_design(win, colour, width * 100, 0)
        net_design(win, colour, width * 100, 100 * (size - 1))

    for height in range(size - 2):
        net_design(win, colour, 0, (height + 1) * 100)
        net_design(win, colour, 100 * (size - 1), (height + 1) * 100)


def second_patch(win, size, colour, colour_tracker):
    """
    Creates the second patch which forms a row of tiles (left-to-right) in the
    empty space of the second row, the third row repeats but with 1 less tile.
    This repeats until only 1 tile is created in a row.
    :param win: the graphics window used to display the patchwork
    :param size: the size of the patchwork grid
    :param colour: the colour being used
    :param colour_tracker: 2d array of each tiles' current colour
    :return colour_tracker: 2d array of each tiles' current colour
    """
    current_size = size
    for height in range(current_size - 2):
        for width in range(current_size - 2):
            circle_design(win, colour, (width + 1) * 100, (height + 1) * 100)
            x_pos = ((width + 1) * 100) // 100
            y_pos = ((height + 1) * 100) // 100
            current_tile = x_pos + y_pos + y_pos * (size - 1)
            colour_tracker[current_tile] = 1
        current_size -= 1
    return colour_tracker


def third_patch(win, size, colour, colour_tracker):
    """
    Creates the third patch which forms a row of tiles (right-to-left) in the
    empty space of the second to last row, the third to last row repeats but
    with 1 less tile. This repeats until only 1 title is created in a row.
    :param win: the graphics window used to display the patchwork
    :param size: the size of the patchwork grid
    :param colour: the colour being used
    :param colour_tracker: 2d array of each tiles' current colour
    :return colour_tracker: 2d array of each tiles' current colour
    """
    current_size = size
    for height in range(current_size - 3):
        for width in range(current_size - 3):
            circle_design(win, colour, 100 * size - width * 100 - 200, 100 * size - height * 100 - 200)
            x_pos = (100 * size - width * 100 - 200) // 100
            y_pos = (100 * size - height * 100 - 200) // 100
            current_tile = x_pos + y_pos + y_pos * (size - 1)
            colour_tracker[current_tile] = 2
        current_size -= 1
    return colour_tracker


def net_design(win, colour, x, y):
    """
    Creates the net design by drawing interlacing lines onto the graphics window.
    :param win: the graphics window used to display the patchwork
    :param colour: the colour of the lines
    :param x: starting x co-ord for the design
    :param y: starting y co-ord for the design
    :return: None
    """
    for distance in (20, 40, 60, 80, 100):
        line = Line(Point(x, distance + y), Point(x + distance, y))
        line.setWidth(2)
        line.setFill(colour)
        line.draw(win)

        line = Line(Point(x + 100 - distance, y), Point(x + 100, y + distance))
        line.setWidth(2)
        line.setFill(colour)
        line.draw(win)

    for distance in (20, 40, 60, 80):
        line = Line(Point(x + distance, y + 100), Point(x + 100, y + distance))
        line.setWidth(2)
        line.setFill(colour)
        line.draw(win)

        line = Line(Point(x, y + distance), Point(x + 100 - distance, y + 100))
        line.setWidth(2)
        line.setFill(colour)
        line.draw(win)


def circle_design(win, colour, x, y):
    """
    Creates the circle design by drawing filled red circles half covered by
    white rectangles. Red outlined circles are drawn over the red circles.
    :param win: the graphics window used to display the patchwork
    :param colour: the colour of the drawn shapes
    :param x: starting x co-ord for the design
    :param y: starting y co-ord for the design
    :return: None
    """
    for width in (10, 30, 50, 70, 90):
        for height in (10, 30, 50, 70, 90):
            fill_circle = Circle(Point(width + x, height + y), 10)
            outline_circle = Circle(Point(width + x, height + y), 10)
            if width in (30, 70):
                white_rectangle = Rectangle(Point(width + x - 10, height + y), Point(width + x + 10, height + y + 10))
            else:
                white_rectangle = Rectangle(Point(width + x - 10, height + y - 10), Point(width + x, height + y + 10))

            fill_circle.setFill(colour)
            fill_circle.draw(win)

            white_rectangle.setFill("white")
            white_rectangle.setOutline("white")
            white_rectangle.draw(win)

            outline_circle.setOutline(colour)
            outline_circle.draw(win)


def cycle_colours(win, size, colours, colour_tracker):
    """
    Allows the user to click on any of the tiles in the graphics window to cycle
    to one of the chosen colours.
    :param win: the graphics window used to display the patchwork
    :param size: the size of the patchwork grid
    :param colours: list of colours being used
    :param colour_tracker: 2d array of each tiles' current colour
    :return: None
    """
    colour_tracker = np.array(colour_tracker)
    print(colour_tracker.reshape(size, size), "\n")

    for i in range(15):
        cursor = win.getMouse()
        x = cursor.getX()
        y = cursor.getY()
        x_pos = x // 100
        y_pos = y // 100
        current_tile = int(x_pos + y_pos + y_pos * (size - 1))
        colour = colour_tracker[current_tile] + 1

        if colour == 3:
            colour = 0

        if x < 100 or x > 100 * (size - 1) or y < 100 or y > 100 * (size - 1):
            net_design(win, colours[colour], x_pos * 100, y_pos * 100)
        else:
            circle_design(win, colours[colour], x_pos * 100, y_pos * 100)

        colour_tracker[current_tile] = colour
        print(colour_tracker.reshape(size, size), "\n")

    win.close()


main()
