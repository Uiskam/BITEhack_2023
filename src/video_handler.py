import string
import cv2

class VideoHandler:
    def __init__(self, video_path: string):
        self.vid = cv2.VideoCapture(video_path)
        self.fps = self.vid.get(cv2.CAP_PROP_FPS)
        self.total_frames = int(self.vid.get(cv2.CAP_PROP_FRAME_COUNT))

    def get_frame(self, ms: int):
        self.vid.set(cv2.CAP_PROP_POS_MSEC, ms)

        ret, frame = self.vid.read()
        return frame