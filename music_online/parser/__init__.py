from bs4 import BeautifulSoup
import requests


class AbstractParser():

    def __init__(self):
        pass

    def get_direct_link(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            return None

        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            #download_tag = soup.find("a", {"id": "tabService"})
            download_tag = self.get_download_tag(soup)
            # code = download_tag.get('data-code')
            # group = download_tag.get('data-group')
            # panel = download_tag.get('data-panel')
            # download_url = 'http://mp3.zing.vn/xhr/song/get-download?panel=%(panel)s&code=%(code)s&group=%(group)s' % {
            #     'code': code,
            #     'group': group,
            #     'panel': panel
            # }
            if not download_tag:
                return None
            download_url = self.get_download_url(download_tag)

            # request download
            response_download = requests.get(download_url)

            if response_download.status_code != 200:
                return None

            # relative_path = response_download.json().get('data').get('128').get('link')
            # return 'http://mp3.zing.vn' + relative_path
            result = self.get_response_direct_link(response_download, soup)
        except Exception as e:
            return None

        return result

    def get_download_tag(self, soup):
        pass

    def get_download_url(self, download_tag):
        pass

    def get_response_direct_link(self, response_download, soup):
        pass



