from django.views.generic import ListView
from .models import AllImages, AllLinks
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages

class BaseHomeView(ListView):
    model = AllImages
    ordering = ['-id']
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['services'] = AllImages.objects.filter(category='services')
        ctx['skills'] = AllImages.objects.filter(category='skills')
        ctx['learning'] = AllImages.objects.filter(category='learning')
        ctx['footer_links'] = AllImages.objects.filter(category='footer_links')

        ctx['social_links'] = AllLinks.objects.filter(category='social_links')
        ctx['site_links'] = AllLinks.objects.filter(category='site_links')
        ctx['footer_links'] = AllLinks.objects.filter(category='footer_links')

        # Додавання об'єкта форми до контексту
        # Add form object to the context
        ctx['contact_form'] = ContactForm()

        return ctx

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            # Отримання даних з форми
            # Getting data from a form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']

            # Відправлення електронного листа
            # Sending an email
            subject = 'New request from {}'.format(name)
            message_body = f'Name: {name}\nEmail: {email}\nPhone nomber: {phone_number}\nMessage: {message}'
            from_email = 'Oleks.Prokopenko92@gmail.com'
            to_email = 'Oleks.Prokopenko92@gmail.com'

            send_mail(subject, message_body, from_email, [to_email])

            messages.success(request, 'Thank you for your inquiry. We will contact you shortly.')

            return self.get(request, *args, **kwargs)

        for errors in form.errors.values():
            for error in errors:
                messages.error(request, f'{error}')

        return self.get(request, *args, **kwargs)

class HomeView(BaseHomeView):
    template_name = 'main/home.html'

class HomeUkrainianView(BaseHomeView):
    template_name = 'main/home_uk.html'
