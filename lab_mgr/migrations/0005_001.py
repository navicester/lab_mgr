# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Product_Subclass_Item_r'
        db.delete_table('lab_product_subclass_item_r')

        # Deleting model 'Product_Class_Subclass_r'
        db.delete_table('lab_product_class_subclass_r')

        # Deleting model 'Product_SubClass'
        db.delete_table('lab_product_subclass')

        # Deleting field 'lab_device_item.Last_Modify_Time'
        db.delete_column('lab_device_item', 'Last_Modify_Time')

        # Deleting field 'lab_device_item.GRV_By'
        db.delete_column('lab_device_item', 'GRV_By')

        # Adding field 'lab_device_item.InFA'
        db.add_column('lab_device_item', 'InFA',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'lab_device_item.User'
        db.add_column('lab_device_item', 'User',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'lab_device_item.PR'
        db.add_column('lab_device_item', 'PR',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'lab_device_item.PR_Launcher'
        db.add_column('lab_device_item', 'PR_Launcher',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'lab_device_item.Asset_By'
        db.add_column('lab_device_item', 'Asset_By',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'lab_device_item.Asset_Number'
        db.add_column('lab_device_item', 'Asset_Number',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Product.Product_SubClass'
        db.delete_column('lab_product', 'Product_SubClass_id')

        # Deleting field 'Product.User'
        db.delete_column('lab_product', 'User')

        # Deleting field 'Product.Password'
        db.delete_column('lab_product', 'Password')

        # Deleting field 'lab_ip.Name'
        db.delete_column('lab_ip', 'Name')

        # Adding field 'lab_ip.hw'
        db.add_column('lab_ip', 'hw',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'lab_ip.ConnLocation'
        db.add_column('lab_ip', 'ConnLocation',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Product_Subclass_Item_r'
        db.create_table('lab_product_subclass_item_r', (
            ('Product_Item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Product_Item'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Product_SubClass', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Product_SubClass'])),
        ))
        db.send_create_signal(u'lab_mgr', ['Product_Subclass_Item_r'])

        # Adding model 'Product_Class_Subclass_r'
        db.create_table('lab_product_class_subclass_r', (
            ('Product_Class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Product_Class'])),
            ('Product_SubClass', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Product_SubClass'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'lab_mgr', ['Product_Class_Subclass_r'])

        # Adding model 'Product_SubClass'
        db.create_table('lab_product_subclass', (
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'lab_mgr', ['Product_SubClass'])

        # Adding field 'lab_device_item.Last_Modify_Time'
        db.add_column('lab_device_item', 'Last_Modify_Time',
                      self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'lab_device_item.GRV_By'
        db.add_column('lab_device_item', 'GRV_By',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'lab_device_item.InFA'
        db.delete_column('lab_device_item', 'InFA')

        # Deleting field 'lab_device_item.User'
        db.delete_column('lab_device_item', 'User')

        # Deleting field 'lab_device_item.PR'
        db.delete_column('lab_device_item', 'PR')

        # Deleting field 'lab_device_item.PR_Launcher'
        db.delete_column('lab_device_item', 'PR_Launcher')

        # Deleting field 'lab_device_item.Asset_By'
        db.delete_column('lab_device_item', 'Asset_By')

        # Deleting field 'lab_device_item.Asset_Number'
        db.delete_column('lab_device_item', 'Asset_Number')


        # User chose to not deal with backwards NULL issues for 'Product.Product_SubClass'
        raise RuntimeError("Cannot reverse this migration. 'Product.Product_SubClass' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Product.Product_SubClass'
        db.add_column('lab_product', 'Product_SubClass',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Product_SubClass']),
                      keep_default=False)

        # Adding field 'Product.User'
        db.add_column('lab_product', 'User',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.Password'
        db.add_column('lab_product', 'Password',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'lab_ip.Name'
        db.add_column('lab_ip', 'Name',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'lab_ip.hw'
        db.delete_column('lab_ip', 'hw')

        # Deleting field 'lab_ip.ConnLocation'
        db.delete_column('lab_ip', 'ConnLocation')


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
            'val1': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'val2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'val3': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'val4': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'val5': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'val6': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'lab_mgr.lab_device_item': {
            'Asset_By': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Asset_Number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Comments': ('django.db.models.fields.TextField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Create_Time': ('django.db.models.fields.DateField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Device_Item_Status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Device_Item_Status']"}),
            'Device_Item_Type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Device_Item_Type']", 'null': 'True', 'blank': 'True'}),
            'FA_Applicant': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'FA_Product_Line': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.FA_Product_Line']", 'null': 'True', 'blank': 'True'}),
            'Good_Received_Date': ('django.db.models.fields.DateField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'InFA': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Location']"}),
            'Meta': {'object_name': 'lab_device_item', 'db_table': "'lab_device_item'"},
            'PC': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.PC']", 'null': 'True', 'blank': 'True'}),
            'PO': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'PR': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'PR_Launcher': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Platform': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Platform']", 'null': 'True', 'blank': 'True'}),
            'Product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product']", 'null': 'True', 'blank': 'True'}),
            'Product_Class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product_Class']"}),
            'Product_Item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product_Item']"}),
            'SN': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'UE': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.UE']", 'null': 'True', 'blank': 'True'}),
            'User': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reserve1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'lab_mgr.lab_ip': {
            'ConnLocation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'IP_Type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.IP_Type']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'lab_ip', 'db_table': "'lab_ip'"},
            'PC': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.PC']", 'null': 'True', 'blank': 'True'}),
            'Platform': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Platform']", 'null': 'True', 'blank': 'True'}),
            'Product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product']", 'null': 'True', 'blank': 'True'}),
            'UE': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.UE']", 'null': 'True', 'blank': 'True'}),
            'gw': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'hw': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'netmask': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'serial_port': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'server_ip': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'sftp_port': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ssh_port': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tftp_port': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'lab_mgr.lab_platform_hws': {
            'Meta': {'object_name': 'lab_platform_hws', 'db_table': "'lab_platform_hws'"},
            'Vendor_unit_family_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Vendor_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Vendor_unit_type_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ritName': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ritType': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'version_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
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
            'Product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product']", 'null': 'True', 'blank': 'True'}),
            'Product_Class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product_Class']"}),
            'Project': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Used_By': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lab_mgr.product_class': {
            'Meta': {'object_name': 'Product_Class', 'db_table': "'lab_product_class'"},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lab_mgr.product_class_item_r': {
            'Meta': {'object_name': 'Product_Class_Item_r', 'db_table': "'lab_product_class_item_r'"},
            'Product_Class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product_Class']"}),
            'Product_Item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product_Item']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lab_mgr.product_item': {
            'Meta': {'object_name': 'Product_Item', 'db_table': "'lab_product_item'"},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lab_mgr.product_item_type_r': {
            'Device_Item_Type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Device_Item_Type']"}),
            'Meta': {'object_name': 'Product_Item_Type_r', 'db_table': "'lab_product_item_type_r'"},
            'Product_Item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product_Item']"}),
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