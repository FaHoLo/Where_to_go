# Generated by Django 3.1 on 2020-09-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0015_auto_20200916_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, max_length=400, verbose_name='Короткое описание'),
        ),
    ]
