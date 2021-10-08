from board import Board
from player import Player

class C4Game:

    def __init__(self,player_1:Player
                 ,player_2:Player):
        self.players = (player_1,player_2)
        self.board = Board()

    def play_game(self,view_game:bool):
        """
        takes action from players by turn and  apply to board
        also handles victory and tie.
        :param view_game:
        :return:
        """
        game_is_on = True
        while game_is_on:
            for player_number,player in enumerate(self.players,1):
                if view_game:
                    self.board.print_board()
                can_place_at = self.board.get_open_columns()
                board_state = self.board.get_state_by_player_perspective(player_number)
                column_to_place = player.select_next_move(board_state,can_place_at)
                player_won = self.board.play_move(column_to_place, player_number)

                if player_won:
                    if view_game:
                        self.board.print_board()
                    print(f"player {player_number} won")
                    game_is_on = False
                    break

                if self.board.is_full():
                    print("tie")
                    game_is_on = False
                    break



