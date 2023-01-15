import random
from enum import Enum
from time import sleep

import cv2

from src.flashcard_template import FlashcardTemplate
from subtitles_handler import SubtitlesHandler
from video_handler import VideoHandler


class Difficulty(Enum):
    EASY = 0,
    NORMAL = 1,
    HARD = 2


def calc_word_list(subt_handl: SubtitlesHandler, difficulty: Difficulty, amount: int, banned_words: list[str]):
    word_list = subt_handl.get_word_list()
    word_list = list(filter(lambda x: x[0] not in banned_words, word_list))
    if difficulty == Difficulty.EASY:
        return random.sample(word_list[:len(word_list) // 3], amount)
    if difficulty == Difficulty.NORMAL:
        return random.sample(word_list[len(word_list) // 3: (2 * len(word_list)) // 3], amount)
    if difficulty == Difficulty.HARD:
        return random.sample(word_list[(2 * len(word_list)) // 3:], amount)


def generate_flashcard_templates_from_file(video_file_path: str, subtitle_file_path: str, amount: int,
                                           difficulty: Difficulty, banned_words: list[str]) -> list[FlashcardTemplate]:
    subt_handl = SubtitlesHandler(subtitle_file_path)
    video_handl = VideoHandler(video_file_path)
    ans = []

    for word in calc_word_list(subt_handl, difficulty, amount, banned_words):
        selection = random.randint(0, len(word[1]) - 1)
        print(">" + word[0] + "<")
        ans.append(FlashcardTemplate(word[0], "translation of " + word[0], word[1][selection][2],
                                     video_handl.get_frame((word[1][selection][0] + word[1][selection][1]) / 2)))
    return ans
