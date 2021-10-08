from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from board import Board
black = [0,0,0,0]
red = [1,0,0,1]
green = [0,1,0,1]
blue = [0,0,1,1]
purple = [1,0,1,1]
turquoise = [0,1,1,1]
gray = [1,1,1,1]


class Find4App(App):
    def build(self):
        self.board = Board()


        self.form = GridLayout(cols=8)
        self.buttons =[]

        for location_index in range(64):
            button = Button(background_color=gray,on_press=self.select_column)
            button.pos = (100,100)
            button.size = (0.1,0.1)
            button.loc_index = location_index
            self.buttons.append(button)
            self.form.add_widget(self.buttons[-1])
        return self.form


    def select_column(self,instance):
        column = instance.loc_index % 8
        row = instance.loc_index // 8
        self.buttons[instance.loc_index].background_color = green
        self.buttons[instance.loc_index].text = f'{row,column,instance.loc_index}'

# class Find4App(App):
#     def build(self):
#         self.board = GridLayout(cols=8)
#         self.butoons =[]
#         self.color_changers =[]
#         for row in range(8):
#             row_to_add = [Button(background_color=red) for column in range(8)]
#             color_funcs = [lambda ]



    # def make_color_change_

if __name__ == '__main__':
    Find4App().run()