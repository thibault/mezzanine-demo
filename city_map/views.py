from mezzanine.utils.views import render
from city_map.models import PointOfInterest


def map(request):
    pois = PointOfInterest.objects.all()
    return render(request, 'map.html', {
            'pois': pois,
    })
