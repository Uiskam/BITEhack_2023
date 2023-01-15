import csv
from typing import List
from flashcard_template import FlashcardTemplate
import cv2
import os
import numpy as np

def save_to_anki(anki_templates: List[FlashcardTemplate], path: str, common_prefix='foo'):
    os.path.exists(path) or os.makedirs(path)
    os.path.exists(f'{path}/images') or os.makedirs(f'{path}/images')

    for card in anki_templates:

        # save image

        if type(card.back_media) == np.ndarray :
            fname = f'{path}/images/{common_prefix}_{card.original_word}.png'
            cv2.imwrite(fname, card.back_media)
            # save csv
            with open(f'{path}/anki.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([card.original_word, card.translation, card.context, f'<img src="{fname}">', ''])
        
        elif type(card.back_media) == str:
            # save csv
            with open(f'{path}/anki.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([card.original_word, card.translation, card.context, card.back_media, ''])


if __name__ == '__main__':
    save_to_anki([FlashcardTemplate("hello", "hola", "hello world", cv2.imread('resources/scr.png'))], 'resources/anki')
    save_to_anki([FlashcardTemplate("hellu", "hole", "hello world", '<iframe width="560" height="315" src="https://www.youtube.com/embed/lC6SRuGtIJ4?start=746" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')], 'resources/anki')
