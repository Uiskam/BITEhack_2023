import random
from urllib.parse import urlparse, parse_qs
from enum import Enum
from time import sleep

import cv2
from youtube_transcript_api import YouTubeTranscriptApi

'''
pip install youtube-transcript-api # for windows
or 
pip3 install youtube-transcript-api # for Linux and MacOs 
'''

from src.flashcard_template import FlashcardTemplate
from subtitles_handler import SubtitlesHandler, FileSubtitlesHandler, LinkSubtitlesHandler
from video_handler import FileVideoHandler, LinkVideoHandler
from translate_api import translate


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
    subt_handl = FileSubtitlesHandler(subtitle_file_path)
    video_handl = FileVideoHandler(video_file_path)
    ans = []

    for word in calc_word_list(subt_handl, difficulty, amount, banned_words):
        selection = random.randint(0, len(word[1]) - 1)
        translated_text = translate(text=[0], source_language='es', destination_language='en')
        ans.append(FlashcardTemplate(word[0], translated_text, word[1][selection][2],
                                     video_handl.get_frame((word[1][selection][0] + word[1][selection][1]) / 2)))
    return ans


def generate_flashcard_templates_from_link(yt_link: str, subt_language_short: str, amount: int, difficulty: Difficulty,
                                           banned_words: list[str]) -> list[FlashcardTemplate]:
    subt_handl = LinkSubtitlesHandler(yt_link, subt_language_short)
    video_handl = LinkVideoHandler(yt_link)
    ans = []

    for word in calc_word_list(subt_handl, difficulty, amount, banned_words):
        print(word[0])
        selection = random.randint(0, len(word[1]) - 1)
        translated_text = translate(text=[0], source_language=subt_language_short, destination_language='en')
        ans.append(FlashcardTemplate(word[0], translated_text, word[1][selection][2],
                                     video_handl.get_frame((word[1][selection][0] + word[1][selection][1]) / 2)))
    return ans
