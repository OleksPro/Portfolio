from .models import AllImages, AllLinks, CallbackForm
from django.views.generic import ListView
from django.contrib import messages


class Home_page(ListView):
    model = AllImages
    template_name = 'main/home.html'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        ctx = super(Home_page, self).get_context_data(**kwargs)
        ctx['services'] = AllImages.objects.filter(category='services')
        ctx['skills'] = AllImages.objects.filter(category='skills')
        ctx['learning'] = AllImages.objects.filter(category='learning')
        ctx['footer_links'] = AllImages.objects.filter(category='footer_links')

        ctx['social_links'] = AllLinks.objects.filter(category='social_links')
        ctx['site_links'] = AllLinks.objects.filter(category='site_links')
        ctx['footer_links'] = AllLinks.objects.filter(category='footer_links')

        if self.request.method == "POST":
            form = CallbackForm(self.request.POST)
            if form.is_valid():
                form.save()
                messages.success(self.request, 'Thank you, your message has been sent successfully')
        else:
            form = CallbackForm()
            
        ctx['form'] = form

        return ctx