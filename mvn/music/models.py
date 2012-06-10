from django.db import models

class MusicAlbum(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField('albumnavn', max_length='100')

class Song(models.Model):
    album = models.ForeignKey(MusicAlbum)
    title = models.CharField('tittel', max_length='100')
    artist = models.CharField(max_length='100', blank=True, null=True)
    track_number = models.SmallIntegerField()
    m4a = models.FileField(upload_to='music')
    ogg = models.FileField(upload_to='music', blank=True, null=True)
   
class CoverPhoto(models.Model):
    album = models.ForeignKey(MusicAlbum)
    photo = models.ImageField('bilde', upload_to='music/cover')
    caption = models.CharField('bildetekst', max_length=250, blank=True, null=True)
