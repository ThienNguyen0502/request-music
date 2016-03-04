#!/usr/bin/env python
#coding:utf-8

import requests
from music_online.parser.nhaccuatui_parser import NhacCuaTuiParser

# parser = NhacCuaTuiParser()
# link = parser.get_direct_link('http://www.nhaccuatui.com/bai-hat/anh-muon-em-song-sao-che-mrkuti-cech.v4G8vwSgeAw1.html')
# print link


message = """
Ngày đầu tiên đi học
Mẹ dắt tay đến trường
Em vừa đi vừa khóc
Mẹ dỗ dành yêu thương.

Ngày đầu tiên đi học
Em mắt ướt nhạt nhòa
Cô vỗ về an ủi
Chao ôi! Sao thiết tha.

Ngày đầu như thế đó
Cô giáo như mẹ hiền
Em bây giờ cứ ngỡ
Cô giáo là cô tiên.

Em bây giờ khôn lớn
Bỗng nhớ về ngày xưa
Ngày đầu tiên đi học
Mẹ cùng cô vỗ về.

            (Viễn Phương)

"""

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
    print None
if response.status_code != 200:
    print None

print 'http://cloudtalk.vn/ttsoutput?id=' + response.text