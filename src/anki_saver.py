import csv
import os
import numpy as np
import cv2


def save_to_anki(anki_templates: list, prefix='anki'):
    pwd = os.getcwd()
    print(pwd)

    for anki in anki_templates:
        if type(anki.back_media) == np.ndarray:
            image_name = f'{prefix}_{anki.original_word}.png'
            image_path = f'../resources/anki/images/{image_name}'
            cv2.imwrite(image_path, anki.back_media)

            with open('../resources/anki/anki.csv', 'a') as file:
                write = csv.writer(file)
                write.writerow([anki.original_word, anki.translation[1:-1], anki.context, f'<img src="{image_name}>"', ''])
        elif type(anki.back_media) == str:
            with open('../resources/anki/anki.csv', 'a') as file:
                write = csv.writer(file)
                write.writerow([anki.original_word, anki.translation[1:-1], anki.context, anki.back_media, ''])
    pass
