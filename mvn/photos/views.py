from django.shortcuts import render, get_object_or_404
from photos.models import Album

def index(request):
    albums = Album.objects.all()
    return render(request, 'photos/index.html', {'albums': albums})
    
def album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'photos/album.html', {'album': album})