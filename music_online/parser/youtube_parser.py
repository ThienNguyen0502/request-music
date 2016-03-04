from music_online.parser import AbstractParser


class YoutubeParser(AbstractParser):
    def get_direct_link(self, url):
        return url.split('=')[1]