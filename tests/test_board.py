import numpy as np
from src.board import Board

def test_board_set_state():
    test_board = Board()
    new_state = np.arange(64)
    test_board.set_state(new_state)
    assert np.all(test_board.state==new_state)

def test_board_get_open_columns():
    test_board = Board()
    assert np.all(test_board.get_open_columns() == np.arange(8))
    full_board = np.ones((8,8))
    test_board.set_state(full_board)
    assert np.all(test_board.get_open_columns() == np.arange(0))

