from django.contrib.admin.options import *
from django.contrib import admin

from lab_mgr.models import *
from lab_mgr import models
from lab_mgr.link_form_admin import LinkFormAdmin
from lab_mgr.my_model_admin import MyModelAdmin

from lab_mgr.link_form_forms import *

import csv,sys,os


class LabDeviceItemLinkFormAdmin(LinkFormAdmin):

    extra = 1
    
    link_form = LabDeviceItemForm
    link_obj_class = lab_device_item
    link_m2m = False
    link_init_search = True

class LabProductLinkFormAdmin(LinkFormAdmin):

    extra = 1
    
    link_form = LabProductForm
    link_obj_class = Product
    link_m2m = False
    link_init_search = True

class LabIPLinkFormAdmin(LinkFormAdmin):

    extra = 1
    
    link_form = LabIPForm
    link_obj_class = lab_ip
    link_m2m = False
    link_init_search = True

class LabConfigurationLinkFormAdmin(LinkFormAdmin):

    extra = 1
    
    link_form = LabConfigurationForm
    link_obj_class = lab_configuration
    link_m2m = False
    link_init_search = True

class LabDeviceItemAdmin(MyModelAdmin):
    list_display = ('Product_Class','Product_Item','SN','Device_Item_Type','Location','PO','Device_Item_Status','FA_Applicant','Product','reserve1',)
    search_fields = ('reserve1','SN','PO','FA_Applicant','Location__Name','Comments')
    list_filter = ('Product_Class','Product_Item','Location','Device_Item_Status','FA_Applicant','Product',)
    ordering = ('Product_Class','Product_Item','SN',)

    actions = ['CopySelected','export_all','export_select','import_all']

    save_as = True
    self_form_link = LabDeviceItemForm

    fieldsets= [
        (None,{
             'fields':
                (
                 'Product_Class',
                 'Product_Item',
                 'SN',
                 'InFA',
                 'FA_Applicant',              
                 'User',
                 'Device_Item_Type',
                 'Location',
                 'Device_Item_Status',            
                 )}),
        (None,{
             'fields':
                 (   
                 'FA_Product_Line',
                 'PR_Launcher',
                 'PR',
                 'PO',
                 'Asset_By',
                 'Asset_Number',
                 'Good_Received_Date',
                 'Create_Time',
                 'Comments',
                 'reserve1',                 
                 )}),
    ]    

    fieldsets_fk= (None,{
             'fields':
                (
#                 'PC',
#                 'UE',
#                 'Platform',
                 'Product',
                 )})

    @csrf_protect_m
    @transaction.commit_on_success
    def add_view(self, request, form_url='', extra_context=None):

        extra_context = {}

        #product_class_subclasss = Product_Class_Subclass_r.objects.all()
        #product_subclass_items = Product_Subclass_Item_r.objects.all()
        product_class_items = Product_Class_Item_r.objects.all()
        product_item_types = Product_Item_Type_r.objects.all()

        extra_context_cur = {        
            #'product_class_subclasss': product_class_subclasss,
            #'product_subclass_items': product_subclass_items,
            'product_class_items': product_class_items,
            'product_item_types': product_item_types,
        }

        extra_context.update(extra_context_cur)
        
        return super(LabDeviceItemAdmin, self).add_view(request,form_url,extra_context)

    @csrf_protect_m
    @transaction.commit_on_success
    def change_view(self, request, object_id, form_url='', extra_context=None):

        extra_context = {}

        #product_class_subclasss = Product_Class_Subclass_r.objects.all()
        #product_subclass_items = Product_Subclass_Item_r.objects.all()
        product_class_items = Product_Class_Item_r.objects.all()
        product_item_types = Product_Item_Type_r.objects.all()

        obj = self.get_object(request, unquote(object_id))        
        cur_Product_Class = obj.Product_Class
        #cur_Product_SubClass = obj.Product_SubClass
        cur_Product_Item = obj.Product_Item
        cur_Device_Item_Type = obj.Device_Item_Type
        
        extra_context_cur = {        
            #'product_class_subclasss': product_class_subclasss,
            #'product_subclass_items': product_subclass_items,
            'product_class_items': product_class_items,
            'product_item_types': product_item_types,

            #'cur_Product_SubClass': cur_Product_SubClass,    
            'cur_Product_Class': cur_Product_Class,
            'cur_Product_Item': cur_Product_Item,    
            'cur_Device_Item_Type': cur_Device_Item_Type,    
        }

        extra_context.update(extra_context_cur)

        return super(LabDeviceItemAdmin, self).change_view(request,object_id, form_url,extra_context)

    def CopySelected(self, request, queryset):
        for obj in queryset:
            obj.pk = None
            obj.SN = obj.SN + "_Copy"
            obj.save()
        self.message_user(request, "Copy finished")

    def export_device_item(self, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="device-item-export.csv"'
        writer = csv.writer(response)
        writer.writerow(['id', 'Product_Class','Product_Item', 'SN', 'Code','InFA', 'FA_Applicant', 'User','FA_Product_Line', 'PR','PR Launcher','PO', 'Asset_By','Asset_Number', 
        'Good_Received_Date', 'Location', 'Device_Item_Status', 'Comments', 'Create_Time', 'reserve1', 'Product'])
        for obj in queryset:
            row = []
            row.append(obj.pk)
            row.append(obj.Product_Class)
            row.append(obj.Product_Item)
            row.append(obj.SN)
            try:
                '''
                dit = obj.Device_Item_Type
                find = False
                for deviceType in Device_Item_Type.objects.all():
                    if deviceType == obj.Device_Item_Type:
                        m = deviceType.Code
                        row.append(m)    
                        find=True
                        break
                if False == find :
                    row.append(dit)
                '''
                row.append(obj.Device_Item_Type.Code)
            except Exception as e:
                row.append(e)
            row.append(obj.InFA)
            row.append(obj.FA_Applicant)
            row.append(obj.User)            
            row.append(obj.FA_Product_Line)
            row.append(obj.PR)
            row.append(obj.PR_Launcher)
            row.append(obj.PO)            
            row.append(obj.Asset_By)
            row.append(obj.Asset_Number)            
            row.append(obj.Good_Received_Date)
            row.append(obj.Location)
            row.append(obj.Device_Item_Status)
            row.append(obj.Comments)
            row.append(obj.Create_Time)
            row.append(obj.reserve1)
            row.append(obj.Product)            
            writer.writerow(row)    

        return response

    def export_select(self, request, queryset):
        return self.export_device_item(queryset)
                
    def export_all(self, request, queryset):
        lab_device_item_all = lab_device_item.objects.all()
        return self.export_device_item(lab_device_item_all )
        
    def import_all(self, request, queryset):
        csv_filepathname=os.path.dirname(__file__)        
        csv_filepathname = csv_filepathname + '/import/device-item.csv'
        
        dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="result.csv"'
        writer = csv.writer(response)        

        i=0
        toExportResult = False
        for row in dataReader:
            j=0
            if row[0] != 'id': # Ignore the header row, import everything else
                i = i+1
                
                if not row[0] =='':
                    an_lab_device_item = lab_device_item.objects.get(pk=row[0])
                else:
                    an_lab_device_item = None

                result = []
                result.append("line = %s" % (i))
                result.append("id = %s" % (row[0]))
                
                if an_lab_device_item == None:
                    an_lab_device_item = lab_device_item()
                    an_lab_device_item.pk = None
                bError = False

                j=j+1
                if len(row)-1<j:
                    continue   
                if row[j] == '':
                    result.append("empty Product_Class class")
                    bError = True
                else:
                    try:
                        an_Product_Class = Product_Class.objects.get(Name = row[j])
                        an_lab_device_item.Product_Class = an_Product_Class
                    except:
                        result.append("missing Product_Class class")
                        bError = True
                        
                j=j+1
                if len(row)-1<j:
                    continue   
                if row[j] == '':
                    result.append("empty Product_Item item")
                    bError = True
                else:
                    try:
                        an_Product_Item = Product_Item.objects.get(Name = row[j])
                        an_lab_device_item.Product_Item = an_Product_Item
                    except:
                        result.append("missing Product_Item item")
                        bError = True                        

                j=j+1
                if len(row)-1<j:
                    continue   
                if row[0] == '':
                    try:
                        new_lab_device_item = lab_device_item.objects.get(SN = row[j])
                        if not new_lab_device_item == None:
                            result.append("dup SN")
                            bError = True
                    except:                        
                        bError = False
                an_lab_device_item.SN = row[j]

                j=j+1
                if len(row)-1<j:
                    continue   
                if row[j] == '':
                    result.append("empty Device_Item_Type class")
                    bError = True
                else:
                    try:
                        an_Device_Item_Type = Device_Item_Type.objects.get(Code = row[j])  ##???? import should be code only
                        an_lab_device_item.Device_Item_Type = an_Device_Item_Type
                    except:
                        result.append("missing Device_Item_Type class")
                        bError = True   

                j=j+1
                if len(row)-1<j:
                    continue   
                an_lab_device_item.InFA = row[j]

                j=j+1
                if len(row)-1<j:
                    continue   
                an_lab_device_item.FA_Applicant = row[j]

                j=j+1
                if len(row)-1<j:
                    continue   
                an_lab_device_item.User = row[j]
                
                j=j+1
                if len(row)-1<j:
                    continue   
                if row[j] == '':
                    result.append("empty FA_Product_Line class")
                    bError = True
                else:
                    try:
                        an_FA_Product_Line = FA_Product_Line.objects.get(Name = row[j])
                        an_lab_device_item.FA_Product_Line = an_FA_Product_Line
                    except:
                        result.append("missing FA_Product_Line class")
                        bError = True                        

                j=j+1
                if len(row)-1<j:
                    continue   
                an_lab_device_item.PR_Launcher = row[j]      
                j=j+1
                if len(row)-1<j:
                    continue   
                an_lab_device_item.PR = row[j]          
                j=j+1
                if len(row)-1<j:
                    continue   
                an_lab_device_item.PO = row[j]
                j=j+1
                if len(row)-1<j:
                    continue   
                an_lab_device_item.Asset_By = row[j]
                j=j+1
                if len(row)-1<j:
                    continue   
                an_lab_device_item.Asset_Number = row[j]
                j=j+1
                if len(row)-1<j:
                    continue   
                an_lab_device_item.Good_Received_Date = row[j]

                j=j+1
                if len(row)-1<j:
                    continue   
                if row[j] == '':
                    result.append("empty Location class")
                    bError = True
                else:
                    try:
                        an_Location = Location.objects.get(Name = row[j])
                        an_lab_device_item.Location = an_Location
                    except:
                        result.append("missing Location class")
                        bError = True                        

                j=j+1
                if len(row)-1<j:
                    continue   
                if row[j] == '':
                    result.append("empty Device_Item_Status class")
                    bError = True
                else:
                    try:
                        an_Device_Item_Status = Device_Item_Status.objects.get(Name = row[j])
                        an_lab_device_item.Device_Item_Status = an_Device_Item_Status
                    except:
                        result.append("missing Device_Item_Status class")
                        bError = True                        

                j=j+1
                if len(row)-1<j:
                    continue   
                an_lab_device_item.Comments = row[j]
                j=j+1
                if len(row)-1<j:
                    continue   
                an_lab_device_item.Create_Time = row[j]
                j=j+1
                if len(row)-1<j:
                    continue   
                an_lab_device_item.reserve1 = row[j]

                j=j+1
                if len(row)-1<j:
                    continue   
                if row[j] == '':
                    result.append("empty Product_Class class")
                    bError = True
                else:
                    try:
                        an_Product = Product.objects.get(Name = row[j])
                        an_lab_device_item.Product = an_Product
                    except:
                        result.append("missing Product class")
                        bError = True                        

                if True == bError:
                    #writer.writerow(['line = %s' % (i),'id = %s' % (row[0]),' %s' % (result)])
                    writer.writerow(result)

                if bError == True:
                    toExportResult = True
                    continue

                an_lab_device_item.save()

        if toExportResult == True:
            return response
        else:
            self.message_user(request, "import finished")
            return super(MyModelAdmin, self).changelist_view( request, None)

class LabIPAdmin(MyModelAdmin):
    list_display = ('IP_Type','ip','server_ip','serial_port','ssh_port','sftp_port','tftp_port','Product')
    search_fields = ('ip','server_ip','serial_port','ssh_port','sftp_port','tftp_port',)
    list_filter = ('IP_Type','Product',)
    ordering = ('IP_Type','ip')

    actions = ['CopySelected','export_all','export_select','import_all']

    self_form_link = LabIPForm

    fieldsets= [
        (None,{
             'fields':
                (
                 'IP_Type',
                 'hw',
                 'ip',
                 'netmask',
                 'gw',
                 'server_ip',
                 )}),
        (None,{
             'fields':
                 (
                 'serial_port',
                 'ssh_port',            
                 'tftp_port',
                 'sftp_port',
                 )}),
    ]    

    fieldsets_fk= (None,{
             'fields':
                (
#                 'PC',
#                 'UE',
#                 'Platform',
                 'Product',
                 )})


    def CopySelected(self, request, queryset):
        for obj in queryset:
            obj.pk = None
            obj.ip = obj.ip + "_Copy"
            obj.save()
        self.message_user(request, "Copy finished")

    def export_ip(self, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="ip-export.csv"'
        writer = csv.writer(response)
        writer.writerow(['id', 'ip','IP_Type', 'hw','ConnLocation','netmask', 'gw', 'server_ip', 'serial_port', 'ssh_port', 'sftp_port', 'tftp_port', 'Product'])
        for obj in queryset:
            row = []
            row.append(obj.pk)
            row.append(obj.ip)            
            row.append(obj.IP_Type)
            row.append(obj.hw)
            row.append(obj.ConnLocation)            
            row.append(obj.netmask)
            row.append(obj.gw)
            row.append(obj.server_ip)
            row.append(obj.serial_port)
            row.append(obj.ssh_port)
            row.append(obj.sftp_port)
            row.append(obj.tftp_port)
            row.append(obj.Product)            
            writer.writerow(row)    

        return response

    def export_select(self, request, queryset):
        return self.export_ip(queryset)
                
    def export_all(self, request, queryset):
        lab_ip_all = lab_ip.objects.all()
        return self.export_ip(lab_ip_all )
        
    def import_all(self, request, queryset):
        csv_filepathname=os.path.dirname(__file__)        
        csv_filepathname = csv_filepathname + '/import/ip.csv'
        
        dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="result.csv"'
        writer = csv.writer(response)        

        i=0
        toExportResult = False
        for row in dataReader:
            if row[0] != 'id': # Ignore the header row, import everything else
                i = i+1
                
                if not row[0] =='':
                    an_lab_ip = lab_ip.objects.get(pk=row[0])
                else:
                    an_lab_ip = None

                result = []
                result.append("line = %s" % (i))
                result.append("id = %s" % (row[0]))
                
                if an_lab_ip == None:
                    an_lab_ip = lab_ip()
                    an_lab_ip.pk = None
                bError = False

                j=1
                an_lab_ip.ip = row[j]
                if row[0] == '':
                    try:
                        new_lab_ip = lab_ip.objects.get(ip = row[j])
                        if not new_lab_ip == None:
                            result.append("dup ip")
                            bError = True
                    except:                        
                        bError = False   
                
                j=j+1
                if len(row)-1<j:
                    continue                 
                if row[j] == '':
                    result.append("empty IP_Type class")
                    bError = True
                else:
                    try:
                        an_IP_Type = IP_Type.objects.get(Name = row[j])                        
                        an_lab_ip.IP_Type = an_IP_Type
                    except:
                        result.append("missing IP_Type class")
                        bError = True

                j=j+1
                if len(row)-1<j:
                    continue                              
                an_lab_ip.hw = row[j]

                j=j+1
                if len(row)-1<j:
                    continue                        
                an_lab_ip.ConnLocation = row[j]
                
                j=j+1
                if len(row)-1<j:
                    continue              
                an_lab_ip.netmask = row[j]
                
                j=j+1
                if len(row)-1<j:
                    continue   
                an_lab_ip.gw = row[j]
                
                j=j+1
                if len(row)-1<j:
                    continue   
                an_lab_ip.server_ip = row[j]
                
                j=j+1
                if len(row)-1<j:
                    continue   
                an_lab_ip.serial_port = row[j]
                
                j=j+1
                if len(row)-1<j:
                    continue   
                an_lab_ip.ssh_port = row[j]
                
                j=j+1
                if len(row)-1<j:
                    continue   
                an_lab_ip.sftp_port = row[j]
                
                j=j+1
                if len(row)-1<j:
                    continue   
                an_lab_ip.tftp_port = row[j]
                
                j=j+1
                if len(row)-1<j:
                    continue   
                if not row[j] == '':
                    try:
                        product = Product.objects.get(Name = row[j])
                        an_lab_ip.Product = product
                    except:
                        result.append("missing product")
                        bError = True

                if True == bError:
                    #writer.writerow(['line = %s' % (i),'id = %s' % (row[0]),' %s' % (result)])
                    writer.writerow(result)

                if bError == True:
                    toExportResult = True
                    continue

                an_lab_ip.save()

        if toExportResult == True:
            return response
        else:
            self.message_user(request, "import finished")
            return super(MyModelAdmin, self).changelist_view( request, None)


#from django.http import HttpResponse
#from django.utils.translation import ugettext as _

class LabConfigurationAdmin(MyModelAdmin):
    list_display = ('Configuration_Type','Name','val1','val2','val3','val4','val5','val6',)
    search_fields = ('Name','val1','val2','val3','val4','val5','val6',)
    list_filter = ('Configuration_Type','Name',)
    ordering = ('Configuration_Type','Name',)
    actions = ['CopySelected','export_all','export_select']

    self_form_link = LabConfigurationForm

    fieldsets= [
        (None,{
             'fields':
                (
                 'Name',
                 'Configuration_Type',
                 'val1',
                 'val2',
                 'val3',
                 )}),
        (None,{
             'fields':
                 (
                 'val4',
                 'val5',            
                 'val6',
                 )}),
    ]    

    fieldsets_fk= (None,{
             'fields':
                (
                 'Product',
                 )})

    def CopySelected(self, request, queryset):
        for obj in queryset:
            obj.pk = None
            obj.Name = obj.Name + "_Copy"
            obj.save()
        self.message_user(request, "Copy finished")

    def export_product(self, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        writer = csv.writer(response)

        writer.writerow(['id', 'Type','Name','val1', 'val2', 'val3', '"val4', 'val5', 'val6'])
        for obj in queryset:
            row = []
            row.append(obj.pk)
            row.append(obj.Configuration_Type)
            row.append(obj.Name)
            row.append(obj.val1)
            row.append(obj.val2)
            row.append(obj.val3)
            row.append(obj.val4)
            row.append(obj.val5)
            row.append(obj.val6)
            writer.writerow(row)    

        return response

    def export_select(self, request, queryset):
        return self.export_product(queryset)
                
    def export_all(self, request, queryset):
        lab_configuration_all = lab_configuration.objects.all()
        return self.export_product(lab_configuration_all )
    
class LabProductClassAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    search_fields = ('Name',)
    list_filter = ('Name',)
    ordering = ('Name',)

class LabProductItemAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    search_fields = ('Name',)
    list_filter = ('Name',)
    ordering = ('Name',)


class LabProductSubClassAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    search_fields = ('Name',)
    list_filter = ('Name',)
    ordering = ('Name',)

class LabDeviceItemStatusAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    search_fields = ('Name',)
    list_filter = ('Name',)
    ordering = ('Name',)

class LabDeviceItemTypeAdmin(admin.ModelAdmin):
    list_display = ('Code','Description',)
    search_fields = ('Code',)
    list_filter = ('Code',)
    ordering = ('Code',)

'''
class LabProductTypeAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    search_fields = ('Name',)
    list_filter = ('Name',)
    ordering = ('Name',)
'''

class LabIPTypeAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    search_fields = ('Name',)
    list_filter = ('Name',)
    ordering = ('Name',)

class LabConfigurationTypeAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    search_fields = ('Name',)
    list_filter = ('Name',)
    ordering = ('Name',)

class LabFAProductLineAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    search_fields = ('Name',)
    list_filter = ('Name',)
    ordering = ('Name',)

class LabLocationAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    search_fields = ('Name',)
    list_filter = ('Name',)
    ordering = ('Name',)

class LabPCAdmin(MyModelAdmin):
    list_display = ('Name','Description','Comments','Location',)
    search_fields = ('Name','Comments',)
    list_filter = ('Name','Description','Location',)
    ordering = ('Name','Location',)

    fieldsets= [
        (None,{
             'fields':
                (
                 'Name',
                 'Description',                                  
                 'Used_By',
                 )}),
        (None,{
             'fields':
                 (
                 'Owner',
                 'User',
                 'Password',
                 'Location',
                 'Comments',                 
                 )}),
    ]    

    form_links = [LabDeviceItemLinkFormAdmin, LabIPLinkFormAdmin, LabConfigurationLinkFormAdmin]    
    
class LabProductAdmin(MyModelAdmin):
    list_display = ('Name','Product_Class','Description','Owner','Location','Product',)
    search_fields = ('Name','Owner','Description',)
    list_filter = ('Product_Class','Owner','Location',)
    ordering = ('Product_Class','Name','Location',)

    actions = ['CopySelected','export_all','export_select','import_all']
    
    fieldsets= [
        (None,{
             'fields':
                (
                 'Product_Class',
                 'Name',
                 'Owner',
                 'Domain',
                 'Project',
                 'Description',
                 )}),
        (None,{
             'fields':
                 (
                 'Location',
                 'Product',
                 'Comments',                 
                 )}),
    ]    

    form_links = [LabDeviceItemLinkFormAdmin, LabIPLinkFormAdmin, LabConfigurationLinkFormAdmin, LabProductLinkFormAdmin]    

    @csrf_protect_m
    @transaction.commit_on_success
    def add_view(self, request, form_url='', extra_context=None):

        extra_context = {}

        #product_class_subclasss = Product_Class_Subclass_r.objects.all()

        extra_context_cur = {        
            #'product_class_subclasss': product_class_subclasss,
        }

        extra_context.update(extra_context_cur)
        
        return super(LabProductAdmin, self).add_view(request,form_url,extra_context)

    @csrf_protect_m
    @transaction.commit_on_success
    def change_view(self, request, object_id, form_url='', extra_context=None):

        extra_context = {}

        #product_class_subclasss = Product_Class_Subclass_r.objects.all()

        obj = self.get_object(request, unquote(object_id))        
        #cur_Product_SubClass = obj.Product_SubClass
        
        extra_context_cur = {        
            #'product_class_subclasss': product_class_subclasss,

            #'cur_Product_SubClass': cur_Product_SubClass,    
        }

        extra_context.update(extra_context_cur)

        return super(LabProductAdmin, self).change_view(request,object_id, form_url,extra_context)

    def CopySelected(self, request, queryset):
        for obj in queryset:
            obj.pk = None
            obj.Name = obj.Name + "_Copy"
            obj.save()
        self.message_user(request, "Copy finished")

    def export_product(self, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        writer = csv.writer(response)
        writer.writerow(['id', 'Product_Class','Name', 'Owner',  'Domain','Project', 'Feature', 'Comments', 'Location', 'Product'])
        for obj in queryset:
            row = []
            row.append(obj.pk)
            row.append(obj.Product_Class)
            row.append(obj.Name)
            row.append(obj.Owner)            
            row.append(obj.Domain)
            row.append(obj.Project)
            row.append(obj.Description)
            row.append(obj.Comments)
            row.append(obj.Location)
            row.append(obj.Product)            
            writer.writerow(row)    

        return response

    def export_select(self, request, queryset):
        return self.export_product(queryset)
                
    def export_all(self, request, queryset):
        product_all = Product.objects.all()
        return self.export_product(product_all )
        
    def import_all(self, request, queryset):
    #    import csv,sys,os
    # Full path and name to your csv file
    #"e:/PythonWeb/code/lab_mgr/lab_mgr/import/product.csv"
        csv_filepathname=os.path.dirname(__file__)         #"e:/PythonWeb/code/lab_mgr/lab_mgr
        csv_filepathname = csv_filepathname + '/import/product.csv'
        
        # Full path to your django project directory
        #your_djangoproject_home="e:/PythonWeb/code/lab_mgr/lab_mgr/"
        #import sys,os
        #sys.path.append(your_djangoproject_home)
        #os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

        dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="result.csv"'
        writer = csv.writer(response)        

        i=0
        toExportResult = False
        for row in dataReader:
            if row[0] != 'id': # Ignore the header row, import everything else
                i = i+1
                
                if not row[0] =='':
                    product = Product.objects.get(pk=row[0])
                else:
                    product = None

                result = []
                result.append("line = %s" % (i))
                result.append("id = %s" % (row[0]))
                
                if product == None:
                    product = Product()
                    product.pk = None
                bError = False

                j=1
                if row[j] == '':
                    result.append("empty product class")
                    bError = True
                else:
                    try:
                        product_class = Product_Class.objects.get(Name = row[j])                        
                        product.Product_Class = product_class
                    except:
                        result.append("missing product class")
                        bError = True                        

                j=j+1
                if len(row)-1<j:
                    continue                        
                if row[0] == '':
                    try:
                        new_product = Product.objects.get(Name = row[j])
                        if not new_product == None:
                            result.append("dup Name")
                            bError = True
                    except:                        
                        bError = False        
                product.Name = row[j]
                
                j=j+1
                if len(row)-1<j:
                    continue   
                product.Owner = row[j]
                
                j=j+1
                if len(row)-1<j:
                    continue   
                product.Domain = row[j]
                
                j=j+1
                if len(row)-1<j:
                    continue   
                product.Project = row[j]
                
                j=j+1
                if len(row)-1<j:
                    continue   
                product.Description = row[j]
                
                j=j+1
                if len(row)-1<j:
                    continue   
                product.Comments = row[j]
                
                j=j+1
                if len(row)-1<j:
                    continue   
                if row[j] == '':
                    result.append("empty location")
                    bError = True
                else:
                    try:
                        location = Location.objects.get(Name = row[j])
                        product.Location = location
                    except:
                        result.append("missing location")
                        bError = True

                j=j+1
                if len(row)-1<j:
                    continue   
                if not row[j] == '':
                    try:
                        product2 = Product.objects.get(Name = row[j])
                        product.Product = product2                        
                    except:
                        result.append("missing product")
                        bError = True

                if True == bError:
                    #writer.writerow(['line = %s' % (i),'id = %s' % (row[0]),' %s' % (result)])
                    writer.writerow(result)

                if bError == True:
                    toExportResult = True
                    continue

                product.save()

        if toExportResult == True:
            return response
        else:
            self.message_user(request, "import finished")
            return super(MyModelAdmin, self).changelist_view( request, None)

class LabPlatformAdmin(MyModelAdmin):
    list_display = ('Name','Description','Comments','Location',)
    search_fields = ('Name','Description',)
    list_filter = ('Name','Description','Location',)
    ordering = ('Name','Location',)

    fieldsets= [
        (None,{
             'fields':
                (
                 'Name',
                 'Description',                                  
                 'Used_By',
                 )}),
        (None,{
             'fields':
                 (
                 'Owner',
                 'Test_Lab',
                 'Location',
                 'Comments',                 
                 )}),
    ]    

    form_links = [LabDeviceItemLinkFormAdmin, LabIPLinkFormAdmin, LabConfigurationLinkFormAdmin]    
    
class LabUEAdmin(MyModelAdmin):
    list_display = ('Name','Description','Comments',)
    search_fields = ('Name','Description',)
    list_filter = ('Name','Description',)
    ordering = ('Name',)

    fieldsets= [
        (None,{
             'fields':
                (
                 'Name',
                 'Description',                                  
                 'Used_By',
                 )}),
        (None,{
             'fields':
                 (
                 'Owner',
                 'PC',
                 'Comments',                 
                 )}),
    ]    

    form_links = [LabDeviceItemLinkFormAdmin, LabIPLinkFormAdmin, LabConfigurationLinkFormAdmin]    

'''
class ProductClassSubclassAdmin(admin.ModelAdmin):
    list_display = ('Product_Class','Product_SubClass') #list head in record table
    search_fields = ('Product_Class__Name','Product_SubClass__Name')    #search bar in record table
    ordering = ('Product_Class',)    #sort by field    

class ProductSubclassItemAdmin(admin.ModelAdmin):
    list_display = ('Product_SubClass','Product_Item') #list head in record table
    search_fields = ('Product_SubClass__Name','Product_Item__Name')    #search bar in record table
    ordering = ('Product_SubClass',)    #sort by field    
'''

class ProductClassItemAdmin(admin.ModelAdmin):
    list_display = ('Product_Class','Product_Item') #list head in record table
    search_fields = ('Product_Class__Name','Product_Item__Name')    #search bar in record table
    ordering = ('Product_Class',)    #sort by field    

class ProductItemTypeAdmin(admin.ModelAdmin):
    list_display = ('Product_Item','Device_Item_Type') #list head in record table
    search_fields = ('Product_Item__Name','Device_Item_Type__Code','Device_Item_Type__Description')    #search bar in record table
    ordering = ('Product_Item',)    #sort by field    

class lab_platform_hwsAdmin(admin.ModelAdmin):

    extra = 1
    
    list_display = ('ip','name','ritType','ritName','Vendor_unit_type','Vendor_unit_family_type','Vendor_unit_type_name','version_number','serial_number')
    search_fields = ('ip','name','ritType','ritName','Vendor_unit_type','Vendor_unit_family_type','Vendor_unit_type_name','version_number','serial_number')
    ordering = ('ip','name','ritType','ritName','Vendor_unit_type','Vendor_unit_family_type','Vendor_unit_type_name','version_number','serial_number')

from django.views.decorators.cache import never_cache

class AdminSiteExtend(admin.AdminSite):

    @never_cache
    def index(self, request, extra_context=None):
        product_list = ['Products', 'Ips', 'Configurations', 'Device Items',  ]
        
        extra_context = {
            'product_list' : product_list,
        }

        return super(AdminSiteExtend, self).index(request, extra_context)

    def app_index(self, request, app_label, extra_context=None):
        product_list = ['Products', 'Ips', 'Configurations', 'Device Items',  ]
        
        extra_context = {
            'product_list' : product_list,
        }

        return super(AdminSiteExtend, self).app_index(request, app_label, extra_context)
        

mysite = AdminSiteExtend()

from PreCI.models import PreCI_Request
from PreCI.admin import PreCI_RequestAdmin
mysite.register(PreCI_Request, PreCI_RequestAdmin)

mysite.register(models.lab_device_item, LabDeviceItemAdmin)   
mysite.register(models.Product, LabProductAdmin)   
mysite.register(models.lab_ip, LabIPAdmin)   
mysite.register(models.lab_configuration, LabConfigurationAdmin)   

mysite.register(models.Product_Class, LabProductClassAdmin)   
#mysite.register(models.Product_SubClass, LabProductSubClassAdmin)   
mysite.register(models.Product_Item, LabProductItemAdmin)   
mysite.register(models.Device_Item_Status, LabDeviceItemStatusAdmin)   
mysite.register(models.FA_Product_Line, LabFAProductLineAdmin)   
mysite.register(models.Device_Item_Type, LabDeviceItemTypeAdmin)   
#mysite.register(models.Product_Type, LabProductTypeAdmin)   
mysite.register(models.IP_Type, LabIPTypeAdmin)   
mysite.register(models.Configuration_Type, LabConfigurationTypeAdmin)   
mysite.register(models.Location, LabLocationAdmin)   
#mysite.register(models.PC, LabPCAdmin)   
#mysite.register(models.Platform, LabPlatformAdmin)   
#mysite.register(models.UE, LabUEAdmin)   
#mysite.register(models.Product_Class_Subclass_r, ProductClassSubclassAdmin)   
#mysite.register(models.Product_Subclass_Item_r, ProductSubclassItemAdmin)
mysite.register(models.Product_Class_Item_r, ProductClassItemAdmin)      
mysite.register(models.Product_Item_Type_r, ProductItemTypeAdmin)   

mysite.register(models.lab_platform_hws, lab_platform_hwsAdmin)  

from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
mysite.register(Group, GroupAdmin)
mysite.register(User, UserAdmin)



