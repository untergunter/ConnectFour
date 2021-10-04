from board import Board
from player import Player

class C4Game:

    def __init__(self,player_1:Player,player_2:Player):
        self.players = (player_1,player_2)
        self.board = Board()

    def play_game(self,view_game:bool):
        """ main function of the game """
        game_over = False
        while not game_over:
            for player_number,player in enumerate(self.players,1):
                if view_game:
                    self.board.print_board()
                can_place_at = self.board.get_open_columns()
                board_state = self.board.get_state(player_number)
                column_to_place = player.select_next_move(board_state,can_place_at)
                player_won = self.board.set(column_to_place,player_number)

                if player_won:
                    if view_game:
                        self.board.print_board()
                    print(f"player {player_number} won")
                    game_over = True
                    break

                if self.board.is_full():
                    print("tie")
                    game_over = True
                    break



