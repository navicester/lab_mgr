from django.db import models

        
class Product_Class(models.Model):
    Name = models.CharField(max_length=50,unique = True,verbose_name='Name')
    def __unicode__(self):
        return u'%s' % (self.Name)

    class Meta:
        verbose_name = 'product_class'  
        db_table = 'lab_product_class'
        
'''
class Product_SubClass(models.Model):
    Name = models.CharField(max_length=50,unique = True,verbose_name='Name')
    def __unicode__(self):
        return u'%s' % (self.Name)

    class Meta:
        verbose_name = 'product_subclass'  
        db_table = 'lab_product_subclass'
'''
        
class Product_Item(models.Model):
    Name = models.CharField(max_length=50,unique = True,verbose_name='Item')
    def __unicode__(self):
        return u'%s' % (self.Name)

    class Meta:
        verbose_name = 'product_Item'  
        db_table = 'lab_product_item'

class Device_Item_Type(models.Model):
    Code = models.CharField(max_length=50,unique = True,verbose_name='Code')
    Description = models.TextField(max_length=500,verbose_name='Descrp_iption')
    def __unicode__(self):
        return u'%s - %s' % (self.Code, self.Description)

    class Meta:
        verbose_name = 'device item type'  
        db_table = 'lab_device_item_type'

'''
class Product_Class_Subclass_r(models.Model):
    Product_Class = models.ForeignKey(Product_Class,verbose_name='Product Class')
    Product_SubClass = models.ForeignKey(Product_SubClass,verbose_name='Product Subclass')
    
    def __unicode__(self):
        return u'%s %s' % (self.Product_Class.Name, self.Product_SubClass.Name)

    class Meta:
        verbose_name = 'rel product class subclass'
        db_table = 'lab_product_class_subclass_r'
        
class Product_Subclass_Item_r(models.Model):
    Product_SubClass = models.ForeignKey(Product_SubClass,verbose_name='Product Subclass')
    Product_Item = models.ForeignKey(Product_Item,verbose_name='Product Item')
    
    def __unicode__(self):
        return u'%s %s' % (self.Product_SubClass.Name, self.Product_Item.Name)

    class Meta:
        verbose_name = 'rel product subclass item'
        db_table = 'lab_product_subclass_item_r'
'''
        
class Product_Class_Item_r(models.Model):
    Product_Class = models.ForeignKey(Product_Class,verbose_name='Product Class')
    Product_Item = models.ForeignKey(Product_Item,verbose_name='Product Item')
    
    def __unicode__(self):
        return u'%s %s' % (self.Product_Class.Name, self.Product_Item.Name)

    class Meta:
        verbose_name = 'rel product class item'
        db_table = 'lab_product_class_item_r'

class Product_Item_Type_r(models.Model):
    Product_Item = models.ForeignKey(Product_Item,verbose_name='Product Item')
    Device_Item_Type = models.ForeignKey(Device_Item_Type,verbose_name='Product Item Type')
    
    def __unicode__(self):
        return u'%s %s' % (self.Product_Item.Name, self.Device_Item_Type.Code)

    class Meta:
        verbose_name = 'rel product item type'
        db_table = 'lab_product_item_type_r'
        
class Device_Item_Status(models.Model):
    Name = models.CharField(max_length=50,unique = True,verbose_name='Name')
    def __unicode__(self):
        return u'%s' % (self.Name)

    class Meta:
        verbose_name = 'device_item_status'  
        db_table = 'lab_device_item_status'
        
class Product_Type(models.Model):
    Name = models.CharField(max_length=50,unique = True,verbose_name='Name')
    def __unicode__(self):
        return u'%s' % (self.Name)

    class Meta:
        verbose_name = 'product type'  
        db_table = 'lab_product_type'

class IP_Type(models.Model):
    Name = models.CharField(max_length=50,unique = True,verbose_name='Name')
    def __unicode__(self):
        return u'%s' % (self.Name)
    class Meta:
        verbose_name = 'ip type'  
        db_table = 'lab_ip_type'

class Configuration_Type(models.Model):
    Name = models.CharField(max_length=50,unique = True,verbose_name='Name')
    def __unicode__(self):
        return u'%s' % (self.Name)

    class Meta:
        verbose_name = 'configuration type'  
        db_table = 'lab_configuration_type'
        
