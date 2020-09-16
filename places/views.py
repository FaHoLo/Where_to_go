from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Place


def show_place_info(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    images = place.images.all()
    imgs = [image.image.url for image in images]
    place_info = {
        'title': place.title,
        'imgs': imgs,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat,
        }
    }
    return JsonResponse(place_info, safe=False, json_dumps_params={'indent': 4,
                                                                   'ensure_ascii': False})
