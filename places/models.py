from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    """Detailed information about the place."""

    title = models.CharField('Заголовок', max_length=60)
    short_title = models.CharField('Короткий заголовок для отображения на карте', max_length=30,
                                   null=True)
    place_id = models.CharField('Уникальный идентификатор локации', max_length=30, unique=True,
                                null=True)
    description_short = models.CharField('Короткое описание', max_length=400, blank=True)
    description_long = HTMLField('Полное описание', blank=True)
    lat = models.FloatField('Широта')
    lng = models.FloatField('Долгота')

    def __str__(self):
        return str(self.title)


class Image(models.Model):
    """Place image."""

    image = models.ImageField('Изображение')
    place = models.ForeignKey(Place, verbose_name='Локация, к которой относится изображение',
                              on_delete=models.CASCADE, related_name='images')
    image_number = models.PositiveIntegerField('Номер изображения для порядка отображения на сайте',
                                               default=0)

    class Meta:
        ordering = ('image_number',)

    def __str__(self):
        return f'{self.image_number} {self.place.title}'
