from django.db import models
from PIL import Image

    
class SocialLinks(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='img_social_links', blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Social Link'
        verbose_name_plural = 'Social links'


class Services(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    img = models.ImageField(upload_to='img_services', blank=True)

    def save(self, *args, **kwargs):
        self.title = self.title.upper()
        super(Services, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Skills(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='img_skills', blank=True)

    def save(self, *args, **kwargs):
        self.title = self.title.upper()
        super(Skills, self).save(*args, **kwargs)

        image = Image.open(self.img.path)
        if image.height > 100 or image.width > 100:
            resize =  (100, 100)
            image.thumbnail(resize)
            image.save(self.img.path)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Skill'

