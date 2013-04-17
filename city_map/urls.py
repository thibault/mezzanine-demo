from django.conf.urls import patterns, include, url


urlpatterns = patterns("city_map.views",
    url('^$', 'map', name='map'),
    url('^(?P<id>\d+)/$', 'point_of_interest', name='point_of_interest'),
)

