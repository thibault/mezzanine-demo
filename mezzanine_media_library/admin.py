from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from mezzanine_media_library.models import MediaLibrary, MediaFile


class MediaFileInline(TabularDynamicInlineAdmin):
    model = MediaFile


class MediaLibraryAdmin(PageAdmin):

    class Media:
        css = {"all": ("mezzanine/css/admin/gallery.css",)}

    inlines = (MediaFileInline,)


admin.site.register(MediaLibrary, MediaLibraryAdmin)
