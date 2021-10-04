from abc import ABC,abstractmethod
import numpy as np


class Player(ABC):
    @abstractmethod
    def select_next_move(self, board_state:np.ndarray,
                         top_column_is_open:np.ndarray):
        pass

class RandomAutoPlayer(Player):
    def select_next_move(self, board_state:np.ndarray,
                         top_column_is_open: np.ndarray):
        column = np.random.choice(top_column_is_open)
        return column