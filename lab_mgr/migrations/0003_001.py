# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product_Class_Item_r'
        db.create_table('lab_product_class_item_r', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Product_Class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Product_Class'])),
            ('Product_Item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_mgr.Product_Item'])),
        ))
        db.send_create_signal(u'lab_mgr', ['Product_Class_Item_r'])


    def backwards(self, orm):
        # Deleting model 'Product_Class_Item_r'
        db.delete_table('lab_product_class_item_r')


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
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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
        u'lab_mgr.product_class_item_r': {
            'Meta': {'object_name': 'Product_Class_Item_r', 'db_table': "'lab_product_class_item_r'"},
            'Product_Class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product_Class']"}),
            'Product_Item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product_Item']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lab_mgr.product_class_subclass_r': {
            'Meta': {'object_name': 'Product_Class_Subclass_r', 'db_table': "'lab_product_class_subclass_r'"},
            'Product_Class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product_Class']"}),
            'Product_SubClass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product_SubClass']"}),
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
        u'lab_mgr.product_subclass': {
            'Meta': {'object_name': 'Product_SubClass', 'db_table': "'lab_product_subclass'"},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lab_mgr.product_subclass_item_r': {
            'Meta': {'object_name': 'Product_Subclass_Item_r', 'db_table': "'lab_product_subclass_item_r'"},
            'Product_Item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product_Item']"}),
            'Product_SubClass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lab_mgr.Product_SubClass']"}),
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