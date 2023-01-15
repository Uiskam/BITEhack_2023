import os
import sys

import pyautogui as pyautogui
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

from src.gui.list_editing_layout import ListEditingLayout
from src.gui.path_chooser import InputFilesScreen

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '')))

from kivy.core.window import Window

from src.flashcards_list_generation import generate_flashcard_templates_from_file, Difficulty
from src.subtitles_handler import SubtitlesHandler
from src.video_handler import VideoHandler
import cv2


def opencv_example():
    print("hello world")
    vid_handl = VideoHandler('../resources/video.mp4')

    cv2.imshow("Frame", vid_handl.get_frame(40000))

    # Wait for user to close the window
    cv2.waitKey(0)


def example_flashcards():
    flashcard_templates_list = generate_flashcard_templates_from_file("../resources/video.mp4",
                                                                      "../resources/subtitles.srt", 40, Difficulty.EASY,
                                                                      ["que"])
    for flashcard_templates_list in flashcard_templates_list:
        print("original:", flashcard_templates_list.original_word)
        print("translation:", flashcard_templates_list.translation)
        print("context:", flashcard_templates_list.context, "\n")
        back_media = flashcard_templates_list.back_media
        if back_media is not None:
            cv2.imshow("Image", back_media)
            cv2.waitKey(0)


class FlashcardGeneratorApp(MDApp):
    # def set_up_menu(self):
    #     menu_items = [
    #         {
    #             "viewclass": "IconListItem",
    #             "icon": "git",
    #             "text": f"Item {i}",
    #             "height": dp(56),
    #             "on_release": lambda x=f"Item {i}": self.set_item(x),
    #         } for i in range(5)
    #     ]
    #     print("self.menu sety")
    #     self.menu = MDDropdownMenu(
    #         # caller=self.screen.ids.drop_item,
    #         items=menu_items,
    #         position="center",
    #         width_mult=4,
    #     )
    #     self.menu.bind()

    def build(self):
        Window.size = (1280, 720)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.material_style = "M3"
        self.file_chooser = InputFilesScreen(name='file_chooser')
        Window.bind(on_drop_file=self._on_file_drop)
        sm = ScreenManager()
        sm.add_widget(self.file_chooser)
        sm.add_widget(
            ListEditingLayout(items=["asd", "basd"], title="Generated flashcards", name='flashcard_suggestions'))
        sm.current = "file_chooser"
        # self.set_up_menu()
        return sm

    def _on_file_drop(self, window, file_path, x, y):
        self.file_chooser.on_file_drop(window, file_path, x, y)
        if Window.focus == False:
            pyautogui.click()


def main():
    # example_flashcards()
    FlashcardGeneratorApp().run()


if __name__ == "__main__":
    main()
