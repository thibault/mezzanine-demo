from django.contrib import admin
from city_map.models import PointOfInterest


class PointOfInterestAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(PointOfInterest, PointOfInterestAdmin)
