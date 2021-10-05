from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class Find4App(App):
    def build(self):
        self.button = Button()
        self.button.pos = (100,100)
        self.button.size = (200,200)
        self.button.text = " nice one"

        self.form = Widget()
        self.form.add_widget(self.button)

        return self.form

if __name__ == '__main__':
    Find4App().run()