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
        while True:
            move = input("Rock, paper, scissors? > ").lower()
            if move in moves:
                return move
            print(f"The move {move} is invalid. Try again!")


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

    def play_game(self):
        print_pause("Rock Paper Scissors, Start!\n")
        self.rounds = 3
        for round in range(self.rounds):
            print_pause(f"Round {round + 1}")
            self.play_round()
        print_pause("Game over!")
        print_pause(f"Player One score is {self.p1_score},"
                    f" and Player Two score is {self.p2_score}\n")
        if self.p1_score > self.p2_score:
            print_pause("Player One Wins the whole game!\n")
        elif self.p1_score < self.p2_score:
            print_pause("Player Two Wins the whole game!\n")
        else:
            print_pause("No one wins\n")

    def play_again(self):
        while True:
            decision = input("Would you like to play again? (y/n)\n").lower()
            if decision == 'y':
                print_pause("Excellent! Restarting the game ...")
                self.play_game()
            elif decision == 'n':
                print_pause("Thanks for playing! See you next time.")
                break
            else:
                self.play_again()


if __name__ == '__main__':
    p1 = HumanPlayer()
    player = [ReflectPlayer(), RandomPlayer(), AllRockPlayer(), CyclePlayer()]
    p2 = random.choice(player)
    game = Game(p1, p2)
    game.play_game()
    game.play_again()
