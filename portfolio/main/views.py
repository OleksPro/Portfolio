from .models import AllImages, AllLinks
from django.views.generic import ListView
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponse


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

        return ctx

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Тестове повідомлення"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'phone_number': form.cleaned_data['phone_number'],
                'message': form.cleaned_data['message']
            }
            message = "\n".join(body.values())
            try:
                send_mail(
                    subject, 
                    message,
                    'admin@example.com',
                    ['admin@example.com']
                )
            except BadHeaderError:
                return HttpResponse("Не коректні дані")
            return redirect("main:homepage")

        return render(request, "main/home.html", {'form': form})


