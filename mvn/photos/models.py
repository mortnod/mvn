from django.db import models

class Album(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField('navn', max_length='100')
    cover = models.ImageField(upload_to='photos/cover')

class Photo(models.Model):
    album = models.ForeignKey(Album)
    photo = models.ImageField('bilde', upload_to='photos')
    caption = models.CharField('bildetekst', max_length='200', blank=True, null=True)