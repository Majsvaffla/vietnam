# Generated by Django 5.1.1 on 2024-10-01 21:00

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'kommentar', 'verbose_name_plural': 'kommentarer'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['order'], 'verbose_name': 'bild', 'verbose_name_plural': 'bilder'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'inlägg', 'verbose_name_plural': 'inlägg'},
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='ordning'),
        ),
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.CharField(max_length=70, verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(upload_to='', verbose_name='fil'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='författare'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='skapad'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='publicerad'),
        ),
        migrations.AlterField(
            model_name='post',
            name='number_of_likes',
            field=models.IntegerField(default=0, verbose_name='antal som gillar'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, verbose_name='titel'),
        ),
    ]
