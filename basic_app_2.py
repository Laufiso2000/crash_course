from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class TestApp(App):
    def build(self):
        f = FloatLayout() #size of layout relative to window size
        s = Scatter() #put the widget anywhere, move with mouse
        l = Label(text="Hello",font_size=150)

        f.add_widget(s) #make scatter widget child of floatlayout widget
        s.add_widget(l) #make labl widget child of scatter widget 

        return f # return the parent widget

if __name__ == "__main__":
    TestApp().run()
