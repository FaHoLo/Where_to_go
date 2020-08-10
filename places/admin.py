from django.contrib import admin
from .models import Place, Image, Location


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    inlines = (ImageInline, )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('place', )


admin.site.register(Location)
