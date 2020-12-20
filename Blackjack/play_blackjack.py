########################################################################################
# play_blackjack.py
#
# Program which allows a player to play blackjack with a computer dealer within a
# graphical user interface.
#
# Rules:
# - dealer must hit below 17 if player isn't bust
# - dealer must stand on 17 or higher.
# - minimum bet of 1 chip
# - maximum bet of 100 chips
# - no card counting :^)
########################################################################################
from time import sleep

from graphics import Circle, Entry, GraphWin, Line, Point, Polygon, Rectangle, Text

from blackjack import Card, Chips, Deck, Hand

card_objects = []


def main():
    global player_chips
    player_chips = Chips()
    win = create_interface()
    while True:
        make_bet(win)
        result = play_game(win)

        if result == 2:
            player_chips.win_bet()
        elif result == 1:
            player_chips.draw_bet()

        for i in card_objects:
            i.undraw()

        chips_text.setText("Chips: " + str(player_chips.total))
        helper_text.setText("Enter a bet to play")


def make_bet(win):
    while True:
        if player_chips.total < 1:
            helper_text.setText("Player out of chips\n GAME OVER")
            sleep(4)
            win.close()
        cursor = win.getMouse()
        if 3.6 <= cursor.getX() <= 4.1 and 0.15 <= cursor.getY() <= 0.45:
            bet = bid_entry.getText()
            if validate_bet(bet):
                break
        elif 9.3 <= cursor.getX() <= 9.9 and 0.15 <= cursor.getY() <= 0.45:
            win.close()
    bid_entry.setText("")


def validate_bet(bet):
    if int(bet) > player_chips.total:
        helper_text.setText("Bet can't be higher\nthan total chips")
        return False
    elif int(bet) > 100:
        helper_text.setText("Bet can't be above 100 chips")
        return False
    elif int(bet) < 1:
        helper_text.setText("Bet can't be less than 1 chip")
        return False
    else:
        player_chips.bet = int(bet)
        player_chips.take_bet()
        # player_chips.total -= player_chips.bet
        chips_text.setText("Chips: " + str(player_chips.total))
        return True


def play_game(win):
    helper_text.setText("Choose whether you want to hit or stand")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    hit(deck, player_hand)
    hit(deck, player_hand)

    dealer_hand = Hand()
    hit(deck, dealer_hand)
    hit(deck, dealer_hand)

    for card_index, player_card in enumerate(player_hand.cards):
        card_name = str(player_card)
        suit = check_suit(card_name)
        draw_card(win, card_index, suit, card_name[0], True)

    show_card = True
    for dealer_card_index, dealer_card in enumerate(dealer_hand.cards):
        card_name = str(dealer_card)
        suit = check_suit(card_name)

        if show_card:
            draw_card(win, dealer_card_index, suit, card_name[0], False)
        else:
            draw_hidden_card(win, dealer_card_index, suit, card_name[0], False)

        show_card = False

    player_bust = hit_or_stand(win, deck, player_hand, card_index)

    if not player_bust:
        helper_text.setText(f"Player stands on {player_hand.value}")
        sleep(3)
        dealer_bust = dealer_hit_or_stand(
            win, deck, dealer_hand, dealer_card_index, player_hand
        )
        if not dealer_bust:
            if dealer_hand.value > player_hand.value:
                helper_text.setText(
                    f"Dealer beats player {dealer_hand.value} to {player_hand.value}"
                )
                sleep(4)
                return 0
            elif dealer_hand.value < player_hand.value:
                helper_text.setText(
                    f"Player beats Dealer {player_hand.value} to {dealer_hand.value}"
                )
                sleep(4)
                return 2
            else:
                helper_text.setText(
                    f"Dealer and Player both have {player_hand.value}\nIt's a push, chips returned"
                )
                sleep(4)
                return 1
        else:
            helper_text.setText(f"Dealer bust, Player wins with {player_hand.value}")
            sleep(4)
            return 2
    else:
        helper_text.setText(f"Player bust, Dealer wins")
        sleep(4)
        return 0


def check_suit(card_name):
    if "Diamonds" in card_name:
        return "♦"
    elif "Hearts" in card_name:
        return "♥"
    elif "Clubs" in card_name:
        return "♣"
    else:
        return "♠"


def hit_or_stand(win, deck, player_hand, card_index):
    player_bust = False

    while player_hand.value < 21:
        cursor = win.getMouse()
        if 0.4 <= cursor.getX() <= 1.3 and 0.15 <= cursor.getY() <= 0.45:
            hit(deck, player_hand)
            # player_hand.add_card(deck.deal())
            card_index += 1
            card_name = str(player_hand.cards[card_index])
            suit = check_suit(card_name)

            helper_text.setText(f"You drew the {card_name}")
            draw_card(win, card_index, suit, card_name[0], True)

        elif 1.4 <= cursor.getX() <= 2.3 and 0.15 <= cursor.getY() <= 0.45:
            helper_text.setText("You have chosen to stand")
            break

        elif 9.3 <= cursor.getX() <= 9.9 and 0.15 <= cursor.getY() <= 0.45:
            win.close()

    if player_hand.value > 21:
        player_bust = True

    return player_bust


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def dealer_hit_or_stand(win, deck, dealer_hand, dealer_card_index, player_hand):
    dealer_bust = False
    card_name = str(dealer_hand.cards[1])
    suit = check_suit(card_name)
    draw_card(win, 1, suit, card_name[0], False)

    if dealer_hand.value <= player_hand.value:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
            dealer_card_index += 1
            card_name = str(dealer_hand.cards[dealer_card_index])
            suit = check_suit(card_name)

            draw_card(win, dealer_card_index, suit, card_name[0], False)

    if dealer_hand.value > 21:
        dealer_bust = True

    return dealer_bust


