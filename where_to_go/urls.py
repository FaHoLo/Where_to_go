from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from where_to_go import views
from places import views as pl_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_index),
    path('places/<int:place_id>/', pl_views.show_place_info, name='place_info'),
    path('tinymce/', include('tinymce.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
