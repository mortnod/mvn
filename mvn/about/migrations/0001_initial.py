# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'About'
        db.create_table('about_about', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('portrait', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('about', ['About'])


    def backwards(self, orm):
        # Deleting model 'About'
        db.delete_table('about_about')


    models = {
        'about.about': {
            'Meta': {'object_name': 'About'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portrait': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['about']