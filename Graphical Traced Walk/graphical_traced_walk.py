from random import random
from graphics import GraphWin, Line, Text, Circle, Rectangle, Point
import time


def main():
    squares = get_inputs()
    squares_with_border = squares + 1
    win, person, square_texts = draw_grid(squares_with_border)
    simulate_steps(win, person, squares, square_texts)


def get_inputs():
    while True:
        squares = input("\nEnter the common height and width of the grid (must "
                        "be an odd number): ")
        squares.replace(" ", "")
        if squares.isdigit():
            squares = int(squares)
            if squares % 2 == 0:
                print("Error: number is not odd")
                continue
            if squares < 3:
                print("Error: number too low")
                continue
            break
        else:
            print("Error: invalid input")

    return squares


def draw_grid(squares_with_border):
    squares = squares_with_border - 1
    win = GraphWin("Graphical traced walk",
                   50 * squares_with_border,
                   50 * squares_with_border)
    win.setCoords(0, squares_with_border,
                  squares_with_border, 0)

    border_rectangle = Rectangle(Point(.5, .5),
                                 Point(squares_with_border - .5,
                                       squares_with_border - .5))
    border_rectangle.setFill("gray")
    border_rectangle.setWidth(2)
    border_rectangle.draw(win)

    centre_square = Rectangle(Point(squares_with_border / 2 - .5,
                                    squares_with_border / 2 - .5),
                              Point(squares_with_border / 2 + .5,
                                    squares_with_border / 2 + .5))
    centre_square.setFill("cyan")
    centre_square.setOutline("")
    centre_square.draw(win)

    person = Circle(Point(squares_with_border / 2,
                          squares_with_border / 2), .25)
    person.setFill("red")
    person.draw(win)

    square_texts = [[""] * squares for _ in range(squares)]

    for i in range(squares):
        for j in range(squares):
            grid_line = Line(Point(1.5 + j, .5),
                             Point(1.5 + j, squares_with_border - .5))
            grid_line.draw(win)

            grid_line = Line(Point(.5, 1.5 + j),
                             Point(squares_with_border - .5, 1.5 + j))
            grid_line.draw(win)

            square_text = Text(Point(1 + j, 1 + i), "")
            square_text.draw(win)
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
        if random_step < .25:
            current_row -= 1    # go up
            draw_step(win, person, 0, -1)
        elif random_step >= .25 and random_step < .5:
            current_col += 1    # go right
            draw_step(win, person, 1, 0)
        elif random_step >= .5 and random_step < .75:
            current_row += 1    # go down
            draw_step(win, person, 0, 1)
        else:
            current_col -= 1    # go left
            draw_step(win, person, -1, 0)

        if current_row == -1 or current_row == squares \
                or current_col == -1 or current_col == squares:
            break

        grid[current_row][current_col] += 1
        square_texts[current_row][current_col].setText(
            grid[current_row][current_col])

    print(f"\nIt took {total_steps} steps to leave the grid")
    win.getMouse()
    win.close()


def draw_step(win, person, x, y):
    person.move(x, y)
    time.sleep(.25)


main()
