import string
from abc import ABC, abstractmethod
from urllib.parse import urlparse, parse_qs

import cv2


class VideoHandler(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_frame(self, ms: int):
        pass


class FileVideoHandler(VideoHandler):
    def __init__(self, video_path: str):
        super().__init__()
        self.vid = cv2.VideoCapture(video_path)
        self.fps = self.vid.get(cv2.CAP_PROP_FPS)
        self.total_frames = int(self.vid.get(cv2.CAP_PROP_FRAME_COUNT))

    def get_frame(self, ms: int):
        self.vid.set(cv2.CAP_PROP_POS_MSEC, ms)
        ret, frame = self.vid.read()
        return frame


class LinkVideoHandler(VideoHandler):
    def __init__(self, link: str):
        super().__init__()
        self.left_link_side = '<iframe width="560" height="315" src="'
        url_data = urlparse(link)
        query = parse_qs(url_data.query)
        video = query["v"][0]
        self.link = "https://www.youtube.com/embed/"+video
        self.right_link_side = '" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; ' \
                               'encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'

    def get_frame(self, ms: int):
        s = ms // 1000
        return self.left_link_side + self.link + "?start=" + str(int(s)) + self.right_link_side
