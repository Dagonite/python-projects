"""Objects and constants for Blackjack."""

# set up the constants
FACE_CARDS = ("Jack", "Queen", "King", "Ace")
RANKS = tuple(range(2, 11)) + FACE_CARDS
SUITS = {chr(9830): "Diamonds", chr(9829): "Hearts", chr(9827): "Clubs", chr(9824): "Spades"}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # if face card, use whole rank name
        for face in FACE_CARDS:
            if self.rank == face[0]:
                rank = face
                break
        else:
            rank = self.rank

        # use suit name instead of symbol
        suit = SUITS[self.suit]

        return f"{rank} of {suit}"

    def get_card_graphic(self, hidden=False):
        # top line of a card
        row_one = " ___  "

        if hidden:
            # backside of a card
            row_two = "|## | "
            row_three = "|###| "
            row_four = "|_##| "
        else:
            # frontside of a card
            row_two = "|{} | ".format(self.rank.ljust(2))
            row_three = "| {} | ".format(self.suit)
            row_four = "|_{}| ".format(self.rank.rjust(2, "_"))

        return [row_one, row_two, row_three, row_four]


class Deck:
    def __init__(self):
        self.deck = [Card(suit, str(rank)[0]) if rank != 10 else Card(suit, "10") for rank in RANKS for suit in SUITS]

    def shuffle(self):
        import random

        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def print_hand(self, hidden=False):
        rows = ["", "", "", ""]

        for card in self.cards:
            for i, row in enumerate(card.get_card_graphic(hidden)):
                rows[i] += row
            hidden = False

        for row in rows:
            print(row)

    def add_card(self, card):
        self.cards.append(card)
        if card.rank.isnumeric():
            self.value += int(card.rank)
        elif card.rank in ("J", "Q", "K"):
            self.value += 10
        elif card.rank == "A":
            self.value += 11
            self.aces += 1

    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
