from time import sleep

from src.video_handler import VideoHandler
import cv2

if __name__ == "__main__":
    print("hello world")
    vid_handl = VideoHandler('../resources/video.mp4')

    cv2.imshow("Frame", vid_handl.get_frame(40000))

    # Wait for user to close the window
    cv2.waitKey(0)
