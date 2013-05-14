# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'PointOfInterest.description'
        db.alter_column(u'city_map_pointofinterest', 'description', self.gf('mezzanine.core.fields.RichTextField')(null=True))

    def backwards(self, orm):

        # Changing field 'PointOfInterest.description'
        db.alter_column(u'city_map_pointofinterest', 'description', self.gf('django.db.models.fields.TextField')(null=True))

    models = {
        u'city_map.pointofinterest': {
            'Meta': {'object_name': 'PointOfInterest'},
            'description': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['city_map']