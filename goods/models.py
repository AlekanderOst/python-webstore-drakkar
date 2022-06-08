from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Good(models.Model):
    slug = models.SlugField()
    kind = models.CharField('Type', max_length=120, default='')
    title = models.CharField('Name', max_length=120, default='')
    material = models.CharField('Material', max_length=120, default='')
    dimensions = models.CharField('Dimensions', max_length=120, default='')
    descriptions = models.TextField('Description', max_length=2000)
    cost = models.CharField('Cost', max_length=120, default='0')
    img = models.ImageField(default='default.jpg', upload_to='goods_images')
    date = models.DateTimeField(verbose_name='Date order', default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('good-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

