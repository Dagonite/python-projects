"""Try to win as much money as possible."""
# pylint: disable = anomalous-backslash-in-string

import os
from dataclasses import dataclass
from operator import attrgetter
from random import shuffle

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
BOXES_PER_ROW = 8
BOXES_COUNT = len(VALUES)
ROWS = BOXES_COUNT // BOXES_PER_ROW
BOXES_IN_LAST_ROW = BOXES_COUNT - ROWS * BOXES_PER_ROW
BOX_TEXT_VALUES = list(VALUES.keys())
BOX_LEFT_MARGIN = (BOXES_PER_ROW - BOXES_IN_LAST_ROW) // 2 * 10 * " "
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
opened_boxes = []


@dataclass
class Box:
    """Basic represenation of a box containing a value."""

    next_box_number = 1
    chosen = None

    text_value: str
    numeric_value: int
    opened: bool = False

    def __post_init__(self):
        self.box_number = self._generate_box_number()

    @classmethod
    def _generate_box_number(cls):
        """Generate a box number."""
        result = cls.next_box_number
        cls.next_box_number += 1
        return result

    def get_box_graphic(self):
        """Return a list of rows that make up a box graphic."""
        rows = [""] * 5
        rows[0] = "     __     "
        rows[1] = "  __|{}|__  ".format(str(self.box_number).zfill(2))
        rows[2] = " |        | "
        if self.opened:
            rows[3] = f" |{self.text_value:-^8}| "
        elif Box.chosen == self.box_number:
            rows[3] = f" |{'':=^8}| "
        else:
            rows[3] = f" |{'':-^8}| "
        rows[4] = " |________| "

        return rows


