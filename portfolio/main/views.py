from django.shortcuts import render

def home(request):
    return render(request, "main/home.html")

def skills(request):
    return render(request, "main/skills.html")

def about(request):
    return render(request, "main/about_me.html")

def portfolio(request):
    return render(request, "main/portfolio.html")