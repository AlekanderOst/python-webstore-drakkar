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
    title = models.CharField('Product', max_length=100, default='')
    cost = models.CharField('Cost', max_length=100, default='0')
    choose_color = models.CharField('Color', max_length=20,choices=COLOR, default='black')
    date = models.DateTimeField(verbose_name ='Date order',default=timezone.now)
    author = models.ForeignKey(User, verbose_name ='Client',on_delete=models.SET_NULL,null=True)
    img = models.ImageField(default='default.jpg', upload_to='goods_images')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slug = None

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def get_absolute_url(self):
        return reverse('cart', kwargs={'username': self.author})




