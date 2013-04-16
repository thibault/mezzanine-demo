from mezzanine.utils.views import render


def map(request):
    return render(request, 'map.html')
