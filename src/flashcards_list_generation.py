import random
from enum import Enum

from src.flashcard_template import FlashcardTemplate
from subtitles_handler import SubtitlesHandler
from video_handler import VideoHandler


class Difficulty(Enum):
    EASY = 0,
    NORMAL = 1,
    HARD = 2


def generate_flashcard_templates_from_file(video_file_path: str, subtitle_file_path: str, difficulty: Difficulty) \
        -> list[FlashcardTemplate]:
    subt_handl = SubtitlesHandler(subtitle_file_path)
    video_handl = VideoHandler(video_file_path)
    ans = []
    for word in subt_handl.get_word_list():
        selection = random.randint(0, len(word[1]) - 1)
        ans.append(FlashcardTemplate(word[0], "translation of " + word[0], word[1][selection][2],
                                     video_handl.get_frame((word[1][selection][0] + word[1][selection][1]) / 2)))
    return ans
