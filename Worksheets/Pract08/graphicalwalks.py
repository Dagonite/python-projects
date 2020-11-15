from pract05 import distance_between_points
from random import random
from graphics import *


'''
4.
Write another random walk program graphicalwalks.py that graphically simulates
two dimensional random walks. Each walk should end when the walker is a specified
distance way from the start point. The program should begin by asking the user for
this distance and the number of walks to simulate. It should then draw a circle
in the centre of a graphics window showing the boundary of the walking area. The
route of each random walk should be traced out starting from the centre point. Use
a black line of length 5 for each step of the walk. (Hint: the step lines should
fill out the circle evenly – if all the walks tend to head in one general direction
then you have made a mistake.)
'''
def main():
    num_walks, distance = get_inputs()
    win = draw_window(distance)
    take_walks(win, num_walks, distance)


def get_inputs():
    while True:
        num_walks = input("Enter the number of random walks: ")
        num_walks = num_walks.replace(" ", "")

        if num_walks.isdigit():
            break

    while True:
        distance = input("Enter the maximum distance for each walk: ")
        distance = distance.replace(" ", "")

        if distance.isdigit():
            break

    return int(num_walks), int(distance)


def draw_window(distance):
    win = GraphWin("Graphical walks", 500, 500)
    win.setCoords(0, 0, distance * 2, distance * 2)
    circle = Circle(Point(distance, distance), distance)
    circle.draw(win)
    return win


def take_walks(win, num_walks, distance):
    for walk in range(num_walks):
        take_a_walk(win, distance)


def take_a_walk(win, distance):
    steps_away = 0
    colour = "black"
    start = Point(distance, distance)
    current_x = start.getX()
    current_y = start.getY()
    while steps_away < distance:
        random_step = random()
        if random_step < 0.25:
            current_y += 1
            step = "north"
        elif random_step >= 0.25 and random_step < 0.5:
            current_x += 1
            step = "east"
        elif random_step >= 0.5 and random_step < 0.75:
            current_y -= 1
            step = "south"
        else:
            current_x -= 1
            step = "west"

        current_pos = Point(current_x, current_y)
        steps_away = distance_between_points(start, current_pos)
        #print(f"Stepping {step}: {steps_away:.2f} steps away")

        if steps_away >= distance:
            colour = "red"

        draw_walk(win, start, current_pos, colour)


def draw_walk(win, start, current_pos, colour):
    line = Line(start, current_pos)
    line.setFill(colour)
    line.draw(win)


main()
