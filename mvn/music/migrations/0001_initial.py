# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MusicAlbum'
        db.create_table('music_musicalbum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='100')),
        ))
        db.send_create_signal('music', ['MusicAlbum'])

        # Adding model 'Song'
        db.create_table('music_song', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.MusicAlbum'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length='100')),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length='100', null=True, blank=True)),
            ('m4a', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('ogg', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('music', ['Song'])

        # Adding model 'CoverPhoto'
        db.create_table('music_coverphoto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.MusicAlbum'])),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal('music', ['CoverPhoto'])


    def backwards(self, orm):
        # Deleting model 'MusicAlbum'
        db.delete_table('music_musicalbum')

        # Deleting model 'Song'
        db.delete_table('music_song')

        # Deleting model 'CoverPhoto'
        db.delete_table('music_coverphoto')


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
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'100'"})
        }
    }

    complete_apps = ['music']