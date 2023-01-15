from time import sleep

from src.flashcards_list_generation import generate_flashcard_templates_from_file, Difficulty
from src.subtitles_handler import SubtitlesHandler
from src.video_handler import VideoHandler
import cv2

if __name__ == "__main__":
    flashcard_templates_list = generate_flashcard_templates_from_file("../resources/video.mp4",
                                                                      "../resources/subtitles.srt", 40, Difficulty.EASY,
                                                                      ["que"])
    for flashcard_templates_list in flashcard_templates_list:
        print("original:", flashcard_templates_list.original_word)
        print("translation:", flashcard_templates_list.translation)
        print("context:", flashcard_templates_list.context, "\n")
        back_media = flashcard_templates_list.back_media
        if back_media is not None:
            cv2.imshow("Image", back_media)
            cv2.waitKey(0)
