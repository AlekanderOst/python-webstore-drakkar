# Generated by Django 4.0.2 on 2022-04-02 18:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_alter_good_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата заказа'),
        ),
    ]