class FA_Product_Line(models.Model):
    Name = models.CharField(max_length=50,unique = True,verbose_name='Name')
    def __unicode__(self):
        return u'%s' % (self.Name)

    class Meta:
        verbose_name = 'fa_product_line'  
        db_table = 'lab_fa_product_line'

class Location(models.Model):
    Name = models.CharField(max_length=50,unique = True,verbose_name='Name')

    def __unicode__(self):
        return u'%s' % (self.Name)

    class Meta:
        verbose_name = 'location'  
        db_table = 'lab_location'


class Product(models.Model):
    Product_Class = models.ForeignKey(Product_Class,verbose_name='Product Class')
    #Product_SubClass = models.ForeignKey(Product_SubClass,verbose_name='Product SubClass')
    Name = models.CharField(max_length=50,unique = True, verbose_name='Name')
    Owner = models.CharField(max_length=50,verbose_name='Owner')
    #Used_By = models.CharField(max_length=50,null=True, blank=True,verbose_name='Used By')
    Domain = models.CharField(max_length=50,null=True, blank=True,verbose_name='Domain')
    Project = models.CharField(max_length=50,null=True, blank=True,verbose_name='Project')
    Description = models.TextField(max_length=500,null=True, blank=True,verbose_name='Feature')    
    #User = models.CharField(max_length=50,null=True, blank=True,verbose_name='User')
    #Password = models.CharField(max_length=50,null=True, blank=True,verbose_name='Password')
    Location = models.ForeignKey(Location,null=True, blank=True,verbose_name='Location')
    Comments = models.TextField(max_length=50,verbose_name='Change History')
    Product = models.ForeignKey('self',null=True, blank=True,verbose_name='Product')    

    def getitems(self):
        return {'id':self.pk, "Name":self.Name,"Owner":self.Owner, "Project":self.Project, "Domain":self.Domain,"Location":self.Location}
    
    def __unicode__(self):
        return u'%s' % (self.Name)

    class Meta:
        verbose_name = 'product'  
        db_table = 'lab_product'
    
class PC(models.Model):
    Name = models.CharField(max_length=50,unique = True,verbose_name='Name')
    Used_By = models.CharField(max_length=50,null=True, blank=True,verbose_name='Used By')
    Description = models.TextField(max_length=500,null=True, blank=True,verbose_name='Description')
    Owner = models.CharField(max_length=50,verbose_name='Owner')
    User = models.CharField(max_length=50,verbose_name='User')
    Password = models.CharField(max_length=50,verbose_name='Password')
    Comments = models.TextField(max_length=50,verbose_name='Change History')
    Location = models.ForeignKey(Location,null=True, blank=True,verbose_name='Location')

    def __unicode__(self):
        return u'%s' % (self.Name)

    class Meta:
        verbose_name = 'pc'  
        db_table = 'lab_pc'
        
class Platform(models.Model):
    Name = models.CharField(max_length=50,unique = True,verbose_name='Name')
    Used_By = models.CharField(max_length=50,null=True, blank=True,verbose_name='Used By')
    Description = models.TextField(max_length=500,null=True, blank=True,verbose_name='Description')
    Owner = models.CharField(max_length=50,verbose_name='Owner')
    Project = models.CharField(max_length=50,null=True, blank=True,verbose_name='Project')
    Domain = models.CharField(max_length=50,null=True, blank=True,verbose_name='Domain')
    Comments = models.TextField(max_length=50,verbose_name='Change History')
    
    Location = models.ForeignKey(Location,null=True, blank=True,verbose_name='Location')    

    def __unicode__(self):
        return u'%s' % (self.Name)

    class Meta:
        verbose_name = 'platform'  
        db_table = 'lab_platform'
    
class UE(models.Model):
    Name = models.CharField(max_length=50,unique = True,verbose_name='Name')
    Used_By = models.CharField(max_length=50,null=True, blank=True,verbose_name='Used By')
    Description = models.TextField(max_length=500,null=True, blank=True,verbose_name='Description')
    Owner = models.CharField(max_length=50,verbose_name='Owner')
    Comments = models.TextField(max_length=50,verbose_name='Change History')

    PC = models.ForeignKey(PC,null=True, blank=True,verbose_name='PC')
    
    def __unicode__(self):
        return u'%s %s %s' % (self.Name, self.Used_By, self.Owner)

    class Meta:
        verbose_name = 'ue'  
        db_table = 'lab_ue'
                
