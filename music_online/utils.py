import requests
from music_online.parser.nhaccuatui_parser import NhacCuaTuiParser
from music_online.parser.youtube_parser import YoutubeParser
from music_online.parser.zing_parser import ZingParser


def find_youtube_id(song):
    if song.source == 'youtube':
        return song.url.split('=')[1]

def get_parser(url):
    if 'mp3.zing.vn' in url:
        return ZingParser()
    elif 'www.nhaccuatui.com' in url:
        return NhacCuaTuiParser()
    elif 'youtube' in url:
        return YoutubeParser()
    else:
        return None

def get_source(url):
    if 'mp3.zing.vn' in url:
        return 'zing'
    elif 'www.nhaccuatui.com' in url:
        return 'nhaccuatui'
    elif 'youtube' in url:
        return 'youtube'
    else:
        return None

def get_direct_link(url):
    parser = get_parser(url)
    if not parser:
        return None
    return parser.get_direct_link(url)

def generate_voice_message(message):
    return None
    form_submit = {
        'text': message,
        'style': 'story',
        'ref': 'http://www.vnspeech.com/vi',
        'sig': 'reserved',
        'pid': 'reserved',
        'uid': 'reserved',
        'otp': 'reserved!'
    }
    try:
        response = requests.post('http://cloudtalk.vn/tts', data=form_submit)
    except:
        return None

    if response.status_code != 200:
        return None

    return 'http://cloudtalk.vn/ttsoutput?id=' + response.text