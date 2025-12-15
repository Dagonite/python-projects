"""Try to beat the computer at rock, paper, scissors in a best of 5."""

from random import choice

STANCES = {
    "r": ("rock", 0),
    "p": ("paper", 1),
    "s": ("scissors", 2),
}

STANCE_ART = {
    "rock": [
        [
            "    _______  ",
            "---'   ____) ",
            "      (_____)",
            "      (_____)",
            "      (____) ",
            "---.__(___)  ",
        ],
        [
            "  _______    ",
            " (____   '---",
            "(_____)      ",
            "(_____)      ",
            " (____)      ",
            "  (___)__.---",
        ],
    ],
    "paper": [
        [
            "     _______      ",
            "---'    ____)____ ",
            "           ______)",
            "          _______)",
            "         _______) ",
            "---.__________)   ",
        ],
        [
            "      _______     ",
            " ____(____    '---",
            "(______           ",
            "(_______          ",
            " (_______         ",
            "   (__________---.",
        ],
    ],
    "scissors": [
        [
            "    _______       ",
            "---'   ____)____  ",
            "          ______) ",
            "       __________)",
            "      (____)      ",
            "---.__(___)       ",
        ],
        [
            "       _______    ",
            "  ____(____   '---",
            " (______          ",
            "(__________       ",
            "      (____)      ",
            "       (___)__.---",
        ],
    ],
}


def main():
    player_score = 0
    ai_score = 0
    while player_score < 3 and ai_score < 3:
        try:
            player_stance, player_stance_value = STANCES[input("(r)ock, (p)aper, or (s)cissors? ")]
        except KeyError:
            continue
        player_art = STANCE_ART[player_stance][0]
        player_art_len = len(player_art[0])

        ai_stance, ai_stance_value = choice(list(STANCES.values()))
        ai_art = STANCE_ART[ai_stance][1]
        ai_art_len = len(ai_art[0])

        centre = player_art_len * 2 + 2

        print(f"\n{'Player:':^{player_art_len}}  {'Computer:':^{ai_art_len}}")
        print(f"{player_stance.title():^{player_art_len}}  {ai_stance.title():^{ai_art_len}}")
        for player_stance_line, ai_stance_line in zip(player_art, ai_art):
            print(f"{player_stance_line}  {ai_stance_line}")

        if (player_stance_value + 1) % 3 == ai_stance_value:
            print(f"\n{'Computer wins':^{centre}}")
            ai_score += 1
        elif player_stance_value == ai_stance_value:
            print(f"\n{'Draw':^{centre}}")
        else:
            print(f"\n{'Player wins':^{centre}}")
            player_score += 1

        print(f"{str(player_score) + ' - ' + str(ai_score):^{centre}}\n")

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
