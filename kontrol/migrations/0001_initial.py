# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Station'
        db.create_table('kontrol_station', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('kontrol', ['Station'])

        # Adding model 'Departure'
        db.create_table('kontrol_departure', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('departure_station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kontrol.Station'])),
            ('departure_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('kontrol', ['Departure'])

        # Adding model 'Trip'
        db.create_table('kontrol_trip', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trip_date', self.gf('django.db.models.fields.DateField')()),
            ('departure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kontrol.Departure'])),
            ('tickets_checked', self.gf('django.db.models.fields.BooleanField')()),
            ('checked_after', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kontrol.Station'])),
            ('bike', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('kontrol', ['Trip'])


    def backwards(self, orm):
        # Deleting model 'Station'
        db.delete_table('kontrol_station')

        # Deleting model 'Departure'
        db.delete_table('kontrol_departure')

        # Deleting model 'Trip'
        db.delete_table('kontrol_trip')


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
            'checked_after': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kontrol.Station']"}),
            'departure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kontrol.Departure']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tickets_checked': ('django.db.models.fields.BooleanField', [], {}),
            'trip_date': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['kontrol']