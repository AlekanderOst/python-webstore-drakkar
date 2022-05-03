from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Good(models.Model):
    slug = models.SlugField()
    kind = models.CharField('Тип', max_length=120, default='')
    title = models.CharField('Название', max_length=120, default='')
    material = models.CharField('Материал', max_length=120, default='')
    dimensions = models.CharField('Габариты', max_length=120, default='')
    descriptions = models.TextField('Описание', max_length=2000)
    cost = models.CharField('Стоимость', max_length=120, default='0')
    img = models.ImageField(default='default.jpg', upload_to='goods_images')
    date = models.DateTimeField(verbose_name='Дата заказа', default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('good-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

