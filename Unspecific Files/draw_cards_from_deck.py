########################################################################################
# draw_cards_from_deck.py
#
# Make a standard deck of cards, shuffle the deck and then draw two cards at random.
# Print the two cards.
########################################################################################
from random import choice, shuffle

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "King", "Queen", "Ace"]
suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
cards = [rank + " of " + suit for rank in ranks for suit in suits]
shuffle(cards)

first_card = choice(cards)
cards.remove(first_card)
print("\nYour first card is the:", first_card)

second_card = choice(cards)
cards.remove(second_card)
print("\nYour second card is the:", second_card)