# patchwork_sampler.py
# fmt: off
"""Program which displays a patchwork using inputs given by the user. The patchwork layout and patterns are specific to 
my student number. This code uses input functions so must be ran using the Python interpreter or at a read/write command
line."""

from graphics import GraphWin, Line, Circle, Point, Rectangle, Text


def main():
    size, colours = get_inputs()
    win, colour_tracker, tiles = create_patchwork(size, colours)
    cycle_colours(win, size, colours, colour_tracker, tiles)
    print("\nGoodbye!")
    win.close()


def get_inputs():
    """Ask user for the patchwork size and colours."""
    sizes = ["4", "5", "6", "7", "8"]
    size = ""

    while size not in sizes:
        size = input("\nEnter how many tiles long the square patchwork should be (" + concat_list(sizes, "or ") + "): ").strip()
        print(f"The patchwork will be a {size} x {size} grid" if size in sizes else "Error: invalid size")

    valid_colours = ["red", "green", "blue", "orange", "brown", "pink"]
    colours = []

    while len(colours) < 3:
        print("\nThe available colours are: ", end="")
        print(concat_list(valid_colours, "and, "))
        colour = input("Enter one of the above colours: ").lower().strip()

        if colour in valid_colours:
            colours.append(colour)
            valid_colours.remove(colour)
            print(colour.capitalize(), "is valid")
        elif colour in colours:
            print("Error:", colour, "already chosen")
        else:
            print("Error: invalid colour")

    print("\nYou have chosen... ", end="")
    print(concat_list(colours, "and, "))

    return int(size), colours


def concat_list(lst, condition):
    """Takes a list and returns a concatenated string of comma separated elements. The condition is a string which is 
    used as the separator for the final element."""
    return "".join(lst[i] + ", " if i < len(lst) - 1 else condition + lst[i] for i in range(len(lst)))


def create_patchwork(size, colours):
    """Creates the graphics window and calls the three different patches that make up the patchwork."""
    win = GraphWin("Patchwork sampler", 100 * (size + 2), 100 * (size + 2))
    win.setBackground("white")
    win.setCoords(0, size + 2, size + 2, 0)

    # initialise empty list which will be filled
    # up with the shapes that make up the patchwork
    tiles = [None] * size ** 2

    # initialise list tracking the
    # current colour of each tile
    colour_tracker = [0] * size ** 2

    # only need to supply colour_tracker to the second and third patches as
    # by default all values of the colour_tracker start with the first colour
    first_patch(win, size, colours[0], tiles)
    second_patch(win, size, colours[1], colour_tracker, tiles)
    third_patch(win, size, colours[2], colour_tracker, tiles)

    return win, colour_tracker, tiles


def first_patch(win, size, colour, tiles):
    """Calls net_design to draw a perimeter of net tiles at the specified positions using the first chosen colour."""
    for row in range(1, size + 1):
        net_design(win, size, colour, 1, row, tiles)  # left column of tiles
        net_design(win, size, colour, size, row, tiles)  # right column of tiles

    for col in range(2, size):
        net_design(win, size, colour, col, 1, tiles)  # top row of tiles
        net_design(win, size, colour, col, size, tiles)  # bottom row of tiles


def second_patch(win, size, colour, colour_tracker, tiles):
    """Calls circle_design to draw an inverted staircase of circle tiles at the specified positions using the second 
    chosen colour."""
    stop_col = size - 1
    for row in range(2, size):
        for col in range(2, stop_col + 1):
            circle_design(win, size, colour, col, row, tiles)
            current_tile_pos = get_current_tile_pos(size, col, row)
            colour_tracker[current_tile_pos] = 1
        stop_col -= 1


def third_patch(win, size, colour, colour_tracker, tiles):
    """Calls circle_design to draw a staircase of circle tiles at the specified positions using the third chosen colour."""
    stop_col = 2
    for row in range(size - 1, 2, -1):
        for col in range(size - 1, stop_col, -1):
            circle_design(win, size, colour, col, row, tiles)
            current_tile_pos = get_current_tile_pos(size, col, row)
            colour_tracker[current_tile_pos] = 2
        stop_col += 1


