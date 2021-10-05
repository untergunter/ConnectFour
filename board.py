import numpy as np

class Board:

    def __init__(self):
        self.state = np.zeros((8,8))

    def print_board(self)->None:
        """
        prints the board
        :return: None
        """
        print(self.state)


    def get_open_columns(self)->np.ndarray:
        """
        for every column in board
        returns True if column is open, False if not
        :return: np.ndarray
        """
        top_is_empty = self.state[0:1].flatten() == 0
        open_column_indexes = np.argwhere(top_is_empty == True).flatten()
        return open_column_indexes

    def get_state(self,player_number):
        """
        player needs to see his placed places as 1,
        other player locations as -1
        and free places as 0
        while board has 0 as free, 1 player 1 and 2 as player 2
        :param player_number:
        :return:
        """
        board = self.state.copy()
        board_to_player_perspective = {1:1 if player_number==1 else -1,
                                       2:-1 if player_number==1 else 1}
        player_view_board = np.vectorize(board_to_player_perspective.get)(board)
        return player_view_board

    def get_open_index_in_column(self,column):
        """
        find the lowest placeable cell in a given column
        :param column:
        :return:
        """
        available_rows_in_column = np.argwhere(self.state[:, column] == 0).flatten()
        if len(available_rows_in_column)==0:
            return None
        lower_row_in_column = np.max(available_rows_in_column)
        return lower_row_in_column

    def is_full(self)->bool:
        """
        checks if board has any open space
        :return:
        """
        is_full = not 0 in self.state
        return is_full

    def column_has_4(self,row, column):
        if row>4:
            return False
        all_values_under_last_entry = np.unique(self.state[row:row+4,column])
        won =  len(all_values_under_last_entry) == 1
        return won

    def row_has_4(self,row, column):
        in_this_row = 1
        player_number = self.state[row, column]
        for column_to_the_right in range(column,8):
            if self.state[row,column_to_the_right] == player_number:
                in_this_row+=1
            else: break
        for column_to_the_left in range(column-1,-1,-1):
            if self.state[0,column_to_the_left] == player_number:
                in_this_row+=1
            else: break

        won = in_this_row >= 4
        return won

    def top_left_to_bottom_right_has_4(self, row, column):
        in_this_diagonal = 1
        player_number = self.state[row, column]

        up_left = min(row, column) + 1
        for step in range(1,up_left):
            if self.state[row - step, column - step] == player_number:
                in_this_diagonal +=1
            else:break

        down_right = min(7-row , 7-column) + 1
        for step in range(1, down_right):
            if self.state[row + step, column + step] == player_number:
                in_this_diagonal += 1
            else:
                break

        won = in_this_diagonal >=4
        return won

    def top_right_to_bottom_left_has_4(self, row, column):
        in_this_diagonal = 1
        player_number = self.state[row, column]

        down_left = min(7-row, column) + 1
        for step in range(1, down_left):
            if self.state[row + step, column - step] == player_number:
                in_this_diagonal += 1
            else:
                break

        up_right = min(row, 7 - column) + 1
        for step in range(1, up_right):
            if self.state[row - step, column + step] == player_number:
                in_this_diagonal += 1
            else:
                break

        won = in_this_diagonal >= 4
        return won


    def Check_if_won(self,row, column):
        """ after placing at row,column chek if player won"""
        player_won = bool(
            self.column_has_4(row, column) +
            self.row_has_4(row,column) +
            self.top_left_to_bottom_right_has_4(row, column) +
            self.top_right_to_bottom_left_has_4(row, column)
        )
        return player_won


    def play_move(self, column, value_to_set):
        row = self.get_open_index_in_column(column)
        assert row is not None, f"{column} is full, cant place there"
        assert self.state[row,column]==0 , f"board[{row},{column}] is not empty"
        self.state[row, column] = value_to_set
        won = self.Check_if_won(row, column)
        return won

    def set_state(self,state):
        self.state = state
