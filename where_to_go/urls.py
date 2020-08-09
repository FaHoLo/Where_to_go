from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from where_to_go import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
