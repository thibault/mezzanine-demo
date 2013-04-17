from django.conf.urls import patterns, include, url


urlpatterns = patterns("city_map.views",
    url('^$', 'map', name='map'),
)

