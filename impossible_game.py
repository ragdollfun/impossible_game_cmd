import numpy as np
rng = np.random.default_rng()

def are_you_playing():
    question = "Do you want to\n" + \
        "\t1) play yourself ?\n" + \
        "\t2) watch a computer simulation ?\n"
    huh = "I did not understand your answer. Please enter the number corresponding to your choice.\n"
    while True:
        try:
            choice = int(input(question))
            if choice == 1:
                return True
            elif choice == 2:
                return False
            else:
                print(huh)
        except:
            print(huh)

def first_round():
    game = {
        'bank': 10_000,
        'alice': {'q': [rd_bin()], 'a': []},
        'bob': {'q': [rd_bin()], 'a': []}
    }
    return game

def answer(game, play, q_str, strat_p1, strat_p2):
    if play:
        print("Type 0 for NO and 1 for YES:")
        game['alice']['a'].append(int(input(q_str[game['alice']['q'][-1]])))
        print("Your answer: " + bin2yesno(game['alice']['a'][-1]))
        print()

        strat_p2(game['bob'])
    else:
        print("Question for player 1: " + q_str[game['alice']['q'][-1]])
        strat_p1(game['alice'])
        print("Their answer: " + bin2yesno(game['alice']['a'][-1]))
        print()

        print("Question for player 2: " + q_str[game['bob']['q'][-1]])
        strat_p2(game['bob'])
        print("Their answer: " + bin2yesno(game['bob']['a'][-1]))
        print()

def rand_strategy(player):
    player['a'].append(rd_bin())

def bin2yesno(num):
    if num == 0: return 'NO'
    elif num == 1: return 'YES'

def resolve(game):
    q_p1 = game['alice']['q'][-1]
    a_p1 = game['alice']['a'][-1]
    q_p2 = game['bob']['q'][-1]
    a_p2 = game['bob']['a'][-1]
    if (q_p1 == 0 and q_p2 == 0 and a_p1 == 1 and a_p2 == 1) or \
        (q_p1 == 0 and q_p2 == 1 and a_p1 == 0 and a_p2 == 1) or \
        (q_p1 == 1 and q_p2 == 0 and a_p1 == 1 and a_p2 == 0):
        return 0
    elif (q_p1 == 0 and q_p2 == 0 and a_p1 == 0 and a_p2 == 0) or \
        (q_p1 == 1 and q_p2 == 1 and a_p1 == 1 and a_p2 == 1):
        return 1
    else:
        return 2

def next_round(game):
    game['bank'] = game['bank'] + 10_000
    game['alice']['q'].append(rd_bin())
    game['bob']['q'].append(rd_bin())

def rd_bin():
    return rng.choice(np.array([0, 1]))

if __name__ == "__main__":
    questions_str = [
        "Do you want to lose your money?",
        "Do you want to cash out?"
    ]

    print("-----------------------------------")
    print("| Welcome to the impossible game! |")
    print("-----------------------------------")
    print()

    play = are_you_playing()
    print()

    game = first_round()
    while True:
        print(f"Money in the Bank: {game['bank']}$")
        answer(game, play, questions_str, rand_strategy, rand_strategy)
        outcome = resolve(game)
        if outcome == 0:
            print("------------------------------")
            print("| Game Over! You both loose! |")
            print("------------------------------")
            print()
            break
        elif outcome == 1:
            mon = game['bank'] // 2
            print("---------------------------------------------")
            print(f"| The Bank Cashes Out! You both win {mon}$! |")
            print("---------------------------------------------")
            print()
            break
        else:
            next_round(game)
            print("----------------------")
            print("| To the Next Round! |")
            print("----------------------")
            print()
