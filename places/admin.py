from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ('get_preview',)
    fields = ('image', 'get_preview', 'image_number')
    extra = 0

    def get_preview(self, obj):
        return format_html('<img src="{url}" style="max-height:{max_height}" />',
                           url=obj.image.url, max_height='200px')
    get_preview.short_description = "Предпросмотр фото"


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    inlines = (ImageInline, )
