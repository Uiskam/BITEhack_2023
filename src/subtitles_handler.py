from abc import ABC, abstractmethod
from urllib.parse import urlparse, parse_qs

import regex as re

import pysrt
from youtube_transcript_api import YouTubeTranscriptApi


class SubtitlesHandler(ABC):
    def __init__(self):
        self.subs = []
        self.word_count = []

    def time_to_ms(self, time):
        return int(time.hour * 3600000 + time.minute * 60000 + time.second * 1000 + time.microsecond / 1000)

    @abstractmethod
    def extract_time(self, sub):
        pass

    @abstractmethod
    def extract_text(self, sub) -> str:
        pass

    def get_word_list(self):
        word_freq = {}
        for sub in self.subs:
            start, end = self.extract_time(sub)
            for potential_word in re.sub("<[^>]*>", "", self.extract_text(sub)).split():
                word = potential_word.lower()
                word = re.sub(r'[\p{P}\p{N}]', '', word)

                if word in word_freq:
                    word_freq[word] += [(start, end, re.sub("<[^>]*>", "", self.extract_text(sub)))]
                else:
                    word_freq[word] = [(start, end, re.sub("<[^>]*>", "", self.extract_text(sub)))]

        for key, value in word_freq.items():
            self.word_count += [(key, value)]
        self.word_count = sorted(self.word_count, key=lambda x: -len(x[1]))
        return self.word_count


class FileSubtitlesHandler(SubtitlesHandler):
    def __init__(self, file_name: str):
        super().__init__()
        self.subs = pysrt.open(file_name)

    def extract_text(self, sub) -> str:
        return sub.text

    def extract_time(self, sub):
        return self.time_to_ms(sub.start.to_time()), self.time_to_ms(sub.end.to_time())


class LinkSubtitlesHandler(SubtitlesHandler):
    def __init__(self, yt_link, language_short: str):
        super().__init__()
        url_data = urlparse(yt_link)
        query = parse_qs(url_data.query)
        video = query["v"][0]
        srt = YouTubeTranscriptApi.get_transcript(video, languages=[language_short])
        self.subs = srt

    def extract_text(self, sub) -> str:
        return sub["text"]

    def extract_time(self, sub):
        return (sub["start"]*1000), ((sub["start"] + sub["duration"])*1000)
