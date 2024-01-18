from django.urls import path
from .views import HomeView, HomeUkrainianView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home_uk/', HomeUkrainianView.as_view(), name='home_uk'),
]

