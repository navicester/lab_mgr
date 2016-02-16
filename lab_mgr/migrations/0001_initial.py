# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product_Class'
        db.create_table('lab_product_class', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'lab_mgr', ['Product_Class'])

        # Adding model 'Product_SubClass'
        db.create_table('lab_product_subclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'lab_mgr', ['Product_SubClass'])

        # Adding model 'Product_Item'
        db.create_table('lab_product_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'lab_mgr', ['Product_Item'])

        # Adding model 'Device_Item_Status'
        db.create_table('lab_device_item_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'lab_mgr', ['Device_Item_Status'])

        # Adding model 'Device_Item_Type'
        db.create_table('lab_device_item_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('Description', self.gf('django.db.models.fields.TextField')(max_length=500)),
        ))
        db.send_create_signal(u'lab_mgr', ['Device_Item_Type'])

        # Adding model 'Product_Type'
        db.create_table('lab_product_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'lab_mgr', ['Product_Type'])

        # Adding model 'IP_Type'
        db.create_table('lab_ip_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'lab_mgr', ['IP_Type'])

        # Adding model 'Configuration_Type'
        db.create_table('lab_configuration_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'lab_mgr', ['Configuration_Type'])

        # Adding model 'FA_Product_Line'
        db.create_table('lab_fa_product_line', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'lab_mgr', ['FA_Product_Line'])

        # Adding model 'Location'
        db.create_table('lab_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'lab_mgr', ['Location'])

        # Adding model 'Product'
        db.create_table('lab_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Product_Class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Product_Class'])),
            ('Product_SubClass', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Product_SubClass'])),
            ('Name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('Used_By', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('Description', self.gf('django.db.models.fields.TextField')(max_length=500, null=True, blank=True)),
            ('Owner', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Project', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('Domain', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('User', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('Password', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('Comments', self.gf('django.db.models.fields.TextField')(max_length=50)),
            ('Location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Location'], null=True, blank=True)),
            ('Product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Product'], null=True, blank=True)),
        ))
        db.send_create_signal(u'lab_mgr', ['Product'])

        # Adding model 'PC'
        db.create_table('lab_pc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('Used_By', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('Description', self.gf('django.db.models.fields.TextField')(max_length=500, null=True, blank=True)),
            ('Owner', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('User', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Password', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Comments', self.gf('django.db.models.fields.TextField')(max_length=50)),
            ('Location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Location'], null=True, blank=True)),
        ))
        db.send_create_signal(u'lab_mgr', ['PC'])

        # Adding model 'Platform'
        db.create_table('lab_platform', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('Used_By', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('Description', self.gf('django.db.models.fields.TextField')(max_length=500, null=True, blank=True)),
            ('Owner', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Project', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('Domain', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('Comments', self.gf('django.db.models.fields.TextField')(max_length=50)),
            ('Location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Location'], null=True, blank=True)),
        ))
        db.send_create_signal(u'lab_mgr', ['Platform'])

        # Adding model 'UE'
        db.create_table('lab_ue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('Used_By', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('Description', self.gf('django.db.models.fields.TextField')(max_length=500, null=True, blank=True)),
            ('Owner', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Comments', self.gf('django.db.models.fields.TextField')(max_length=50)),
            ('PC', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.PC'], null=True, blank=True)),
        ))
        db.send_create_signal(u'lab_mgr', ['UE'])

        # Adding model 'lab_device_item'
        db.create_table('lab_device_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Product_Class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Product_Class'])),
            ('Product_SubClass', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Product_SubClass'])),
            ('Product_Item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Product_Item'])),
            ('SN', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('Device_Item_Type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Device_Item_Type'], null=True, blank=True)),
            ('FA_Applicant', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('FA_Product_Line', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.FA_Product_Line'], null=True, blank=True)),
            ('PO', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('GRV_By', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('Good_Received_Date', self.gf('django.db.models.fields.DateTimeField')(max_length=50, null=True, blank=True)),
            ('Location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Location'])),
            ('Device_Item_Status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Device_Item_Status'])),
            ('Comments', self.gf('django.db.models.fields.TextField')(max_length=50, null=True, blank=True)),
            ('Create_Time', self.gf('django.db.models.fields.DateTimeField')(max_length=50, null=True, blank=True)),
            ('Last_Modify_Time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, max_length=50, null=True, auto_now_add=True, blank=True)),
            ('reserve1', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('PC', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.PC'], null=True, blank=True)),
            ('UE', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.UE'], null=True, blank=True)),
            ('Platform', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Platform'], null=True, blank=True)),
            ('Product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Product'], null=True, blank=True)),
        ))
        db.send_create_signal(u'lab_mgr', ['lab_device_item'])

        # Adding model 'lab_ip'
        db.create_table('lab_ip', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('IP_Type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.IP_Type'], null=True, blank=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('netmask', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('gw', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('server_ip', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('serial_port', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('ssh_port', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('sftp_port', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('tftp_port', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('PC', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.PC'], null=True, blank=True)),
            ('UE', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.UE'], null=True, blank=True)),
            ('Platform', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Platform'], null=True, blank=True)),
            ('Product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Product'], null=True, blank=True)),
        ))
        db.send_create_signal(u'lab_mgr', ['lab_ip'])

        # Adding model 'lab_configuration'
        db.create_table('lab_configuration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Configuration_Type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Configuration_Type'], null=True, blank=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('val1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('val2', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('val3', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('val4', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('val5', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('val6', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('PC', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.PC'], null=True, blank=True)),
            ('UE', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.UE'], null=True, blank=True)),
            ('Platform', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Platform'], null=True, blank=True)),
            ('Product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Product'], null=True, blank=True)),
        ))
        db.send_create_signal(u'lab_mgr', ['lab_configuration'])


    def backwards(self, orm):
        # Deleting model 'Product_Class'
        db.delete_table('lab_product_class')

        # Deleting model 'Product_SubClass'
        db.delete_table('lab_product_subclass')

        # Deleting model 'Product_Item'
        db.delete_table('lab_product_item')

        # Deleting model 'Device_Item_Status'
        db.delete_table('lab_device_item_status')

        # Deleting model 'Device_Item_Type'
        db.delete_table('lab_device_item_type')

        # Deleting model 'Product_Type'
        db.delete_table('lab_product_type')

        # Deleting model 'IP_Type'
        db.delete_table('lab_ip_type')

        # Deleting model 'Configuration_Type'
        db.delete_table('lab_configuration_type')

        # Deleting model 'FA_Product_Line'
        db.delete_table('lab_fa_product_line')

        # Deleting model 'Location'
        db.delete_table('lab_location')

        # Deleting model 'Product'
        db.delete_table('lab_product')

        # Deleting model 'PC'
        db.delete_table('lab_pc')

        # Deleting model 'Platform'
        db.delete_table('lab_platform')

        # Deleting model 'UE'
        db.delete_table('lab_ue')

        # Deleting model 'lab_device_item'
        db.delete_table('lab_device_item')

        # Deleting model 'lab_ip'
        db.delete_table('lab_ip')

        # Deleting model 'lab_configuration'
        db.delete_table('lab_configuration')


    models = {
        u'lab_mgr.configuration_type': {
            'Meta': {'object_name': 'Configuration_Type', 'db_table': "'lab_configuration_type'"},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lab_mgr.device_item_status': {
            'Meta': {'object_name': 'Device_Item_Status', 'db_table': "'lab_device_item_status'"},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lab_mgr.device_item_type': {
            'Code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'Description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'Meta': {'object_name': 'Device_Item_Type', 'db_table': "'lab_device_item_type'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lab_mgr.fa_product_line': {
            'Meta': {'object_name': 'FA_Product_Line', 'db_table': "'lab_fa_product_line'"},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lab_mgr.ip_type': {
            'Meta': {'object_name': 'IP_Type', 'db_table': "'lab_ip_type'"},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lab_mgr.lab_configuration': {
            'Configuration_Type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Configuration_Type']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'lab_configuration', 'db_table': "'lab_configuration'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'PC': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.PC']", 'null': 'True', 'blank': 'True'}),
            'Platform': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Platform']", 'null': 'True', 'blank': 'True'}),
            'Product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product']", 'null': 'True', 'blank': 'True'}),
            'UE': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.UE']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'val1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'val2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'val3': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'val4': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'val5': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'val6': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'lab_mgr.lab_device_item': {
            'Comments': ('django.db.models.fields.TextField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Create_Time': ('django.db.models.fields.DateTimeField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Device_Item_Status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Device_Item_Status']"}),
            'Device_Item_Type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Device_Item_Type']", 'null': 'True', 'blank': 'True'}),
            'FA_Applicant': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'FA_Product_Line': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.FA_Product_Line']", 'null': 'True', 'blank': 'True'}),
            'GRV_By': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Good_Received_Date': ('django.db.models.fields.DateTimeField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Last_Modify_Time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'max_length': '50', 'null': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'Location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Location']"}),
            'Meta': {'object_name': 'lab_device_item', 'db_table': "'lab_device_item'"},
            'PC': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.PC']", 'null': 'True', 'blank': 'True'}),
            'PO': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Platform': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Platform']", 'null': 'True', 'blank': 'True'}),
            'Product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product']", 'null': 'True', 'blank': 'True'}),
            'Product_Class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product_Class']"}),
            'Product_Item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product_Item']"}),
            'Product_SubClass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product_SubClass']"}),
            'SN': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'UE': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.UE']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reserve1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'lab_mgr.lab_ip': {
            'IP_Type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.IP_Type']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'lab_ip', 'db_table': "'lab_ip'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'PC': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.PC']", 'null': 'True', 'blank': 'True'}),
            'Platform': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Platform']", 'null': 'True', 'blank': 'True'}),
            'Product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product']", 'null': 'True', 'blank': 'True'}),
            'UE': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.UE']", 'null': 'True', 'blank': 'True'}),
            'gw': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'netmask': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'serial_port': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'server_ip': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'sftp_port': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ssh_port': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tftp_port': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'lab_mgr.location': {
            'Meta': {'object_name': 'Location', 'db_table': "'lab_location'"},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lab_mgr.pc': {
            'Comments': ('django.db.models.fields.TextField', [], {'max_length': '50'}),
            'Description': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'Location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Location']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'PC', 'db_table': "'lab_pc'"},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'Owner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Password': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Used_By': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'User': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lab_mgr.platform': {
            'Comments': ('django.db.models.fields.TextField', [], {'max_length': '50'}),
            'Description': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'Domain': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Location']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Platform', 'db_table': "'lab_platform'"},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'Owner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Project': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Used_By': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lab_mgr.product': {
            'Comments': ('django.db.models.fields.TextField', [], {'max_length': '50'}),
            'Description': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'Domain': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Location']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Product', 'db_table': "'lab_product'"},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'Owner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Password': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product']", 'null': 'True', 'blank': 'True'}),
            'Product_Class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product_Class']"}),
            'Product_SubClass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product_SubClass']"}),
            'Project': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Used_By': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'User': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lab_mgr.product_class': {
            'Meta': {'object_name': 'Product_Class', 'db_table': "'lab_product_class'"},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lab_mgr.product_item': {
            'Meta': {'object_name': 'Product_Item', 'db_table': "'lab_product_item'"},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lab_mgr.product_subclass': {
            'Meta': {'object_name': 'Product_SubClass', 'db_table': "'lab_product_subclass'"},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lab_mgr.product_type': {
            'Meta': {'object_name': 'Product_Type', 'db_table': "'lab_product_type'"},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lab_mgr.ue': {
            'Comments': ('django.db.models.fields.TextField', [], {'max_length': '50'}),
            'Description': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'UE', 'db_table': "'lab_ue'"},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'Owner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'PC': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.PC']", 'null': 'True', 'blank': 'True'}),
            'Used_By': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['lab_mgr']