from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from kivy.clock import Clock

from player import SingleStepAutoPlayer
from board import Board

BLACK = [0, 0, 0, 0]
RED = [1, 0, 0, 1]
GREEN = [0, 1, 0, 1]
BLUE = [0, 0, 1, 1]
PURPLE = [1, 0, 1, 1]
GRAY = [1, 1, 1, 1]


class Find4App(App):
    def build(self):
        self.board = Board()
        self.computer_player = SingleStepAutoPlayer()
        self.player_color = GREEN
        self.computer_color = RED
        self.game_ui = GridLayout(cols=8)
        self.buttons =[]

        for location_index in range(64):
            button = Button(background_color=GRAY, on_press=self.select_column)
            button.location_index = location_index
            button.column = location_index % 8
            button.row = location_index // 8
            self.buttons.append(button)
            self.game_ui.add_widget(self.buttons[-1])
        return self.game_ui


    def column_and_row_to_button_index(self,row,column):
        return column * 8 + row

    def set_color_ui(self,row,column,color):
        button_index = self.column_and_row_to_button_index(column,row)
        self.buttons[button_index].background_color = color


    def computer_take_turn(self):
        can_place_at = self.board.get_open_columns()
        board_state = self.board.get_state_by_player_perspective(2)
        column = self.computer_player.select_next_move(board_state, can_place_at)
        row = self.board.get_open_index_in_column(column)
        computer_won = self.board.play_move(column, 2)
        self.set_color_ui(row, column, self.computer_color)
        if computer_won:
            print('you lose, better luck next time :)')
        elif self.board.is_full():
            print("tie")

    def aet_selected_column(self,column):
        row = self.board.get_open_index_in_column(column)  # row to insert to
        player_won = self.board.play_move(column, 1)
        self.set_color_ui(row, column, self.player_color)
        return player_won

    def select_column(self,instance):
        column = instance.column
        valid_columns = self.board.get_open_columns()
        if column in valid_columns:
            player_won = self.aet_selected_column(column)
            if player_won:
                print('victory!!!')
            elif self.board.is_full():
                print("tie")
            else:
                Clock.schedule_once(lambda x: self.computer_take_turn(),0.5)

if __name__ == '__main__':
    Find4App().run()