class lab_device_item(models.Model):
    Product_Class = models.ForeignKey(Product_Class,verbose_name='Product Class')
    #Product_SubClass = models.ForeignKey(Product_SubClass,verbose_name='Product SubClass')
    Product_Item = models.ForeignKey(Product_Item,verbose_name='Product Item')    
    SN = models.CharField(max_length=50,unique = True,verbose_name='SN')    
    Device_Item_Type = models.ForeignKey(Device_Item_Type,null=True, blank=True,verbose_name='Type')
    InFA = models.CharField(max_length=50,null=True, blank=True,verbose_name='InFA ?')
    FA_Applicant = models.CharField(max_length=50,null=True, blank=True,verbose_name='FA Applicant')
    User = models.CharField(max_length=50,null=True, blank=True,verbose_name='User')
    FA_Product_Line = models.ForeignKey(FA_Product_Line,null=True, blank=True,verbose_name='FA Product Line')    
    PR_Launcher = models.CharField(max_length=50,null=True, blank=True,verbose_name='PR Launcher')
    PR = models.CharField(max_length=50,null=True, blank=True,verbose_name='PR Number')    
    PO = models.CharField(max_length=50,null=True, blank=True,verbose_name='PO Number')
    Asset_By = models.CharField(max_length=50,null=True, blank=True,verbose_name='Asset Owner')
    Asset_Number = models.CharField(max_length=50,null=True, blank=True,verbose_name='Asset Number')
    Good_Received_Date = models.DateField(max_length=50,null=True, blank=True,auto_now=False, auto_now_add=False,verbose_name='Goods Received Date')
    Location = models.ForeignKey(Location,verbose_name='Location')
    Device_Item_Status = models.ForeignKey(Device_Item_Status,verbose_name='Status')
    Comments = models.TextField(max_length=50,null=True, blank=True,verbose_name='Change History')
    Create_Time = models.DateField(max_length=50,null=True, blank=True,verbose_name='Record Create Date')
    #Last_Modify_Time = models.DateField(max_length=50,auto_now=True, auto_now_add=True,blank=True, null=True, verbose_name='Last Modified Date')
    reserve1  = models.CharField(max_length=50,null=True, blank=True,verbose_name='reserve1')

    PC = models.ForeignKey(PC,null=True, blank=True,verbose_name='PC')
    UE = models.ForeignKey(UE,null=True, blank=True,verbose_name='UE')
    Platform = models.ForeignKey(Platform,null=True, blank=True,verbose_name='Platform')
    Product = models.ForeignKey(Product,null=True, blank=True,verbose_name='Product')
    
    def __unicode__(self):
        return u'%s %s %s' % (self.Product_Item, self.SN, self.Location)

    def getitems(self):
        return {'id':self.pk, "Product_Item":self.Product_Item, "SN":self.SN, "Location":self.Location}
    
    class Meta:
        verbose_name = 'device item'  
        db_table = 'lab_device_item'
                
           
