from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty, NumericProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

from src.flashcards_list_generation import Difficulty


class FlashcardAmountSelector(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.items = []
        for diff in Difficulty:
            self.items += [FlashcardViewClass(diff.name)]
            self.ids.main_box.add_widget(self.items[-1])

    def get_amounts(self):
        return [int(t.ids.text_field.text) for t in self.items]


class FlashcardViewClass(MDBoxLayout):
    title = StringProperty()

    def __init__(self, title="test", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title


Builder.load_file('gui/flashcards_amount_selector.kv')
