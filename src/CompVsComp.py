from game import C4Game
from player import RandomAutoPlayer

if __name__ == '__main__':
    p1 = RandomAutoPlayer()
    p2 = RandomAutoPlayer()
    game = C4Game(p1,p2)
    game.play_game(True)