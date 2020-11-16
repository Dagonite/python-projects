from random import random


'''1. Write a program coinflips.py that simulates the flipping of a (fair) 
coin. The user should be asked how many times they wish the coin to be 
flipped, and the program should display the proportion of times that heads 
and tails appeared. i.e. If the user enters 100, and 53 of the simulated 
flips are heads, your program should give the output Heads 0.53, Tails 0.47. 
Make sure that the program consists of four functions: main, get_inputs, 
simulate_flips & display_results and that there is a call to main at the 
bottom of the program to initiate its execution. '''
def main():
    flips = get_inputs()
    heads, tails = simulate_flips(flips)
    display_results(heads/flips, tails/flips)


def get_inputs():
    while True:
        flips = input("\nEnter the amount of flips: ")
        if flips.isdigit():
            return int(flips)
        else:
            print("Error: Invalid amount")


def simulate_flips(flips):
    heads, tails = 0, 0
    for i in range(flips):
        if random() < .5:
            heads += 1
        else:
            tails += 1

    return heads, tails


def display_results(heads, tails):
    print("Heads {0:.2f}, Tails {1:.2f} ".format(heads, tails))


main()
