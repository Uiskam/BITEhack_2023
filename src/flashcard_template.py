class FlashcardTemplate:
    def __init__(self, original_word: str, translation: str, context: str, back_media):
        self.original_word: str = original_word
        self.translation: str = translation
        self.context: str = context
        self.back_media = back_media
