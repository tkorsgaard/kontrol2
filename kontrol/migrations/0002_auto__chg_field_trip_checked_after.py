# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Trip.checked_after'
        db.alter_column('kontrol_trip', 'checked_after_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kontrol.Station'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Trip.checked_after'
        raise RuntimeError("Cannot reverse this migration. 'Trip.checked_after' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Trip.checked_after'
        db.alter_column('kontrol_trip', 'checked_after_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kontrol.Station']))

    models = {
        'kontrol.departure': {
            'Meta': {'object_name': 'Departure'},
            'departure_station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kontrol.Station']"}),
            'departure_time': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'kontrol.station': {
            'Meta': {'object_name': 'Station'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'station_name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'kontrol.trip': {
            'Meta': {'object_name': 'Trip'},
            'bike': ('django.db.models.fields.BooleanField', [], {}),
            'checked_after': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kontrol.Station']", 'blank': 'True', 'null': 'True'}),
            'departure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kontrol.Departure']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tickets_checked': ('django.db.models.fields.BooleanField', [], {}),
            'trip_date': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['kontrol']