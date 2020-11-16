from random import random


'''
6.
Recall the one-dimensional random walk program from pract08 that simulated
several random walks in order to estimate the expected distance away from the
start point. Write a similar program tracedwalk.py that simulates a single random
walk that begins in the centre point of a pavement that is n steps (or squares)
long (the value of n should be input be the user). The program should keep a count
of how many times the walker steps upon each square of the pavement. The walk ends
when the walker steps off either end of the pavement. For example, if the pavement
is 5 squares long, the walker begins on square 3. If the random walk takes steps
forward, backward, forward, forward, forward, then the program should report:

    Square      Steps
       1          0
       2          0
       3          1
       4          2
       5          1
'''
def main():
    squares = get_inputs()
    steps, total_steps = simulate_steps(squares)
    print_steps(squares, steps, total_steps)


def get_inputs():
    while True:
        squares = input("\nEnter the number of squares (must be odd): ")
        squares.replace(" ", "")
        if squares.isdigit():
            squares = int(squares)
            if squares % 2 == 0:
                print("Error: number is not odd")
                continue
            break
        else:
            print("Error: invalid input")

    return squares


def simulate_steps(squares):
    steps = [0] * squares
    current_step = int((squares + 1) / 2)
    total_steps = 0

    while True:
        if random() < .5:
            current_step -= 1
        else:
            current_step += 1

        if current_step > squares or current_step < 1:
            break

        steps[current_step-1] += 1
        total_steps += 1

    return steps, total_steps


def print_steps(squares, steps, total_steps):
    print("\nA total of", total_steps, "steps were taken")
    print("\n{0:10}{1:1}".format("Square", "Steps"))
    for square in range(1, squares + 1):
        print("{0:4}{1:9}".format(square, steps[square-1]))


main()
