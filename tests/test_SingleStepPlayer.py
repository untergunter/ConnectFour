import numpy as np
from src.player import SingleStepAutoPlayer


def test_SingleStepAutoPlayer_select_next_move():
    new_state = np.zeros((8,8))
    new_state[7, :3] = 1
    new_state[7, 5:] = 2
    player = SingleStepAutoPlayer()
    player.inner_board.set_state(new_state)
    can_place_at = player.inner_board.get_open_columns()
    board_state = player.inner_board.get_state_by_player_perspective(1)
    column = player.select_next_move(board_state, can_place_at)
    assert column==3

    player.inner_board.set_state(new_state)
    board_state = player.inner_board.get_state_by_player_perspective(2)
    column = player.select_next_move(board_state, can_place_at)
    assert column == 4
