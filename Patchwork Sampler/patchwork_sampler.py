"""
Program which displays a patchwork. The layout and patterns are specific to my
student number but a user can stipulate the patchwork size and colours. This
code uses the input() function so must be ran using the Python interpreter
(REPL).
"""
# pylint: disable=too-many-arguments

import random

from graphics import GraphWin, Line, Circle, Point, Rectangle


SIZES = ("4", "5", "6", "7", "8")
VALID_COLOURS = ("red", "green", "blue", "orange", "brown", "pink")


def main():
    """Program entry point."""
    size, colours = prompt_user_for_inputs()
    win, colour_tracker, tiles = create_patchwork(size, colours)
    cycle_colours(win, size, colours, colour_tracker, tiles)
    print("\nGoodbye!")
    win.close()


def prompt_user_for_inputs():
    """
    Call functions asking user for the patchwork size and colours then return
    these values.
    """
    size = prompt_user_for_patchwork_size()
    colours = prompt_user_for_patchwork_colours()
    return size, colours


def prompt_user_for_patchwork_size():
    """Ask user for the patchwork size."""
    while True:
        print(f"\nEnter one of the following sizes for the patchwork: {list_of_items(SIZES, conjunction='or')}")
        try:
            size = input("> ").strip()
            if size not in SIZES:
                raise ValueError("Error: invalid size")
        except ValueError as err:
            print(err)
        else:
            print(f"The patchwork will be a {size} x {size} grid")
            break

    return int(size)


def prompt_user_for_patchwork_colours():
    """Ask user for the patchwork colours."""
    colours = []
    while len(colours) < 3:
        print(f"\nEnter one of the following colours: {list_of_items(VALID_COLOURS, conjunction='or')}")
        print("Or (r)andomise your remaining options")
        try:
            colour = input("> ").lower().strip()
            if colour == "r":
                colours.extend(random.sample(VALID_COLOURS, 3 - len(colours)))
            elif colour in colours:
                raise ValueError(f"Error: {colour} already chosen")
            elif colour not in VALID_COLOURS:
                raise ValueError("Error: invalid colour")
        except ValueError as err:
            print(err)
        else:
            colours.append(colour)
            print(f"{colour.capitalize()} is valid")

    print(f"\nYou have chosen... {list_of_items(colours, conjunction='and')}")
    return colours


def list_of_items(items, *, conjunction):
    """
    Return a concatenated string of comma separated items. The conjuction is a
    string which is used as the separator for the last list item.
    """
    return f"{', '.join(items[:-1])}, {conjunction} {items[-1]}"


def create_patchwork(size, colours):
    """
    Create a graphics window and call the three different patches that make up
    the patchwork.
    """
    win = GraphWin("Patchwork sampler", 100 * (size + 2), 100 * (size + 2))
    win.setBackground("white")
    win.setCoords(0, size + 2, size + 2, 0)

    # Initialise a list of length size^2 which will be filled up with the shapes
    # that make up the patchwork later
    tiles = [None] * size ** 2

    # Initialise a list tracking the current colour of each tile. For
    # convenience, make all of the values 0 -- the initial colour of the first
    # patch. This way we don't need to supply colour_tracker as an arg for
    # first_patch()
    colour_tracker = [0] * size ** 2

    first_patch(win, size, colours[0], tiles)
    second_patch(win, size, colours[1], colour_tracker, tiles)
    third_patch(win, size, colours[2], colour_tracker, tiles)
    return win, colour_tracker, tiles


def first_patch(win, size, colour, tiles):
    """
    Call net_design() to draw a perimeter of net tiles at the specified
    positions.
    """
    for row in range(1, size + 1):
        net_design(win, size, colour, 1, row, tiles)  # Left column of tiles
        net_design(win, size, colour, size, row, tiles)  # Right column of tiles

    for col in range(2, size):
        net_design(win, size, colour, col, 1, tiles)  # Top row of tiles
        net_design(win, size, colour, col, size, tiles)  # Bottom row of tiles


def second_patch(win, size, colour, colour_tracker, tiles):
    """
    Call circle_design() to draw an inverted staircase of circle tiles at the
    specified positions.
    """
    stop_col = size
    for row in range(2, size):
        for col in range(2, stop_col):
            circle_design(win, size, colour, col, row, tiles)
            current_tile_pos = get_current_tile_pos(size, col, row)
            colour_tracker[current_tile_pos] = 1
        stop_col -= 1


def third_patch(win, size, colour, colour_tracker, tiles):
    """
    Call circle_design() to draw a staircase of circle tiles at the specified
    positions in the remaining space.
    """
    stop_col = 2
    for row in range(size - 1, 2, -1):
        for col in range(size - 1, stop_col, -1):
            circle_design(win, size, colour, col, row, tiles)
            current_tile_pos = get_current_tile_pos(size, col, row)
            colour_tracker[current_tile_pos] = 2
        stop_col += 1


