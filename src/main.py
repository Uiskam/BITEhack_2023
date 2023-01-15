import os
import sys

from youtube_transcript_api import YouTubeTranscriptApi

from src.anki_saver import save_to_anki
from src.generation_parameters import GenerationParameters
from src.gui.source_chooser import SourceChooser

'''
pip install youtube-transcript-api # for windows
or 
pip3 install youtube-transcript-api # for Linux and MacOs 
'''

import pyautogui as pyautogui
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

from src.gui.flashcard_amount_selector import FlashcardAmountSelector
from src.gui.list_editing_layout import ListEditingLayout
from src.gui.path_chooser import InputFilesScreen, LanguagesChooser

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '')))

from kivy.core.window import Window

from src.flashcards_list_generation import generate_flashcard_templates_from_file, Difficulty, \
    generate_flashcard_templates_from_link, generate_flashcard_templates
from src.subtitles_handler import SubtitlesHandler
from src.video_handler import VideoHandler
import cv2


def opencv_example():
    print("hello world")
    vid_handl = VideoHandler('../resources/video.mp4')

    cv2.imshow("Frame", vid_handl.get_frame(40000))

    # Wait for user to close the window
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
        self.generation_params = GenerationParameters(None, None, None, None, None, [], [])
        Window.size = (1280, 720)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.material_style = "M3"
        self.source_chooser = SourceChooser(name='source_chooser')
        self.file_chooser = InputFilesScreen(name='file_chooser')
        self.amount_picker = FlashcardAmountSelector(name='amount_picker')
        Window.bind(on_drop_file=self._on_file_drop)
        self.sm = ScreenManager()
        self.sm.add_widget(self.source_chooser)
        self.sm.add_widget(self.amount_picker)
        self.sm.add_widget(self.file_chooser)

        # prints the result

        # flashcards = generate_flashcard_templates_from_file("../resources/video.mp4",
        #                                                     "../resources/subtitles.srt", 40, Difficulty.EASY,
        #                                                     ["que"])
        # # generate_flashcard_templates_from_link(
        #     "https://www.youtube.com/watch?v=lC6SRuGtIJ4&ab_channel=ChejoQuemeAndrino","es")

        # self.sm.add_widget(
        #     ListEditingLayout(items=flashcards, title="Generated flashcards", name='flashcard_suggestions'))
        self.sm.current = "source_chooser"
        # self.set_up_menu()
        return self.sm

    def go_amounts_from_yt(self, link: str, original_lang: str, translated_lang: str):
        original_lang = LanguagesChooser.lang_code[original_lang]
        translated_lang = LanguagesChooser.lang_code[translated_lang]
        self.generation_params.link = link
        self.generation_params.original_language = original_lang
        self.generation_params.translation_language = 'en'
        self.amount_picker.prev = "source_chooser"
        self.sm.current = "amount_picker"

    def go_suggestions_from_amounts(self):
        self.generation_params.amounts = self.amount_picker.get_amounts()
        self.flashcards = generate_flashcard_templates(self.generation_params)
        self.sm.add_widget(
            ListEditingLayout(items=self.flashcards, title="Generated flashcards", name='flashcard_suggestions'))
        self.sm.current = "flashcard_suggestions"

    # def suggestion_from_link(self, link: str):
    #     self.flashcards = generate_flashcard_templates_from_link(link, 'es')
    #     self.sm.add_widget(
    #         ListEditingLayout(items=self.flashcards, title="Generated flashcards", name='flashcard_suggestions'))
    #     self.sm.current = "source_chooser"

    def _on_file_drop(self, window, file_path, x, y):
        self.file_chooser.on_file_drop(window, file_path, x, y)
        if Window.focus == False:
            pyautogui.click()

    def generate_anki(self):
        print("generating anki")
        save_to_anki(self.flashcards, os.path.join('output'))


def main():
    # example_flashcards()
    FlashcardGeneratorApp().run()


if __name__ == "__main__":
    main()
