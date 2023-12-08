from .models import AllImages
from django.views.generic import ListView


class Home_page(ListView):
    model = AllImages
    template_name = 'main/home.html'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        ctx = super(Home_page, self).get_context_data(**kwargs)
        ctx['social_links'] = AllImages.objects.filter(category='sociallinks')
        ctx['services'] = AllImages.objects.filter(category='services')
        ctx['skills'] = AllImages.objects.filter(category='skills')
        ctx['learning'] = AllImages.objects.filter(category='learning')

        return ctx