class lab_ip(models.Model):    
    #Name = models.CharField(max_length=50,null=True, blank=True,verbose_name='Name')    
    ip  = models.CharField(max_length=50,verbose_name='ip')
    IP_Type = models.ForeignKey(IP_Type,null=True, blank=True,verbose_name='Type')
    ConnLocation  = models.CharField(max_length=50,null=True, blank=True,verbose_name='Conn Location')
    netmask  = models.CharField(max_length=50,null=True, blank=True,verbose_name='netmask')
    gw  = models.CharField(max_length=50,null=True, blank=True,verbose_name='gw')
    server_ip  = models.CharField(max_length=50,null=True, blank=True,verbose_name='server ip')        
    serial_port  = models.CharField(max_length=50,null=True, blank=True,verbose_name='serial port')
    ssh_port  = models.CharField(max_length=50,null=True, blank=True,verbose_name='ssh port')
    sftp_port  = models.CharField(max_length=50,null=True, blank=True,verbose_name='sftp port')
    tftp_port  = models.CharField(max_length=50,null=True, blank=True,verbose_name='tftp port')    
    hw  = models.CharField(max_length=50,null=True, blank=True,verbose_name='Hw')

    PC = models.ForeignKey(PC,null=True, blank=True,verbose_name='PC')
    UE = models.ForeignKey(UE,null=True, blank=True,verbose_name='UE')
    Platform = models.ForeignKey(Platform,null=True, blank=True,verbose_name='Platform')
    Product = models.ForeignKey(Product,null=True, blank=True,verbose_name='Product')
    
    def __unicode__(self):
        return u'%s : %s %s %s %s ' % (self.ip, self.serial_port, self.ssh_port, self.sftp_port, self.tftp_port)

    def getitems(self):
        return {'id':self.pk, "IP_Type":self.IP_Type,"ip":self.ip, "netmask":self.netmask, "gw":self.gw, "server_ip":self.server_ip,"serial_port":self.serial_port,"ssh_port":self.ssh_port, "sftp_port":self.sftp_port, "tftp_port":self.tftp_port}
    
    class Meta:
        verbose_name = 'ip'  
        db_table = 'lab_ip'

class lab_configuration(models.Model):
    Configuration_Type = models.ForeignKey(Configuration_Type,null=True, blank=True,verbose_name='Type')
    Name = models.CharField(max_length=50,null=True, blank=True,verbose_name='Name')    
    val1  = models.CharField(max_length=500,verbose_name='val1')
    val2  = models.CharField(max_length=50,null=True, blank=True,verbose_name='val2')
    val3  = models.CharField(max_length=50,null=True, blank=True,verbose_name='val3')
    val4  = models.CharField(max_length=50,null=True, blank=True,verbose_name='val4')
    val5  = models.CharField(max_length=50,null=True, blank=True,verbose_name='val5')
    val6  = models.CharField(max_length=50,null=True, blank=True,verbose_name='val6')
    
    PC = models.ForeignKey(PC,null=True, blank=True,verbose_name='PC')
    UE = models.ForeignKey(UE,null=True, blank=True,verbose_name='UE')
    Platform = models.ForeignKey(Platform,null=True, blank=True,verbose_name='Platform')
    Product = models.ForeignKey(Product,null=True, blank=True,verbose_name='Product')    
    
    def __unicode__(self):
        return u'%s' % (self.Configuration_Type)

    def getitems(self):
        return {'id':self.pk, "Configuration_Type":self.Configuration_Type,"val1":self.val1,"val2":self.val2, "val3":self.val3,"val4":self.val4, "val5":self.val5,"val6":self.val6}
    
    class Meta:
        verbose_name = 'configuration'  
        db_table = 'lab_configuration'

class lab_platform_hws(models.Model):
    ip = models.CharField(max_length=50,null=False, blank=False,verbose_name='eccm ip')
    name = models.CharField(max_length=50,null=False, blank=False,verbose_name='platform name')
    ritType= models.CharField(max_length=50,null=True, blank=True,verbose_name='ritType')
    ritName = models.CharField(max_length=50,null=True, blank=True,verbose_name='ritName')
    Vendor_unit_type = models.CharField(max_length=50,null=True, blank=True,verbose_name='Vendor_unit_type')
    Vendor_unit_family_type = models.CharField(max_length=50,null=True, blank=True,verbose_name='Vendor_unit_family_type')
    Vendor_unit_type_name = models.CharField(max_length=50,null=True, blank=True,verbose_name='Vendor_unit_type_name')
    version_number = models.CharField(max_length=50,null=True, blank=True,verbose_name='version_number')
    serial_number  = models.CharField(max_length=50,null=True, blank=True,verbose_name='serial_number')

    def __unicode__(self):
        return u'%s %s' % (self.name , self.ip)

    #def getitems(self):
    #    return {'id':self.pk, "Configuration_Type":self.Configuration_Type,"val1":self.val1,"val2":self.val2, "val3":self.val3,"val4":self.val4, "val5":self.val5,"val6":self.val6}
    
    class Meta:
        verbose_name = 'lab_platform_hws'  
        db_table = 'lab_platform_hws'

