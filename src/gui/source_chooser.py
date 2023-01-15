from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from src.gui.path_chooser import LanguagesChooser


class SourceChooser(Screen):
    pass


Builder.load_file('gui/source_chooser.kv')