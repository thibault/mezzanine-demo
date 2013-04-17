from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.utils import simplejson
from mezzanine.utils.views import render
from city_map.models import PointOfInterest


def map(request):
    return render(request, 'map.html')

def point_of_interest(request, slug):
    selected_poi = get_object_or_404(PointOfInterest, slug=slug)
    return render(request, 'map.html', {
            'selected_poi': selected_poi,
    })

def markers_data(request):
    pois = PointOfInterest.objects.all().values()
    data = simplejson.dumps(list(pois))
    return HttpResponse(data, mimetype='application/json')
