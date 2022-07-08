# Generated by Django 3.2.12 on 2022-05-23 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isis', '0004_auto_20220523_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='media', verbose_name='Primary Image'),
        ),
    ]
