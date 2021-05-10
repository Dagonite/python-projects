# blackjack.py

# set up the constants
FACE_CARDS = ("Jack", "Queen", "King", "Ace")
RANKS = tuple(range(2, 11)) + FACE_CARDS
SUITS = {chr(9830): "Diamonds", chr(9829): "Hearts", chr(9827): "Clubs", chr(9824): "Spades"}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # if face card, use whole name
        for face in FACE_CARDS:
            if self.rank == face[0]:
                rank = face
                break
        else:
            rank = self.rank

        # use suit name instead of symbol
        suit = SUITS[self.suit]

        # determine what article to use
        article = "a"
        if rank == "8" or rank == "Ace":
            article += "n"

        return f"{article} {rank} of {suit}"

    def format_card(self, rows, hidden=False):
        rows[0] += " ___  "  # top line of a card
        if hidden:
            # backside of a card
            rows[1] += "|## | "
            rows[2] += "|###| "
            rows[3] += "|_##| "
        else:
            # frontside of a card
            rows[1] += "|{} | ".format(self.rank.ljust(2))
            rows[2] += "| {} | ".format(self.suit)
            rows[3] += "|_{}| ".format(self.rank.rjust(2, "_"))


class Deck:
    def __init__(self):
        self.deck = [Card(suit, str(rank)[0]) if rank != 10 else Card(suit, "10") for rank in RANKS for suit in SUITS]

    def shuffle_deck(self):
        import random

        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def format_hand(self, hidden=False):
        rows = ["", "", "", "", ""]
        for card in self.cards:
            card.format_card(rows, hidden)
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

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self, total):
        self.total = total
        self.full_bet = 0

    def __str__(self):
        return str(self.total)

    def take_bet(self, additional_bet):
        self.full_bet += additional_bet
        self.total -= additional_bet

    def win_bet(self):
        self.total += self.full_bet * 2

    def draw_bet(self):
        self.total += self.full_bet

    def clear_bet(self):
        self.full_bet = 0