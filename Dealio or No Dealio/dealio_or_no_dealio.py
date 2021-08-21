"""Dealio or No Dealio. Open boxes and try to win as much money as possible."""
# pylint: disable=anomalous-backslash-in-string

from random import shuffle
import os

# Globals
VALUES = {
    "1p": 0.01,
    "10p": 0.1,
    "50p": 0.5,
    "£1": 1,
    "£5": 5,
    "£10": 10,
    "£50": 50,
    "£100": 100,
    "£250": 250,
    "£500": 500,
    "£750": 750,
    "£1k": 1000,
    "£3k": 3000,
    "£5k": 5000,
    "£10k": 10000,
    "£15k": 15000,
    "£20k": 20000,
    "£35k": 35000,
    "£50k": 50000,
    "£75k": 75000,
    "£100k": 100000,
    "£250k": 250000,
}
BOX_TOP = "     __     "
BOX_NUMBER = "  __|{}|__  "
BOX_MIDDLE = " |        | "
BOX_VALUE = " |{}| "
BOX_BOTTOM = " |________| "
UNOPENED_BOX_GRAPHIC = f"{'':-^8}"
CHOSEN_BOX_GRAPHIC = f"{'':=^8}"
BOXES_PER_ROW = 6
BOXES_COUNT = len(VALUES)
ROWS = BOXES_COUNT // BOXES_PER_ROW
BOXES_IN_LAST_ROW = BOXES_COUNT - ROWS * BOXES_PER_ROW
BOX_TEXT_VALUES = list(VALUES.keys())
LOWS = BOX_TEXT_VALUES[: BOXES_COUNT // 2]
HIGHS = BOX_TEXT_VALUES[BOXES_COUNT // 2 :]
BOX_LENGTH = len(BOX_TOP)
BOX_LEFT_MARGIN = (BOXES_PER_ROW - BOXES_IN_LAST_ROW) // 2 * BOX_LENGTH * " "
TEXT_LEFT_MARGIN = " " * 23
BOARD_DIVIDER = "=" * 26
BOX_OPENED = "opened"
BOX_UNOPENED = "unopened"
BOX_CHOSEN = "chosen"
NO_RESPONSES = ["n", "no"]
YES_RESPONSES = ["y", "yes"]
ASCII_PHONE = """
            ____________
          /   ,,____,,   \:.
          |__| [][][] |__|:  :
            /  [][][]  \   :  :
           /   [][][]   \   :  :
          /    [][][]    \   ..
=========|________________|\n
"""


def main():
    """Entry point for the game."""
    # Assign values to boxes randomly
    randomised_values = BOX_TEXT_VALUES.copy()
    shuffle(randomised_values)
    boxes = {randomised_values[i]: BOX_UNOPENED for i in range(BOXES_COUNT)}

    # Prompt user to pick a box to keep
    chosen_box = choose_a_box()

    # Mark user box as chosen
    chosen_box_value = randomised_values[chosen_box - 1]
    boxes[chosen_box_value] = BOX_CHOSEN

    # Display the boxes
    print_boxes(boxes)

    # Play the game
    winnings = gameplay_loop(boxes, chosen_box, randomised_values)

    print(f"\nYou leave with £{winnings:,.2f}")

    return winnings


def gameplay_loop(boxes, chosen_box, randomised_values):
    """The game's main loop."""
    for opens, multiplier in ((5, 0.28), (3, 0.29), (3, 0.32), (3, 0.36), (3, 0.48), (3, 0.7)):
        # Prompt the user to pick boxes
        open_boxes(boxes, opens, chosen_box, randomised_values)

        # Determine the banker's offer
        unopened_box_sum = sum(VALUES[box] for box, box_status in boxes.items() if box_status != BOX_OPENED)
        unopened_box_count = sum(1 for box_status in list(boxes.values()) if box_status != BOX_OPENED)
        offer = (unopened_box_sum // unopened_box_count) * multiplier

        # Prompt user to accept or reject the offer for their box
        accepted = dealio_or_no_dealio(offer, chosen_box)
        print_boxes(boxes)

        # Exit gameplay loop early if user accepts banker's offer
        if accepted:
            chosen_box_value = offer
            break
    else:
        # If user doesn't accept any offer. Ask if they want to swap their box
        chosen_box = swap_or_no_swap(boxes, chosen_box, randomised_values)

        # Get the value of the box
        chosen_box_value = VALUES[randomised_values[chosen_box - 1]]

        print(f"\nYou have chosen box {chosen_box}")

    # Find all of the unopened boxes
    unopened_boxes = [
        (box_number, box_value)
        for box_number, (box_value, box_status) in enumerate(boxes.items(), start=1)
        if box_status != BOX_OPENED
    ]

    # Open all unopened boxes and print them
    for box in boxes:
        boxes[box] = BOX_OPENED
    print_boxes(boxes)
    print()

    # Print what box contained which amount
    for box_number, box_value in unopened_boxes:
        print(f"Box {box_number} contained {box_value}")

    return chosen_box_value


def choose_a_box():
    """User is prompted to choose a box to keep by inputting the box's number."""
    while True:
        try:
            chosen_box = int(input("\nEnter the number of the box you want to keep > "))
            if chosen_box < 1 or chosen_box > BOXES_COUNT:
                raise ValueError(f"invalid: {chosen_box} is outside the range of boxes")
            break
        except ValueError as exc:
            print(exc)

    return chosen_box


def open_boxes(boxes, opens, chosen_box, randomised_values):
    """User is prompted to open boxes by inputting their numbers."""
    for _ in range(opens):
        while True:
            try:
                box = int(input("\nEnter the number of a box to open > "))

                if box == chosen_box:
                    raise ValueError("invalid: can't open your own box")
                elif box < 1 or box > BOXES_COUNT:
                    raise ValueError(f"invalid: {box} is outside the range of boxes")
                elif boxes[randomised_values[box - 1]] == "opened":
                    raise ValueError(f"invalid: box {box} has already been opened")
            except ValueError as exc:
                print(exc)
            else:
                box_value = randomised_values[box - 1]
                boxes[box_value] = "opened"
                print_boxes(boxes)
                print(f"\nBox {box} contained {box_value}")
                break


def dealio_or_no_dealio(offer, chosen_box):
    """
    Prompt user whether they want to accept the banker's offer for their box.
    """
    print(ASCII_PHONE)
    input("The banker is calling. Press the Enter key to answer... ")
    print(f'\n"How does £{offer:,.2f} for box {chosen_box} sound?"')

    while True:
        try:
            accepted = input(f"\nDo you accept the offer? (y/n) > ")

            if accepted not in YES_RESPONSES + NO_RESPONSES:
                raise ValueError("invalid: answer must be 'y' or 'n'")
        except ValueError as exc:
            print(exc)
        else:
            break

    return accepted in YES_RESPONSES


def print_boxes(boxes):
    """
    Print all the boxes. If the box hasn't been opened, show the box number.
    Otherwise show the box value.
    """
    # Clear the screen and print out the values still in play
    os.system("cls" if os.name == "nt" else "clear")
    print_board(boxes)

    # Enumerate the boxes to get their numbers
    numbered_boxes = list(enumerate(boxes.items(), start=1))

    # Print boxes which can fill out whole rows
    for i in range(ROWS):
        box_numbers, box_data = zip(*numbered_boxes[BOXES_PER_ROW * i : BOXES_PER_ROW * i + BOXES_PER_ROW])
        print(BOX_TOP * BOXES_PER_ROW)
        print((BOX_NUMBER * BOXES_PER_ROW).format(*[str(box_number).zfill(2) for box_number in box_numbers]))
        print(BOX_MIDDLE * BOXES_PER_ROW)
        print(
            (BOX_VALUE * BOXES_PER_ROW).format(
                *[
                    UNOPENED_BOX_GRAPHIC
                    if box_status == BOX_UNOPENED
                    else CHOSEN_BOX_GRAPHIC
                    if box_status == BOX_CHOSEN
                    else f"{box_value:-^8}"
                    for box_value, box_status in box_data
                ]
            )
        )
        print(BOX_BOTTOM * BOXES_PER_ROW)

    # Print out remaining boxes which couldn't fill out a whole row
    box_numbers, box_data = zip(*numbered_boxes[BOXES_COUNT - BOXES_IN_LAST_ROW :])
    print(BOX_LEFT_MARGIN + BOX_TOP * BOXES_IN_LAST_ROW)
    print(
        BOX_LEFT_MARGIN
        + (BOX_NUMBER * BOXES_IN_LAST_ROW).format(*[str(box_number).zfill(2) for box_number in box_numbers])
    )
    print(BOX_LEFT_MARGIN + BOX_MIDDLE * BOXES_IN_LAST_ROW)
    print(
        BOX_LEFT_MARGIN
        + (BOX_VALUE * BOXES_IN_LAST_ROW).format(
            *[
                UNOPENED_BOX_GRAPHIC
                if box_status == BOX_UNOPENED
                else CHOSEN_BOX_GRAPHIC
                if box_status == BOX_CHOSEN
                else f"{box_value:-^8}"
                for box_value, box_status in box_data
            ]
        )
    )
    print(BOX_LEFT_MARGIN + BOX_BOTTOM * BOXES_IN_LAST_ROW)


def print_board(boxes):
    """Print out the board showing the prize money values still in play."""
    # Get the prize money values of all opened boxes
    opened_boxes = [box for box in boxes if boxes[box] == BOX_OPENED]

    # Print out the board
    print(TEXT_LEFT_MARGIN + BOARD_DIVIDER)
    print(TEXT_LEFT_MARGIN + f"|{'DEALIO OR NO DEALIO?':^24}|")
    print(TEXT_LEFT_MARGIN + BOARD_DIVIDER)
    for i in range(BOXES_COUNT // 2):
        print(
            TEXT_LEFT_MARGIN
            + f"|{' ' + LOWS[i] if LOWS[i] not in opened_boxes else '':=>10} || {HIGHS[i] + ' ' if HIGHS[i] not in opened_boxes else '':=<10}|"
        )
    print(TEXT_LEFT_MARGIN + BOARD_DIVIDER)


def swap_or_no_swap(boxes, chosen_box, randomised_values):
    """
    User is prompted whether they want to swap their box with the other
    remaining box.
    """
    for box_value, box_status in boxes.items():
        if box_status == BOX_UNOPENED:
            other_box = randomised_values.index(box_value) + 1
            break

    while True:
        try:
            swap = input(f"\nDo you want to swap box {chosen_box} with box {other_box}? (y/n) > ")

            if swap not in YES_RESPONSES + NO_RESPONSES:
                raise ValueError("invalid: answer must be 'y' or 'n'")
            break
        except ValueError as exc:
            print(exc)

    if swap in YES_RESPONSES:
        return other_box

    return chosen_box


def write_to_csv(*data, path="dealios.csv"):
    """Store supplied data in a CSV file."""
    import csv

    with open(path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(data)


if __name__ == "__main__":
    import datetime

    winnings = main()
    write_to_csv(winnings, datetime.datetime.now().date())
