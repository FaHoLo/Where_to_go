# Generated by Django 3.1 on 2020-08-17 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20200812_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_number',
            field=models.PositiveIntegerField(default=0, verbose_name='Номер изображения для порядка отображения на сайте'),
        ),
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place', verbose_name='Локация, к которой относится изображение'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lng',
            field=models.FloatField(verbose_name='Долгота'),
        ),
    ]