def net_design(win, size, colour, col, row, tiles):
    """Draws the net design using the supplied position and colour."""
    current_tile = []
    for distance in (0.2, 0.4, 0.6, 0.8, 1):
        draw_line(win, colour, (col, distance + row), (col + distance, row), current_tile)
        draw_line(win, colour, (col + 1 - distance, row), (col + 1, row + distance), current_tile)

    for distance in (0.2, 0.4, 0.6, 0.8):
        draw_line(win, colour, (col + distance, row + 1), (col + 1, row + distance), current_tile)
        draw_line(win, colour, (col, row + distance), (col + 1 - distance, row + 1), current_tile)

    # draw black border for current tile
    draw_rectangle(win, "black", (col, row), (col + 1, row + 1), current_tile, False)

    # store current_tile in a list of ordered tiles
    current_tile_pos = get_current_tile_pos(size, col, row)
    tiles[current_tile_pos] = current_tile


def circle_design(win, size, colour, col, row, tiles):
    """Draws the circle design using the supplied position and colour."""
    current_tile = []
    for width in (0.1, 0.3, 0.5, 0.7, 0.9):
        for height in (0.1, 0.3, 0.5, 0.7, 0.9):
            # draw filled circle
            draw_circle(win, colour, (width + col, height + row), 0.1, current_tile, True)

            if width in (0.3, 0.7):
                # draw horizontal white rectangle
                draw_rectangle(win, "white", (width + col - 0.1, height + row), (width + col + 0.1, height + row + 0.1), current_tile, True)
            else:
                # draw vertical white rectangle
                draw_rectangle(win, "white", (width + col - 0.1, height + row - 0.1), (width + col, height + row + 0.1), current_tile, True)

            # draw outlined circle
            draw_circle(win, colour, (width + col, height + row), 0.1, current_tile, False)

    # draw black border for current tile
    draw_rectangle(win, "black", (col, row), (col + 1, row + 1), current_tile, False)

    # store current_tile in a list of ordered tiles
    current_tile_pos = get_current_tile_pos(size, col, row)
    tiles[current_tile_pos] = current_tile


def cycle_colours(win, size, colours, colour_tracker, tiles):
    """User can endlessly click tiles to cycle their colour. Clicking the whitespace outside the patchwork will exit the
    program."""
    while True:
        cursor = win.getMouse()
        col = int(cursor.getX())
        row = int(cursor.getY())
        current_tile_pos = get_current_tile_pos(size, col, row)

        if 1 <= row <= size and 1 <= col <= size:
            colour_n = (colour_tracker[current_tile_pos] + 1) % 3
            colour_tracker[current_tile_pos] = colour_n

            undraw_shapes(win, current_tile_pos, tiles)
            redraw_shapes(win, size, colours[colour_n], col, row, tiles)
        else:
            break


def draw_line(win, colour, point1, point2, current_tile):
    "Helper function for drawing lines."
    current_line = Line(Point(point1[0], point1[1]), Point(point2[0], point2[1]))
    current_line.setWidth(2)
    current_line.setFill(colour)
    current_line.draw(win)
    current_tile.append(current_line)


def draw_circle(win, colour, centre, radius, current_tile, fill):
    "Helper function for drawing circles."
    current_circle = Circle(Point(centre[0], centre[1]), radius)
    if fill:
        current_circle.setFill(colour)
    else:
        current_circle.setOutline(colour)
    current_circle.setOutline(colour)
    current_circle.draw(win)
    current_tile.append(current_circle)


def draw_rectangle(win, colour, point1, point2, current_tile, fill):
    "Helper function for drawing rectangles."
    current_rectangle = Rectangle(Point(point1[0], point1[1]), Point(point2[0], point2[1]))
    if fill:
        current_rectangle.setFill(colour)
    current_rectangle.setOutline(colour)
    current_rectangle.draw(win)
    current_tile.append(current_rectangle)


def get_current_tile_pos(size, col, row):
    """Return the position within the patchwork of the current tile."""
    return (row - 1) * (size - 1) + (col - 1) + (row - 1)


def undraw_shapes(win, current_tile_pos, tiles):
    """Undraw the shapes that make up the provided tile index."""
    current_tile = tiles[current_tile_pos]
    for shape in current_tile:
        shape.undraw()


def redraw_shapes(win, size, colour, col, row, tiles):
    """Redraw the shapes that make up the previously undrawn tile using the next colour in the list of chosen colours."""
    if row == 1 or row == size or col == 1 or col == size:
        net_design(win, size, colour, col, row, tiles)
    else:
        circle_design(win, size, colour, col, row, tiles)


main()