# Generated by Django 3.1 on 2020-08-17 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20200817_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_images', to='places.place', verbose_name='Локация, к которой относится изображение'),
        ),
    ]
