# Generated by Django 4.0.2 on 2022-04-02 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_alter_good_kind'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='good',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
