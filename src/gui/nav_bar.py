from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.boxlayout import MDBoxLayout


class NavBar(MDBoxLayout):
    parent = ObjectProperty()
    prev = StringProperty()
    next = StringProperty()

    pass

# Builder.load_file('gui/nav_bar.kv')