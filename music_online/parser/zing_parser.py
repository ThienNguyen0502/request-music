from bs4 import BeautifulSoup
import requests

from music_online.parser import AbstractParser


class ZingParser(AbstractParser):

    def get_download_tag(self, soup):
        return soup.find("div", {"id": "html5player"})

    def get_download_url(self, download_tag):
        # code = download_tag.get('data-code')
        # group = download_tag.get('data-group')
        # panel = download_tag.get('data-panel')
        # download_url = 'http://mp3.zing.vn/xhr/song/get-download?panel=%(panel)s&code=%(code)s&group=%(group)s' % {
        #     'code': code,
        #     'group': group,
        #     'panel': panel
        # }

        return download_tag.attrs['data-xml']

    def get_response_direct_link(self, response_download, soup):
        # data = response_download.json().get('data')
        # if data:
        #     relative_path = data.get('128').get('link')
        #     return 'http://mp3.zing.vn' + relative_path
        # else:
            # Permission denied. Get download link from xml
            # div_player = soup.find("div", {"id": "player5"})
            # data_xml = div_player.get('data-xml')
            # response_data_xml = requests.get(data_xml)
            # if response_data_xml.status_code != 200:
            #     return None
            #
            # soup = BeautifulSoup(response_data_xml.content, 'html.parser')
            # source = soup.find('source')
            # if source:
            #     return source.contents[0]
            # return None

        if response_download.status_code != 200:
            return None

        soup = BeautifulSoup(response_download.content, 'html.parser')
        source = soup.find('source')
        if source:
            return source.contents[0]
        return None
