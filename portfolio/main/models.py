from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    img_main = models.ImageField(upload_to='images', default='images/default.svg')
    img_email = models.ImageField(upload_to='images', default='images/default.svg')
    img_github = models.ImageField(upload_to='images', default='images/default.svg')
    img_linkedin = models.ImageField(upload_to='images', default='images/default.svg')


    def __str__(self):
        return self.title