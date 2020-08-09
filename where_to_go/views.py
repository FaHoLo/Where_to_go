from django.shortcuts import render
from places.models import Location


def show_index(request):
    places_geojson = {
      "type": "FeatureCollection",
      "features": []
    }
    all_locations = Location.objects.all()
    for location in all_locations:
        places_geojson['features'].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [location.lng, location.lat]
            },
            "properties": {
                "title": location.title,
                "placeId": location.place_id,
                "detailsUrl": "static/places/moscow_legends.json",
            }
        })
    data = {'places_geojson': places_geojson}
    return render(request, 'index.html', context=data)
