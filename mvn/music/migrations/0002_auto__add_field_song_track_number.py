# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Song.track_number'
        db.add_column('music_song', 'track_number',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=-1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Song.track_number'
        db.delete_column('music_song', 'track_number')


    models = {
        'music.coverphoto': {
            'Meta': {'object_name': 'CoverPhoto'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.MusicAlbum']"}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'music.musicalbum': {
            'Meta': {'object_name': 'MusicAlbum'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'100'"})
        },
        'music.song': {
            'Meta': {'object_name': 'Song'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.MusicAlbum']"}),
            'artist': ('django.db.models.fields.CharField', [], {'max_length': "'100'", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm4a': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'ogg': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'track_number': ('django.db.models.fields.SmallIntegerField', [], {})
        }
    }

    complete_apps = ['music']