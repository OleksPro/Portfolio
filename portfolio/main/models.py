from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    img_main = models.ImageField(upload_to='images', blank=True)
    img_email = models.ImageField(upload_to='images', blank=True)
    img_github = models.ImageField(upload_to='images', blank=True)
    img_linkedin = models.ImageField(upload_to='images', blank=True)
    img_it = models.ImageField(upload_to='images', blank=True)
    img_separator = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.title