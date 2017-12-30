from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):
    def build(self):
        return Button(text='Hello World',background_color=(1,1,1,1),font_size=150)

TestApp().run()

