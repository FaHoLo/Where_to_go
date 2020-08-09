from django.contrib import admin
from .models import Place, Image, Location


class PlaceAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('place', )


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Location)
