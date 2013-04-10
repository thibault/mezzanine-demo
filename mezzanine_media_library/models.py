from cStringIO import StringIO
import os
from string import punctuation
from urllib import unquote
from zipfile import ZipFile

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.core.fields import FileField
from mezzanine.core.models import Orderable, RichText
from mezzanine.pages.models import Page
from mezzanine.utils.importing import import_dotted_path
from mezzanine.utils.models import upload_to


# Set the directory where files are uploaded to,
# either MEDIA_ROOT + 'galleries', or filebrowser's upload
# directory if being used.
GALLERIES_UPLOAD_DIR = "galleries"
if settings.PACKAGE_NAME_FILEBROWSER in settings.INSTALLED_APPS:
    fb_settings = "%s.settings" % settings.PACKAGE_NAME_FILEBROWSER
    try:
        GALLERIES_UPLOAD_DIR = import_dotted_path(fb_settings).DIRECTORY
    except ImportError:
        pass


class MediaLibrary(Page, RichText):
    """Page bucket for media files."""

    #zip_import = models.FileField(verbose_name=_("Zip import"), blank=True,
    #    upload_to=upload_to("galleries.Gallery.zip_import", "galleries"),
    #    help_text=_("Upload a zip file containing images, and "
    #                "they'll be imported into this gallery."))

    class Meta:
        verbose_name = _("Media Library")
        verbose_name_plural = _("Media Libraries")


class MediaFile(Orderable):
    """Single file to add in a library."""

    library = models.ForeignKey("MediaLibrary", related_name="files")
    file = FileField(_("File"), max_length=200,
            upload_to=upload_to("galleries.GalleryImage.file", "galleries"))
    description = models.CharField(_("Description"), max_length=1000,
                                   blank=True)

    class Meta:
        verbose_name = _("Media File")
        verbose_name_plural = _("Media Files")

    def __unicode__(self):
        return self.description

    def save(self, *args, **kwargs):
        """
        If no description is given when created, create one from the
        file name.
        """
        if not self.id and not self.description:
            name = unquote(self.file.url).split("/")[-1].rsplit(".", 1)[0]
            name = name.replace("'", "")
            name = "".join([c if c not in punctuation else " " for c in name])
            # str.title() doesn't deal with unicode very well.
            # http://bugs.python.org/issue6412
            name = "".join([s.upper() if i == 0 or name[i - 1] == " " else s
                            for i, s in enumerate(name)])
            self.description = name
        super(MediaFile, self).save(*args, **kwargs)
