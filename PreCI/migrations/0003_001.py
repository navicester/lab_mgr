# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PreCI_Request.Name'
        db.delete_column('PreCI_Request', 'Name')

        # Adding field 'PreCI_Request.Request_By'
        db.add_column('PreCI_Request', 'Request_By',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 5, 13, 0, 0), max_length=50),
                      keep_default=False)

        # Adding field 'PreCI_Request.HW_Type'
        db.add_column('PreCI_Request', 'HW_Type',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 5, 13, 0, 0), max_length=50),
                      keep_default=False)

        # Adding field 'PreCI_Request.FeatureId'
        db.add_column('PreCI_Request', 'FeatureId',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 5, 13, 0, 0), max_length=50),
                      keep_default=False)

        # Adding field 'PreCI_Request.Manager'
        db.add_column('PreCI_Request', 'Manager',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 5, 13, 0, 0), max_length=50),
                      keep_default=False)

        # Adding field 'PreCI_Request.LoadName'
        db.add_column('PreCI_Request', 'LoadName',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 5, 13, 0, 0), max_length=50),
                      keep_default=False)

        # Adding field 'PreCI_Request.LoadLink'
        db.add_column('PreCI_Request', 'LoadLink',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 5, 13, 0, 0), max_length=500),
                      keep_default=False)

        # Adding field 'PreCI_Request.Note'
        db.add_column('PreCI_Request', 'Note',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 5, 13, 0, 0), max_length=50),
                      keep_default=False)

        # Adding field 'PreCI_Request.ExpectDate'
        db.add_column('PreCI_Request', 'ExpectDate',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 5, 13, 0, 0), unique=True, max_length=50),
                      keep_default=False)

        # Adding field 'PreCI_Request.SubmissionDate'
        db.add_column('PreCI_Request', 'SubmissionDate',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 5, 13, 0, 0), max_length=50),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'PreCI_Request.Name'
        raise RuntimeError("Cannot reverse this migration. 'PreCI_Request.Name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'PreCI_Request.Name'
        db.add_column('PreCI_Request', 'Name',
                      self.gf('django.db.models.fields.CharField')(max_length=50, unique=True),
                      keep_default=False)

        # Deleting field 'PreCI_Request.Request_By'
        db.delete_column('PreCI_Request', 'Request_By')

        # Deleting field 'PreCI_Request.HW_Type'
        db.delete_column('PreCI_Request', 'HW_Type')

        # Deleting field 'PreCI_Request.FeatureId'
        db.delete_column('PreCI_Request', 'FeatureId')

        # Deleting field 'PreCI_Request.Manager'
        db.delete_column('PreCI_Request', 'Manager')

        # Deleting field 'PreCI_Request.LoadName'
        db.delete_column('PreCI_Request', 'LoadName')

        # Deleting field 'PreCI_Request.LoadLink'
        db.delete_column('PreCI_Request', 'LoadLink')

        # Deleting field 'PreCI_Request.Note'
        db.delete_column('PreCI_Request', 'Note')

        # Deleting field 'PreCI_Request.ExpectDate'
        db.delete_column('PreCI_Request', 'ExpectDate')

        # Deleting field 'PreCI_Request.SubmissionDate'
        db.delete_column('PreCI_Request', 'SubmissionDate')


    models = {
        u'PreCI.preci_request': {
            'ExpectDate': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'FeatureId': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'HW_Type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'LoadLink': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'LoadName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Manager': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'object_name': 'PreCI_Request', 'db_table': "'PreCI_Request'"},
            'Note': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Request_By': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'SubmissionDate': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['PreCI']