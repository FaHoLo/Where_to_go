# Generated by Django 3.1 on 2020-08-10 13:37

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20200810_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Полное описание'),
        ),
    ]
