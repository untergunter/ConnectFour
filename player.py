from abc import ABC, abstractmethod
import numpy as np
from board import Board

class Player(ABC):
    @abstractmethod
    def select_next_move(self, board_state: np.ndarray,
                         top_column_is_open: np.ndarray):
        pass


class RandomAutoPlayer(Player):
    def select_next_move(self, board_state: np.ndarray,
                         top_column_is_open: np.ndarray):
        column = np.random.choice(top_column_is_open)
        return column

class HumanPlayer(Player):

    def select_next_move(self, board_state: np.ndarray,
                         top_column_is_open: np.ndarray):
        """
        get a valid move from a human player via cli
        :param board_state:
        :param top_column_is_open:
        :return:
        """
        user_column = -1
        top_column_is_open = {str(column) for column in top_column_is_open}
        columns_for_view = tuple(column for column in top_column_is_open)
        while user_column not in top_column_is_open:
            user_column = input(f'please select column from {columns_for_view}')
        selected_column = int(user_column)
        return selected_column

class SingleStepAutoPlayer(Player):
    def __init__(self):
        self.inner_board = Board()

    def select_next_move(self, board_state: np.ndarray,
                         top_column_is_open: np.ndarray):
        """
        if any action is a winner action - select it. else - act randomly.
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
        random_move = np.random.choice(top_column_is_open)
        return random_move

    def winning_move_for_player(self,state,player_number,optional_columns):
        """ try every column if it gets 4 """
        for column in optional_columns:

            self.inner_board.set_state(state)
            self.inner_board.play_move(column, player_number)
            if self.inner_board.Check_if_won():
                return column
        return None
