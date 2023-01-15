import random
from urllib.parse import urlparse, parse_qs
from enum import Enum
from time import sleep

import cv2
from youtube_transcript_api import YouTubeTranscriptApi

from src.generation_parameters import GenerationParameters

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


def calc_word_list(subt_handl: SubtitlesHandler, params: GenerationParameters):
    word_list = subt_handl.get_word_list()
    word_list = list(filter(lambda x: x[0] not in params.banned_words, word_list))
    i = 0
    ans = []
    for amount in params.amounts:
        ans += random.sample(word_list[(i * len(word_list)) // len(Difficulty):
                                       ((i + 1) * len(word_list)) // len(Difficulty)], amount)
        i += 1
    return ans


def generate_flashcard_templates(params: GenerationParameters):
    if params.link is not None:
        return generate_flashcard_templates_from_link(params)
    return generate_flashcard_templates_from_file(params)


def generate_flashcard_templates_from_file(params: GenerationParameters) -> list[FlashcardTemplate]:
    subt_handl = FileSubtitlesHandler(params.subtitles_file)
    video_handl = FileVideoHandler(params.video_file)
    ans = []

    for word in calc_word_list(subt_handl, params):
        selection = random.randint(0, len(word[1]) - 1)
        translated_text = translate(text=word[0], source_language=params.original_language,
                                    destination_language=params.translation_language)
        # print("\n", params.original_language, " ------> ", params.translation_language)
        ans.append(FlashcardTemplate(word[0], translated_text, word[1][selection][2],
                                     video_handl.get_frame((word[1][selection][0] + word[1][selection][1]) / 2)))
    return ans


def generate_flashcard_templates_from_link(params: GenerationParameters) -> list[FlashcardTemplate]:
    subt_handl = LinkSubtitlesHandler(params.link, params.original_language)
    video_handl = LinkVideoHandler(params.link)
    ans = []

    for word in calc_word_list(subt_handl, params):
        selection = random.randint(0, len(word[1]) - 1)
        translated_text = translate(text=word[0], source_language=params.original_language,
                                    destination_language=params.translation_language)

        ans.append(FlashcardTemplate(word[0], translated_text, word[1][selection][2],
                                     video_handl.get_frame((word[1][selection][0] + word[1][selection][1]) / 2)))
        print(video_handl.get_frame((word[1][selection][0] + word[1][selection][1]) / 2))
    return ans
