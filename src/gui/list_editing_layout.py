from typing import List

from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout

from src.flashcard_template import FlashcardTemplate


class ListEditingLayout(Screen):
    title = StringProperty()
    items = ListProperty()

    def __init__(self, title: str, items: List[FlashcardTemplate], **kwargs):
        super().__init__(**kwargs)
        self.items = items
        self.title = title

    def add_item(self, name: str):
        self.items.append(name)

    def remove_item(self, item):
        self.items.remove(item)


class ItemViewClass(MDBoxLayout):
    flashcard = ObjectProperty()
    remove = ObjectProperty()


Builder.load_file('gui/list_editing_layout.kv')
