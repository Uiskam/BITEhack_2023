import re

import pysrt


class SubtitlesHandler:
    def __init__(self, file_name):
        self.subs = pysrt.open(file_name)
        self.word_count = []

    def get_word_list(self):
        def time_to_ms(time):
            return int(time.hour * 3600000 + time.minute * 60000 + time.second * 1000 + time.microsecond / 1000)

        word_freq = {}
        for sub in self.subs:
            start = time_to_ms(sub.start.to_time())
            end = time_to_ms(sub.end.to_time())
            for potential_word in re.sub("<[^>]*>", "", sub.text).split():
                potential_word
                word = re.sub(r'[^0-9\w\s\u0300-\u036f]', '', potential_word).lower()

                if word in word_freq:
                    word_freq[word] += [(start, end, re.sub("<[^>]*>", "", sub.text))]
                else:
                    word_freq[word] = [(start, end, re.sub("<[^>]*>", "", sub.text))]

        for key, value in word_freq.items():
            self.word_count += [(key, value)]
        self.word_count = sorted(self.word_count, key=lambda x: -len(x[1]))
        return self.word_count
