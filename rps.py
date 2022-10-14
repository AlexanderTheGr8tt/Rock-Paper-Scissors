import random
import time

moves = ['rock', 'paper', 'scissors']


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


class Player:
    my_move = random.choice(moves)
    their_move = random.choice(moves)

    def move(self):
        return

    def learn(self, my_move, their_move):
        pass


class AllRockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        return valid_input("Rock, Paper or Scissors? > ", moves)


class ReflectPlayer(Player):
    def move(self):
        return self.their_move


class CyclePlayer(Player):
    def move(self):
        index = moves.index(self.my_move) + 1
        return moves[index % len(moves)]

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause(f"You choose {move1}.\n"
                    f"Your rival played {move2}.")
        if move1 == move2:
            print_pause("** Draw **")
        if beats(move1, move2):
            print_pause("** Player One Wins! **")
            self.p1_score += 1
        else:
            print_pause("** Player Two Wins! **")
            self.p2_score += 1
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"Points: Player One {self.p1_score}, "
              f"Player Two {self.p2_score}\n")

    def play_game(self, rounds):
        for round in range(rounds):
            self.play_round()


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print(f'Sorry, the option "{option}" is invalid. Try again!')


def play_again():
    choice = valid_input('Would you like to play again? (y/n):', ['n', 'y'])
    if choice == 'n':
        print('Thanks for playing! See you next time.')
        exit(0)


def get_rounds():
    options = []
    max_rounds = 10
    for x in range(1, max_rounds + 1):
        options.append(str(x))
    return int(valid_input(f'Rounds? (from 1 to {max_rounds})', options))


def get_opponent():
    return valid_input('Choose the opponent player:\n'
                       '1 - Always rock\n'
                       '2 - Random\n'
                       '3 - Reflect\n'
                       '4 - Cycle\n',
                       ['1', '2', '3', '4'])


def game():
    while True:
        opponents = {
            '1': AllRockPlayer(),
            '2': RandomPlayer(),
            '3': ReflectPlayer(),
            '4': CyclePlayer()
        }
        p1 = HumanPlayer()
        p2 = opponents[get_opponent()]
        game = Game(p1, p2)
        rounds = get_rounds()
        game.play_game(rounds)

        play_again()


if __name__ == '__main__':
    game()
