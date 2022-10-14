import random
import time

moves = ['rock', 'paper', 'scissors']


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            player_pick = input("Rock, paper, scissors? > ")
            if player_pick in moves:
                return player_pick


class ReflectPlayer(Player):
    their_move = "None"

    def move(self):
        if self.their_move == "None":
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    my_move = "None"

    def move(self):
        if self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        elif self.my_move == "scissors":
            return "rock"
        else:
            return random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause(f"You choose {move1}.\n"
                    f"Your rival played {move2}.")
        if beats(move1, move2):
            print_pause("** Player One Wins! **")
            self.p1_score += 1
        elif beats(move2, move1):
            print_pause("** Player Two Wins! **")
            self.p2_score += 1
        else:
            print_pause("** Draw **")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"Points: Player One: {self.p1_score},"
              f"Player Two: {self.p2_score}\n")

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
                Game.play_again()


if __name__ == '__main__':
    p1 = HumanPlayer()
    player = [ReflectPlayer(), RandomPlayer(), Player(), CyclePlayer()]
    p2 = random.choice(player)
    game = Game(p1, p2)
    game.play_game()
    game.play_again()
