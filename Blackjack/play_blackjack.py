"""A game of Blackjack."""

import os
import sys

from blackjack import Deck, Hand

CHIPS = 1000


def main(chips=CHIPS):
    while True:
        # quit if player is out of chips
        if chips < 1:
            print("\nYou're out of chips. Thanks for playing!")
            break

        # create a deck to use
        deck = get_deck()

        # get the player's initial bet
        bet = get_bet(chips)

        # deal the initial hands
        dealer_hand, player_hand = deal_initial_hands(deck)

        # get player moves
        prompt_player_for_moves(deck, (dealer_hand, player_hand), chips, bet)

        # redisplay the board to hide player's previous actions
        display_hands(deck, (dealer_hand, player_hand), hidden=True)

        # player has bust - move onto next round
        if player_hand.value > 21:
            print(f"\nYou have gone over 21, you lose!")
            chips -= bet
            continue
        # player has not bust - reveal dealer's hidden card
        else:
            display_hands(deck, (dealer_hand, player_hand))
            print(f"\nDealer has revealed the {dealer_hand.cards[0]}")

        # get the dealer's moves
        prompt_dealer_for_moves(deck, (dealer_hand, player_hand), chips, bet)

        # redisplay the board to hide dealer's previous actions
        display_hands(deck, (dealer_hand, player_hand))

        # dealer has bust
        if dealer_hand.value > 21:
            print(f"\nDealer has gone over 21, you win {bet} chips!")
            chips += bet
            continue

        # determine who has the better hand
        if player_hand.value > dealer_hand.value:
            print(f"\nYou have the stronger hand, you win {bet} chips!")
            chips += bet
        elif player_hand.value < dealer_hand.value:
            print("\nYou have the weaker hand, you lose!")
            chips -= bet
        else:
            print(f"\nIt's a draw!")


def get_deck():
    """Return a shuffled deck object."""
    deck = Deck()
    deck.shuffle()
    return deck


def get_bet(chips, initial_bet=None):
    """Prompt the player for a bet."""
    max_bet = min(initial_bet, chips) if initial_bet is not None else chips

    while True:
        try:
            bet = input(f"\nEnter an amount to bet (1-{max_bet}), or (q)uit > ").lower()

            if bet == "q":
                print(f"\nYou retire on {chips} chip{'s' if chips > 1 else ''}\nThanks for playing!")
                sys.exit()
            elif not bet.isdecimal():
                raise TypeError("invalid: input must be a positive integer")

            bet = int(bet)

            if bet < 1:
                raise ValueError("invalid: input must be more than or equal to 1")
            elif bet > max_bet:
                raise ValueError("invalid: input must not exceed the maximum bet allowed")
            else:
                return bet

        except (ValueError, TypeError) as error:
            print(error)


def deal_initial_hands(deck):
    """Add two cards to each hand and return the hand objects."""
    dealer_hand = Hand()
    hit(deck, dealer_hand)
    hit(deck, dealer_hand)

    player_hand = Hand()
    hit(deck, player_hand)
    hit(deck, player_hand)

    return dealer_hand, player_hand


def hit(deck, hand):
    """Remove a card from the deck and add it to the supplied hand. Also return the card"""
    new_card = deck.deal()
    hand.add_card(new_card)
    hand.adjust_for_aces()
    return new_card


def display_hands(deck, hands, hidden=False):
    """Clear the screen and print out the cards in each hand."""
    os.system("cls" if os.name == "nt" else "clear")

    dealer_hand, player_hand = hands

    print(f"DEALER: {'??' if hidden else dealer_hand.value}")
    dealer_hand.print_hand(hidden)

    print(f"\nPLAYER: {player_hand.value}")
    player_hand.print_hand()


def prompt_player_for_moves(deck, hands, chips, bet):
    """Prompt the player for moves until they go bust, get 21, stand, or have doubled down."""
    _, player_hand = hands
    new_cards = []

    while True:
        moves = ["(h)it", "(s)tand"]
        display_hands(deck, hands, hidden=True)

        for new_card in new_cards:
            print(f"\nYou have drawn the {new_card}")

        if player_hand.value > 20:
            break

        if len(player_hand.cards) == 2 and chips > 0:
            moves.append("(d)ouble down")

        move = ""
        while move not in [i[1:2] for i in moves]:
            move_prompt = f"\n{', '.join(moves)} > "
            move = input(move_prompt).lower()

        if move == "h":
            new_card = hit(deck, player_hand)
            new_cards.append(new_card)
        elif move == "s":
            break
        elif move == "d" and "d" in [i[1:2] for i in moves]:
            bet += get_bet(chips, initial_bet=bet)
            new_card = hit(deck, player_hand)
            new_cards.append(new_card)
            display_hands(deck, hands, hidden=True)
            print(f"\nYou have drawn the {new_card}")
            break

    input("\nPress Enter to continue... ")


def prompt_dealer_for_moves(deck, hands, chips, bet):
    """Prompt dealer for moves until they go bust or go over 16."""
    dealer_hand, _ = hands
    new_cards = []

    while dealer_hand.value < 17:
        input("\nPress Enter to continue... ")

        new_card = hit(deck, dealer_hand)
        new_cards.append(new_card)
        display_hands(deck, hands)

        print(f"\nDealer has revealed the {dealer_hand.cards[0]}")
        for new_card in new_cards:
            print(f"\nDealer has drawn the {new_card}")

    input("\nPress Enter to continue... ")


if __name__ == "__main__":
    main()
