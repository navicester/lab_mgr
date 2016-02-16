from lab_mgr.link_form_admin import LinkFormAdminForm
from django import forms
from django.utils.html import escape, escapejs

class LabDeviceItemForm(LinkFormAdminForm):
    class Meta:
        verbose_name = 'lab device item'
        class_name = "lab_device_item"
        
    id = forms.CharField(max_length=11, label = "id", widget = forms.TextInput(attrs={'readonly':'readonly','disable':True})) 
    Product_Item = forms.CharField(max_length=11, label = "Product Item", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    SN = forms.CharField(max_length=50, label = "SN", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    Location = forms.CharField(max_length=11, label = "Location", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    

    def __unicode__(self):
        return u'%s %s' % (self.id, self.Product_Item)  

    def is_valid(self):
        return super(LabDeviceItemForm, self).is_valid()            

    def get_back_array(self, obj):
        array= []
        array.append("Product_Item")
        array.append(escape(obj.Product_Item))
        array.append("SN")
        array.append(escape(obj.SN))
        array.append("Location")
        array.append(escape(obj.Location))
        return array

class LabProductForm(LinkFormAdminForm):
    class Meta:
        verbose_name = 'product'
        class_name = "product"
        
    id = forms.CharField(max_length=11, label = "id", widget = forms.TextInput(attrs={'readonly':'readonly','disable':True})) 
    Name = forms.CharField(max_length=11, label = "Name", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    Owner = forms.CharField(max_length=11, label = "Owner", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    Project = forms.CharField(max_length=11, label = "Project", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    Domain = forms.CharField(max_length=11, label = "Domain", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    Location = forms.CharField(max_length=11, label = "Location", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    

    def __unicode__(self):
        return u'%s %s' % (self.id, self.Name)  

    def is_valid(self):
        return super(LabProductForm, self).is_valid()            

    def get_back_array(self, obj):
        array= []
        array.append("Name")
        array.append(escape(obj.Name))
        array.append("Owner")
        array.append(escape(obj.Owner))
        array.append("Project")
        array.append(escape(obj.Project))
        array.append("Domain")
        array.append(escape(obj.Domain))
        array.append("Location")
        array.append(escape(obj.Location))
        return array

class LabIPForm(LinkFormAdminForm):
    class Meta:
        verbose_name = 'lab ip'
        class_name = "lab_ip"
        
    id = forms.CharField(max_length=11, label = "id", widget = forms.TextInput(attrs={'readonly':'readonly','disable':True})) 
    IP_Type = forms.CharField(max_length=11, label = "IP_Type", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    ip = forms.CharField(max_length=50, label = "ip", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    server_ip = forms.CharField(max_length=11, label = "server ip", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    

    serial_port = forms.CharField(max_length=11, label = "serial port", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    ssh_port = forms.CharField(max_length=11, label = "ssh port", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    tftp_port = forms.CharField(max_length=11, label = "tftp port", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    sftp_port = forms.CharField(max_length=11, label = "sftp port", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    

    def __unicode__(self):
        return u'%s %s' % (self.id, self.IP_Type)  

    def is_valid(self):
        return super(LabIPForm, self).is_valid()            

    def get_back_array(self, obj):
        array= []
        array.append("IP_Type")
        array.append(escape(obj.IP_Type))
        array.append("ip")
        array.append(escape(obj.ip))
        array.append("server_ip")
        array.append(escape(obj.server_ip))        
        array.append("serial_port")
        array.append(escape(obj.serial_port))
        array.append("ssh_port")
        array.append(escape(obj.ssh_port))
        array.append("sftp_port")
        array.append(escape(obj.sftp_port))
        array.append("tftp_port")
        array.append(escape(obj.tftp_port))

        return array

class LabConfigurationForm(LinkFormAdminForm):
    class Meta:
        verbose_name = 'lab configuration'
        class_name = "lab_configuration"
        
    id = forms.CharField(max_length=11, label = "id", widget = forms.TextInput(attrs={'readonly':'readonly','disable':True})) 
    IP_Type = forms.CharField(max_length=11, label = "IP_Type", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    val1 = forms.CharField(max_length=50, label = "val1", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    val2 = forms.CharField(max_length=11, label = "val2", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    val3 = forms.CharField(max_length=11, label = "val3", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    val4 = forms.CharField(max_length=11, label = "val4", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    val5 = forms.CharField(max_length=11, label = "val5", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    val6 = forms.CharField(max_length=11, label = "val6", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    

    def __unicode__(self):
        return u'%s %s' % (self.id, self.IP_Type)  

    def is_valid(self):
        return super(LabConfigurationForm, self).is_valid()            

    def get_back_array(self, obj):
        array= []
        array.append("IP_Type")
        array.append(escape(obj.IP_Type))
        array.append("val1")
        array.append(escape(obj.val1))
        array.append("val2")
        array.append(escape(obj.val2))        
        array.append("val3")
        array.append(escape(obj.val3))
        array.append("val4")
        array.append(escape(obj.val4))        
        array.append("val5")
        array.append(escape(obj.val5))
        array.append("val6")
        array.append(escape(obj.val6))        

        return array


