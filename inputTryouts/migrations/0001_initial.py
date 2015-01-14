# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DateTryout'
        db.create_table('inputTryouts_datetryout', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('when', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('inputTryouts', ['DateTryout'])

        # Adding model 'Person'
        db.create_table('inputTryouts_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('has_work', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('inputTryouts', ['Person'])


    def backwards(self, orm):
        # Deleting model 'DateTryout'
        db.delete_table('inputTryouts_datetryout')

        # Deleting model 'Person'
        db.delete_table('inputTryouts_person')


    models = {
        'inputTryouts.datetryout': {
            'Meta': {'object_name': 'DateTryout'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'when': ('django.db.models.fields.DateTimeField', [], {})
        },
        'inputTryouts.person': {
            'Meta': {'object_name': 'Person'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'has_work': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['inputTryouts']