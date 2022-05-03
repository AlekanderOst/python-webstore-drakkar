from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Cart(models.Model):
    COLOR = [
        ('black', 'black'),
        ('green', 'green'),
        ('red', 'red'),
        ('yelow', 'yelow'),
        ('blue', 'blue'),
    ]
    title = models.CharField('Товар', max_length=100, default='')
    cost = models.CharField('Стоимость', max_length=100, default='0')
    choose_color = models.CharField('Цвет', max_length=20,choices=COLOR, default='black')
    date = models.DateTimeField(verbose_name ='Дата заказа',default=timezone.now)
    author = models.ForeignKey(User, verbose_name ='Клиент',on_delete=models.SET_NULL,null=True)
    img = models.ImageField(default='default.jpg', upload_to='goods_images')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slug = None

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def get_absolute_url(self):
        return reverse('cart', kwargs={'username': self.author})




