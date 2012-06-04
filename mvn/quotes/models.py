from django.db import models

class Quote(models.Model):
    def __unicode__(self):
        return self.quote
    quote = models.CharField('sitat', max_length='300')
    name = models.CharField('navn', max_length='100')

    