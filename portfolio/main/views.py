from django.shortcuts import render
from .models import SocialLinks, Services

def home(request):
    links = SocialLinks.objects.all()
    services = Services.objects.all()

    return render(
        request, 
        'main/home.html', 
        {
            'links': links,
            'services': services
        }
    )