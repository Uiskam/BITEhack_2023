from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.boxlayout import MDBoxLayout


class NavBar(MDBoxLayout):
    next_button_text = StringProperty("next")
    parent = ObjectProperty()
    next_callback = ObjectProperty()
    prev = StringProperty()
    next = StringProperty()

    def go_next(self):
        if self.next_callback is not None:
            self.next_callback()
        else:
            self.parent.manager.current = self.next

# Builder.load_file('gui/nav_bar.kv')