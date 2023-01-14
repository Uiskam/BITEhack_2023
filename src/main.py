import os
import sys

import pyautogui as pyautogui
from kivymd.app import MDApp

from src.gui.path_chooser import InputFilesScreen

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '')))

from kivy.core.window import Window

from src.video_handler import VideoHandler
import cv2


def opencv_example():
    print("hello world")
    vid_handl = VideoHandler('../resources/video.mp4')

    cv2.imshow("Frame", vid_handl.get_frame(40000))

    # Wait for user to close the window
    cv2.waitKey(0)


class FlashcardGeneratorApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.material_style = "M3"
        self.file_chooser = InputFilesScreen()
        Window.bind(on_drop_file=self._on_file_drop)
        return self.file_chooser

    def _on_file_drop(self, window, file_path, x, y):
        self.file_chooser.on_file_drop(window, file_path, x, y)
        if Window.focus == False:
            pyautogui.click()


def main():
    FlashcardGeneratorApp().run()


if __name__ == "__main__":
    main()