def net_design(win, size, colour, col, row, tiles):
    """Draw the net design using the supplied position and colour."""
    current_tile = []
    for distance in (0.2, 0.4, 0.6, 0.8, 1):
        draw_line(win, colour, (col, distance + row), (col + distance, row), current_tile)
        draw_line(win, colour, (col + 1 - distance, row), (col + 1, row + distance), current_tile)

    for distance in (0.2, 0.4, 0.6, 0.8):
        draw_line(win, colour, (col + distance, row + 1), (col + 1, row + distance), current_tile)
        draw_line(win, colour, (col, row + distance), (col + 1 - distance, row + 1), current_tile)

    # Draw black border for current tile
    draw_rectangle(win, "black", (col, row), (col + 1, row + 1), current_tile)

    # Store current_tile in a list of ordered tiles
    current_tile_pos = get_current_tile_pos(size, col, row)
    tiles[current_tile_pos] = current_tile


def circle_design(win, size, colour, col, row, tiles):
    """Draw the circle design using the supplied position and colour."""
    current_tile = []
    for width in (0.1, 0.3, 0.5, 0.7, 0.9):
        for height in (0.1, 0.3, 0.5, 0.7, 0.9):
            # Draw filled circle
            draw_circle(win, colour, (width + col, height + row), 0.1, current_tile, fill=True)

            if width in (0.3, 0.7):
                # Draw horizontal white rectangle
                draw_rectangle(
                    win,
                    "white",
                    (width + col - 0.1, height + row),
                    (width + col + 0.1, height + row + 0.1),
                    current_tile,
                    fill=True,
                )
            else:
                # Draw vertical white rectangle
                draw_rectangle(
                    win,
                    "white",
                    (width + col - 0.1, height + row - 0.1),
                    (width + col, height + row + 0.1),
                    current_tile,
                    fill=True,
                )

            # Draw outlined circle
            draw_circle(win, colour, (width + col, height + row), 0.1, current_tile)

    # Draw black border for current tile
    draw_rectangle(win, "black", (col, row), (col + 1, row + 1), current_tile)

    # Store current_tile in a list of ordered tiles
    current_tile_pos = get_current_tile_pos(size, col, row)
    tiles[current_tile_pos] = current_tile


def cycle_colours(win, size, colours, colour_tracker, tiles):
    """
    User can endlessly click tiles to cycle the colours. Clicking the whitespace
    outside the patchwork will exit the program.
    """
    while True:
        cursor = win.getMouse()
        col, row = int(cursor.getX()), int(cursor.getY())
        current_tile_pos = get_current_tile_pos(size, col, row)

        if not all((1 <= vector <= size) for vector in (col, row)):
            break

        colour_n = (colour_tracker[current_tile_pos] + 1) % 3
        colour_tracker[current_tile_pos] = colour_n
        undraw_shapes(current_tile_pos, tiles)
        redraw_shapes(win, size, colours[colour_n], col, row, tiles)


def draw_line(win, colour, point1, point2, current_tile):
    """Helper function for drawing lines."""
    current_line = Line(Point(*point1), Point(*point2))
    current_line.setWidth(2)
    current_line.setFill(colour)
    current_line.draw(win)
    current_tile.append(current_line)


def draw_circle(win, colour, centre, radius, current_tile, fill=False):
    """Helper function for drawing circles."""
    current_circle = Circle(Point(*centre), radius)
    if fill:
        current_circle.setFill(colour)
    else:
        current_circle.setOutline(colour)
    current_circle.setOutline(colour)
    current_circle.draw(win)
    current_tile.append(current_circle)


def draw_rectangle(win, colour, point1, point2, current_tile, fill=False):
    """Helper function for drawing rectangles."""
    current_rectangle = Rectangle(Point(*point1), Point(*point2))
    if fill:
        current_rectangle.setFill(colour)
    current_rectangle.setOutline(colour)
    current_rectangle.draw(win)
    current_tile.append(current_rectangle)


def get_current_tile_pos(size, col, row):
    """Return the position within the patchwork of a tile using its vectors."""
    return (row - 1) * (size - 1) + (col - 1) + (row - 1)


def undraw_shapes(current_tile_pos, tiles):
    """Using the provided tile position undraw the shapes that make up a tile."""
    current_tile = tiles[current_tile_pos]
    for shape in current_tile:
        shape.undraw()


def redraw_shapes(win, size, colour, col, row, tiles):
    """
    Determine what tile design needs to be drawn then call the relevant design
    function with the next colour for that tile.

    If the supplied vectors point to a perimeter tile, draw the net design.
    Otherwise draw the circle design.
    """
    if any(vector in (1, size) for vector in (col, row)):
        net_design(win, size, colour, col, row, tiles)
    else:
        circle_design(win, size, colour, col, row, tiles)


if __name__ == "__main__":
    main()