class Scoreboard:
    """Class for displaying a scoreboard using a supplied list of boxes."""

    BOARD_DIVIDER = "=" * 26
    TEXT_LEFT_MARGIN = " " * 35

    def __init__(self, boxes):
        self.boxes = boxes
        self.lows, self.highs = self.determine_low_and_high_values()

    def determine_low_and_high_values(self):
        """Return a tuple of lists denoting the high and low values."""
        sorted_boxes = sorted(self.boxes, key=attrgetter("numeric_value"))
        lows = sorted_boxes[: BOXES_COUNT // 2]
        highs = sorted_boxes[BOXES_COUNT // 2 :]
        return lows, highs

    def print_scoreboard(self):
        """Print out the scoreboard."""
        print(f"{Scoreboard.TEXT_LEFT_MARGIN}{Scoreboard.BOARD_DIVIDER}")
        print(f"{Scoreboard.TEXT_LEFT_MARGIN}|{'DEAL OR NO DEAL?':^24}|")
        print(f"{Scoreboard.TEXT_LEFT_MARGIN}{Scoreboard.BOARD_DIVIDER}")
        for low, high in zip(self.lows, self.highs):
            print(
                f"{Scoreboard.TEXT_LEFT_MARGIN}|"
                f"{' ' + low.text_value if not low.opened else '':=>10} || "
                f"{high.text_value + ' ' if not high.opened else '':=<10}|"
            )
        print(f"{Scoreboard.TEXT_LEFT_MARGIN}{Scoreboard.BOARD_DIVIDER}")


def main():
    """Entry point for the game."""
    randomised_values = BOX_TEXT_VALUES
    shuffle(randomised_values)
    boxes = [Box(text_value, VALUES[text_value]) for text_value in randomised_values]

    sb = Scoreboard(boxes)
    print_gui(boxes, sb)
    choose_initial_box()
    print_gui(boxes, sb)

    for opens, multiplier in ((5, 0.28), (3, 0.29), (3, 0.32), (3, 0.36), (3, 0.52), (3, 0.8)):
        open_boxes(boxes, opens, sb)

        unopened_boxes = [box.numeric_value for box in boxes if not box.opened]
        unopened_boxes_sum = sum(unopened_boxes)
        unopened_boxes_count = len(unopened_boxes)
        offer = unopened_boxes_sum / unopened_boxes_count * multiplier
        dealt = deal_or_no_deal(offer)

        print_gui(boxes, sb)

        if dealt:
            winnings = offer
            break

    else:
        swap_or_no_swap(boxes)
        print(f"\nYou have chosen box {Box.chosen}\n")
        winnings = boxes[Box.chosen - 1].numeric_value

    unopened_boxes = [box for box in boxes if not box.opened]
    messages = []
    for box in unopened_boxes:
        messages.append(f"Box {box.box_number} contained {box.text_value}")
        box.opened = True

    print_gui(boxes, sb)
    print("\n", *messages, sep="\n")
    print(f"\nYou leave with £{winnings:,.2f}")


def swap_or_no_swap(boxes):
    """
    Prompt user to accept or decline an offer to swap their box with the other
    remaining box.
    """
    for box in boxes:
        if not box.opened and box.box_number != Box.chosen:
            other_box = box
            break

    while True:
        try:
            swap = input(f"\nDo you want to swap box {Box.chosen} with box {other_box.box_number}? (y/n) > ")
            if swap not in YES_RESPONSES + NO_RESPONSES:
                raise ValueError("invalid: answer must be 'y' or 'n'")
            break
        except ValueError as exc:
            print(exc)

    if swap in YES_RESPONSES:
        Box.chosen = other_box.box_number


def deal_or_no_deal(offer):
    """Prompt user to accept or decline the banker's offer for their box."""
    print(ASCII_PHONE)
    input("The banker is calling. Press the Enter key to answer... ")
    print(f'\n"How does £{offer:,.2f} for box {Box.chosen} sound?"')

    while True:
        try:
            accepted = input("\nDo you accept the offer? (y/n) > ")

            if accepted not in YES_RESPONSES + NO_RESPONSES:
                raise ValueError("invalid: answer must be 'y' or 'n'")
            break
        except ValueError as exc:
            print(exc)

    return accepted in YES_RESPONSES


def choose_initial_box():
    """Prompt user to choose an initial box."""
    while True:
        try:
            box_number = int(input("\nEnter the number of the box you want to keep > "))
            if box_number < 1 or box_number > BOXES_COUNT:
                raise ValueError(f"invalid: {box_number} is outside the range of boxes")
            break
        except ValueError as exc:
            print(exc)

    Box.chosen = box_number


def open_boxes(boxes, opens, sb):
    """Prompt user to open boxes by inputting box numbers."""
    for _ in range(opens):
        while True:
            try:
                box = int(input("\nEnter the number of a box to open > "))

                if Box.chosen == box:
                    raise ValueError("invalid: can't open your own box")
                if box < 1 or box > BOXES_COUNT:
                    raise ValueError(f"invalid: {box} is outside the range of boxes")
                if boxes[box - 1].opened:
                    raise ValueError(f"invalid: box {box} has already been opened")

                current_box = boxes[box - 1]
                current_box.opened = True
                print_gui(boxes, sb)
                print(f"\nBox {box} contained {current_box.text_value}")
                break

            except ValueError as exc:
                print(exc)


def print_gui(boxes, sb):
    """Print and call functions for displaying the graphical user interface."""
    os.system("cls" if os.name == "nt" else "clear")
    sb.print_scoreboard()

    for i in range(ROWS):
        row_of_boxes = boxes[BOXES_PER_ROW * i : BOXES_PER_ROW * (i + 1)]
        print_box(row_of_boxes)

    row_of_boxes = boxes[BOXES_COUNT - BOXES_IN_LAST_ROW :]
    print_box(row_of_boxes, centre=True)


def print_box(row_of_boxes, centre=False):
    """Helper function for printing out a box."""
    rows = [""] * 5
    for box in row_of_boxes:
        current_rows = box.get_box_graphic()

        for i, row in enumerate(rows):
            rows[i] += current_rows[i]

    for row in rows:
        print(f"{BOX_LEFT_MARGIN if centre else ''}{row}")


if __name__ == "__main__":
    main()
