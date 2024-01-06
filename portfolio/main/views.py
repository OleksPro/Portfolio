from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView
from .forms import ContactForm
from .models import AllImages, AllLinks


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

        # Додайте об'єкт вашої форми до контексту
        ctx['contact_form'] = ContactForm()

        return ctx
    
    def post(self, request, *args, **kwargs):
            form = ContactForm(request.POST)
            if form.is_valid():
                # Отримати дані з форми
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                phone_number = form.cleaned_data['phone_number']
                message = form.cleaned_data['message']

                # Відправлення електронного листа
                subject = 'Новий запит від {}'.format(name)
                message_body = f'Ім\'я: {name}\nEmail: {email}\nТелефон: {phone_number}\nПовідомлення: {message}'
                from_email = 'Oleks.Prokopenko92@gmail.com'  # Ваша електронна адреса
                to_email = 'Oleks.Prokopenko92@gmail.com'  # Електронна адреса отримувача (ваша електронна адреса)

                send_mail(subject, message_body, from_email, [to_email])

                # Опціонально, можна також зберегти дані в базу даних
                # form.save()

                # Додайте повідомлення
                messages.success(request, 'Thank you for your inquiry. We will contact you shortly.')

                # Оновіть контекст знову, щоб передати форму та будь-які інші дані
                return self.get(request, *args, **kwargs)

            # Якщо форма не є валідною, додайте помилки до повідомлень
            for errors in form.errors.values():
                for error in errors:
                    messages.error(request, f'{error}')

            # Оновіть контекст знову, щоб передати форму та будь-які інші дані
            return self.get(request, *args, **kwargs)