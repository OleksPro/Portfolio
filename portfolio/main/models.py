from django.db import models

    
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

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Skill'