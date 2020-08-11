from django.shortcuts import render
from django.urls import reverse

from places.models import Location


def show_index(request):
    places_geojson = {
      "type": "FeatureCollection",
      "features": []
    }
    all_locations = Location.objects.prefetch_related('place_info')
    for location in all_locations:
        details_url = reverse('place_info', args=[location.place_info.id])
        places_geojson['features'].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [location.lng, location.lat]
            },
            "properties": {
                "title": location.title,
                "placeId": location.place_id,
                "detailsUrl": details_url,
            }
        })
    data = {'places_geojson': places_geojson}
    return render(request, 'index.html', context=data)
