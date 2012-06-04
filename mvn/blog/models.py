from django.db import models

class Entry(models.Model):
    def __unicode__(self):
        return self.headline
    headline = models.CharField('overskrift', max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    body = models.TextField('tekst')

class Image(models.Model):
    entry = models.ForeignKey(Entry)
    image = models.ImageField('bilde', upload_to='entries/images')
    caption = models.CharField('bildetekst', max_length=250, blank=True, null=True)
    
class File(models.Model):
    entry = models.ForeignKey(Entry)
    customfile = models.FileField('fil', upload_to='entries/files')
    
class Youtube(models.Model):
    entry = models.ForeignKey(Entry)
    videoid = models.CharField('video ID', max_length=200)