def draw_text(
    win,
    centre,
    txt,
    text_size=14,
    colour="black",
    style="normal",
    face="courier",
    card_shape="False",
):
    current_text = Text(Point(centre[0], centre[1]), txt)
    current_text.setFace(face)
    current_text.setSize(text_size)
    current_text.setTextColor(colour)
    current_text.setStyle(style)
    current_text.draw(win)
    if card_shape:
        return current_text


def create_interface():
    win = GraphWin("Blackjack", 1000, 500)
    win.setBackground("green")
    win.setCoords(0, 0, 10, 5)

    # draw player interface
    draw_rectangle(win, (0, 0), (10, 0.6), "black")

    # draw player's hand text
    draw_text(win, (1.1, 0.76), "Player's hand", 14, "black", "bold")

    # draw player's chips text
    global chips_text
    chips_text = Text(Point(9.0, 0.76), "Chips: 100")
    chips_text.setFace("courier")
    chips_text.setSize(14)
    chips_text.setStyle("bold")
    chips_text.draw(win)

    # draw dealer's hand text
    draw_text(win, (1.1, 4.82), "Dealer's hand", 14, "black", "bold")

    # draw hit button
    draw_rectangle(win, (0.4, 0.15), (1.3, 0.45), "grey")
    draw_text(win, (0.85, 0.29), "Hit", 14, "black", "bold", "arial")

    # draw stand button
    draw_rectangle(win, (1.4, 0.15), (2.3, 0.45), "grey")
    draw_text(win, (1.85, 0.29), "Stand", 14, "black", "bold", "arial")

    # draw bet entry point
    global bid_entry
    bid_entry = Entry(Point(3, 0.3), 10)
    bid_entry.draw(win)

    # draw bet button
    draw_rectangle(win, (3.6, 0.15), (4.1, 0.45), "green")
    draw_text(win, (3.84, 0.29), "Bet", 14, "black", "bold", "arial")

    # draw helper text
    global helper_text
    helper_text = Text(Point(6.7, 0.29), "Enter a bet to play")
    helper_text.setFace("arial")
    helper_text.setSize(14)
    helper_text.setTextColor("white")
    helper_text.setStyle("bold")
    helper_text.draw(win)

    # draw quit button
    draw_rectangle(win, (9.3, 0.15), (9.9, 0.45), "red")
    draw_text(win, (9.6, 0.29), "Quit", 14, "black", "bold", "arial")

    return win


def draw_card(win, offset, suit, rank, player):
    if rank == "1":
        rank = "1" + "0"

    if player:
        vertical_offset = 0
    else:
        vertical_offset = 2

    card_rectangle = draw_rectangle(
        win,
        (0.4 + offset, 0.95 + vertical_offset),
        (1.8 + offset, 2.6 + vertical_offset),
        "white",
        True,
    )
    card_objects.append(card_rectangle)

    if suit in ("♦", "♥"):
        colour = "red"
    else:
        colour = "black"

    card_shape1 = draw_text(
        win,
        (0.6 + offset, 2.4 + vertical_offset),
        rank,
        18,
        colour,
        "bold",
        "courier",
        True,
    )
    card_shape2 = draw_text(
        win,
        (0.6 + offset, 1.12 + vertical_offset),
        suit,
        30,
        colour,
        "bold",
        "courier",
        True,
    )
    card_shape3 = draw_text(
        win,
        (1.6 + offset, 1.12 + vertical_offset),
        rank,
        18,
        colour,
        "bold",
        "courier",
        True,
    )
    card_shape4 = draw_text(
        win,
        (1.6 + offset, 2.4 + vertical_offset),
        suit,
        30,
        colour,
        "bold",
        "courier",
        True,
    )
    card_objects.append(card_shape1)
    card_objects.append(card_shape2)
    card_objects.append(card_shape3)
    card_objects.append(card_shape4)


def draw_hidden_card(win, offset, suit, rank, player):
    if rank == "1":
        rank = "1" + "0"

    if player:
        vertical_offset = 0
    else:
        vertical_offset = 2

    card_rectangle = draw_rectangle(
        win,
        (0.4 + offset, 0.95 + vertical_offset),
        (1.8 + offset, 2.6 + vertical_offset),
        "blue",
        True,
    )
    card_objects.append(card_rectangle)


def draw_rectangle(win, point1, point2, colour, card_object="False"):
    current_rectangle = Rectangle(
        Point(point1[0], point1[1]),
        Point(point2[0], point2[1]),
    )
    current_rectangle.setFill(colour)
    current_rectangle.draw(win)

    if card_object:
        return current_rectangle


main()
