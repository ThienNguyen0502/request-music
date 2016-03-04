from django.db import models

class Song(models.Model):
    YOUTUBE_KEY = 'youtube'
    YOUTUBE_VALUE = 'From youtube'
    OTHER_KEY = 'other'
    OTHER_VALUE = 'From zing or nhaccuatui'

    SOURCE_CHOICES = (
        (YOUTUBE_KEY, YOUTUBE_VALUE),
        (OTHER_KEY, OTHER_VALUE),
    )
    song_name = models.CharField('Song name', max_length=200)
    url = models.TextField('URL')
    source = models.CharField(max_length=50, choices=SOURCE_CHOICES, default=OTHER_KEY)
    sender = models.CharField('Sender', max_length=200)
    message = models.TextField('Message', blank=True)
    pub_date = models.DateField('Play on')

    def __unicode__(self):
        return self.song_name

    class Meta:
        ordering = ['song_name']
        verbose_name = "song"
