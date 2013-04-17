from django.conf.urls import patterns, include, url


urlpatterns = patterns("city_map.views",
    url('^$', 'map', name='map'),
    url('^markers.json$', 'markers_data', name='markers_data'),
    url('^(?P<slug>[\w-]+)/$', 'point_of_interest', name='point_of_interest'),
)

