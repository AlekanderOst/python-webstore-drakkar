# Generated by Django 4.0.2 on 2022-04-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_good_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='cost',
            field=models.CharField(default='0', max_length=120, verbose_name='Стоимость'),
        ),
    ]
