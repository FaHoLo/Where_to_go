from django.shortcuts import render
from django.urls import reverse

from places.models import Place


def show_index(request):
    places_geojson = {
        'type': 'FeatureCollection',
        'features': []
    }
    all_places = Place.objects.all()

    for place in all_places:
        details_url = reverse('place_info', args=[place.id])
        places_geojson['features'].append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.short_title,
                'placeId': place.place_id,
                'detailsUrl': details_url,
            }
        })
    data = {'places_geojson': places_geojson}
    return render(request, 'index.html', context=data)
