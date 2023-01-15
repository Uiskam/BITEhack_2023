import csv
from typing import List
# from flashcard_template import FlashcardTemplate


# import re

def save_to_anki(anki_templates: List, path: str):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        for card in anki_templates:
            writer.writerow([card.original_word, card.translation])
