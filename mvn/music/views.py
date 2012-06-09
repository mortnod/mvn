from django.shortcuts import render
from music.models import MusicAlbum

def index(request):
    albums = MusicAlbum.objects.all()
    return render(request, 'music/index.html', {'albums': albums})
