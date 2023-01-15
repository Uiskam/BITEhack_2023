import cv2
from kivy.graphics.texture import Texture
from kivy.core.image import Image


class FlashcardTemplate:
    yt_texture = texture = Image('../resources/yt_logo.png').texture
    def __init__(self, original_word: str, translation: str, context: str, back_media):
        self.original_word: str = original_word
        self.translation: str = translation
        self.context: str = context
        self.back_media = back_media

    def get_texture(self):
        if isinstance(self.back_media, str):
            return self.yt_texture
        data = self.back_media.tobytes()
        w, h, _ = self.back_media.shape
        buf1 = cv2.flip(self.back_media, 0)
        buf = buf1.tobytes()

        # texture
        texture = Texture.create(size=(h, w), colorfmt="bgr")
        texture.blit_buffer(buf, bufferfmt="ubyte", colorfmt="bgr")
        return texture

