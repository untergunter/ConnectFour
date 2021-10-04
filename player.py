from abc import ABC, abstractmethod
import numpy as np


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
        user_column = -1
        top_column_is_open = {str(column) for column in top_column_is_open}
        columns_for_view = tuple(column for column in top_column_is_open)
        while user_column not in top_column_is_open:
            user_column = input(f'please select column from {columns_for_view}')
        selected_column = int(user_column)
        return selected_column
