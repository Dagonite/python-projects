from pract05 import distance_between_points
from random import random
from graphics import *


'''
3.
Modify the original one-dimensional random walk program described in this worksheet
to give a two-dimensional random walk program randomwalks2d.py. In this program,
instead of taking steps forwards and backwards, steps can be made in any direction:
north, east, south and west (with equal probability). The program should report
the expected distance from the starting point. (Hint: Make sure that the probability
of stepping in each direction is equal (i.e. 1/4). You might try to count the total
number of steps made in each direction to ensure that this is the case with your
program. Your program will probably include a function distance_between_points(x1,
y1, x2, y2) to calculate the distances from the start point.)
'''
def main():
    num_walks, num_steps = get_inputs()
    average_steps = take_walks(num_walks, num_steps)
    print_expected_distance(average_steps)


def get_inputs():
    num_walks = eval(input("How many random walks to take? "))
    num_steps = eval(input("How many steps for each walk? "))
    return num_walks, num_steps


def take_walks(num_walks, num_steps):
    total_steps = 0
    for walk in range(num_walks):
        steps_away = take_a_walk(num_steps)
        total_steps = total_steps + steps_away
    return total_steps / num_walks


def take_a_walk(num_steps):
    horizontal_steps = 0
    vertical_steps = 0
    for step in range(num_steps):
        random_step = random()
        if random_step < 0.25:
            vertical_steps += 1
        elif random_step >= 0.25 and random_step < 0.5:
            horizontal_steps += 1
        elif random_step >= 0.5 and random_step < 0.75:
            vertical_steps -= 1
        else:
            horizontal_steps -= 1

    steps = distance_between_points(Point(0, 0), Point(horizontal_steps, vertical_steps))
    return abs(steps)


def print_expected_distance(average_steps):
    print("The expected number of steps away from the start point is {:.2f}".format(average_steps))

main()
