from about.models import About
from django.shortcuts import render

def index(request): 
        about = About.objects.all()
        # If there's more than one about article, choose the newest one 
        if about > 1:
            about = about.order_by('-id')[0]
        return render(request, 'about/index.html', { 'about': about })
