from abc import ABC, abstractmethod
import numpy as np
from board import Board

class Player(ABC):
    """ only plays next move """
    @abstractmethod
    def select_next_move(self, board_state: np.ndarray,
                         top_column_is_open: np.ndarray):
        pass


class RandomAutoPlayer(Player):
    """ plays next move randomly """
    def select_next_move(self, board_state: np.ndarray,
                         top_column_is_open: np.ndarray):
        column = np.random.choice(top_column_is_open)
        return column

class HumanPlayer(Player):
    """ plays move by preasing 1-8"""

    def select_next_move(self, board_state: np.ndarray,
                         top_column_is_open: np.ndarray):
        """
        get a valid move from a human player via cli.
        players enter 1-8, but game takes 0-7, so input is transformed.
        :param board_state:
        :param top_column_is_open:
        :return:
        """
        user_column = -1
        top_column_is_open = {str(column+1) for column in top_column_is_open}
        while user_column not in top_column_is_open:
            user_column = input(f'please select column from {top_column_is_open}')
        selected_column = int(user_column)-1
        return selected_column

class SingleStepAutoPlayer(Player):
    def __init__(self):
        self.inner_board = Board()
        self.random_player = RandomAutoPlayer()

    def select_next_move(self, board_state: np.ndarray,
                         top_column_is_open: np.ndarray):
        """
        if any action is a winner action - select it.
        if any action stops other player from wining next turn - select it.
        else - act randomly.
        :param board_state:
        :param top_column_is_open:
        :return:
        """

        """ find and return wining move """
        move_to_win = self.winning_move_for_player(board_state,1,top_column_is_open)
        if move_to_win:
            return move_to_win

        """ find and return rival wining move """
        move_not_to_lose = self.winning_move_for_player(board_state, 1, top_column_is_open)
        if move_not_to_lose:
            return move_not_to_lose

        """ return random """
        random_move = self.random_player.select_next_move(board_state,top_column_is_open)
        return random_move

    def winning_move_for_player(self,state:np.ndarray,
                                player_number:int
                                ,optional_columns:np.ndarray):

        """ try every column, return the column if player_number gets 4 """
        for column in optional_columns:

            self.inner_board.set_state(state)
            won = self.inner_board.play_move(column, player_number)
            if won:
                return column
        return None
