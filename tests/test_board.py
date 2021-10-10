import numpy as np
from src.board import Board

def test_board_set_state():
    new_state = np.arange(64)
    test_board = Board()
    test_board.set_state(new_state)
    assert np.all(test_board.state==new_state)

def test_board_get_open_columns():
    test_board = Board()
    assert np.all(test_board.get_open_columns() == np.arange(8))
    full_board = np.ones((8,8))
    test_board.set_state(full_board)
    assert np.all(test_board.get_open_columns() == np.arange(0))

def test_board_get_state_by_player_perspective():
    test_board = Board()
    assert np.all(test_board.get_state_by_player_perspective(1) == np.zeros((8,8)))
    assert np.all(test_board.get_state_by_player_perspective(2) == np.zeros((8, 8)))
    all_1 = np.ones((8,8))
    test_board.set_state(all_1)
    assert np.all(test_board.get_state_by_player_perspective(1) == np.ones((8,8)))
    assert np.all(test_board.get_state_by_player_perspective(2) == -1 * np.ones((8, 8)))
    all_2 = 2 * np.ones((8,8))
    test_board.set_state(all_2)
    assert np.all(test_board.get_state_by_player_perspective(1) == -1 * np.ones((8,8)))
    assert np.all(test_board.get_state_by_player_perspective(2) == np.ones((8, 8)))

def test_board_column_has_4():
    new_state = np.zeros((8,8))
    new_state[4:8,0] = 1
    new_state[5:8, 1] = 1
    new_state[0:4, 2] = 1
    new_state[0:3, 3] = 1
    test_board = Board()
    test_board.set_state(new_state)
    assert test_board.column_has_4(4,0) is True
    assert test_board.column_has_4(5,1) is False
    assert test_board.column_has_4(0,2) is True
    assert test_board.column_has_4(0,3) is False

def test_board_row_has_4():
    new_state = np.zeros((8, 8))
    new_state[0,0:4] = 1
    new_state[0, 5:8] = 1
    test_board = Board()
    test_board.set_state(new_state)
    assert test_board.row_has_4(0,0) is True
    assert test_board.row_has_4(0,1) is True
    assert test_board.row_has_4(0,2) is True
    assert test_board.row_has_4(0,3) is True

    assert test_board.row_has_4(0,5) is False
    assert test_board.row_has_4(0,6) is False
    assert test_board.row_has_4(0,7) is False

def test_board_top_left_to_bottom_right_has_4():
    new_state = np.zeros((8, 8))
    for i in range(3):
        new_state[i,i]=1

    test_board = Board()
    test_board.set_state(new_state)
    for i in range(3):
        assert test_board.top_left_to_bottom_right_has_4(i,i) is False

    new_state[3,3]=1
    test_board.set_state(new_state)
    for i in range(4):
        assert test_board.top_left_to_bottom_right_has_4(i,i) is True
