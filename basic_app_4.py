from __future__ import print_function

from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout # child widgets vertical or horizontal


class Booger(BoxLayout):
    pass

class TestApp(App):
    def build(self):
        return Booger()


if __name__ == "__main__":
    TestApp().run()
