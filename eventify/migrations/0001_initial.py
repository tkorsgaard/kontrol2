# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table('eventify_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('event_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('eventify', ['Event'])

        # Adding model 'Wish'
        db.create_table('eventify_wish', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wish_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('wish_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('wish_price_low', self.gf('django.db.models.fields.IntegerField')()),
            ('wish_price_high', self.gf('django.db.models.fields.IntegerField')()),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventify.Event'])),
        ))
        db.send_create_signal('eventify', ['Wish'])

        # Adding model 'Guest'
        db.create_table('eventify_guest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('guset_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('guest_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('wish', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventify.Wish'])),
        ))
        db.send_create_signal('eventify', ['Guest'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table('eventify_event')

        # Deleting model 'Wish'
        db.delete_table('eventify_wish')

        # Deleting model 'Guest'
        db.delete_table('eventify_guest')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'eventify.event': {
            'Meta': {'object_name': 'Event'},
            'event_date': ('django.db.models.fields.DateTimeField', [], {}),
            'event_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'eventify.guest': {
            'Meta': {'object_name': 'Guest'},
            'guest_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'guset_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'wish': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eventify.Wish']"})
        },
        'eventify.wish': {
            'Meta': {'object_name': 'Wish'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eventify.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'wish_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'wish_price_high': ('django.db.models.fields.IntegerField', [], {}),
            'wish_price_low': ('django.db.models.fields.IntegerField', [], {}),
            'wish_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['eventify']