# Generated by Django 4.0.2 on 2022-04-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0009_alter_good_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='dimensions',
            field=models.CharField(default='', max_length=120, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='good',
            name='material',
            field=models.CharField(default='', max_length=120, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='good',
            name='descriptions',
            field=models.TextField(max_length=2000, verbose_name='Описание'),
        ),
    ]
