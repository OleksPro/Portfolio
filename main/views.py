from django.shortcuts import render
from .models import SocialLinks, Services, Skills

def home(request):
    links = SocialLinks.objects.all()
    services = Services.objects.all()
    skills = Skills.objects.all()

    return render(
        request, 
        'main/home.html', 
        {
            'links': links,
            'services': services,
            'skills': skills
        }
    )