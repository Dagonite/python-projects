# patchwork_sampler.py
# The patchwork layout and patterns are specific to my student number.

from graphics import GraphWin, Line, Circle, Point, Rectangle, Text


def main():
    size, colours = get_inputs()
    win, colour_tracker = create_patchwork(size, colours)
    cycle_colours(win, size, colours, colour_tracker)


def get_inputs():
    """
    Get user input to determine the size and colours of the patchwork.
    :return size: the size of the patchwork grid
    :return colours: list of colours being used
    """
    sizes = ["5", "7", "9"]
    size = ""

    while size not in sizes:
        size = input("\nEnter how many tiles long the square patchwork should "
                     "be (5, 7, or 9): ")

        size = size.replace(" ", "")

        if size in sizes:
            print(f"The patchwork will be a {size} x {size} grid")
        else:
            print("Error: Invalid size")

    valid_colours = ["red", "green", "blue", "orange", "brown", "pink"]
    colours = []

    while len(colours) < 3:
        print("\nThe available colours are: ", end="")
        print_colours(valid_colours)
        colour = input("Enter one of the above colours: ").lower()

        colour = colour.replace(" ", "")

        if colour in valid_colours:
            colours.append(colour)
            valid_colours.remove(colour)
            print(colour.capitalize(), "is valid")
        elif colour in colours:
            print("Error:", colour.capitalize(), "already chosen")
        else:
            print("Error: Invalid colour")

    print("You have chosen... ", end="")
    print_colours(colours)

    return int(size), colours


def print_colours(colours):
    """
    Prints out a list of colours by comma separating them.
    :return colours: list of colours
    :return: None
    """
    for i in range(len(colours)):
        if i == len(colours) - 1:
            print("and", colours[i])
        else:
            print(colours[i], end=", ")


def create_patchwork(size, colours):
    """
    Generates the three different patch types.
    :param win: the graphics window used to display the patchwork
    :param size: the size of the patchwork grid
    :param colours: list of colours being used
    :return colour_tracker: list of each tiles' current colour
    :return win: the graphics window used to display the patchwork
    """
    win = GraphWin("Patchwork sampler", 100 * size, 100 * (size + 1))
    win.setBackground("white")
    win.setCoords(0, size + 1, size, 0)

    quit_but = Rectangle(Point(size / 2 - .47, .8),
                         Point(size / 2 + .47, .2))
    quit_but.setFill("gray")
    quit_but.setWidth(3)
    quit_but.draw(win)

    quit_text = Text(Point(size / 2, .5), "Quit")
    quit_text.setSize(14)
    quit_text.setStyle("bold")
    quit_text.setFill("white")
    quit_text.draw(win)

    colour_tracker = [0] * size ** 2

    first_patch(win, size, colours[0])
    second_patch(win, size, colours[1], colour_tracker)
    third_patch(win, size, colours[2], colour_tracker)

    return win, colour_tracker


def first_patch(win, size, colour):
    """
    Creates the first patch which is a tile wide outline for the patchwork.
    :param win: the graphics window used to display the patchwork
    :param size: the size of the patchwork grid
    :param colour: the colour being used
    :return: None
    """
    for row in range(1, size + 1):
        # left column of tiles
        net_design(win, colour, 0, row)
        # right column of tiles
        net_design(win, colour, size - 1, row)

    for col in range(1, size - 1):
        # top-most row of tiles
        net_design(win, colour, col, 1)
        # bottom row of tiles
        net_design(win, colour, col, size)


def net_design(win, colour, col, row):
    """
    Creates the net design by drawing interlacing lines for a tile.
    :param win: the graphics window used to display the patchwork
    :param colour: the colour of the lines
    :param col: starting x co-ord for the design
    :param row: starting y co-ord for the design
    :return: None
    """
    for distance in (.2, .4, .6, .8, 1):
        line1 = Line(Point(col, distance + row),
                     Point(col + distance, row))
        line1.setWidth(2)
        line1.setFill(colour)
        line1.draw(win)

        line2 = Line(Point(col + 1 - distance, row),
                     Point(col + 1, row + distance))
        line2.setWidth(2)
        line2.setFill(colour)
        line2.draw(win)

    for distance in (.2, .4, .6, .8):
        line3 = Line(Point(col + distance, row + 1),
                     Point(col + 1, row + distance))
        line3.setWidth(2)
        line3.setFill(colour)
        line3.draw(win)

        line4 = Line(Point(col, row + distance),
                     Point(col + 1 - distance, row + 1))
        line4.setWidth(2)
        line4.setFill(colour)
        line4.draw(win)

    border_rectangle = Rectangle(Point(col, row), Point(col + 1, row + 1))
    border_rectangle.draw(win)


