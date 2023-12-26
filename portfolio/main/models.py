from django.db import models
from PIL import Image
from django import forms

img_category = (
    ('services', 'Services'),
    ('skills', 'Skills'),
    ('learning', 'learning'),
)

class AllImages(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='all_images', blank=True)
    category = models.CharField(blank=True, max_length=11, choices=img_category)

    def save(self, *args, **kwargs):
        super(AllImages, self).save(*args, **kwargs)
        image = Image.open(self.img.path)
        if image.height > 100 or image.width > 100:
            resize =  (100, 100)
            image.thumbnail(resize)
            image.save(self.img.path)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'All images'


links_category = (
    ('social_links', 'social_links'),
    ('site_links', 'site_links'),
    ('footer_links', 'footer_links'),
)

class AllLinks(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='site_images', blank=True)
    link = models.URLField(null=True, blank=True)
    category = models.CharField(blank=True, max_length=12, choices=links_category)

    def save(self, *args, **kwargs):
        super(AllLinks, self).save(*args, **kwargs)
        image = Image.open(self.img.path)
        if image.height > 640 or image.width > 400:
            resize =  (640, 400)
            image.thumbnail(resize)
            image.save(self.img.path)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'All links'


class CallbackForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ENTER YOUR NAME*'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'ENTER YOUR EMAIL*'}))
    phone_number = forms.CharField(max_length=13, widget=forms.TextInput(attrs={'placeholder': 'PHONE NUMBER'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'YOUR MESSAGE*'}))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Contact form'