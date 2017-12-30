from __future__ import print_function

from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout # child widgets vertical or horizontal



class TestApp(App):
    def build(self):
        # widget declarations
        b = BoxLayout(orientation='vertical')
        t = TextInput(font_size=150, 
                    size_hint_y=None, # turn off autoscaling in y direction. 
                    height=200) #200 pixels sets height of visual block, 
                                # - this doesn't scale with window resize.

        f = FloatLayout() #size of layout relative to window size
        s = Scatter() #put the widget anywhere, move with mouse
        l = Label(text="Hello",font_size=150)

        
        t.bind(text=some_function) # when ever the text of the t changes 
                                    # - call the function some_function.
        
        # widget tree
        f.add_widget(s) #make scatter widget child of floatlayout widget
        s.add_widget(l) #make label widget child of scatter widget 

        b.add_widget(t) # order of widget declaration deteremines layout. 
        b.add_widget(f)
        return b # return the root widget

def some_function(*args): # I don't understand <<< TODO
    print("text changed")

if __name__ == "__main__":
    TestApp().run()
