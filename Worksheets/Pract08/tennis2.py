from random import random


'''
5.
Write a modified version tennis2.py of the tennis program from the lecture. This
program should ask the user to enter the probability of winning a point for one of
the players, and how many sets of tennis between the two players should be simulated.
It should report on the proportion of the sets won by each player. Assume that to
win a set a player has to have won 6 games and be at least two games ahead of his
opponent.
'''
def main():
    prob, sets = get_inputs()
    set_wins = simulate_n_sets(prob, sets)
    print_summary(set_wins, sets)


def get_inputs():
    while True:
        prob = input("\nEnter the % chance of player one winning a point (0 to 100): ")
        prob = prob.replace(" ", "")
        if prob.isdigit():
            prob = int(prob)
            if prob > 100:
                print("Error: Input out of range")
                continue
            break
        else:
            print("Error: Input not an integer")

    while True:
        sets = input("\nEnter the number of sets to be played: ")
        sets = sets.replace(" ", "")
        if sets.isdigit():
            sets = int(sets)
            break
        else:
            print("Error: Input not an integer")
    return prob/100, sets


def simulate_n_sets(prob, sets):
    set_wins = 0
    for set in range(1, sets + 1):
        p1_games, p2_games = simulate_set(prob, set)
        if p1_games > p2_games:
            set_wins += 1
    return set_wins


def simulate_set(prob, set):
    p1_games, p2_games, game = 0, 0, 1
    while not set_over(p1_games, p2_games):
        p1_points, p2_points = simulate_game(prob, game, set)
        if p1_points > p2_points:
            p1_games += 1
        else:
            p2_games += 1
        game += 1
    print("\nFor set", set)
    print("Player 1 won", p1_games, "game(s)")
    print("Player 2 won", p2_games, "game(s)")
    return p1_games, p2_games


def set_over(p1_games, p2_games):
    return (p1_games >= 6 or p2_games >= 6) and  \
              abs(p1_games - p2_games) >= 2


def simulate_game(prob, game, set):
    p1_points, p2_points = 0, 0
    while not game_over(p1_points, p2_points):
        if random() < prob:
            p1_points += 1
        else:
            p2_points += 1
    print("\nFor set", set, "game", game)
    print("Player 1 scored", p1_points, "point(s)")
    print("Player 2 scored", p2_points, "point(s)")
    return p1_points, p2_points


def game_over(p1_points, p2_points):
    return (p1_points >= 4 or p2_points >= 4) and  \
              abs(p1_points - p2_points) >= 2


def print_summary(set_wins, sets):
    proportion = set_wins / sets
    print("\nPlayer 1 won", set_wins, "set(s)", end="  ")
    print("Proportion: {:.2f}".format(proportion))

    set_wins = sets - set_wins
    proportion = set_wins / sets
    print("Player 2 won", set_wins, "set(s)", end="  ")
    print("Proportion: {:.2f}".format(proportion))


main()
