from game import C4Game
from player import RandomAutoPlayer,HumanPlayer,SingleStepAutoPlayer
from random import shuffle

if __name__ == '__main__':
    p1 = SingleStepAutoPlayer()
    p2 = HumanPlayer()
    players = [p1,p2]
    shuffle(players)
    game = C4Game(*players)
    game.play_game(True)