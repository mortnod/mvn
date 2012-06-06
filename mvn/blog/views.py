from django.shortcuts import render
from blog.models import Entry, Image

def index(request):
    entries = Entry.objects.all().order_by('-created')
    return render(request, 'blog/index.html', {'entries': entries})
