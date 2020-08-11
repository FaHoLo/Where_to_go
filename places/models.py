from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    '''Detailed information about the place'''
    title = models.CharField('Заголовок', max_length=60)
    description_short = models.CharField('Короткое описание', max_length=300, blank=True)
    description_long = HTMLField('Полное описание', blank=True)
    lat = models.FloatField('Широта', blank=True)
    lng = models.FloatField('Долгота', blank=True)

    def __str__(self):
        return '{}'.format(self.title)


class Image(models.Model):
    image = models.ImageField('Изображение')
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image_number = models.PositiveIntegerField('Номер картинки для порядка отображения на сайте',
                                               default=0)

    class Meta:
        ordering = ('image_number',)

    def __str__(self):
        return f'{self.image_number} {self.place.title}'


class Location(models.Model):
    '''Location of event'''
    title = models.CharField('Короткое название', max_length=30)
    place_id = models.CharField('Уникальный идентификатор локации', max_length=30, unique=True)
    lat = models.FloatField('Широта')
    lng = models.FloatField('Долгота')

    def __str__(self):
        return f'{self.title}'
