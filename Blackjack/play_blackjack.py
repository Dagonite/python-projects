import sys

from blackjack import RANKS, DIAMONDS, HEARTS, CLUBS, SPADES, SUITS, Card, Deck, Hand, Chips


START_CHIPS = 1000


def main():
    print(
        """\nA game of Blackjack

    Rules:
      Try to beat the dealer's hand by without going over 21.
      Cards 2 through 10 are worth their face value.
      Kings, Queens, and Jacks are worth 10 points. 
      Each Ace is worth 11 points but are reduced to 1 individually if the hand goes over 21.
      (H)it to take another card. (S)tand to stop taking cards.
      On the first play of a round, you can (D)ouble down to increase your bet.
      By doubling down you commit to one hit followed by a stand (assuming you don't go over 21).
      In case of a tie, the bet is returned to the player.
      The dealer must hit until they reach 17 or over.\n"""
    )

    # give the player their starting chips
    player_chips = Chips(START_CHIPS)

    while True:  # main game loop
        if player_chips.total < 1:  # check if the player has run out of chips
            print("\nYou've run out of chips. Thanks for playing!")
            sys.exit()

        # prompt the player for their intitial bet
        bet = get_bet(player_chips)

        # get and shuffle a deck of cards
        deck = get_deck()

        # give the dealer and player two cards from the deck each
        dealer_hand, player_hand = deal_initial_hands(deck)

        # prompt the player for moves
        player_is_bust = process_player_moves(deck, dealer_hand, player_hand, player_chips, bet)

        print()

        if player_is_bust:  # check if the player has bust
            print("You've gone over 21.")
            print(f"You've lost {player_chips.bet} chip(s).")
        else:  # player hasn't bust

            # reveal dealer's hidden card
            display_hands(deck, (dealer_hand, player_hand), False)

            # await for user input beforing proceeding
            input("Press Enter to continue... ")

            # process the dealer's moves
            dealer_is_bust = process_dealer_moves(deck, dealer_hand, player_hand)

            print()

            if dealer_is_bust:  # check if the dealer has bust
                print("The dealer has gone over 21.")
                print(f"You've won {player_chips.win_bet()} chip(s).")
            else:
                if player_hand.value > dealer_hand.value:  # check if player hand beats dealer's
                    print("You have the better hand.")
                    print(f"You've won {player_chips.win_bet()} chip(s).")
                elif player_hand.value == dealer_hand.value:  # check if the hands are equal
                    print("Both hands are equal. It's a draw.")
                    player_chips.draw_bet()
                    print("Your chips have been returned.")
                else:  # otherwise dealer's hand is better
                    print("Dealer has the better hand.")
                    print(f"You've lost {player_chips.bet} chip(s).")

        print()

        # clear the player's current bet
        player_chips.clear_bet()


def get_deck():
    """Return a Deck object containing 52 Card objects."""
    # create deck object
    deck = Deck()

    # shuffle the deck
    deck.shuffle_deck()

    return deck


def deal_initial_hands(deck):
    """Return the initial hands of the player and dealer containing two cards each."""
    # draw two cards for the dealer
    dealer_hand = Hand()
    hit(deck, dealer_hand)
    hit(deck, dealer_hand)

    # draw two cards for the player
    player_hand = Hand()
    hit(deck, player_hand)
    hit(deck, player_hand)

    # show the cards
    display_hands(deck, (dealer_hand, player_hand))

    return dealer_hand, player_hand


def hit(deck, hand):
    """Add a card to the supplied hand by taking a card from the deck."""
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def display_hands(deck, hands, hidden=True):
    hidden_value = "??" if hidden else hands[0].value
    print(f"\nDEALER: {hidden_value}")
    hands[0].format_hand(hidden)

    print(f"PLAYER: {hands[1].value}")
    hands[1].format_hand()


def get_bet(player_chips, initial_bet=None):
    # determine the maximum chips the player can bet
    # if there has already been an initial bet: use the minimum of the initial bet and the player's total chips
    # else: use the player's total chips
    max_bet = min(initial_bet, (player_chips.total)) if initial_bet is not None else player_chips.total

    while True:  # loop until the player gives a valid bet
        bet = input(f"Enter an amount to bet (1-{max_bet}, or (Q)uit)> ").upper().strip()

        if bet == "Q":
            print("Thanks for playing!")
            sys.exit()

        if not bet.isdecimal():
            continue  # if the player didn't enter a number, ask again.

        bet = int(bet)
        if 1 <= bet <= max_bet:
            player_chips.take_bet(bet)
            return bet  # player entered a valid bet.


def process_player_moves(deck, dealer_hand, player_hand, player_chips, bet):
    move = ""
    while player_hand.value < 22:  # loop whilst player hasn't bust
        if player_hand.value == 21 or move == "D":
            return False  # automatically stand for the player if they have 21 or doubled down

        # get the player's move
        move = get_move(player_hand, player_chips)

        if move == "H":
            hit(deck, player_hand)  # add a card to the player's hand
        elif move == "S":
            return False  # player decides to stand
        elif move == "D":
            # player has doubled down so get another bet
            bet = get_bet(player_chips, bet)

            # add a card to the player's hand
            hit(deck, player_hand)

        # show the cards
        display_hands(deck, (dealer_hand, player_hand))

    return True


def get_move(player_hand, player_chips):
    while True:  # loop until the player gives a valid answer
        moves = ["(H)it", "(S)tand"]

        if len(player_hand.cards) == 2 and player_chips.total > 0:
            moves.append("(D)ouble down")

        # prompt the player for a move
        move_prompt = ", ".join(moves) + "> "
        move = input(move_prompt).upper()

        if move in ("H", "S") or (move == "D" and "(D)ouble down" in moves):
            return move  # player has entered a valid move.


def process_dealer_moves(deck, dealer_hand, player_hand):
    while dealer_hand.value < 17:  # dealer must hit until they have at least 17
        hit(deck, dealer_hand)
        display_hands(deck, (dealer_hand, player_hand), False)

        # await for user input beforing proceeding
        input("Press Enter to continue... ")

    # return True if dealer has bust
    return True if dealer_hand.value > 21 else False


if __name__ == "__main__":
    main()
