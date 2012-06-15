from django.db import models

class About(models.Model):
    portrait = models.ImageField(upload_to='about/')
    text = models.TextField()
