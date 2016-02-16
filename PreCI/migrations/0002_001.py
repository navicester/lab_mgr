# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PreCI_Request'
        db.create_table('PreCI_Request', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'PreCI', ['PreCI_Request'])


    def backwards(self, orm):
        # Deleting model 'PreCI_Request'
        db.delete_table('PreCI_Request')


    models = {
        u'PreCI.preci_request': {
            'Meta': {'object_name': 'PreCI_Request', 'db_table': "'PreCI_Request'"},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['PreCI']