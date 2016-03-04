from music_online.parser import AbstractParser


class NhacCuaTuiParser(AbstractParser):

    def get_download_tag(self, soup):
        download_tag = soup.find("a", {"class": "btnDownload download"})
        if download_tag:
            return download_tag
        else:
            return soup.find("a", {"class": "btn btnDownload download"})

    def get_download_url(self, download_tag):
        key = download_tag.get('key')
        download_url = 'http://www.nhaccuatui.com/download/song/%(key)s' % {
            'key': key,
        }
        return download_url

    def get_response_direct_link(self, response_download, soup):
        result = response_download.json().get('data').get('stream_url')
        return result