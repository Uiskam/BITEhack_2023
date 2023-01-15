from dataclasses import dataclass, field
from typing import Optional

from src.flashcards_list_generation import Difficulty


@dataclass
class GenerationParameters:
    link: Optional[str]
    video_file: Optional[str]
    subtitles_file: Optional[str]
    original_language: str
    translation_language: str
    amounts: list[int]
    banned_words: list[str] = field(default_factory=lambda: [])
