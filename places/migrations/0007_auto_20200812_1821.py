# Generated by Django 3.1 on 2020-08-12 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20200811_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='place_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.place', verbose_name='Подробная информация о локации'),
        ),
    ]
