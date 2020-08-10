# Generated by Django 3.1 on 2020-08-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('image_number',)},
        ),
        migrations.AlterField(
            model_name='image',
            name='image_number',
            field=models.PositiveIntegerField(default=0, verbose_name='Номер картинки для порядка отображения на сайте'),
        ),
    ]