def second_patch(win, size, colour, colour_tracker):
    """
    Patch which forms a row of tiles (left-to-right) in the empty space of the
    second row. The following rows have 1 less tile than the row above until
    only 1 tile is in a single row.
    :param win: the graphics window used to display the patchwork
    :param size: the size of the patchwork grid
    :param colour: the colour being used
    :param colour_tracker: list of each tiles' current colour
    """
    # tiles will be drawn left to right up until this column
    stop_col = size - 1

    for row in range(2, size):
        for col in range(1, stop_col):
            circle_design(win, colour, col, row)

            # gives the tile's position in a list of length size^2
            # 1 subtracted from row because of top row dedicated to quit button
            current_tile = (row - 1) * (size - 1) + col + (row - 1)
            colour_tracker[current_tile] = 1
        stop_col -= 1


def third_patch(win, size, colour, colour_tracker):
    """
    Patch which forms a row of tiles (right-to-left) in the empty space of the
    second to last row. The aboes rows have 1 less tile than the row subsequent
    row below until only 1 tile is in a single row.
    :param win: the graphics window used to display the patchwork
    :param size: the size of the patchwork grid
    :param colour: the colour being used
    :param colour_tracker: 2d array of each tiles' current colour
    """
    # tiles will be drawn right to left up until this column
    stop_col = 1

    for row in range(size - 1, 2, -1):
        for col in range(size - 2, stop_col, -1):
            circle_design(win, colour, col, row)

            # gives the tile's position in a list of length size^2
            # 1 subtracted from row because of top row dedicated to quit button
            current_tile = (row - 1) * (size - 1) + col + (row - 1)
            colour_tracker[current_tile] = 2
        stop_col += 1


def circle_design(win, colour, col, row):
    """
    Creates the circle design by drawing filled circles half covered by
    white rectangles. Outlined circles are drawn over both the rectangles and
    the filled circles.
    :param win: the graphics window used to display the patchwork
    :param colour: the colour of the drawn shapes
    :param col: starting x co-ord for the design
    :param row: starting y co-ord for the design
    :return: None
    """
    for width in (.1, .3, .5, .7, .9):
        for height in (.1, .3, .5, .7, .9):
            full_circle = Circle(Point(width + col, height + row), .1)
            outline_circle = Circle(Point(width + col, height + row), .1)
            if width in (.3, .7):
                white_rectangle = Rectangle(Point(width + col - .1,
                                                  height + row),
                                            Point(width + col + .1,
                                                  height + row + .1))
            else:
                white_rectangle = Rectangle(Point(width + col - .1,
                                                  height + row - .1),
                                            Point(width + col,
                                                  height + row + .1))

            full_circle.setFill(colour)
            full_circle.draw(win)

            white_rectangle.setFill("white")
            white_rectangle.setOutline("white")
            white_rectangle.draw(win)

            outline_circle.setOutline(colour)
            outline_circle.draw(win)

    border_rectangle = Rectangle(Point(col, row), Point(col + 1, row + 1))
    border_rectangle.draw(win)


def cycle_colours(win, size, colours, colour_tracker):
    """
    Allows user to click on any of the tiles in the graphics window to cycle to
    another chosen colour.
    :param win: the graphics window used to display the patchwork
    :param size: the size of the patchwork grid
    :param colours: list of colours being used
    :param colour_tracker: list of each tiles' current colour
    :return: None
    """
    while True:
        cursor = win.getMouse()
        col = int(cursor.getX())
        row = int(cursor.getY())
        current_tile = (row - 1) * (size - 1) + col + (row - 1)

        if row >= 1:
            colour_n = (colour_tracker[current_tile] + 1) % 3
            colour_tracker[current_tile] = colour_n
            print()
            for i in range(3):
                print(colours[i].capitalize(), "tiles:",
                      colour_tracker.count(i))

            if row == 1 or row == size or col == 0 or col == size - 1:
                net_design(win, colours[colour_n], col, row)
            else:
                circle_design(win, colours[colour_n], col, row)
        elif col == int(size / 2) and row == 0:
            break
    print("\nGoodbye!")
    win.close()


main()
