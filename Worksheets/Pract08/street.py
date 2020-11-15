from random import random
from graphics import *


'''
6.
Write a new program street.py which draws a whole street (i.e. row) of houses like
those in the original house.py program. The user should input the number of houses,
the height of the graphics window, the (shared) door colour and the probability
that any light is on. The houses should be numbered (on their doors) starting from
1, and the houses should fill the graphics window.
'''
def main():
    houses, size, door_colour, prob = get_inputs()
    #houses, size, door_colour, prob = 8, 4, "red", .5
    draw_houses(houses, size, door_colour, prob)


def get_inputs():
    while True:
        houses = input("\nEnter the number of houses on the street: ")
        houses = houses.replace(" ", "")
        if houses.isdigit():
            houses = int(houses)
            if houses > 10:
                print("Error: Too many houses")
                continue
            elif houses < 1:
                print("Error: Must be at least 1 house")
                continue
            break
        else:
            print("Error: Input is not an integer")

    while True:
        size = input("\nEnter the size of the graphics window: ")
        size = size.replace(" ", "")
        if size.isdigit():
            size = int(size)
            if size > 10:
                print("Error: Number too big")
                continue
            elif size < 1:
                print("Error: Size must be at least 1")
                continue
            break
        else:
            print("Error: Input is not an integer")

    valid_door_colours = ["black", "red", "orange", "blue", "pink", "white"]
    door_colour = ""
    while door_colour not in valid_door_colours:
        print("\nThe available door colours are: ", end="")
        for i in range(len(valid_door_colours)):
            if i == len(valid_door_colours) - 1:
                print("and", valid_door_colours[i])
            else:
                print(valid_door_colours[i], end=", ")

        door_colour = input("Enter the shared door colour: ")
        door_colour = door_colour.replace(" ", "")
        if door_colour not in valid_door_colours:
            print("Error: Input is not a valid colour")

    while True:
        prob = input("\nEnter the % chance that a house's light is on (0 to 100): ")
        prob = prob.replace(" ", "")
        if prob.isdigit():
            prob = int(prob)
            if prob > 100:
                print("Error: Input out of range")
                continue
            break
        else:
            print("Error: Input is not an integer")

    return houses, size, door_colour, prob/100


def draw_houses(houses, size, door_colour, prob):
    win = GraphWin("Street", 50 * houses * size, 50 * size)
    win.setCoords(0, 0, houses * size, 1)

    for house in range(houses):
        lights_on = random()
        if lights_on > prob:
            lights_on = False
        else:
            lights_on = True
        draw_house(win, door_colour, lights_on, house, size)


def draw_house(win, door_colour, lights_on, n, size):
    roof = Polygon(Point(n * size + .01, .7), Point(n * size + .22, .992),
                   Point(size * (n + 1) - .22, .992), Point(size * (n + 1) - .008, .7))
    roof.setFill("pink")
    roof.draw(win)

    # draw wall and door
    draw_rectangle(win, Point(n * size + .008, .008),
                        Point(size * (n + 1) - .008, .7), "brown")

    draw_rectangle(win, Point(n * size + .15 * size, .008),
                        Point(size * (n + 1) - .6 * size, .45), door_colour)

    # draw door number
    door_n = Text(Point(n * size + .275 * size, .35), n + 1)
    door_n.setSize(4 + 2 * size)
    if door_colour == "black":
        door_n.setFill("white")
    door_n.draw(win)

    # draw window
    if lights_on:
        window_colour = "yellow"
    else:
        window_colour = "black"
    draw_rectangle(win, Point(n * size + .55 * size, .15),
                        Point(size * (n + 1) - .15 * size, .45), window_colour)


def draw_rectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.setFill(colour)
    rectangle.setOutline(colour)
    rectangle.draw(win)


main()
