from django.shortcuts import get_object_or_404
from mezzanine.utils.views import render
from city_map.models import PointOfInterest


def map(request):
    pois = PointOfInterest.objects.all()
    return render(request, 'map.html', {
            'pois': pois,
    })

def point_of_interest(request, slug):
    pois = PointOfInterest.objects.all()
    selected_poi = get_object_or_404(PointOfInterest, slug=slug)
    return render(request, 'map.html', {
            'pois': pois,
            'selected_poi': selected_poi,
    })
