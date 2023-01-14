from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu

Builder.load_file('gui/path_chooser.kv')
Builder.load_file('gui/input_files_screen.kv')


class InputFilesScreen(Screen):
    def on_file_drop(self, window, file_path, x, y):
        print("file dropped, im InputFilesScreen")
        self.ids.video_chooser.on_file_drop(window, file_path, x, y)
        self.ids.subtitles_chooser.on_file_drop(window, file_path, x, y)


class PathChooser(MDBoxLayout):
    file_type = StringProperty("file_type")

    def on_file_drop(self, window, file_path, x, y):
        if self.collide_point(*Window.mouse_pos):
            self.ids.input_field.text = file_path


class IconListItem(OneLineIconListItem):
    icon = StringProperty()


class LanguagesChooser(MDBoxLayout):
    file_type = StringProperty("file_type")
    supported_languages = ['Spanish', 'English']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": lang,
                "height": dp(56),
                "on_release": lambda x=lang: self.set_item(x),
            } for lang in self.supported_languages
        ]
        print("Langage Chooser init")
        self.menu = MDDropdownMenu(
            caller=self,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        # self.menu.bind()

    def set_item(self, text_item):
        self.ids.drop_item.set_item(text_item)
        self.menu.dismiss()

    def open_menu(self):
        # self.menu.caller = caller
        self.menu.open()
