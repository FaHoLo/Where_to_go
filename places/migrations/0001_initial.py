# Generated by Django 3.1 on 2020-08-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Заголовок')),
                ('description_short', models.CharField(blank=True, max_length=300, verbose_name='Короткое описание')),
                ('description_long', models.TextField(blank=True, verbose_name='Полное описание')),
                ('lat', models.FloatField(blank=True, verbose_name='Широта')),
                ('lng', models.FloatField(blank=True, verbose_name='Долгота')),
            ],
        ),
    ]
