from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window


class InputFilesScreen(MDBoxLayout):
    def on_file_drop(self, window, file_path, x, y):
        print("file dropped, im InputFilesScreen")
        self.ids.video_chooser.on_file_drop(window, file_path, x, y)
        self.ids.subtitles_chooser.on_file_drop(window, file_path, x, y)


class PathChooser(MDBoxLayout):
    file_type = StringProperty("file_type")

    def on_file_drop(self, window, file_path, x, y):
        if self.collide_point(*Window.mouse_pos):
            self.ids.input_field.text = file_path


Builder.load_file('gui/path_chooser.kv')
Builder.load_file('gui/input_files_screen.kv')
