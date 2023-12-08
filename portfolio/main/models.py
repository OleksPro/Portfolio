from django.db import models
from PIL import Image

select_options = (
    ('sociallinks', 'Sochial links'),
    ('services', 'Services'),
    ('skills', 'Skills'),
    ('learning', 'learning')
)

class AllImages(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    img = models.ImageField(upload_to='db_images', blank=True)
    category = models.CharField(max_length=11, choices=select_options)

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