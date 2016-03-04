#!/usr/bin/env python
# coding:utf-8

import datetime
from random import random, randint

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from music_online.models import Song
from music_online.utils import get_direct_link, find_youtube_id, generate_voice_message, get_parser, get_source


def index(request):
    if 'localhost' not in request.META['HTTP_HOST']:
        return render(request, 'stop_music.html', {})

    now = datetime.datetime.now()
    today1515 = now.replace(hour=15, minute=15, second=0, microsecond=0)
    if now > today1515:
        return render(request, 'stop_music.html', {})

    today = datetime.date.today().strftime('%d/%m/%Y')
    song = Song.objects.get(song_name="Giấc Mơ Thiên Đường")
    song_list = Song.objects.filter(pub_date__exact=datetime.date.today())
    len_song_list = len(song_list)
    random_list = request.session.get(today)

    song_index = randint(0, len_song_list - 1)
    if random_list:
        count = 0
        while song_index in random_list:
            if count == len_song_list:
                random_list = []
                break
            song_index = randint(0, len(song_list) - 1)
            count += 1
    else:
        random_list = []

    random_list.append(song_index)
    request.session[today] = random_list

    selected_song = song
    if selected_song.source == 'other':
        direct_link = get_direct_link(selected_song.url)
        if not direct_link:
            return HttpResponseRedirect(reverse('index'))
    else:
        direct_link = None


    context = {
        'songlist': song_list,
        'direct_link': direct_link,
        'song_id': find_youtube_id(selected_song),
        'voice_message': generate_voice_message(selected_song.message)
    }
    return render(request, 'playerList.html', context)


def check_link(request):

    result = None
    error = None

    if request.method == 'POST':
        url = request.POST.get('url')
        if not url:
            error = 'input'
        else:
            parser = get_parser(url)
            if not parser:
                error = 'fail'
            else:
                link = parser.get_direct_link(url)
                if not link:
                    error = 'fail'
                else:
                    result = {
                        'link': link,
                        'source': get_source(url)
                    }

    return render(request, 'check_link.html', {'result': result, 'error': error})
